from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        TrackNetCountSensor(coordinator),
        TrackNetRawSensor(coordinator),
    ]

    async_add_entities(entities)


class TrackNetCountSensor(CoordinatorEntity, SensorEntity):
    """Sensor: number of devices."""

    _attr_name = "TrackNet Devices"
    _attr_icon = "mdi:lan"
    _attr_unique_id = "tracknet_device_count"

    @property
    def native_value(self):
        # On garde le comportement normal : nombre de devices
        data = self.coordinator.data or []
        return len(data)


class TrackNetRawSensor(CoordinatorEntity, SensorEntity):
    """Sensor: raw device list."""

    _attr_name = "TrackNet Raw"
    _attr_icon = "mdi:code-json"
    _attr_unique_id = "tracknet_raw"

    @property
    def native_value(self):
        # Ici seulement : on force un changement de state
        # pour que les attributs soient réévalués.
        return datetime.now().isoformat()

    @property
    def extra_state_attributes(self):
        """Return full device list."""
        return {
            "devices": self.coordinator.data or []
        }
