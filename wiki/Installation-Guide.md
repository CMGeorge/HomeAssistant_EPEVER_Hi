# Installation Guide

This integration supports multiple installation methods for maximum flexibility. Choose the method that works best for your Home Assistant setup.

## 🚀 Quick Installation (Recommended)

### One-Command Installation

**Linux/macOS (Bash):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh | bash
```

**Any Platform (Python):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.py | python3
```

Both scripts will:
- Auto-detect your Home Assistant directory
- Download and install the integration
- Provide interactive prompts for custom paths
- Work across different Home Assistant installations

## 📦 Installation Methods

### Method 1: HACS Integration (Most Popular)

**Best for**: Users already using HACS  
**Difficulty**: Easy  
**Auto-updates**: Yes

**Steps:**
1. Open Home Assistant
2. Go to **HACS → Integrations → Custom Repositories**
3. Add repository: `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi`
4. Choose category: **Integration**
5. Click **Install**
6. Restart Home Assistant

### Method 2: Central Repository Installation (New!)

**Best for**: Users who want multiple George Călugăr integrations  
**Difficulty**: Easy  
**Auto-updates**: Yes

**Steps:**
1. Add central repository: `https://github.com/CMGeorge/ha_repository`
2. Access multiple integrations:
   - EPEVER Hi Integration
   - Sabiana Smart Energy Integration
   - Future integrations
3. One-stop installation for all integrations

### Method 3: Direct Repository Installation

**Best for**: Users who want to add this repository directly to Home Assistant  
**Difficulty**: Medium  
**Auto-updates**: With repository support

**Steps:**
1. In Home Assistant, go to **Settings → Add-ons → Add-on Store**
2. Click **⋮** menu → **Repositories**
3. Add: `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi`
4. Install the integration from the repository
5. Restart Home Assistant

### Method 4: Automated Script Installation

**Best for**: Command line users and automation  
**Difficulty**: Easy to Medium  
**Auto-updates**: Manual

**Features:**
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

### Method 5: Manual Installation

**Best for**: Users who prefer manual control  
**Difficulty**: Medium  
**Auto-updates**: Manual

**Steps:**
1. Download: [Latest Release](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/archive/main.zip)
2. Extract the archive
3. Copy `custom_components/epever_hi` to your Home Assistant `custom_components` directory
4. Ensure the directory structure is:
   ```
   custom_components/
   └── epever_hi/
       ├── __init__.py
       ├── manifest.json
       ├── config_flow.py
       └── ... (other files)
   ```
5. Restart Home Assistant

## 🔗 Installation URLs

For quick access, here are all the relevant URLs:

- **Central Repository**: https://github.com/CMGeorge/ha_repository
- **HACS Repository**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
- **Direct Download**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/archive/main.zip
- **Latest Release**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/releases/latest
- **Repository JSON**: https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/repository.json

## ✅ After Installation

Regardless of installation method:

1. **Restart Home Assistant**
2. **Clear Browser Cache** (Ctrl+F5 or Cmd+Shift+R)
3. **Add Integration**: Settings → Devices & Services → **Add Integration**
4. **Search**: "EPEVER Hi"
5. **Configure**: Enter your Modbus connection details

## 🏗️ Repository Structure

This repository is designed for compatibility with multiple installation systems:

- `hacs.json` + `info.md` - HACS compatibility
- `repository.json` - Direct Home Assistant repository support  
- `install.sh` / `install.py` - Automated installation scripts
- `custom_components/epever_hi/` - The integration itself

## 🔧 Troubleshooting Installation

### Script Installation Issues
- **Missing tools**: Ensure you have `curl`, `wget`, or `python3` available
- **Permissions**: Check Home Assistant directory write permissions
- **Directory**: Verify `custom_components` directory exists
- **Path**: Script will prompt for custom Home Assistant path if auto-detection fails

### Repository Installation Issues  
- **URL**: Ensure the repository URL is correct
- **Network**: Check that Home Assistant can access GitHub
- **Restart**: Verify the integration appears after restart
- **Browser**: Clear browser cache after installation

### HACS Installation Issues
- **HACS**: Ensure HACS is properly installed and configured
- **Custom Repository**: Add the repository URL correctly
- **Category**: Select "Integration" as the category
- **Updates**: HACS will handle automatic updates

### General Issues
- **Logs**: Check Home Assistant logs for errors: Settings → System → Logs
- **Integration**: Look for "epever_hi" in the logs
- **Modbus**: Ensure your Modbus device is accessible
- **Configuration**: Verify integration configuration parameters
- **Dependencies**: The integration requires `pymodbus>=3.0.0` (installed automatically)

## 📋 System Requirements

- **Home Assistant**: 2024.1.0 or later
- **Python**: 3.12+ (handled by Home Assistant)
- **Dependencies**: `pymodbus>=3.0.0` (installed automatically)
- **Hardware**: EPEVER Hi compatible charge controller with Modbus support

## 🆕 Next Steps

After installation, proceed to:
- **[Configuration Guide](Configuration)** - Set up your Modbus connection
- **[Supported Devices](Supported-Devices)** - Verify device compatibility
- **[Entities Reference](Entities-Reference)** - Explore available sensors and controls