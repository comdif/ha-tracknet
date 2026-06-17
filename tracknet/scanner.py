import logging
import re
import os
import socket

_LOGGER = logging.getLogger(__name__)

NMAP_OUI_PATH = os.path.join(
    os.path.dirname(__file__),
    "oui"
)

COMMON_PORTS = [21, 22, 23, 53, 80, 443, 8080, 139, 445]


def check_port(ip, port, timeout=0.2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def ping(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((ip, 80))
        sock.close()
        return result == 0
    except Exception:
        return False


def ip_in_subnet(ip, subnet):
    base = subnet.rsplit(".", 1)[0]
    return ip.startswith(base + ".")


class TrackNetScanner:
    def __init__(self, network: str):
        self.network = network
        self.oui = {}

    def load_oui(self):
        if not os.path.exists(NMAP_OUI_PATH):
            _LOGGER.warning("TrackNet: OUI file not found: %s", NMAP_OUI_PATH)
            return

        try:
            with open(NMAP_OUI_PATH, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue

                    parts = line.split(None, 1)
                    if len(parts) != 2:
                        continue

                    prefix = parts[0].lower()
                    vendor = parts[1].strip()
                    self.oui[prefix] = vendor

            _LOGGER.debug("TrackNet: Loaded %d OUI entries", len(self.oui))

        except Exception as err:
            _LOGGER.error("TrackNet: error loading OUI: %s", err)

    def lookup_vendor(self, mac: str):
        mac_clean = mac.replace(":", "").replace("-", "").lower()

        # Longest-prefix match: MAC complète → 9 hex → 6 hex
        for length in (12, 9, 6):
            prefix = mac_clean[:length]
            if prefix in self.oui:
                return self.oui[prefix]

        return "Unknown"

    def scan(self):
        devices = []

        try:
            with open("/proc/net/arp", "r", encoding="utf-8") as f:
                lines = f.readlines()[1:]
        except Exception as err:
            _LOGGER.error("TrackNet: error reading /proc/net/arp: %s", err)
            return devices

        for line in lines:
            parts = line.split()
            if len(parts) < 4:
                continue

            ip = parts[0]
            mac = parts[3].lower()

            if not ip_in_subnet(ip, self.network):
                continue

            if mac == "00:00:00:00:00:00":
                continue

            if not re.match(r"^[0-9a-f:]{17}$", mac):
                continue

            vendor = self.lookup_vendor(mac)
            ping_ok = ping(ip)

            ports = []
            for port in COMMON_PORTS:
                if check_port(ip, port):
                    ports.append(port)

            ports.sort()

            if 443 in ports:
                best_port = 443
                url = f"https://{ip}"
            elif 80 in ports:
                best_port = 80
                url = f"http://{ip}"
            elif 8080 in ports:
                best_port = 8080
                url = f"http://{ip}:8080"
            else:
                best_port = None
                url = None

            devices.append({
                "ip": ip,
                "mac": mac,
                "vendor": vendor,
                "ports": ports,
                "best_port": best_port,
                "url": url,
                "ping": ping_ok,
            })

        devices.sort(key=lambda d: list(map(int, d["ip"].split("."))))
        return devices
