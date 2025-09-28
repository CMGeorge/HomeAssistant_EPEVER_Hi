# Modbus Registers Reference

This page provides a complete reference for all Modbus registers used by the EPEVER Hi Integration. The integration is based on official EPEVER Hi Modbus documentation.

## 📊 Register Overview

The integration supports four main register categories:
- **📈 Input Registers** (Read-only sensors and status)
- **🔧 Holding Registers** (Read/write configuration parameters)
- **💡 Coil Registers** (Binary on/off controls)
- **📋 Discrete Inputs** (Binary status indicators)

### Register Address Ranges

| Category | Address Range | Purpose | Access |
|----------|---------------|---------|---------|
| **Grid/Utility** | `0x3500-0x351F` | Grid voltage, current, power | Read |
| **Load Monitoring** | `0x3520-0x353F` | Load voltage, current, power | Read |
| **Battery System** | `0x3580-0x359F` | Battery voltage, current, SOC | Read |
| **System Status** | `0x3400-0x34FF` | Controller status, diagnostics | Read |
| **Configuration** | `0x9000-0x900F` | Battery settings, thresholds | Read/Write |
| **Operation Control** | `0x9600-0x960F` | Charging, inverter modes | Read/Write |
| **System Control** | `0x0001-0x000F` | Load control, system switches | Read/Write |

## 📈 Input Registers (Read-Only Sensors)

### Grid/Utility Sensors (0x3500-0x351F)

| Register | Entity | Unit | Scale | Device Class | Description |
|----------|--------|------|-------|--------------|-------------|
| `0x3500` | Grid Voltage | V | 0.01 | voltage | Grid input voltage |
| `0x3501` | Grid Current | A | 0.01 | current | Grid input current |
| `0x350F` | Grid Total Energy | kWh | 0.01 | energy | Total grid energy (32-bit) |
| `0x3511` | Grid State | - | 1 | - | Grid connection status |

### Load Monitoring (0x3520-0x353F)

| Register | Entity | Unit | Scale | Device Class | Description |
|----------|--------|------|-------|--------------|-------------|
| `0x3521` | Load Voltage | V | 0.01 | voltage | Load output voltage |
| `0x3522` | Load Current | A | 0.01 | current | Load output current |
| `0x3530` | Load Total Energy | kWh | 0.01 | energy | Total load energy (32-bit) |
| `0x3533` | Inverter Temperature | °C | 0.01 | temperature | Inverter temperature |

### Battery System (0x3580-0x359F)

| Register | Entity | Unit | Scale | Device Class | Description |
|----------|--------|------|-------|--------------|-------------|
| `0x3580` | Battery Voltage | V | 0.01 | voltage | Battery terminal voltage |
| `0x3581` | Battery Current | A | 0.01 | current | Battery charge/discharge current |
| `0x3586` | Battery Capacity | % | 1 | battery | State of charge (SOC) |
| `0x3589` | Battery State | - | 1 | - | Battery status code |
| `0x3512` | Battery Temperature | °C | 0.01 | temperature | Battery temperature |

## 🔧 Holding Registers (Configuration Parameters)

### Battery Configuration (0x9000-0x900F)

| Register | Entity | Unit | Scale | Range | Description |
|----------|--------|------|-------|-------|-------------|
| `0x9000` | Battery Type | - | 1 | 1-7 | Battery chemistry type |
| `0x9001` | Battery Capacity | Ah | 1 | 1-1000 | Rated battery capacity |
| `0x9002` | Temp Compensation | mV/°C/2V | 1 | 0-9 | Temperature compensation |
| `0x9003` | Over Voltage Disconnect | V | 0.01 | 9-17 | High voltage disconnect |
| `0x9004` | Charging Limit Voltage | V | 0.01 | 9-17 | Maximum charge voltage |
| `0x9005` | Over Voltage Reconnect | V | 0.01 | 9-17 | High voltage reconnect |
| `0x9006` | Equalization Voltage | V | 0.01 | 9-17 | Equalization charge voltage |
| `0x9007` | Boost Voltage | V | 0.01 | 9-17 | Boost charge voltage |
| `0x9008` | Float Voltage | V | 0.01 | 9-17 | Float charge voltage |
| `0x9009` | Boost Reconnect Voltage | V | 0.01 | 9-17 | Boost reconnect voltage |
| `0x900A` | Low Voltage Reconnect | V | 0.01 | 9-17 | Low voltage reconnect |
| `0x900B` | Under Voltage Recover | V | 0.01 | 9-17 | Under voltage recovery |
| `0x900C` | Under Voltage Warning | V | 0.01 | 9-17 | Under voltage warning |
| `0x900D` | Low Voltage Disconnect | V | 0.01 | 9-17 | Low voltage disconnect |
| `0x900E` | Discharging Limit Voltage | V | 0.01 | 9-17 | Minimum discharge voltage |

### Operation Control (0x9600-0x960F)

| Register | Entity | Unit | Scale | Range | Description |
|----------|--------|------|-------|-------|-------------|
| `0x9607` | Charging Mode | - | 1 | 0-10 | Charging algorithm mode |
| `0x9608` | Inverter Mode | - | 1 | 0-10 | Inverter operation mode |

## 💡 Coil Registers (Binary Controls)

### System Control (0x0001-0x000F)

| Register | Entity | Type | Access | Description |
|----------|--------|------|--------|-------------|
| `0x0002` | Manual Control Load | Switch | R/W | Manual load control enable |
| `0x0005` | Enable Load Test | Switch | R/W | Load testing mode enable |

## 📋 Data Types and Formats

### Numeric Data Types

| Type | Size | Description | Example Registers |
|------|------|-------------|-------------------|
| **uint16** | 16-bit | Single register unsigned integer | Most sensor values |
| **int16** | 16-bit | Single register signed integer | Temperature (with offset) |
| **uint32** | 32-bit | Two registers, word-swapped | Energy totals (0x350F, 0x3530) |

### Scale Factors

| Scale | Purpose | Example | Raw → Actual |
|-------|---------|---------|---------------|
| **1** | Direct values | Battery capacity (%) | 85 → 85% |
| **0.01** | Two decimal places | Voltage, current | 1250 → 12.50V |
| **0.001** | Three decimal places | High-precision values | 12500 → 12.500V |

### Word Swapping (32-bit Values)
For 32-bit registers like energy totals:
- **Raw registers**: [High Word, Low Word]
- **Word swapped**: [Low Word, High Word]
- **Final value**: (High Word << 16) + Low Word

## 🎛️ Register Categories by Entity Type

### Sensors (Read-Only)
- **Voltage Sensors**: Battery, grid, load voltages
- **Current Sensors**: Battery, grid, load currents  
- **Power Sensors**: Calculated from voltage × current
- **Energy Sensors**: Cumulative energy totals (32-bit)
- **Temperature Sensors**: Battery, inverter temperatures
- **Status Sensors**: System state indicators

### Numbers (Configurable Values)
- **Voltage Thresholds**: Charge, discharge, warning levels
- **Battery Settings**: Capacity, type, compensation
- **Timing Parameters**: Charge durations, delays

### Selects (Mode Selection)
- **Charging Mode**: PWM, MPPT algorithms
- **Inverter Mode**: Auto, manual, priority settings
- **Battery Type**: Lead-acid, lithium, gel, AGM

### Switches (Binary Controls)
- **Load Control**: Manual load enable/disable
- **Test Modes**: Load testing, diagnostics
- **System Functions**: Reset, calibration

### Binary Sensors (Status Indicators)
- **System Status**: Online, charging, error states
- **Alarm Status**: Fault conditions, warnings
- **Connection Status**: Grid, battery, load connections

## ⚠️ Register Access Notes

### Read-Only Registers
- **Input Registers**: System status and measurements
- **Cannot be modified**: Attempting to write will cause errors
- **Polling Frequency**: Updated based on integration polling interval

### Read-Write Registers
- **Configuration Parameters**: Battery settings, thresholds
- **Operation Modes**: Charging, inverter control
- **Validation**: Values are validated against min/max ranges
- **Persistence**: Changes are saved to controller memory

### Register Timing
- **Read Interval**: Default 30 seconds (configurable)
- **Write Response**: Immediate for most registers
- **Batch Operations**: Multiple registers read in single operation
- **Error Handling**: Automatic retry on communication failures

## 🔍 Advanced Register Details

### Battery Type Codes (Register 0x9000)
| Value | Battery Type | Description |
|-------|-------------|-------------|
| 1 | User | User-defined parameters |
| 2 | Sealed | Sealed lead-acid |
| 3 | Gel | Gel electrolyte |
| 4 | Flooded | Flooded lead-acid |
| 5 | Lithium | Lithium-ion |
| 6 | AGM | Absorbed Glass Mat |
| 7 | Custom | Custom profile |

### Charging Mode Codes (Register 0x9607)
| Value | Mode | Description |
|-------|------|-------------|
| 0 | PWM | Pulse Width Modulation |
| 1 | MPPT | Maximum Power Point Tracking |
| 2 | Auto | Automatic algorithm selection |
| 3 | Manual | Manual control mode |

### System Status Codes
Various status registers return numeric codes:
- **0**: Normal/OK
- **1-10**: Information states
- **11-20**: Warning states  
- **21+**: Error/fault states

## 🛠️ Troubleshooting Register Issues

### Communication Problems
- **Timeout Errors**: Increase timeout in configuration
- **Invalid Register**: Check device model compatibility
- **Permission Errors**: Verify read/write permissions

### Value Interpretation
- **Scale Factors**: Ensure correct scaling applied
- **Signed/Unsigned**: Check for negative value handling
- **Word Order**: Verify 32-bit value byte ordering

### Register Validation
- **Range Checking**: Values must be within min/max limits
- **Data Type**: Ensure correct data type interpretation  
- **Device Support**: Not all registers supported by all models

## 🆕 Extending Register Support

### Adding New Registers
To add support for additional registers:

1. **Update const.py**: Add register definition to appropriate dictionary
2. **Specify Parameters**: Include scale, range, data type
3. **Test Communication**: Verify register accessibility
4. **Update Documentation**: Add to this reference page

### Register Definition Format
```python
0x1234: {
    "key": "unique_identifier",
    "name": "Display Name",
    "unit": "V",  # Unit of measurement
    "scale": 0.01,  # Raw value multiplier
    "precision": 2,  # Decimal places
    "device_class": "voltage",  # HA device class
    "readable": True,
    "writable": False,  # Set True for configurable registers
    "min": 0,  # Minimum value (for writable)
    "max": 100,  # Maximum value (for writable)
    "data_type": "uint16",  # Optional: specify data type
    "swap": "word",  # Optional: for 32-bit values
}
```

## 📚 Related Documentation

- **[Entities Reference](Entities-Reference)** - See how registers become Home Assistant entities
- **[Configuration](Configuration)** - Set up Modbus communication
- **[Troubleshooting](Troubleshooting)** - Resolve register communication issues