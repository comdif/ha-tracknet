from __future__ import annotations

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .scanner import TrackNetScanner
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up TrackNet integration."""
    network = entry.data["network"]
    interval = entry.data["scan_interval"]

    scanner = TrackNetScanner(network)

    # Load OUI database
    await hass.async_add_executor_job(scanner.load_oui)

    async def async_update_data():
        """Fetch data from scanner."""
        try:
            return await hass.async_add_executor_job(scanner.scan)
        except Exception as err:
            raise UpdateFailed(err)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="tracknet",
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL(interval),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload TrackNet integration."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
