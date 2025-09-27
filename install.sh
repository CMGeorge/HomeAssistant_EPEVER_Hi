#!/bin/bash
#
# EPEVER Hi Integration Installation Script
# This script downloads and installs the EPEVER Hi integration directly to Home Assistant
#

set -e

REPO_URL="https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi"
INTEGRATION_NAME="epever_hi"
TEMP_DIR="/tmp/epever_hi_install"
CUSTOM_COMPONENTS_DIR=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to detect Home Assistant custom_components directory
detect_ha_directory() {
    local possible_dirs=(
        "/config/custom_components"
        "/usr/share/hassio/homeassistant/custom_components"
        "/home/homeassistant/.homeassistant/custom_components"
        "$HOME/.homeassistant/custom_components"
        "./config/custom_components"
        "../config/custom_components"
    )
    
    for dir in "${possible_dirs[@]}"; do
        if [[ -d "$dir" ]]; then
            CUSTOM_COMPONENTS_DIR="$dir"
            return 0
        fi
    done
    
    return 1
}

# Function to install the integration
install_integration() {
    print_info "Starting EPEVER Hi Integration installation..."
    
    # Clean up any existing temp directory
    if [[ -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
    
    # Create temp directory
    mkdir -p "$TEMP_DIR"
    cd "$TEMP_DIR"
    
    # Download the repository
    print_info "Downloading integration from $REPO_URL..."
    if command -v wget &> /dev/null; then
        wget -q -O main.zip "$REPO_URL/archive/main.zip"
    elif command -v curl &> /dev/null; then
        curl -sL -o main.zip "$REPO_URL/archive/main.zip"
    else
        print_error "Neither wget nor curl found. Please install one of them."
        exit 1
    fi
    
    # Extract the archive
    print_info "Extracting files..."
    if command -v unzip &> /dev/null; then
        unzip -q main.zip
    else
        print_error "unzip command not found. Please install unzip."
        exit 1
    fi
    
    # Find the extracted directory
    EXTRACTED_DIR=$(find . -name "HomeAssistant_EPEVER_Hi-*" -type d | head -n1)
    if [[ -z "$EXTRACTED_DIR" ]]; then
        print_error "Could not find extracted directory."
        exit 1
    fi
    
    # Create custom_components directory if it doesn't exist
    mkdir -p "$CUSTOM_COMPONENTS_DIR"
    
    # Copy the integration
    print_info "Installing integration to $CUSTOM_COMPONENTS_DIR/$INTEGRATION_NAME..."
    cp -r "$EXTRACTED_DIR/custom_components/$INTEGRATION_NAME" "$CUSTOM_COMPONENTS_DIR/"
    
    # Clean up
    cd /
    rm -rf "$TEMP_DIR"
    
    print_success "EPEVER Hi Integration installed successfully!"
    print_warning "Please restart Home Assistant to load the new integration."
    print_info "After restart, go to Settings → Devices & Services → Add Integration → Search for 'EPEVER Hi'"
}

# Main script
main() {
    print_info "EPEVER Hi Integration Installer"
    print_info "==============================="
    
    # Detect Home Assistant directory
    if detect_ha_directory; then
        print_info "Found Home Assistant custom_components directory: $CUSTOM_COMPONENTS_DIR"
    else
        print_warning "Could not automatically detect Home Assistant directory."
        print_info "Please specify the path to your Home Assistant custom_components directory:"
        read -r -p "Path: " CUSTOM_COMPONENTS_DIR
        
        if [[ ! -d "$CUSTOM_COMPONENTS_DIR" ]]; then
            print_error "Directory does not exist: $CUSTOM_COMPONENTS_DIR"
            print_info "Creating directory..."
            mkdir -p "$CUSTOM_COMPONENTS_DIR" || {
                print_error "Failed to create directory. Please check permissions."
                exit 1
            }
        fi
    fi
    
    # Check if integration already exists
    if [[ -d "$CUSTOM_COMPONENTS_DIR/$INTEGRATION_NAME" ]]; then
        print_warning "EPEVER Hi integration is already installed."
        print_info "Do you want to update it? (y/N)"
        read -r -n 1 response
        echo
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            print_info "Installation cancelled."
            exit 0
        fi
        print_info "Updating existing installation..."
    fi
    
    # Install the integration
    install_integration
}

# Run the main function
main "$@"