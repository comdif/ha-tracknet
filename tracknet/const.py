DOMAIN = "tracknet"

DEFAULT_NETWORK = "192.168.1.0/24"
DEFAULT_SCAN_INTERVAL = 30  # seconds


def SCAN_INTERVAL(value: int):
    from datetime import timedelta

    return timedelta(seconds=int(value))
