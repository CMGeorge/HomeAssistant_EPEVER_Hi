# EPEVER Hi Installation Guide

This integration now supports multiple installation methods for maximum flexibility. Choose the method that works best for your Home Assistant setup.

## Quick Installation (Recommended)

### One-Command Installation

**Linux/macOS (Bash):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh | bash
```

**Any Platform (Python):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.py | python3
```

## Installation Methods

### 1. HACS Integration (Most Popular)
- **Best for**: Users already using HACS
- **Steps**:
  1. Open HACS → Integrations → Custom Repositories
  2. Add: `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi`
  3. Category: Integration
  4. Install and restart

### 2. Direct Repository Installation
- **Best for**: Users who want to add this as a repository to Home Assistant
- **Steps**:
  1. Use the repository URL: `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi`
  2. Repository metadata is available at: `repository.json`
  3. Download URL: `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/archive/main.zip`

### 3. Automated Script Installation
- **Best for**: Command line users and automation
- **Features**:
  - Auto-detects Home Assistant directory
  - Cross-platform support (Bash and Python versions)
  - Interactive prompts for custom paths
  - Automatic download and extraction
  
**Download and run:**
```bash
# Bash version
wget https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh
chmod +x install.sh
./install.sh

# Python version  
wget https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.py
python3 install.py
```

### 4. Manual Installation
- **Best for**: Users who prefer manual control
- **Steps**:
  1. Download: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/archive/main.zip
  2. Extract and copy `custom_components/epever_hi` to your Home Assistant `custom_components` directory
  3. Restart Home Assistant

## After Installation

Regardless of installation method:

1. **Restart Home Assistant**
2. **Add Integration**: Settings → Devices & Services → Add Integration
3. **Search**: "EPEVER Hi"
4. **Configure**: Enter your Modbus connection details

## Repository Structure

This repository is designed to be compatible with multiple installation systems:

- `hacs.json` + `info.md` - HACS compatibility
- `repository.json` - Direct Home Assistant repository support  
- `install.sh` / `install.py` - Automated installation scripts
- `custom_components/epever_hi/` - The integration itself

## Troubleshooting

### Script Installation Issues
- Ensure you have `curl`, `wget`, or `python3` available
- Check Home Assistant directory permissions
- Verify custom_components directory exists

### Repository Installation Issues  
- Ensure the repository URL is correct
- Check that Home Assistant can access GitHub
- Verify the integration appears after restart

### General Issues
- Check Home Assistant logs for errors
- Ensure Modbus device is accessible
- Verify integration configuration parameters