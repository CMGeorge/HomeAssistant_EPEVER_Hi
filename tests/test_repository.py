"""Tests for repository structure and installation support."""

import json
import os
from pathlib import Path


def test_repository_json_exists():
    """Test that repository.json exists and is valid."""
    repo_path = Path(__file__).parent.parent / "repository.json"
    assert repo_path.exists(), "repository.json file does not exist"

    with open(repo_path, encoding="utf-8") as f:
        repo_data = json.load(f)

    # Required fields for repository.json
    required_fields = [
        "name",
        "url",
        "maintainer",
        "description",
        "version",
        "repository_type",
        "integrations",
    ]
    for field in required_fields:
        assert field in repo_data, (
            f"Required field '{field}' missing from repository.json"
        )

    # Validate integrations array
    assert isinstance(repo_data["integrations"], list), (
        "integrations should be an array"
    )
    assert len(repo_data["integrations"]) > 0, "integrations array should not be empty"

    # Validate first integration
    integration = repo_data["integrations"][0]
    integration_fields = [
        "name",
        "description",
        "domain",
        "version",
        "documentation",
        "codeowners",
        "iot_class",
        "config_flow",
        "integration_type",
    ]
    for field in integration_fields:
        assert field in integration, f"Required integration field '{field}' missing"

    # Validate specific values
    assert integration["domain"] == "epever_hi", "Domain should be epever_hi"
    assert integration["config_flow"] is True, "config_flow should be True"
    assert integration["integration_type"] == "hub", "integration_type should be hub"


def test_installation_scripts_exist():
    """Test that installation scripts exist and are executable."""
    base_dir = Path(__file__).parent.parent

    # Check bash script
    bash_script = base_dir / "install.sh"
    assert bash_script.exists(), "install.sh does not exist"
    assert os.access(bash_script, os.X_OK), "install.sh is not executable"

    # Check Python script
    python_script = base_dir / "install.py"
    assert python_script.exists(), "install.py does not exist"
    assert os.access(python_script, os.X_OK), "install.py is not executable"


def test_installation_script_content():
    """Test that installation scripts have expected content."""
    base_dir = Path(__file__).parent.parent

    # Test bash script content
    bash_script = base_dir / "install.sh"
    with open(bash_script, encoding="utf-8") as f:
        bash_content = f.read()

    assert "EPEVER Hi Integration" in bash_content
    assert "github.com/CMGeorge/HomeAssistant_EPEVER_Hi" in bash_content
    assert "custom_components" in bash_content
    assert "epever_hi" in bash_content

    # Test Python script content
    python_script = base_dir / "install.py"
    with open(python_script, encoding="utf-8") as f:
        python_content = f.read()

    assert "EPEVER Hi Integration" in python_content
    assert "github.com/CMGeorge/HomeAssistant_EPEVER_Hi" in python_content
    assert "custom_components" in python_content
    assert "epever_hi" in python_content


def test_existing_hacs_files_still_present():
    """Test that existing HACS files are still present."""
    base_dir = Path(__file__).parent.parent

    # Check HACS files
    assert (base_dir / "hacs.json").exists(), "hacs.json should still exist"
    assert (base_dir / "info.md").exists(), "info.md should still exist"

    # Validate hacs.json
    with open(base_dir / "hacs.json", encoding="utf-8") as f:
        hacs_data = json.load(f)

    assert "name" in hacs_data, "hacs.json should have name field"
    assert hacs_data["name"] == "EPEVER Hi", "HACS name should be 'EPEVER Hi'"


def test_repository_compatibility():
    """Test that repository structure supports both HACS and direct installation."""
    base_dir = Path(__file__).parent.parent

    # Check that both HACS and direct repository files exist
    assert (base_dir / "hacs.json").exists()
    assert (base_dir / "repository.json").exists()
    assert (base_dir / "info.md").exists()

    # Check installation scripts
    assert (base_dir / "install.sh").exists()
    assert (base_dir / "install.py").exists()

    # Check integration files
    integration_dir = base_dir / "custom_components" / "epever_hi"
    assert integration_dir.exists(), "Integration directory should exist"
    assert (integration_dir / "manifest.json").exists(), (
        "Integration manifest should exist"
    )


def test_urls_consistency():
    """Test that URLs are consistent across all configuration files."""
    base_dir = Path(__file__).parent.parent
    expected_repo_url = "https://github.com/CMGeorge/HomeAssistant_EPEVER_Hi"

    # Check repository.json
    with open(base_dir / "repository.json", encoding="utf-8") as f:
        repo_data = json.load(f)
    assert repo_data["url"] == expected_repo_url
    assert repo_data["integrations"][0]["documentation"] == expected_repo_url

    # Check manifest.json
    with open(
        base_dir / "custom_components" / "epever_hi" / "manifest.json", encoding="utf-8"
    ) as f:
        manifest_data = json.load(f)
    assert manifest_data["documentation"] == expected_repo_url
    assert manifest_data["issue_tracker"] == f"{expected_repo_url}/issues"
