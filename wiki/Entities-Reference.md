# Entities Reference

This page provides a comprehensive reference for all Home Assistant entities created by the EPEVER Hi Integration. Each entity corresponds to specific Modbus registers and provides different types of data and control.

## 📊 Entity Overview

The integration creates **40+ entities** across multiple categories:

| Entity Type | Count | Purpose | Examples |
|-------------|--------|---------|----------|
| **Sensors** | 25-30 | Read-only measurements | Voltage, current, power, temperature |
| **Numbers** | 8-12 | Configurable parameters | Battery settings, voltage thresholds |
| **Selects** | 2-4 | Mode selections | Charging mode, inverter mode |
| **Binary Sensors** | 3-5 | Status indicators | System status, alarms |
| **Switches** | 2-3 | Binary controls | Load control, test modes |
| **Buttons** | 1-2 | Action triggers | Reset functions |

## 🔋 Battery Entities

### Battery Monitoring Sensors

| Entity ID | Name | Unit | Device Class | Description |
|-----------|------|------|--------------|-------------|
| `sensor.battery_voltage` | Battery Voltage | V | voltage | Current battery terminal voltage |
| `sensor.battery_current` | Battery Current | A | current | Charge (+) or discharge (-) current |
| `sensor.battery_capacity` | Battery Capacity | % | battery | State of charge (SOC) |
| `sensor.battery_temp` | Battery Temperature | °C | temperature | Battery temperature |
| `sensor.battery_state` | Battery State | - | - | Battery status code |

### Battery Configuration Numbers

| Entity ID | Name | Unit | Range | Description |
|-----------|------|------|-------|-------------|
| `number.battery_capacity` | Battery Capacity | Ah | 1-1000 | Rated battery capacity |
| `number.over_voltage_disconnect` | Over Voltage Disconnect | V | 9-17 | High voltage protection |
| `number.charging_limit_voltage` | Charging Limit Voltage | V | 9-17 | Maximum charge voltage |
| `number.float_voltage` | Float Voltage | V | 9-17 | Float charge voltage |
| `number.boost_voltage` | Boost Voltage | V | 9-17 | Boost charge voltage |
| `number.low_voltage_disconnect` | Low Voltage Disconnect | V | 9-17 | Low voltage cutoff |
| `number.under_voltage_recover` | Under Voltage Recovery | V | 9-17 | Recovery voltage |

### Battery Type Selection

| Entity ID | Options | Description |
|-----------|---------|-------------|
| `select.battery_type` | User, Sealed, Gel, Flooded, Lithium, AGM, Custom | Battery chemistry selection |

## ⚡ Solar/Grid Entities  

### Grid Monitoring Sensors

| Entity ID | Name | Unit | Device Class | Description |
|-----------|------|------|--------------|-------------|
| `sensor.grid_voltage` | Grid Voltage | V | voltage | AC grid input voltage |
| `sensor.grid_current` | Grid Current | A | current | AC grid input current |
| `sensor.grid_total` | Grid Total Energy | kWh | energy | Cumulative grid energy |
| `sensor.grid_state` | Grid State | - | - | Grid connection status |

## 🔌 Load Entities

### Load Monitoring Sensors

| Entity ID | Name | Unit | Device Class | Description |
|-----------|------|------|--------------|-------------|
| `sensor.load_voltage` | Load Voltage | V | voltage | DC load output voltage |
| `sensor.load_current` | Load Current | A | current | DC load current consumption |
| `sensor.load_total` | Load Total Energy | kWh | energy | Cumulative load energy |

### Load Control

| Entity ID | Name | Type | Description |
|-----------|------|------|-------------|
| `switch.manual_control_load` | Manual Load Control | Switch | Enable/disable manual load control |
| `switch.enable_load_test` | Load Test Mode | Switch | Enable load testing mode |

## 🌡️ Temperature Entities

| Entity ID | Name | Unit | Device Class | Description |
|-----------|------|------|--------------|-------------|
| `sensor.battery_temp` | Battery Temperature | °C | temperature | Battery temperature sensor |
| `sensor.inverter_temp` | Inverter Temperature | °C | temperature | Power inverter temperature |

## ⚙️ System Control Entities

### Operation Mode Selection

| Entity ID | Name | Options | Description |
|-----------|------|---------|-------------|
| `select.charging_mode` | Charging Mode | PWM, MPPT, Auto, Manual | Charging algorithm selection |
| `select.inverter_mode` | Inverter Mode | Auto, Manual, Priority | Inverter operation mode |

### System Configuration Numbers

| Entity ID | Name | Unit | Range | Description |
|-----------|------|------|-------|-------------|
| `number.temp_compensation` | Temperature Compensation | mV/°C/2V | 0-9 | Battery temperature compensation |
| `number.equalization_voltage` | Equalization Voltage | V | 9-17 | Battery equalization voltage |
| `number.boost_reconnect_voltage` | Boost Reconnect Voltage | V | 9-17 | Boost charge reconnect threshold |

## 🚨 Status and Diagnostic Entities

### Binary Status Sensors

| Entity ID | Name | Device Class | Description |
|-----------|------|--------------|-------------|
| `binary_sensor.system_status` | System Status | connectivity | Overall system health |
| `binary_sensor.charging_active` | Charging Active | battery_charging | Battery charging indicator |
| `binary_sensor.grid_connected` | Grid Connected | connectivity | Grid connection status |
| `binary_sensor.load_active` | Load Active | power | Load output status |

### Diagnostic Sensors

| Entity ID | Name | Unit | Category | Description |
|-----------|------|------|----------|-------------|
| `sensor.battery_state` | Battery State | - | diagnostic | Battery status code |
| `sensor.grid_state` | Grid State | - | diagnostic | Grid status code |

## 🏷️ Entity Categories

Entities are organized into Home Assistant categories for better organization:

### Config Category
Configuration parameters that users might need to adjust:
- Battery settings (capacity, type, voltages)
- Temperature compensation
- Charging parameters

### Diagnostic Category  
Technical information for troubleshooting:
- Status codes
- System states
- Error conditions

### Default Category
Primary operational data shown by default:
- Voltage and current readings
- Power measurements
- Temperature sensors
- Energy totals

## 🎨 Entity Properties

### Device Classes
Entities use appropriate Home Assistant device classes:
- **voltage**: Voltage sensors with V unit
- **current**: Current sensors with A unit  
- **power**: Power sensors with W unit
- **energy**: Energy sensors with Wh/kWh units
- **temperature**: Temperature sensors with °C unit
- **battery**: Battery percentage sensors

### State Classes
For energy tracking and statistics:
- **measurement**: Instantaneous values (voltage, current)
- **total_increasing**: Cumulative totals (energy counters)
- **total**: Resettable totals

### Icons
Custom icons for better visualization:
- **🔋** Battery-related entities
- **⚡** Power and electrical entities
- **🌡️** Temperature entities
- **🔌** Load and output entities
- **⚙️** Configuration entities

## 📈 Entity Value Processing

### Scaling and Precision
Raw Modbus values are scaled and formatted:

```python
# Example: Battery voltage
Raw Value: 1250 (from register 0x3580)
Scale: 0.01
Final Value: 12.50V
Precision: 2 decimal places
```

### Data Validation
- **Range checking**: Values validated against expected ranges
- **Error handling**: Invalid values reported as unavailable
- **Unit conversion**: Automatic unit standardization

### Update Frequency
- **Polling interval**: Default 30 seconds (configurable)
- **Batch updates**: Multiple entities updated simultaneously
- **Error recovery**: Automatic reconnection on communication failures

## 🔧 Entity Customization

### Disabling Unused Entities
1. Go to Settings → Devices & Services → EPEVER Hi
2. Click on the device
3. Find entities you don't need
4. Toggle "Enabled" switch to disable

### Renaming Entities
1. Click on entity in device page
2. Click settings gear icon
3. Change "Name" field
4. Entity ID can also be customized

### Entity Areas
Assign entities to rooms/areas:
1. Open entity settings
2. Select appropriate area from dropdown
3. Entities will appear in area dashboards

## 📊 Using Entities in Dashboards

### Recommended Cards

**Energy Dashboard**
- Add battery capacity sensor to energy dashboard
- Include solar and grid energy totals
- Monitor load consumption

**Gauge Cards**
- Battery voltage and SOC
- System temperatures  
- Current measurements

**Entity Cards**
- Battery configuration numbers
- System mode selects
- Control switches

**History Graphs**
- Voltage and current trends
- Temperature monitoring
- Energy consumption patterns

### Example Dashboard Configuration

```yaml
type: entities
title: EPEVER Hi Solar System
entities:
  - entity: sensor.battery_voltage
  - entity: sensor.battery_capacity
  - entity: sensor.battery_current
  - entity: sensor.grid_voltage
  - entity: sensor.load_current
  - type: divider
  - entity: select.charging_mode
  - entity: switch.manual_control_load
```

## 🤖 Automation Examples

### Low Battery Alert
```yaml
trigger:
  - platform: numeric_state
    entity_id: sensor.battery_capacity
    below: 20
action:
  - service: notify.mobile_app
    data:
      title: "Low Battery Alert"
      message: "Solar battery is at {{ states('sensor.battery_capacity') }}%"
```

### Automatic Load Control
```yaml
trigger:
  - platform: numeric_state
    entity_id: sensor.battery_voltage
    below: 11.5
action:
  - service: switch.turn_off
    target:
      entity_id: switch.manual_control_load
```

### Temperature Monitoring
```yaml
trigger:
  - platform: numeric_state
    entity_id: sensor.battery_temp
    above: 45
action:
  - service: persistent_notification.create
    data:
      title: "High Battery Temperature"
      message: "Battery temperature is {{ states('sensor.battery_temp') }}°C"
```

## 🏷️ Entity Naming Conventions

### Standard Format
Entities follow consistent naming:
- **Sensors**: `sensor.[device]_[measurement]`
- **Numbers**: `number.[setting]_[parameter]`  
- **Selects**: `select.[setting]_[type]`
- **Switches**: `switch.[function]_[control]`

### Multi-Device Support
With multiple controllers:
- **Device Name Prefix**: Entities include device name
- **Unique IDs**: Each device has unique entity IDs
- **Area Assignment**: Different devices can be in different areas

Example with two controllers:
```
sensor.main_controller_battery_voltage
sensor.backup_controller_battery_voltage
```

## 🔍 Troubleshooting Entities

### Missing Entities
- **Device Compatibility**: Not all registers supported by all models
- **Communication Errors**: Check Modbus connection
- **Integration Restart**: Restart integration after configuration changes

### Unavailable Entities
- **Connection Issues**: Modbus communication problems  
- **Register Errors**: Invalid register addresses
- **Device Offline**: Controller not responding

### Incorrect Values
- **Scaling Issues**: Check register scale factors
- **Unit Conversion**: Verify unit interpretations
- **Device Configuration**: Check controller settings

## 📚 Related Documentation

- **[Modbus Registers](Modbus-Registers)** - Technical register details
- **[Configuration](Configuration)** - Setup and connection configuration  
- **[Troubleshooting](Troubleshooting)** - Resolve entity issues