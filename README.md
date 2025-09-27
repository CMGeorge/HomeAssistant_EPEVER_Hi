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

### Option 2: Manual
1. Clone or download this repository: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
2. Copy the folder to: config/custom_components/epever_hi

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

📚 Modbus Register Map

This integration is based on EPEVER Hi official Modbus documentation.
You can find/extend register definitions in: custom_components/epever_hi/const.py


📜 License

MIT License © George Călugăr
Not affiliated with EPEVER Co., Ltd.