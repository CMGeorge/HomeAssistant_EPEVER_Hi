# API Reference

This page provides technical API documentation for the EPEVER Hi Integration, including internal APIs, service calls, and integration interfaces.

## 🏗️ Integration Architecture

### Core Components

The integration consists of several interconnected components:

```python
# Component hierarchy
EPEVERHiIntegration
├── ModbusClient          # Low-level Modbus communication
├── ModbusCoordinator     # Data coordination and polling
├── ConfigFlow           # Configuration UI flow
└── EntityPlatforms      # Home Assistant entities
    ├── SensorPlatform
    ├── NumberPlatform  
    ├── SelectPlatform
    ├── SwitchPlatform
    ├── BinarySensorPlatform
    └── ButtonPlatform
```

### Integration Entry Point

**File**: `custom_components/epever_hi/__init__.py`

#### `async_setup_entry(hass, entry)`
Main integration setup function called by Home Assistant.

**Parameters**:
- `hass`: Home Assistant instance
- `entry`: ConfigEntry object with user configuration

**Returns**: `bool` - Success status

**Functionality**:
- Creates ModbusCoordinator instance
- Sets up entity platforms
- Registers update listeners
- Handles integration lifecycle

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up EPEVER Hi from a config entry."""
    coordinator = ModbusCoordinator(hass, entry.data)
    await coordinator.async_config_entry_first_refresh()
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

#### `async_unload_entry(hass, entry)`
Integration cleanup function.

**Parameters**:
- `hass`: Home Assistant instance  
- `entry`: ConfigEntry being removed

**Returns**: `bool` - Unload success status

## 📡 Modbus Client API

**File**: `custom_components/epever_hi/modbus_client.py`

### ModbusClient Class

#### `__init__(self, host, port, slave_id, timeout=10, retries=3)`
Initialize Modbus client connection.

**Parameters**:
- `host`: IP address (TCP) or serial port path (RTU)
- `port`: TCP port number or baudrate for RTU
- `slave_id`: Modbus device address (1-247)
- `timeout`: Connection timeout in seconds
- `retries`: Number of retry attempts

#### `async def connect(self) -> bool`
Establish Modbus connection.

**Returns**: `bool` - Connection success status

**Raises**:
- `ConnectionException`: Failed to connect
- `ModbusException`: Protocol-level error

#### `async def read_registers(self, address, count, register_type="input") -> list`
Read multiple registers from device.

**Parameters**:
- `address`: Starting register address (hex or int)
- `count`: Number of registers to read
- `register_type`: "input", "holding", "coil", or "discrete"

**Returns**: `list[int]` - Register values

**Example**:
```python
# Read battery voltage register
values = await client.read_registers(0x3580, 1, "input")
voltage = values[0] * 0.01  # Apply scale factor
```

#### `async def write_register(self, address, value, register_type="holding") -> bool`
Write single register to device.

**Parameters**:
- `address`: Register address
- `value`: Value to write
- `register_type`: "holding" or "coil"

**Returns**: `bool` - Write success status

#### `async def disconnect(self)`
Close Modbus connection and cleanup resources.

### Error Handling

**Custom Exceptions**:
```python
class ModbusConnectionError(Exception):
    """Raised when Modbus connection fails."""
    
class ModbusTimeoutError(Exception):
    """Raised when Modbus operation times out."""
    
class ModbusProtocolError(Exception):  
    """Raised for Modbus protocol errors."""
```

## 🎛️ Coordinator API

**File**: `custom_components/epever_hi/modbus_coordinator.py`

### ModbusCoordinator Class
Extends Home Assistant's `DataUpdateCoordinator`.

#### `__init__(self, hass, config)`
Initialize coordinator with configuration.

**Parameters**:
- `hass`: Home Assistant instance
- `config`: Integration configuration dictionary

#### `async def _async_update_data(self) -> dict`
Core data polling method called by coordinator.

**Returns**: `dict` - All sensor data keyed by register address

**Process**:
1. Connect to Modbus device
2. Read all registered sensor addresses
3. Apply scaling and validation
4. Return formatted data dictionary

#### `def register_entity(self, address, entity_type)`
Register entity for data polling.

**Parameters**:
- `address`: Modbus register address
- `entity_type`: Type of entity ("sensor", "number", etc.)

**Usage**:
```python
# Called by entity platforms during setup
coordinator.register_entity(0x3580, "sensor")
```

#### `async def write_register_value(self, address, value) -> bool`
Write value to device register with validation.

**Parameters**:
- `address`: Register address to write
- `value`: Scaled value to write

**Returns**: `bool` - Write success status

**Features**:
- Value validation against min/max ranges
- Automatic scaling application  
- Error handling and logging
- Entity state updates

### Data Processing

#### `def process_register_value(self, address, raw_value) -> any`
Process raw register value according to definition.

**Parameters**:
- `address`: Register address
- `raw_value`: Raw integer value from device

**Returns**: Scaled and formatted value

**Processing Steps**:
1. Apply data type conversion (uint16, int16, uint32)
2. Handle word swapping for 32-bit values
3. Apply scale factor
4. Format precision
5. Validate ranges

## 🔧 Configuration Flow API

**File**: `custom_components/epever_hi/config_flow.py`

### EPEVERHiConfigFlow Class
Extends Home Assistant's `ConfigFlow`.

#### `async def async_step_user(self, user_input=None)`
Handle initial configuration step.

**Parameters**:
- `user_input`: User-provided configuration data

**Returns**: Configuration flow result

**Flow Steps**:
1. Display connection type selection
2. Collect TCP or RTU parameters  
3. Test connection
4. Create config entry

#### Connection Schemas

**TCP Configuration Schema**:
```python
TCP_SCHEMA = vol.Schema({
    vol.Required("host"): str,
    vol.Required("port", default=502): int,
    vol.Required("slave_id", default=1): vol.Range(min=1, max=247),
    vol.Optional("name", default="EPEVER Hi"): str,
    vol.Optional("polling_interval", default=30): vol.Range(min=5, max=300),
})
```

**RTU Configuration Schema**:
```python
RTU_SCHEMA = vol.Schema({
    vol.Required("serial_port"): str,
    vol.Required("baudrate", default=9600): vol.In([9600, 19200, 38400, 115200]),
    vol.Required("bytesize", default=8): vol.In([7, 8]),
    vol.Required("parity", default="N"): vol.In(["N", "E", "O"]),
    vol.Required("stopbits", default=1): vol.In([1, 2]),
    vol.Required("slave_id", default=1): vol.Range(min=1, max=247),
    vol.Optional("name", default="EPEVER Hi"): str,
})
```

#### `async def test_connection(self, config) -> bool`
Test Modbus connection with provided configuration.

**Parameters**:
- `config`: Connection configuration dictionary

**Returns**: `bool` - Connection test result

## 🏷️ Entity Platform APIs

### Base Entity Classes

#### EPEVERHiEntity
Base class for all EPEVER Hi entities.

**Attributes**:
- `coordinator`: ModbusCoordinator instance
- `address`: Modbus register address
- `definition`: Register definition from const.py

**Properties**:
```python
@property
def device_info(self) -> DeviceInfo:
    """Return device information."""
    
@property  
def unique_id(self) -> str:
    """Return unique ID for entity."""
    
@property
def available(self) -> bool:
    """Return entity availability."""
```

### Sensor Platform

**File**: `custom_components/epever_hi/sensor.py`

#### EPEVERHiSensor Class
Sensor entity for read-only measurements.

**Key Methods**:
```python
@property
def native_value(self) -> float | int | str:
    """Return sensor value."""
    
@property
def device_class(self) -> str:
    """Return device class (voltage, current, etc.)."""
    
@property
def native_unit_of_measurement(self) -> str:
    """Return unit of measurement."""
```

### Number Platform

**File**: `custom_components/epever_hi/number.py`

#### EPEVERHiNumber Class
Number entity for configurable parameters.

**Key Methods**:
```python
async def async_set_native_value(self, value: float) -> None:
    """Set number value."""
    
@property
def native_min_value(self) -> float:
    """Return minimum value."""
    
@property
def native_max_value(self) -> float:
    """Return maximum value."""
```

### Select Platform

**File**: `custom_components/epever_hi/select.py`

#### EPEVERHiSelect Class
Select entity for mode selections.

**Key Methods**:
```python
async def async_select_option(self, option: str) -> None:
    """Select option."""
    
@property
def options(self) -> list[str]:
    """Return available options."""
    
@property
def current_option(self) -> str:
    """Return current selection."""
```

## 📊 Data Structures

### Register Definitions

**Structure in const.py**:
```python
SENSOR_DEFINITIONS_NEW = {
    0x3580: {  # Register address (hex)
        "key": "battery_voltage",           # Unique identifier
        "name": "Battery Voltage",          # Display name
        "unit": "V",                       # Unit of measurement
        "scale": 0.01,                     # Raw value multiplier
        "precision": 2,                    # Decimal places
        "device_class": "voltage",         # HA device class
        "readable": True,                  # Can read from register
        "writable": False,                 # Can write to register
        "min": 0,                         # Minimum value (writable only)
        "max": 30,                        # Maximum value (writable only)
        "data_type": "uint16",            # Optional: data type
        "swap": "word",                   # Optional: byte swapping
        "register_type": "input",         # Register type
        "entity_category": "diagnostic",   # Optional: HA entity category
    }
}
```

### Configuration Data

**Config Entry Data Structure**:
```python
{
    "connection_type": "tcp",  # or "rtu"
    "host": "192.168.1.100",   # TCP only
    "port": 502,               # TCP only
    "serial_port": "/dev/ttyUSB0",  # RTU only
    "baudrate": 9600,          # RTU only
    "slave_id": 1,
    "name": "EPEVER Hi",
    "polling_interval": 30,
    "timeout": 10,
}
```

### Coordinator Data Format

**Data Dictionary Structure**:
```python
{
    0x3580: 1250,    # Raw register values
    0x3581: -50,     # Negative for discharging
    0x3586: 85,      # Battery SOC percentage
    # ... more register values
}
```

## 🔌 Service Calls

### Custom Services

The integration can define custom services for advanced functionality:

#### `epever_hi.write_register`
Write value to specific register.

**Parameters**:
- `entity_id`: Target device entity
- `register`: Register address (hex string or int)
- `value`: Value to write

**Example**:
```yaml
service: epever_hi.write_register
data:
  entity_id: number.battery_capacity
  register: "0x9001"
  value: 200
```

#### `epever_hi.read_register`
Read value from specific register.

**Parameters**:
- `entity_id`: Target device entity  
- `register`: Register address
- `count`: Number of registers (default: 1)

## 🎯 Event System

### Integration Events

The integration can fire Home Assistant events for important occurrences:

#### `epever_hi_connection_lost`
Fired when Modbus connection is lost.

**Event Data**:
```python
{
    "device_id": "unique_device_identifier",
    "error": "Connection timeout",
    "timestamp": "2024-01-15T10:30:00Z"
}
```

#### `epever_hi_alarm_triggered`
Fired for device alarm conditions.

**Event Data**:
```python
{
    "device_id": "unique_device_identifier", 
    "alarm_type": "battery_low_voltage",
    "alarm_value": 11.2,
    "threshold": 11.5
}
```

## 🔍 Debugging APIs

### Debug Information

#### Device Diagnostics
The integration provides diagnostics data for debugging:

**Diagnostics Structure**:
```python
{
    "config": {
        "connection_type": "tcp",
        "host": "192.168.1.100",
        # ... sanitized config
    },
    "coordinator": {
        "last_update": "2024-01-15T10:30:00Z",
        "update_count": 150,
        "error_count": 2,
        "available": True
    },
    "registers": {
        "read_count": 1500,
        "write_count": 5,
        "error_registers": [0x1234],
        "last_values": {
            0x3580: 1250,
            # ... register values
        }
    }
}
```

### Logging Integration

**Log Levels and Categories**:
```python
# Enable debug logging in configuration.yaml
logger:
  logs:
    custom_components.epever_hi: debug
    custom_components.epever_hi.modbus_client: debug
    custom_components.epever_hi.coordinator: debug
```

**Log Message Format**:
```
2024-01-15 10:30:00.000 DEBUG (MainThread) [custom_components.epever_hi.coordinator] 
Register 0x3580: raw=1250, scaled=12.50V
```

## 🔧 Extension Points

### Adding Custom Register Processing

**Custom Processing Function**:
```python
def custom_register_processor(address: int, raw_value: int, definition: dict) -> any:
    """Custom processing for specific registers."""
    if address == 0x1234:  # Custom register
        # Apply custom logic
        return custom_calculation(raw_value)
    return None  # Use default processing
```

### Custom Entity Classes

**Extending Base Entity**:
```python
class CustomEPEVERHiEntity(EPEVERHiEntity):
    """Custom entity with extended functionality."""
    
    @property
    def extra_state_attributes(self) -> dict:
        """Return additional state attributes."""
        return {
            "raw_value": self.coordinator.data.get(self.address),
            "last_update": self.coordinator.last_update_success,
        }
```

## 📋 Integration Manifest

**File**: `custom_components/epever_hi/manifest.json`

```json
{
    "domain": "epever_hi",
    "name": "EPEVER Hi",
    "codeowners": ["@cmgeorge"],
    "config_flow": true,
    "dependencies": ["modbus"],
    "documentation": "https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi",
    "integration_type": "hub",
    "iot_class": "local_polling",
    "issue_tracker": "https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/issues",
    "requirements": ["pymodbus>=3.0.0"],
    "version": "1.0.0"
}
```

**Key Properties**:
- **domain**: Unique integration identifier
- **config_flow**: Supports UI configuration
- **dependencies**: Requires Home Assistant modbus component
- **integration_type**: Hub-style integration (manages multiple entities)
- **iot_class**: Local polling (no cloud dependency)

## 🆕 API Usage Examples

### Reading Sensor Data Programmatically

```python
# In Home Assistant automation or script
battery_voltage = hass.states.get("sensor.battery_voltage")
if battery_voltage and float(battery_voltage.state) < 11.5:
    # Battery low - take action
    pass
```

### Writing Configuration Values

```python
# Via service call in automation
await hass.services.async_call(
    "number", "set_value",
    {
        "entity_id": "number.battery_capacity",
        "value": 200
    }
)
```

### Accessing Raw Coordinator Data

```python
# In custom component or integration
coordinator = hass.data[DOMAIN][entry_id]
raw_voltage = coordinator.data.get(0x3580)  # Raw register value
scaled_voltage = raw_voltage * 0.01  # Apply scaling
```

## 📚 Related Documentation

- **[Development](Development)** - Development setup and contribution guidelines
- **[Modbus Registers](Modbus-Registers)** - Complete register reference
- **[Entities Reference](Entities-Reference)** - Entity usage and examples
- **[Configuration](Configuration)** - Integration setup and configuration