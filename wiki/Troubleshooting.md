# Troubleshooting Guide

This guide helps resolve common issues with the EPEVER Hi Integration. Issues are organized by category for easy reference.

## 🔍 Quick Diagnostics

### Check Integration Status
1. Go to **Settings → Devices & Services**
2. Find **EPEVER Hi** integration
3. Check status indicator:
   - ✅ **Connected**: Working properly
   - ⚠️ **Warning**: Partial connectivity
   - ❌ **Error**: Communication failed

### View Logs
1. Go to **Settings → System → Logs**
2. Search for `epever_hi`
3. Look for error patterns and timestamps

### Basic Connection Test
```bash
# Test Modbus TCP connection (if accessible)
telnet [DEVICE_IP] 502

# Check serial port (Linux)
ls -l /dev/ttyUSB*
sudo dmesg | grep tty
```

## 🔌 Connection Issues

### Modbus TCP Connection Problems

#### Cannot Connect to Device
**Symptoms**: Integration shows "Connection failed" or timeout errors

**Solutions**:
1. **Network Connectivity**:
   ```bash
   ping [DEVICE_IP]  # Test basic connectivity
   nmap -p 502 [DEVICE_IP]  # Test Modbus port
   ```

2. **IP Address Issues**:
   - Verify device IP address in router DHCP table
   - Try connecting directly with Ethernet cable
   - Check if device uses DHCP or static IP

3. **Port Configuration**:
   - Confirm port 502 is open on device
   - Check firewall rules on Home Assistant host
   - Verify no other applications using port 502

4. **Device Configuration**:
   - Ensure Modbus TCP is enabled on controller
   - Check device manual for network setup
   - Verify device is in correct operation mode

#### Intermittent Disconnections
**Symptoms**: Connection works but frequently drops

**Solutions**:
- **Increase Timeout**: Set timeout to 10+ seconds in configuration
- **Network Stability**: Check network quality and congestion
- **Power Issues**: Ensure stable power to controller
- **Interference**: Check for electromagnetic interference

### Modbus RTU Connection Problems

#### Serial Port Issues
**Symptoms**: "Permission denied" or "Port not found" errors

**Solutions**:
1. **Port Permissions** (Linux):
   ```bash
   sudo usermod -a -G dialout homeassistant
   sudo systemctl restart home-assistant
   ```

2. **Port Identification**:
   ```bash
   # Find available ports
   dmesg | grep ttyUSB
   ls -l /dev/serial/by-id/
   ```

3. **USB Adapter Issues**:
   - Try different USB ports
   - Check adapter LED indicators
   - Test adapter with other software

#### Communication Parameters
**Symptoms**: Timeout errors, garbled data, or no response

**Solutions**:
- **Baudrate**: Try common rates (9600, 19200, 38400, 115200)
- **Serial Format**: Verify 8N1 (8 data bits, no parity, 1 stop bit)
- **Slave ID**: Try addresses 1-247
- **Cable Wiring**: Check A/B (D+/D-) connections

#### RS485 Wiring Issues
**Common Problems**:
- **Reversed Polarity**: Swap A/B connections
- **Missing Termination**: Add 120Ω resistors at bus ends
- **Ground Loop**: Use isolated adapters
- **Cable Length**: Keep under 1200m for RS485

## ⚙️ Configuration Issues

### Entity Creation Problems

#### No Entities Created
**Symptoms**: Integration connects but no entities appear

**Solutions**:
1. **Device Compatibility**: Verify device supports EPEVER Hi registers
2. **Register Access**: Check if device responds to test registers
3. **Integration Restart**: 
   ```
   Settings → Devices & Services → EPEVER Hi → Configure → Submit
   ```

#### Partial Entity Creation
**Symptoms**: Some entities missing or unavailable

**Solutions**:
- **Device Model**: Not all registers supported by all models
- **Firmware Version**: Update controller firmware if possible
- **Register Verification**: Check which registers your device supports

#### Entity Values Show "Unavailable"
**Symptoms**: Entities exist but show no data

**Solutions**:
1. **Communication Test**: Verify basic Modbus connectivity
2. **Register Addresses**: Check if device uses different register mapping
3. **Data Type Issues**: Verify register data types match expectations
4. **Polling Interval**: Increase polling interval to reduce load

### Configuration Parameters

#### Invalid Parameter Values
**Symptoms**: Configuration rejected or causes errors

**Solutions**:
- **Value Ranges**: Ensure values are within acceptable limits
- **Data Types**: Check integer vs. decimal requirements
- **Device Limits**: Consult device manual for parameter ranges

#### Changes Not Applied
**Symptoms**: Configuration changes don't take effect

**Solutions**:
1. **Integration Restart**: Restart integration after changes
2. **Home Assistant Restart**: Full restart may be required
3. **Browser Cache**: Clear cache (Ctrl+F5)
4. **Device Write Support**: Verify device supports parameter changes

## 📊 Data and Performance Issues

### Incorrect Sensor Values

#### Wrong Units or Scale
**Symptoms**: Values too high, too low, or wrong units

**Solutions**:
- **Scale Factor**: Check register scaling in const.py
- **Unit Conversion**: Verify expected units match display units
- **Device Configuration**: Check device internal scaling settings

#### Negative Values Where Unexpected
**Symptoms**: Negative currents, voltages, or power readings

**Solutions**:
- **Signed/Unsigned**: Check if register should be signed integer
- **Direction Convention**: Negative current may indicate charging vs. discharging
- **Register Order**: Verify byte order for multi-register values

#### Values Don't Update
**Symptoms**: Sensor values are static or stale

**Solutions**:
1. **Polling Issues**: Check integration polling status
2. **Communication Errors**: Look for Modbus errors in logs
3. **Device Issues**: Verify device is operational
4. **Register Lock**: Some devices lock registers during certain operations

### Performance Problems

#### High CPU Usage
**Symptoms**: Home Assistant sluggish, high system load

**Solutions**:
- **Polling Interval**: Increase from 30s to 60s+ in configuration
- **Entity Reduction**: Disable unused entities
- **Multiple Devices**: Stagger polling for multiple controllers

#### Memory Issues
**Symptoms**: Increasing memory usage over time

**Solutions**:
- **Log Level**: Reduce logging verbosity
- **History Purge**: Configure appropriate history retention
- **Integration Restart**: Periodic restart to clear memory

#### Timeout Errors
**Symptoms**: Frequent "Request timeout" errors

**Solutions**:
- **Timeout Setting**: Increase to 15-30 seconds
- **Network Quality**: Check connection stability
- **Device Load**: Reduce polling frequency
- **Retry Logic**: Increase retry count in configuration

## 🚨 Error Messages

### Common Error Patterns

#### "ModbusException: Exception Response(131, 3, GatewayTargetDeviceFailedToRespond)"
**Meaning**: Device not responding on specified slave ID

**Solutions**:
- Try different slave IDs (1, 2, 247)
- Check device addressing configuration
- Verify device is powered and operational

#### "ConnectionException: Failed to connect"
**Meaning**: Cannot establish Modbus connection

**Solutions**:
- Verify IP address and port (TCP) or serial port (RTU)
- Check network connectivity or serial port access
- Confirm device has Modbus enabled

#### "IllegalFunctionException"
**Meaning**: Unsupported Modbus function code

**Solutions**:
- Device doesn't support specific register type
- Try different register addresses
- Check device manual for supported functions

#### "PermissionError: [Errno 13] Permission denied: '/dev/ttyUSB0'"
**Meaning**: No permission to access serial port

**Solutions**:
```bash
# Add user to dialout group (Linux)
sudo usermod -a -G dialout homeassistant
sudo systemctl restart home-assistant

# Check port permissions
ls -l /dev/ttyUSB0
```

### Integration-Specific Errors

#### "Unknown register type"
**Meaning**: Integration doesn't recognize register configuration

**Solutions**:
- Check const.py for register definition
- Verify register address is correct
- Report issue if register should be supported

#### "Invalid scale factor"
**Meaning**: Mathematical error in value scaling

**Solutions**:
- Check register scale definition
- Verify raw register values are reasonable
- Look for divide-by-zero or overflow conditions

## 🔧 Hardware Issues

### Serial Adapter Problems

#### USB Adapter Not Recognized
**Symptoms**: /dev/ttyUSB* not appearing

**Solutions**:
1. **Driver Issues**:
   ```bash
   # Check for adapter
   lsusb
   dmesg | tail -20
   
   # Common drivers
   sudo modprobe ftdi_sio
   sudo modprobe cp210x
   ```

2. **Hardware Test**:
   - Try different USB port
   - Test with known working device
   - Check adapter LED indicators

#### Adapter Works But No Communication
**Symptoms**: Port accessible but no Modbus response

**Solutions**:
- **Wiring**: Verify A/B connections to charge controller
- **Adapter Type**: Ensure RS485 adapter (not RS232)
- **Isolation**: Use isolated adapter if ground loop issues
- **Termination**: Add 120Ω resistors if required

### Device Hardware Issues

#### Controller Not Responding
**Symptoms**: No response to any Modbus commands

**Solutions**:
- **Power Cycle**: Turn controller off/on
- **Factory Reset**: Reset to defaults if accessible
- **Firmware**: Check for firmware updates
- **Hardware Fault**: Contact manufacturer support

#### Partial Functionality
**Symptoms**: Some readings work, others don't

**Solutions**:
- **Sensor Issues**: Individual sensor problems
- **Register Support**: Limited register implementation
- **Firmware Bugs**: Try different firmware version

## 🛠️ Advanced Troubleshooting

### Debug Mode Configuration

#### Enable Verbose Logging
Add to `configuration.yaml`:
```yaml
logger:
  default: warning
  logs:
    custom_components.epever_hi: debug
    pymodbus: debug
```

#### Monitor Raw Modbus Traffic
Use external tools:
```bash
# Monitor serial traffic (Linux)
sudo cat /dev/ttyUSB0

# TCP packet capture
sudo tcpdump -i any port 502

# Modbus testing tools
modpoll -m tcp -a 1 -r 1 -c 10 [DEVICE_IP]
```

### Integration Diagnostics

#### Export Diagnostic Data
1. Settings → Devices & Services → EPEVER Hi
2. Click device name
3. Download diagnostics

#### Manual Register Testing
```python
# Test individual registers
from pymodbus.client.sync import ModbusSerialClient
client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600)
result = client.read_input_registers(0x3580, 1, unit=1)
print(result.registers if not result.isError() else result)
```

### Performance Analysis

#### Monitor Resource Usage
```bash
# Check Home Assistant processes
top -p `pgrep -f home-assistant`

# Monitor network connections
netstat -an | grep 502

# Check disk space and I/O
df -h
iostat -x 1
```

## 📞 Getting Help

### Before Requesting Support

1. **Check Logs**: Include relevant log entries
2. **Test Basics**: Verify basic connectivity
3. **Document Setup**: Note device model, connection type, settings
4. **Try Solutions**: Attempt recommended fixes above

### Information to Provide

When requesting support, include:
- **Integration Version**: Check in HACS or integration page
- **Home Assistant Version**: Settings → About
- **Device Model**: Exact EPEVER Hi model number
- **Connection Type**: TCP or RTU, with settings
- **Error Messages**: Complete log entries with timestamps
- **Configuration**: Sanitized configuration details
- **Testing Results**: Results from basic connectivity tests

### Support Channels

- **GitHub Issues**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/issues
- **Home Assistant Community**: Forum discussions
- **Documentation**: Check other wiki pages first

### Creating Good Bug Reports

1. **Clear Title**: Describe the specific issue
2. **Environment**: HA version, integration version, hardware
3. **Steps to Reproduce**: Exact steps that cause the issue
4. **Expected vs. Actual**: What should happen vs. what happens
5. **Logs**: Relevant log entries
6. **Additional Context**: Network setup, device configuration

## 🔄 Recovery Procedures

### Complete Reset
If all else fails:

1. **Remove Integration**:
   - Settings → Devices & Services → EPEVER Hi → Delete
   - Restart Home Assistant

2. **Clear Configuration**:
   - Remove any manual configuration entries
   - Clear browser cache

3. **Fresh Installation**:
   - Re-add integration
   - Use minimal configuration first
   - Test basic connectivity before adding features

### Backup and Restore
- **Export Configuration**: Back up working configurations
- **Document Settings**: Keep notes on working parameters  
- **Version Control**: Track what changes cause issues

## 📚 Related Documentation

- **[Configuration](Configuration)** - Proper setup procedures
- **[Installation Guide](Installation-Guide)** - Installation troubleshooting
- **[Supported Devices](Supported-Devices)** - Device compatibility issues