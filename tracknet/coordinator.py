from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from .const import DOMAIN

class TrackNetCoordinator(DataUpdateCoordinator):
    """Coordinator for TrackNet."""

    def __init__(self, hass: HomeAssistant, scanner):
        super().__init__(
            hass,
            logger=hass.logger.getChild(DOMAIN),
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.scanner = scanner

    async def _async_update_data(self):
        """Run the network scan."""
        return await self.hass.async_add_executor_job(self.scanner.scan)
