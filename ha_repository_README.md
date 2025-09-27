# ha_repository - Home Assistant Integrations Repository

This is a central repository that provides metadata for multiple Home Assistant custom integrations by George Călugăr (@CMGeorge).

## Integrations Included

### EPEVER Hi Integration
- **Repository**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi
- **Description**: Monitor and control EPEVER Hi solar charge controllers via Modbus RTU/TCP
- **Domain**: `epever_hi`

### Sabiana Smart Energy Integration  
- **Repository**: https://github.com/CMGeorge/homeassistant_sabiana_smart_energy
- **Description**: Integration for Sabiana Smart Energy devices
- **Domain**: `sabiana_smart_energy`

## Installation

### Add Repository to Home Assistant

1. **Go to**: Settings → Add-ons → Add-on Store → ⋮ (three dots) → Repositories
2. **Add**: `https://github.com/CMGeorge/ha_repository`
3. **Browse**: Available integrations and install as needed

### One-Command Installation

```bash
# Install EPEVER Hi Integration
curl -sSL https://raw.githubusercontent.com/CMGeorge/HomeAssistant_EPEVER_Hi/main/install.sh | bash

# Install Sabiana Smart Energy Integration  
curl -sSL https://raw.githubusercontent.com/CMGeorge/homeassistant_sabiana_smart_energy/main/install.sh | bash
```

## Repository Structure

```
ha_repository/
├── repository.json          # Repository metadata
├── README.md               # This file
├── integrations/           # Integration-specific files
│   ├── epever_hi/         # EPEVER Hi resources
│   └── sabiana_smart_energy/  # Sabiana resources
└── docs/                  # Documentation
```

## Integration Details

Each integration maintains its own repository with full documentation, code, and releases. This repository serves only as a central metadata hub for installation convenience.

## Support

For integration-specific issues, please use the respective repository issue trackers:

- EPEVER Hi: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi/issues
- Sabiana Smart Energy: https://github.com/CMGeorge/homeassistant_sabiana_smart_energy/issues

## License

Individual integrations maintain their own licenses. See respective repositories for details.