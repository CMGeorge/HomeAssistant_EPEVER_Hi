from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DIAGNOSTIC_DEFINITIONS, DOMAIN, get_device_info

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]
    sensors = []

    for addr, reg in DIAGNOSTIC_DEFINITIONS.items():
        entity_category = reg.get("entity_category", None)
        for bit_num, bit_def in reg.get("bits", {}).items():
            coordinator.register_address(addr)
            sensors.append(
                EpeverHiBinarySensor(
                    coordinator=coordinator,
                    address=addr,
                    bit_num=bit_num,
                    key=bit_def["key"],
                    name=bit_def["name"],
                    entry_id=entry.entry_id,
                    entity_category=entity_category,
                )
            )

    _LOGGER.debug("Adding %d binary sensors for EPEVER Hi", len(sensors))
    async_add_entities(sensors)


class EpeverHiBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Binary sensor for EPEVER Hi device status bits."""

    def __init__(
        self,
        coordinator: CoordinatorEntity,
        address: int,
        bit_num: int,
        key: str,
        name: str,
        entry_id: str,
        entity_category=None,
    ):
        super().__init__(coordinator)
        self._address = address
        self._bit_num = bit_num

        self._attr_name = name
        self._attr_unique_id = f"epever_hi_bin_{key}"
        self._attr_device_info = DeviceInfo(**get_device_info(entry_id))
        self._attr_entity_category = entity_category
        _LOGGER.debug(
            "Initialized binary sensor %s (bit %d @ 0x%04X)", name, bit_num, address
        )

    @property
    def is_on(self) -> bool | None:
        raw = self.coordinator.data.get(self._address)

        if raw is None:
            _LOGGER.debug("No data at 0x%04X for %s", self._address, self.name)
            return None

        bit_value = bool((raw >> self._bit_num) & 1)

        _LOGGER.debug(
            "%s: raw=0x%04X → bit[%d]=%s",
            self.name,
            raw,
            self._bit_num,
            bit_value,
        )

        return bit_value
