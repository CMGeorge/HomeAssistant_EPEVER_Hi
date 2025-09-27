# EPEVER Hi Integration for Home Assistant

A custom integration for Home Assistant that enables communication with **EPEVER Hi** solar charge controllers over **Modbus** (RTU or TCP).  
This integration provides access to solar panel data, battery monitoring, charge controller status, and control over various operational parameters.

[![Validate](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/validate.yml/badge.svg)](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/validate.yml)
[![Lint](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/lint.yml/badge.svg)](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/lint.yml)
[![hassfest](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/actions/workflows/hassfest.yaml)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=CMGeorge&repository=https%3A%2F%2Fgithub.com%2FCMGeorge%2FHomeAssistant_EPEVER_Hi&category=Integration)

---

## 🔧 Features

- 📡 Modbus communication support (TCP or RTU)
- ⚡ Solar readings: voltage, current, power from solar panels
- 🔋 Battery monitoring: voltage, current, SOC, temperature
- 🔌 Load monitoring: voltage, current, power consumption
- ⚙️ Charge controller status and diagnostics
- 🛠️ Write support for supported registers (battery settings, charging parameters)
- 🏠 Native integration with Home Assistant UI

---

## 🧪 Supported Devices

- EPEVER **Hi Series** solar charge controllers  
- Should also support other **EPEVER Hi** compatible models (via Modbus)

---

## 📦 Installation

### Option 1: HACS (Recommended)
1. In Home Assistant, go to **HACS → Integrations → Custom Repositories**
2. Add this repository: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
3. Choose category: **Integration**
4. Install and restart Home Assistant

### Option 2: Central Repository Installation (New!)
Add the central repository for all George Călugăr integrations:

1. **Add Repository**: `https://github.com/CMGeorge/ha_repository`
2. **Access Multiple Integrations**: Get EPEVER Hi, Sabiana Smart Energy, and future integrations
3. **One-Stop Installation**: Central location for all integrations

### Option 3: Direct Repository Installation
You can add this repository directly to Home Assistant as an integration repository:

1. **Via Repository URL**: Add `https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi` as a custom integration repository
2. **Via repository.json**: This repository provides a `repository.json` file for direct integration installation

### Option 4: Automated Installation Script
Use the provided installation scripts for automatic setup:

**Bash script (Linux/macOS):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh | bash
```

**Python script (Cross-platform):**
```bash
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.py | python3
```

**Manual script download:**
```bash
# Download and run bash script
wget https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh
chmod +x install.sh
./install.sh

# Or download and run Python script
wget https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.py
python3 install.py
```

### Option 5: Manual Installation
1. Clone or download this repository: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
2. Copy the `custom_components/epever_hi` folder to: `config/custom_components/epever_hi`
3. Restart Home Assistant

---

## ⚙️ Configuration

The integration uses the UI (no YAML required). After install:

1. Go to **Settings → Devices & Services**
2. Click **Add Integration** → Search for **EPEVER Hi**
3. Enter the required connection details:
- Host or Serial port
- Modbus type (TCP/RTU)
- Unit ID
- Polling interval

---

## 🧾 Entities

- `sensor.epever_hi_solar_voltage`
- `sensor.epever_hi_battery_voltage`
- `sensor.epever_hi_battery_soc`
- `sensor.epever_hi_battery_temperature`
- `binary_sensor.epever_hi_charging`
- `number.epever_hi_battery_capacity`
- And many more...

Entity categories (`diagnostic`, `config`) are used where appropriate.

---

## 🧑‍💻 Development / Contribute

You're welcome to open issues, pull requests, or discussions!

To test locally:

```bash
git clone https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi.git
cp -r HomeAssistant_EPEVER_Hi/custom_components/epever_hi \
~/.homeassistant/custom_components/

```

### 🧪 Development Setup

For development and contributing:

```bash
# Clone the repository
git clone https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi.git
cd HomeAssistant_EPEVER_Hi

# Install development dependencies
pip install -r requirements-dev.txt

# Run linting and formatting
make check          # Run all checks (lint, format, test)
make lint           # Run linting only
make format         # Format code
make lint-fix       # Fix linting issues
make test           # Run tests
make test-cov       # Run tests with coverage

# Or use tools directly
ruff check .        # Check for issues
ruff check . --fix  # Fix issues automatically
ruff format .       # Format code
pytest              # Run tests
pytest --cov       # Run tests with coverage

# Set up pre-commit hooks (optional)
pre-commit install
```

### 🧪 Testing

The integration includes automated tests to ensure code quality and functionality:

**Test Categories:**
- **Manifest validation**: Ensures `manifest.json` is valid and contains required fields
- **Code structure tests**: Validates all Python files have correct syntax and structure
- **Configuration tests**: Tests config flow validation without requiring Home Assistant runtime
- **Register definitions**: Validates Modbus register definitions in `const.py`
- **Integration tests**: Checks file structure and imports

**Running Tests:**
```bash
# Run all tests
make test

# Run tests with coverage report
make test-cov

# Run tests directly with pytest
pytest
pytest -v  # verbose output
pytest tests/test_manifest.py  # run specific test file
```

**Test Structure:**
```
tests/
├── __init__.py
├── conftest.py              # Test configuration and fixtures
├── test_manifest.py         # Manifest.json validation tests
├── test_const.py           # Constants and register definition tests
├── test_config_flow.py     # Configuration flow tests
└── test_integration.py     # Integration and syntax tests
```

**Note**: These tests are designed to work without a full Home Assistant installation, focusing on static analysis, syntax validation, and structure verification.

---

## 📂 Repository Structure

This repository supports multiple installation methods:

- **HACS Integration**: Uses `hacs.json` and `info.md` for HACS compatibility
- **Direct Repository**: Provides `repository.json` for direct Home Assistant integration installation
- **Automated Scripts**: Includes `install.sh` and `install.py` for one-command installation
- **Manual Installation**: Traditional copy-paste method

### Repository Files:
- `repository.json` - Metadata for direct Home Assistant repository support
- `install.sh` - Bash installation script  
- `install.py` - Python installation script (cross-platform)
- `hacs.json` - HACS integration metadata
- `info.md` - Integration description for HACS
- `custom_components/epever_hi/` - The actual integration code

---

## 🔗 Installation URLs

- **Central Repository**: https://github.com/CMGeorge/ha_repository (All integrations)
- **HACS Repository**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
- **Direct Download**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/archive/main.zip
- **Latest Release**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/releases/latest
- **Repository JSON**: https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/repository.json

---

## 📚 Modbus Register Map

This integration is based on EPEVER Hi official Modbus documentation.
You can find/extend register definitions in: custom_components/epever_hi/const.py


## 📜 License

MIT License © George Călugăr
Not affiliated with EPEVER Co., Ltd.