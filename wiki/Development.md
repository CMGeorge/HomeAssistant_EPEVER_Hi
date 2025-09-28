# Development Guide

This guide provides information for developers who want to contribute to the EPEVER Hi Integration or understand its technical implementation.

## 🚀 Development Setup

### Prerequisites

- **Python 3.12+** (required for Home Assistant 2024.1+)
- **Home Assistant Development Environment** (optional but recommended)
- **Git** for version control
- **EPEVER Hi Device** or Modbus simulator for testing

### Quick Development Setup

```bash
# Clone the repository
git clone https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi.git
cd HomeAssistant_EPEVER_Hi

# Install development dependencies
pip install -r requirements-dev.txt

# Install integration dependencies
pip install pymodbus>=3.0.0 voluptuous

# Set up pre-commit hooks (optional but recommended)
pre-commit install
```

### Development Tools Installation

```bash
# Install essential development tools
python3 -m pip install ruff yamllint pytest pytest-cov

# Verify installation
ruff --version
yamllint --version
pytest --version
```

## 🏗️ Project Structure

### Repository Layout

```
/
├── .github/
│   ├── workflows/          # CI/CD pipelines
│   │   ├── validate.yml    # Home Assistant validation
│   │   ├── lint.yml        # Code linting
│   │   ├── test.yml        # Test execution
│   │   └── hassfest.yaml   # HA integration validation
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── copilot-instructions.md  # AI development guidelines
├── .devcontainer/          # VS Code dev container
├── custom_components/
│   └── epever_hi/          # Integration source code
│       ├── __init__.py         # Integration entry point
│       ├── manifest.json       # Integration metadata
│       ├── config_flow.py      # Configuration UI flow
│       ├── const.py           # Constants and register definitions
│       ├── modbus_client.py   # Modbus communication layer
│       ├── modbus_coordinator.py  # Data coordination
│       ├── sensor.py          # Sensor entities
│       ├── binary_sensor.py   # Binary sensor entities
│       ├── number.py          # Number entities (setpoints)
│       ├── select.py          # Select entities (modes)
│       ├── switch.py          # Switch entities
│       ├── button.py          # Button entities
│       ├── helpers.py         # Helper functions
│       └── info_sensor.py     # Information sensors
├── tests/                  # Test suite
├── wiki/                   # Documentation (GitHub Wiki)
├── requirements-dev.txt    # Development dependencies
├── pyproject.toml         # Project configuration
├── Makefile               # Development commands
└── README.md              # Project documentation
```

### Key Files

#### `manifest.json`
Integration metadata and dependencies:
```json
{
    "domain": "epever_hi",
    "name": "EPEVER Hi",
    "config_flow": true,
    "dependencies": ["modbus"],
    "requirements": ["pymodbus>=3.0.0"],
    "integration_type": "hub",
    "iot_class": "local_polling"
}
```

#### `const.py`
Register definitions and constants (555 lines):
- `SENSOR_DEFINITIONS_NEW`: Input registers for sensors
- `REGISTER_DEFINITIONS`: Holding registers for configuration
- `NUMBER_DEFINITIONS`: Configurable number entities
- `SELECT_DEFINITIONS`: Mode selection entities
- `SWITCH_DEFINITIONS`: Binary control entities

#### `modbus_coordinator.py`
Data coordination and polling logic:
- Manages Modbus connections
- Handles data polling and caching
- Implements error recovery
- Provides entity registration system

## 🧪 Development Workflow

### Development Commands

The project includes a `Makefile` for common development tasks:

```bash
# Install development dependencies
make install-dev

# Run linting checks
make lint

# Fix linting issues automatically
make lint-fix

# Format code
make format

# Check formatting without changes
make format-check

# Run tests
make test

# Run tests with coverage
make test-cov

# Run all checks (lint + format + test)
make check

# Run all fixes (lint-fix + format)
make fix
```

### Manual Tool Usage

```bash
# Linting with ruff (NEVER CANCEL - takes <1 second)
python3 -m ruff check .
python3 -m ruff check . --fix  # Auto-fix issues

# Code formatting (NEVER CANCEL - takes <1 second)
python3 -m ruff format .
python3 -m ruff format . --check  # Check only

# YAML validation (NEVER CANCEL - takes <1 second)
yamllint .

# Run tests (NEVER CANCEL - takes <1 second)
pytest
pytest -v  # Verbose output
pytest --cov  # With coverage report
```

### Pre-commit Validation

Always run before committing:

```bash
# Full validation pipeline
make check

# Or run individually
python3 -m ruff check .
python3 -m ruff format . --check
yamllint .
pytest
```

## 🧪 Testing Framework

### Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Test configuration and fixtures
├── test_manifest.py         # Manifest validation tests
├── test_const.py           # Constants and register tests
├── test_config_flow.py     # Configuration flow tests
├── test_integration.py     # Integration structure tests
├── test_modbus_simple.py   # Basic Modbus tests
└── test_repository.py      # Repository structure tests
```

### Test Categories

1. **Static Analysis Tests**:
   - Syntax validation for all Python files
   - Import verification
   - Manifest.json validation

2. **Structure Tests**:
   - Required file existence
   - Proper docstring presence
   - Register definition validation

3. **Configuration Tests**:
   - Config flow validation
   - Schema verification
   - Import availability

4. **Integration Tests**:
   - File structure validation
   - Cross-file import testing
   - No Home Assistant runtime required

### Running Specific Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_manifest.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=custom_components.epever_hi

# Run specific test function
pytest tests/test_const.py::test_register_definitions_structure
```

### Test Design Philosophy

The tests are designed to:
- ✅ **Work without Home Assistant**: Static analysis and syntax validation
- ✅ **Validate Code Quality**: Ensure consistent coding standards
- ✅ **Check Integration Structure**: Verify HA integration requirements
- ✅ **Fast Execution**: Complete test suite runs in <1 second
- ✅ **CI/CD Ready**: Automated validation in GitHub Actions

## 🔧 Architecture Overview

### Integration Components

#### Data Flow
```
EPEVER Hi Controller
         ↓
    Modbus TCP/RTU
         ↓
   ModbusClient (modbus_client.py)
         ↓
   ModbusCoordinator (modbus_coordinator.py)
         ↓
   Entity Platforms (sensor.py, number.py, etc.)
         ↓
   Home Assistant Core
```

#### Component Responsibilities

**ModbusClient** (`modbus_client.py`):
- Low-level Modbus communication
- Connection management
- Error handling and retries
- Support for both TCP and RTU

**ModbusCoordinator** (`modbus_coordinator.py`):
- High-level data coordination  
- Polling management
- Data caching and validation
- Entity registration system

**Entity Platforms** (`sensor.py`, `number.py`, etc.):
- Home Assistant entity creation
- Data formatting and validation
- State and attribute management
- User interface integration

**Configuration Flow** (`config_flow.py`):
- Integration setup UI
- Connection parameter validation
- Device discovery
- Configuration persistence

### Register System

The integration uses a sophisticated register definition system:

```python
# Example register definition
0x3580: {
    "key": "battery_voltage",
    "name": "Battery Voltage",
    "unit": "V",
    "scale": 0.01,
    "precision": 2,
    "device_class": "voltage",
    "readable": True,
    "writable": False,
    "min": 0,
    "max": 30,
    "data_type": "uint16",
}
```

**Key Features**:
- **Flexible Scaling**: Support for decimal scaling factors
- **Data Type Support**: uint16, int16, uint32 with word swapping
- **Validation**: Min/max ranges for writable registers
- **Home Assistant Integration**: Device classes, units, precision
- **Extensibility**: Easy to add new registers

## 🔌 Adding New Features

### Adding New Registers

1. **Update const.py**:
   ```python
   # Add to appropriate definitions dictionary
   SENSOR_DEFINITIONS_NEW = {
       # ... existing registers
       0x1234: {
           "key": "new_sensor",
           "name": "New Sensor",
           "unit": "V",
           "scale": 0.01,
           "precision": 2,
           "device_class": "voltage",
           "readable": True,
       }
   }
   ```

2. **Test the Register**:
   - Verify device supports the register
   - Test with manual Modbus tools
   - Validate data format and scaling

3. **Update Documentation**:
   - Add to Modbus Registers wiki page
   - Update Entities Reference if needed
   - Document any device-specific behavior

### Adding New Entity Types

1. **Create Entity Platform File**:
   ```python
   # custom_components/epever_hi/new_entity.py
   from homeassistant.components.new_entity import NewEntity
   from .modbus_coordinator import ModbusCoordinator
   ```

2. **Update `__init__.py`**:
   ```python
   PLATFORMS = [
       Platform.SENSOR,
       Platform.NUMBER,
       Platform.SELECT,
       Platform.SWITCH,
       Platform.BINARY_SENSOR,
       Platform.BUTTON,
       Platform.NEW_ENTITY,  # Add new platform
   ]
   ```

3. **Add Entity Definitions**:
   - Create definitions in `const.py`
   - Follow existing patterns for consistency

### Modifying Communication Logic

**ModbusClient Changes**:
- Connection handling improvements
- Error recovery enhancements
- Protocol extensions

**ModbusCoordinator Changes**:
- Polling optimization
- Caching improvements
- Data validation enhancements

## 🔍 Debugging and Testing

### Local Development Testing

#### Without Home Assistant
```bash
# Test syntax and structure
pytest

# Test Modbus communication directly
python3 -c "
from custom_components.epever_hi.modbus_client import ModbusClient
client = ModbusClient('192.168.1.100', 502, 1)
# Test basic connectivity
"
```

#### With Home Assistant Development
1. **Copy Integration**:
   ```bash
   cp -r custom_components/epever_hi ~/.homeassistant/custom_components/
   ```

2. **Enable Debug Logging**:
   ```yaml
   # configuration.yaml
   logger:
     default: info
     logs:
       custom_components.epever_hi: debug
   ```

3. **Test in UI**:
   - Add integration through UI
   - Monitor logs for errors
   - Test entity functionality

### Modbus Testing Tools

#### External Tools
```bash
# Test Modbus TCP connection
modpoll -m tcp -a 1 -r 0x3580 -c 1 192.168.1.100

# Test Modbus RTU connection  
modpoll -m rtu -a 1 -r 0x3580 -c 1 -b 9600 /dev/ttyUSB0

# Monitor RTU traffic
sudo cat /dev/ttyUSB0 | hexdump -C
```

#### Python Testing
```python
from pymodbus.client.sync import ModbusTcpClient

# Test specific register
client = ModbusTcpClient('192.168.1.100', port=502)
client.connect()
result = client.read_input_registers(0x3580, 1, unit=1)
print(f"Battery Voltage Raw: {result.registers[0]}")
print(f"Battery Voltage Scaled: {result.registers[0] * 0.01}V")
client.close()
```

## 📋 Code Style and Standards

### Coding Standards

**Python Style**:
- **PEP 8 Compliance**: Enforced by ruff
- **Type Hints**: Use where beneficial
- **Docstrings**: Required for all public functions
- **Error Handling**: Comprehensive exception handling

**Home Assistant Conventions**:
- **Entity IDs**: Use consistent naming patterns
- **Device Classes**: Use appropriate HA device classes
- **State Classes**: Implement for statistics support
- **Configuration**: Use config flow for UI setup

### Code Quality Tools

**Ruff Configuration** (pyproject.toml):
- Line length: 88 characters
- Import sorting
- Code formatting
- Linting rules

**YAML Lint Configuration** (.yamllint):
- Consistent indentation
- Line length limits
- Key ordering

## 🤝 Contributing Guidelines

### Pull Request Process

1. **Fork Repository**: Create your own fork
2. **Create Branch**: Use descriptive branch names
3. **Make Changes**: Follow coding standards
4. **Test Changes**: Run full test suite
5. **Update Documentation**: Update relevant wiki pages
6. **Submit PR**: Use PR template, provide clear description

### PR Requirements

- ✅ **All tests pass**: `make check` succeeds
- ✅ **Code formatted**: `ruff format` applied
- ✅ **Linting clean**: No `ruff check` errors
- ✅ **YAML valid**: `yamllint` passes
- ✅ **Documentation updated**: Wiki pages updated if needed
- ✅ **Backward compatibility**: Don't break existing functionality

### Issue Templates

The repository provides issue templates for:
- **Bug Reports**: Structured bug reporting
- **Feature Requests**: New feature proposals
- **Questions**: Support and usage questions

## 🔄 Release Process

### Version Management

**Versioning**: Follows semantic versioning (MAJOR.MINOR.PATCH)
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

**Version Locations**:
- `manifest.json`: Integration version
- Release tags: GitHub release tags
- CHANGELOG: Version history documentation

### CI/CD Pipeline

**GitHub Actions Workflows**:
1. **Validate** (`.github/workflows/validate.yml`):
   - Home Assistant hassfest validation
   - HACS validation
   - Integration structure checks

2. **Lint** (`.github/workflows/lint.yml`):
   - Ruff code checking and formatting
   - YAML validation
   - Code quality enforcement

3. **Test** (`.github/workflows/test.yml`):
   - Pytest execution on Python 3.12 and 3.13
   - Test coverage reporting
   - Integration testing

## 📚 Additional Resources

### Home Assistant Development

- **[HA Developer Documentation](https://developers.home-assistant.io/)**
- **[Integration Development](https://developers.home-assistant.io/docs/creating_integration)**
- **[Entity Development](https://developers.home-assistant.io/docs/core/entity)**

### Modbus Protocol

- **[Modbus Specification](https://modbus.org/specs.php)**
- **[PyModbus Documentation](https://pymodbus.readthedocs.io/)**
- **[EPEVER Modbus Protocol](https://www.epsolarpv.com/uploads/download/)**

### Development Tools

- **[VS Code Home Assistant Extension](https://marketplace.visualstudio.com/items?itemName=keesschollaart.vscode-home-assistant)**
- **[Home Assistant Dev Container](https://github.com/home-assistant/devcontainer)**
- **[HACS Development](https://hacs.xyz/docs/publish/start)**

## 🆕 Next Steps for Contributors

1. **Set Up Environment**: Follow development setup instructions
2. **Read Codebase**: Understand the architecture and patterns
3. **Run Tests**: Verify your environment with `make check`
4. **Pick Issues**: Look for "good first issue" labels
5. **Ask Questions**: Use GitHub discussions for clarification

For more detailed information, see:
- **[Troubleshooting](Troubleshooting)** - Debug common development issues
- **[API Reference](API-Reference)** - Technical API documentation
- **[Modbus Registers](Modbus-Registers)** - Register implementation details