#!/usr/bin/env python3
"""
EPEVER Hi Integration Installation Script
This script downloads and installs the EPEVER Hi integration directly to Home Assistant
"""

from pathlib import Path
import shutil
import sys
import tempfile
import urllib.request
import zipfile


class Colors:
    """ANSI color codes for terminal output."""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    NC = "\033[0m"  # No Color


def print_info(message: str) -> None:
    """Print info message."""
    print(f"{Colors.BLUE}[INFO]{Colors.NC} {message}")


def print_success(message: str) -> None:
    """Print success message."""
    print(f"{Colors.GREEN}[SUCCESS]{Colors.NC} {message}")


def print_warning(message: str) -> None:
    """Print warning message."""
    print(f"{Colors.YELLOW}[WARNING]{Colors.NC} {message}")


def print_error(message: str) -> None:
    """Print error message."""
    print(f"{Colors.RED}[ERROR]{Colors.NC} {message}")


def detect_ha_directory() -> Path | None:
    """Detect Home Assistant custom_components directory."""
    possible_dirs = [
        Path("/config/custom_components"),
        Path("/usr/share/hassio/homeassistant/custom_components"),
        Path("/home/homeassistant/.homeassistant/custom_components"),
        Path.home() / ".homeassistant" / "custom_components",
        Path("./config/custom_components"),
        Path("../config/custom_components"),
    ]

    for directory in possible_dirs:
        if directory.is_dir():
            return directory

    return None


def download_and_extract(repo_url: str, temp_dir: Path) -> Path:
    """Download and extract the repository."""
    print_info(f"Downloading integration from {repo_url}...")

    # Download the ZIP file
    zip_url = f"{repo_url}/archive/main.zip"
    zip_path = temp_dir / "main.zip"

    try:
        urllib.request.urlretrieve(zip_url, zip_path)
    except Exception as e:
        print_error(f"Failed to download repository: {e}")
        sys.exit(1)

    print_info("Extracting files...")

    # Extract the ZIP file
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
    except Exception as e:
        print_error(f"Failed to extract files: {e}")
        sys.exit(1)

    # Find the extracted directory
    extracted_dirs = [
        d
        for d in temp_dir.iterdir()
        if d.is_dir() and d.name.startswith("HomeAssistant_EPEVER_Hi-")
    ]

    if not extracted_dirs:
        print_error("Could not find extracted directory.")
        sys.exit(1)

    return extracted_dirs[0]


def install_integration(custom_components_dir: Path, extracted_dir: Path) -> None:
    """Install the integration to the custom_components directory."""
    integration_name = "epever_hi"
    source_dir = extracted_dir / "custom_components" / integration_name
    target_dir = custom_components_dir / integration_name

    if not source_dir.is_dir():
        print_error(f"Source integration directory not found: {source_dir}")
        sys.exit(1)

    print_info(f"Installing integration to {target_dir}...")

    # Remove existing installation if present
    if target_dir.exists():
        shutil.rmtree(target_dir)

    # Copy the integration
    try:
        shutil.copytree(source_dir, target_dir)
    except Exception as e:
        print_error(f"Failed to copy integration files: {e}")
        sys.exit(1)

    print_success("EPEVER Hi Integration installed successfully!")


def main():
    """Main installation function."""
    print_info("EPEVER Hi Integration Installer")
    print_info("===============================")

    repo_url = "https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi"
    integration_name = "epever_hi"

    # Detect Home Assistant directory
    custom_components_dir = detect_ha_directory()

    if custom_components_dir:
        print_info(
            f"Found Home Assistant custom_components directory: {custom_components_dir}"
        )
    else:
        print_warning("Could not automatically detect Home Assistant directory.")
        custom_path = input(
            "Please specify the path to your Home Assistant custom_components directory: "
        )
        custom_components_dir = Path(custom_path)

        if not custom_components_dir.exists():
            print_error(f"Directory does not exist: {custom_components_dir}")
            print_info("Creating directory...")
            try:
                custom_components_dir.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print_error(f"Failed to create directory: {e}")
                sys.exit(1)

    # Check if integration already exists
    integration_dir = custom_components_dir / integration_name
    if integration_dir.exists():
        print_warning("EPEVER Hi integration is already installed.")
        response = input("Do you want to update it? (y/N): ").strip().lower()
        if response not in ["y", "yes"]:
            print_info("Installation cancelled.")
            sys.exit(0)
        print_info("Updating existing installation...")

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Download and extract
        extracted_dir = download_and_extract(repo_url, temp_path)

        # Install the integration
        install_integration(custom_components_dir, extracted_dir)

    print_warning("Please restart Home Assistant to load the new integration.")
    print_info(
        "After restart, go to Settings → Devices & Services → Add Integration → Search for 'EPEVER Hi'"
    )


if __name__ == "__main__":
    main()
