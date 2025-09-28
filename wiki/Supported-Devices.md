# Supported Devices

This integration is designed for EPEVER Hi series solar charge controllers that support Modbus communication. This page lists compatible devices and their specific features.

## 🎯 Primary Target Devices

### EPEVER Hi Series
The integration is specifically developed and tested for the **EPEVER Hi** series of solar charge controllers:

- **EPEVER Hi1000** series
- **EPEVER Hi2000** series  
- **EPEVER Hi3000** series
- **EPEVER Hi4000** series
- **Other EPEVER Hi variants** with Modbus support

### Key Requirements
For a device to be compatible:
- ✅ **Modbus Protocol**: Must support Modbus RTU or TCP
- ✅ **EPEVER Hi Registers**: Must use EPEVER Hi register mapping
- ✅ **Communication Interface**: RS485, Ethernet, or WiFi connectivity
- ✅ **Register Access**: Read/write access to charge controller registers

## 📋 Device Compatibility Matrix

| Device Series | Modbus RTU | Modbus TCP | Write Support | Status |
|---------------|------------|------------|---------------|---------|
| EPEVER Hi1000 | ✅ | ✅ | ✅ | Fully Supported |
| EPEVER Hi2000 | ✅ | ✅ | ✅ | Fully Supported |
| EPEVER Hi3000 | ✅ | ✅ | ✅ | Fully Supported |
| EPEVER Hi4000 | ✅ | ✅ | ✅ | Fully Supported |
| Generic EPEVER Hi | ✅ | ⚠️ | ⚠️ | Model Dependent |

**Legend:**
- ✅ **Fully Supported**: Tested and confirmed working
- ⚠️ **Model Dependent**: May work depending on specific model features
- ❌ **Not Supported**: Known incompatibility

## 🔧 Communication Interfaces

### Modbus RTU (Serial)
Most EPEVER Hi controllers support RS485 Modbus RTU:

**Connection Options:**
- **Direct RS485**: USB-to-RS485 adapter to charge controller
- **Serial Gateway**: RS485-to-Ethernet converter
- **Wireless**: RS485-to-WiFi adapter

**Typical Settings:**
- **Baudrate**: 9600, 19200, 38400, or 115200 bps
- **Data Format**: 8N1 (8 data bits, no parity, 1 stop bit)
- **Slave Address**: 1-247 (usually 1 by default)

### Modbus TCP (Ethernet)
Some EPEVER Hi models include built-in Ethernet or WiFi:

**Connection Options:**
- **Built-in Ethernet**: Direct network connection
- **Built-in WiFi**: Wireless network connection
- **External Gateway**: Modbus RTU-to-TCP gateway

**Typical Settings:**
- **Port**: 502 (standard Modbus TCP port)
- **IP Address**: Configured via device interface
- **Slave Address**: Usually 1

## 🎛️ Supported Features by Device Type

### Standard Features (All Compatible Devices)
- ⚡ **Solar Input Monitoring**: Voltage, current, power
- 🔋 **Battery Monitoring**: Voltage, current, SOC, temperature
- 🔌 **Load Monitoring**: Voltage, current, power consumption
- 📊 **System Status**: Charging state, error codes, operation mode
- 🌡️ **Environmental**: Temperature readings

### Advanced Features (Model Dependent)
- 🔧 **Parameter Configuration**: Battery settings, charging profiles
- ⚙️ **Operation Control**: Load control, charging enable/disable
- 📈 **Historical Data**: Energy totals, runtime statistics
- 🚨 **Alarm Management**: Fault conditions, warnings
- 🔄 **Firmware Info**: Version, device identification

## 🔍 Device Identification

### How to Check Compatibility

1. **Check Device Manual**: Look for "Modbus" support in specifications
2. **Physical Inspection**: Look for RS485 terminals or Ethernet port
3. **Software Test**: Try connecting with Modbus testing software
4. **Model Number**: Compare with known compatible models

### Register Map Verification
The integration uses specific EPEVER Hi register addresses:
- **Solar Registers**: 0x3100-0x311F (PV voltage, current, power)
- **Battery Registers**: 0x3200-0x321F (Battery voltage, current, SOC)
- **Load Registers**: 0x3300-0x331F (Load voltage, current, power)
- **System Registers**: 0x3400-0x34FF (Status, settings, diagnostics)

### Testing Device Compatibility
Before full integration setup:

1. **Basic Connection Test**:
   ```bash
   # Using modbus-cli (if available)
   modbus-cli read 192.168.1.100:502 --slave 1 --register 0x3100
   ```

2. **Manual Register Reading**: Use Modbus testing tools to read key registers
3. **Integration Test**: Add device to integration and check entity creation

## ⚠️ Known Limitations

### Device-Specific Limitations

#### Older EPEVER Models
- **Limited Registers**: May not support all register addresses
- **Read-Only**: Some older models don't support write operations
- **Communication Speed**: May require lower baudrates

#### Firmware Variations
- **Register Mapping**: Some firmware versions may have different register layouts
- **Feature Support**: Not all features available in all firmware versions
- **Update Requirements**: May need firmware updates for full compatibility

### Communication Limitations

#### RTU Connections
- **Distance**: Limited by RS485 cable length (typically <1200m)
- **Bus Load**: Multiple devices on same bus may affect performance
- **Interference**: Electrical noise can affect communication quality

#### TCP Connections  
- **Network Dependency**: Requires stable network connection
- **Firewall**: Port 502 must be accessible
- **IP Configuration**: Device must have valid network settings

## 🛠️ Unsupported Devices

### EPEVER Non-Hi Series
- **EPEVER AN Series**: Different register mapping
- **EPEVER BN Series**: Different communication protocol
- **EPEVER LS Series**: May have limited Modbus support
- **EPEVER ViewStar**: Different product line

### Other Manufacturers
This integration is specifically for EPEVER Hi controllers. For other manufacturers:
- **Victron**: Use official Victron integration
- **Renogy**: May need generic Modbus integration
- **AIMS**: Check for specific integrations
- **Outback**: Use appropriate manufacturer integration

## 📞 Device Support

### Getting Device Information
If you're unsure about compatibility:

1. **Model Number**: Note exact model number and revision
2. **Manual Check**: Look for Modbus specifications in manual
3. **Physical Check**: Look for communication ports
4. **Test Setup**: Try basic Modbus communication

### Reporting Compatibility
Help improve device support:

1. **Success Reports**: Report working devices in GitHub issues
2. **Failure Reports**: Report incompatible devices with details
3. **Register Mapping**: Share different register layouts if found
4. **Documentation**: Contribute device-specific setup instructions

### Community Support
- **GitHub Issues**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/issues
- **Home Assistant Community**: Search for EPEVER discussions
- **EPEVER Support**: Contact manufacturer for technical specifications

## 🔄 Future Device Support

### Planned Additions
- **Extended EPEVER Hi Models**: As new models are released
- **Alternative Communication**: USB, CAN bus if supported
- **Enhanced Features**: As firmware capabilities expand

### Contributing Device Support
Help expand device compatibility:
1. **Testing**: Test with new EPEVER Hi models
2. **Documentation**: Document register differences
3. **Code Contributions**: Submit pull requests for new features
4. **Feedback**: Provide feedback on device-specific issues

## ✅ Verification Steps

### Confirming Device Compatibility

1. **Physical Setup**: Connect device using preferred method (RTU/TCP)
2. **Basic Test**: Attempt to read basic registers
3. **Integration Test**: Add to Home Assistant integration
4. **Entity Check**: Verify expected entities are created
5. **Functionality Test**: Confirm sensors update and controls work

### Expected Results
For a fully compatible device:
- ✅ **Connection Success**: Integration shows "Connected" status
- ✅ **Entity Creation**: 40+ entities created automatically
- ✅ **Data Updates**: Sensor values update with polling interval
- ✅ **Write Operations**: Number/select controls function properly
- ✅ **Error-Free**: No errors in Home Assistant logs

## 🆕 Next Steps

- **[Configuration](Configuration)** - Set up your compatible device
- **[Entities Reference](Entities-Reference)** - Explore available entities
- **[Troubleshooting](Troubleshooting)** - Resolve device-specific issues