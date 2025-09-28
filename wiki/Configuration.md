# Configuration Guide

After installing the EPEVER Hi integration, you need to configure it with your Modbus connection details. This guide covers all configuration options and common scenarios.

## 🎯 Quick Setup

1. **Add Integration**: Go to Settings → Devices & Services → Add Integration
2. **Search**: Type "EPEVER Hi" and select it
3. **Configure**: Enter your Modbus connection details
4. **Test**: Verify connection and device discovery
5. **Complete**: Integration will create all available entities

## 🔧 Configuration Parameters

### Modbus Connection Settings

#### Modbus TCP Configuration
For Modbus TCP connections (Ethernet or WiFi):

| Parameter | Description | Example | Required |
|-----------|-------------|---------|----------|
| **Host** | IP address of the charge controller | `192.168.1.100` | Yes |
| **Port** | Modbus TCP port (usually 502) | `502` | Yes |
| **Slave ID** | Modbus device address | `1` | Yes |
| **Name** | Friendly name for the integration | `Solar Controller` | No |

#### Modbus RTU Configuration
For Modbus RTU connections (RS485/Serial):

| Parameter | Description | Example | Required |
|-----------|-------------|---------|----------|
| **Serial Port** | Serial port path | `/dev/ttyUSB0` (Linux)<br>`COM3` (Windows) | Yes |
| **Baudrate** | Serial communication speed | `9600`, `19200`, `38400`, `115200` | Yes |
| **Bytesize** | Data bits | `8` | Yes |
| **Parity** | Parity checking | `None`, `Even`, `Odd` | Yes |
| **Stopbits** | Stop bits | `1`, `2` | Yes |
| **Slave ID** | Modbus device address | `1` | Yes |
| **Name** | Friendly name for the integration | `Solar Controller` | No |

### Advanced Settings

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| **Polling Interval** | How often to read data (seconds) | `30` | `5-300` |
| **Timeout** | Connection timeout (seconds) | `10` | `1-60` |
| **Retries** | Connection retry attempts | `3` | `1-10` |

## 📝 Step-by-Step Configuration

### TCP Configuration Example

1. **Add Integration**:
   - Go to Settings → Devices & Services
   - Click "Add Integration"
   - Search for "EPEVER Hi"

2. **Enter TCP Details**:
   ```
   Connection Type: Modbus TCP
   Host: 192.168.1.100
   Port: 502
   Slave ID: 1
   Name: Main Solar Controller
   ```

3. **Test Connection**:
   - Click "Submit"
   - Integration will attempt to connect
   - If successful, entities will be created

### RTU Configuration Example

1. **Prepare Serial Connection**:
   - Connect RS485 adapter to charge controller
   - Note the serial port path (e.g., `/dev/ttyUSB0`)

2. **Enter RTU Details**:
   ```
   Connection Type: Modbus RTU
   Serial Port: /dev/ttyUSB0
   Baudrate: 9600
   Bytesize: 8
   Parity: None
   Stopbits: 1
   Slave ID: 1
   Name: Solar Controller RTU
   ```

3. **Verify Connection**:
   - Check that the serial port is available
   - Ensure correct baudrate matches controller settings
   - Submit configuration

## 🔍 Finding Your Device Settings

### Determining Modbus Parameters

#### TCP Settings
- **IP Address**: Check your router's DHCP table or use network scanner
- **Port**: Default is 502 for Modbus TCP
- **Slave ID**: Usually 1, check device manual or try 1-247

#### RTU Settings
- **Serial Port**: 
  - Linux: Usually `/dev/ttyUSB0`, `/dev/ttyACM0`
  - Windows: Usually `COM1`, `COM3`, etc.
  - Check device manager or `dmesg` output
- **Baudrate**: Check device manual (common: 9600, 19200)
- **Other Serial Settings**: Usually 8N1 (8 data bits, no parity, 1 stop bit)

### Device Manual References
Consult your EPEVER Hi device manual for:
- Default Modbus address (slave ID)
- Supported baudrates
- Pinout for RS485 connections
- Network configuration options

## 🎛️ Integration Options

### Multiple Devices
You can add multiple EPEVER Hi controllers:

1. **Different Names**: Use unique names for each controller
2. **Different Addresses**: Each device needs a unique slave ID
3. **Same Connection**: Multiple devices can share TCP connection or serial bus
4. **Entity Separation**: Entities will be grouped by device name

Example multi-device setup:
```
Device 1: "Main Controller" (Slave ID 1)
Device 2: "Backup Controller" (Slave ID 2)  
Device 3: "Workshop Controller" (Slave ID 3)
```

### Polling Configuration
Adjust polling based on your needs:

- **Fast Updates** (5-10 seconds): Real-time monitoring, higher system load
- **Standard Updates** (30-60 seconds): Balanced performance, recommended
- **Slow Updates** (120-300 seconds): Minimal system impact, less responsive

### Entity Configuration
After adding the integration:

1. **Review Entities**: Check Settings → Devices & Services → EPEVER Hi
2. **Disable Unused**: Disable entities you don't need
3. **Customize Names**: Rename entities for clarity
4. **Set Areas**: Assign entities to appropriate areas/rooms

## 🔧 Hardware Setup

### TCP Connection Setup
1. **Network Connection**: Connect controller to your network via Ethernet or WiFi
2. **IP Configuration**: Assign static IP or note DHCP address
3. **Firewall**: Ensure port 502 is accessible
4. **Testing**: Use Modbus testing tools to verify connectivity

### RTU Connection Setup
1. **RS485 Adapter**: Use USB-to-RS485 or Ethernet-to-RS485 converter
2. **Wiring**: Connect A/B (or D+/D-) pins correctly
3. **Termination**: Add 120Ω resistors at bus ends if required
4. **Power**: Ensure adapter is properly powered
5. **Permissions**: On Linux, ensure user has access to serial port

## ⚠️ Common Configuration Issues

### Connection Problems
- **TCP Timeout**: Check IP address and network connectivity
- **RTU No Response**: Verify serial port, baudrate, and wiring
- **Wrong Slave ID**: Try different slave IDs (1-247)
- **Permission Denied**: Add user to dialout group on Linux

### Entity Creation Issues
- **No Entities Created**: Check device compatibility and Modbus registers
- **Partial Entities**: Some registers may not be supported by your device model
- **Error Values**: Invalid register addresses for your specific controller

### Performance Issues
- **High CPU Usage**: Increase polling interval
- **Timeout Errors**: Increase timeout value or check connection stability
- **Memory Usage**: Disable unused entities to reduce overhead

## 🔄 Reconfiguration

### Changing Settings
1. Go to Settings → Devices & Services
2. Find your EPEVER Hi integration
3. Click "Configure" to modify settings
4. Update parameters and submit
5. Integration will restart with new settings

### Removing and Re-adding
If needed, you can completely remove and re-add the integration:
1. Click "Delete" on the integration
2. Restart Home Assistant
3. Add integration again with new settings

## ✅ Verification

### Confirming Successful Configuration

1. **Check Integration Status**: Should show "Connected" or "OK"
2. **Review Entities**: All expected entities should be created
3. **Test Values**: Sensor values should update with polling interval
4. **Control Entities**: Test number/select controls if supported
5. **Logs**: No error messages in Home Assistant logs

### Entity Count Expectations
A typical EPEVER Hi integration creates:
- **40+ Sensors**: Voltage, current, power, temperature readings
- **5-10 Numbers**: Configurable setpoints and parameters
- **3-5 Selects**: Operation modes and settings
- **2-4 Binary Sensors**: Status indicators
- **1-2 Switches**: Control outputs
- **1-2 Buttons**: Action triggers

## 🆕 Next Steps

After successful configuration:
- **[Entities Reference](Entities-Reference)** - Explore all available entities
- **[Modbus Registers](Modbus-Registers)** - Understand the underlying data
- **[Troubleshooting](Troubleshooting)** - Resolve common issues