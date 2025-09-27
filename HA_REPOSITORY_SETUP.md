# Setup Instructions for ha_repository

This document provides step-by-step instructions for setting up the new dedicated `ha_repository` for hosting multiple Home Assistant integrations.

## Step 1: Create New Repository

1. **Go to GitHub**: https://github.com/CMGeorge
2. **Click**: "New Repository" 
3. **Repository name**: `ha_repository`
4. **Description**: "Central repository for Home Assistant custom integrations by George Călugăr"
5. **Visibility**: Public
6. **Initialize**: with README
7. **Click**: "Create repository"

## Step 2: Setup Repository Structure

Clone the new repository and add the necessary files:

```bash
git clone https://github.com/CMGeorge/ha_repository.git
cd ha_repository
```

Copy these files from this current repository:
- `ha_repository_README.md` → `README.md`  
- `ha_repository_repository.json` → `repository.json`

## Step 3: Update repository.json

The provided `repository.json` includes placeholder information for the Sabiana Smart Energy integration. Update it with the correct information from the Sabiana repository's `manifest.json`:

```json
{
  "name": "Sabiana Smart Energy",
  "domain": "sabiana_smart_energy",
  "version": "x.x.x",  // Update with actual version
  "requirements": [...], // Update with actual requirements
  "dependencies": [...], // Update with actual dependencies
  "integration_type": "device" // Update if different
}
```

## Step 4: Create Installation Scripts (Optional)

To provide one-command installation like the EPEVER Hi integration:

```bash
mkdir -p scripts
# Create install.sh and install.py for multi-integration installation
```

## Step 5: Update Individual Integration Repositories

### Update EPEVER Hi Repository

Add a note to the README.md pointing to the central repository:

```markdown
## Alternative Installation

This integration is also available through the central repository:
https://github.com/CMGeorge/ha_repository

Add the repository URL to Home Assistant to access multiple integrations.
```

### Update Sabiana Smart Energy Repository

Add similar installation scripts and documentation as done for EPEVER Hi.

## Step 6: Testing

Test the repository structure:

1. **JSON Validation**: `python3 -c "import json; json.load(open('repository.json'))"`
2. **Installation Test**: Try adding the repository URL to a test Home Assistant instance
3. **Download Test**: Verify that the download URLs work correctly

## Step 7: Documentation Updates

Update the documentation in both individual repositories to reference the central repository for users who want to install multiple integrations.

## Benefits of This Approach

✅ **Centralized Management**: One repository.json for multiple integrations  
✅ **Easy Discovery**: Users can find all your integrations in one place  
✅ **Simplified Installation**: Add one repository URL to get access to all integrations  
✅ **Individual Repositories**: Each integration maintains its own codebase  
✅ **Flexibility**: Users can still install individually or through HACS  

## Repository URLs

- **Central Repository**: https://github.com/CMGeorge/ha_repository
- **EPEVER Hi**: https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi  
- **Sabiana Smart Energy**: https://github.com/CMGeorge/homeassistant_sabiana_smart_energy

## Next Steps

1. Create the ha_repository on GitHub
2. Upload the files and customize the repository.json 
3. Test the installation process
4. Update individual repository documentation
5. Announce the new installation method to users