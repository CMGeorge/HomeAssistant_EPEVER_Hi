import logging

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException
from pymodbus.framer import FramerType

_LOGGER = logging.getLogger(__name__)

# Configure pymodbus logging to reduce verbose retry messages
_PYMODBUS_LOGGER = logging.getLogger("pymodbus.logging")
_PYMODBUS_LOGGER.setLevel(logging.WARNING)


class EpeverHiModbusClient:
    """Handles persistent async Modbus TCP communication for EPEVER Hi devices."""

    def __init__(self, host: str, port: int, framer: str = "tcp") -> None:
        self.host = host
        self.port = port
        self.framer = framer
        self.client: AsyncModbusTcpClient | None = None

    async def ensure_connected(self) -> bool:
        """Ensure the Modbus client is connected, reconnect if needed."""
        if self.client is None:
            # Choose framer based on configuration
            framer_type = (
                FramerType.RTU if self.framer.lower() == "rtu" else FramerType.SOCKET
            )

            # Configure client with reduced retries to minimize verbose logging
            self.client = AsyncModbusTcpClient(
                self.host,
                port=self.port,
                framer=framer_type,
                timeout=2.0,  # Shorter timeout to fail faster
                retries=1,  # Fewer retries to reduce log noise
            )

        if not self.client.connected:
            try:
                connected = await self.client.connect()
                if not connected:
                    _LOGGER.error(
                        "Failed to connect to Modbus server at %s:%s (framer: %s)",
                        self.host,
                        self.port,
                        self.framer,
                    )
                    return False
            except Exception as e:
                _LOGGER.error("Modbus connection error: %s", e)
                return False

        return True

    async def read_register(
        self,
        address: int,
        count: int = 1,
        slave: int = 1,
        register_type: str = "holding",
    ) -> list[int] | None:
        """Read registers from Modbus server.

        Args:
            address: Register address to read
            count: Number of registers to read
            slave: Slave device ID
            register_type: Type of register - "holding" or "input"
        """
        if not await self.ensure_connected():
            return None

        try:
            if register_type.lower() == "input":
                result = await self.client.read_input_registers(
                    address=address, count=count, device_id=slave
                )
            else:
                result = await self.client.read_holding_registers(
                    address=address, count=count, device_id=slave
                )

            if result is None or result.isError():
                _LOGGER.warning(
                    "Read failed at address 0x%04X (type: %s)", address, register_type
                )
                return None
            return result.registers
        except ModbusException as me:
            _LOGGER.error("Modbus protocol error at 0x%04X: %s", address, me)
        except Exception as e:
            _LOGGER.error("Unexpected error reading 0x%04X: %s", address, e)

        return None

    async def write_register(self, address: int, value: int, slave: int = 1) -> bool:
        """Write a value to a Modbus register."""
        if not await self.ensure_connected():
            return False

        try:
            result = await self.client.write_register(
                address=address, value=value, device_id=slave
            )
            if result.isError():
                _LOGGER.warning("Write failed at 0x%04X: %s", address, result)
                return False
            return True
        except ModbusException as me:
            _LOGGER.error("Modbus write error at 0x%04X: %s", address, me)
        except Exception as e:
            _LOGGER.error("Unexpected error writing 0x%04X: %s", address, e)

        return False

    async def close(self) -> None:
        """Close the Modbus connection gracefully."""
        if self.client:
            try:
                await self.client.close()
            except Exception as e:
                _LOGGER.warning("Error while closing Modbus client: %s", e)
            finally:
                self.client = None
