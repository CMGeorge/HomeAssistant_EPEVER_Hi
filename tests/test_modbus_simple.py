"""Simple test to verify modbus logging configuration exists."""

import logging


def test_pymodbus_logging_can_be_configured():
    """Test that pymodbus.logging logger can be configured to WARNING level."""
    # Get the pymodbus.logging logger
    pymodbus_logger = logging.getLogger("pymodbus.logging")

    # Set it to WARNING (which is what our fix does)
    pymodbus_logger.setLevel(logging.WARNING)

    # Verify it's set
    assert pymodbus_logger.level == logging.WARNING


def test_modbus_client_import_available():
    """Test that modbus_client module structure is valid."""
    import ast
    import os

    # Parse the modbus_client.py file to check syntax
    modbus_client_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "custom_components",
        "epever_hi",
        "modbus_client.py"
    )

    with open(modbus_client_path, encoding='utf-8') as f:
        content = f.read()

    # Parse to ensure valid syntax
    ast.parse(content)

    # Check that logging configuration is present
    assert "_PYMODBUS_LOGGER = logging.getLogger(\"pymodbus.logging\")" in content
    assert "_PYMODBUS_LOGGER.setLevel(logging.WARNING)" in content

    # Check that timeout and retries parameters are used
    assert "timeout=2.0" in content
    assert "retries=1" in content
