"""Test configuration and pytest fixtures for EPEVER Hi integration."""

import pytest


@pytest.fixture
def mock_entry_data():
    """Mock config entry data."""
    return {
        "host": "192.168.1.100",
        "port": 502,
        "slave": 1,
        "name": "Test EPEVER Hi Solar Controller",
    }


@pytest.fixture
def mock_epever_hi_data():
    """Mock EPEVER Hi device data for testing."""
    return {
        0x3100: 2850,  # Solar voltage (28.50V)
        0x3101: 580,  # Solar current (5.80A)
        0x3104: 1240,  # Battery voltage (12.40V)
        0x3105: 520,  # Battery current (5.20A)
        0x310E: 85,  # Battery SOC (85%)
        0x310C: 2450,  # Battery temperature (24.50°C)
        0x3200: 1,  # Charging status
        0x3201: 0,  # Load status
    }
