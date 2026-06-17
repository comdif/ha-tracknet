import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, DEFAULT_NETWORK, DEFAULT_SCAN_INTERVAL


class TrackNetConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle TrackNet config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Initial step."""
        if user_input is not None:
            return self.async_create_entry(title="TrackNet", data=user_input)

        schema = vol.Schema(
            {
                vol.Required("network", default=DEFAULT_NETWORK): str,
                vol.Required("scan_interval", default=DEFAULT_SCAN_INTERVAL): int,
            }
        )

        return self.async_show_form(step_id="user", data_schema=schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return TrackNetOptionsFlow(config_entry)


class TrackNetOptionsFlow(config_entries.OptionsFlow):
    """Handle TrackNet options."""

    def __init__(self, config_entry):
        super().__init__()
        self.entry = config_entry  # FIX: ne pas utiliser le nom réservé config_entry

    async def async_step_init(self, user_input=None):
        """Options menu."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema(
            {
                vol.Required(
                    "network",
                    default=self.entry.options.get(
                        "network",
                        self.entry.data.get("network", DEFAULT_NETWORK),
                    ),
                ): str,
                vol.Required(
                    "scan_interval",
                    default=self.entry.options.get(
                        "scan_interval",
                        self.entry.data.get(
                            "scan_interval", DEFAULT_SCAN_INTERVAL
                        ),
                    ),
                ): int,
            }
        )

        return self.async_show_form(step_id="init", data_schema=schema)
