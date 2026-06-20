ha-tracknet

Local network inventory & device tracker for Home Assistant  
Fast · Local · Zero dependencies · Dashboard‑ready
🔍 What TrackNet Does

TrackNet builds a clean, real‑time inventory of all devices on your LAN by combining:

    ARP refresh

    Parallel ICMP ping

    Web port auto‑detection

    Clickable device URLs

    Custom names via oui file

Everything is exposed as Home Assistant entities, ready for dashboards.
🧩 Custom Device Names (oui file)

TrackNet supports a simple file named: "oui"

Each line maps a full MAC address to a custom device name:

AABBCCDDEEFF LivingRoomCamera

112233445566 MyLaptop

This gives you a clean, human‑friendly inventory with stable names.
⚡ Presence Detection (Ping)

For every IP discovered in ARP:

    TrackNet sends a parallel ICMP ping

    Returns a clear state: online / offline

    Updates the HA entity accordingly

Fast, reliable, and perfect for dashboards.
🌐 Web Interface Detection

TrackNet automatically selects the most likely web port:

    80

    443

    8080

    8123

    etc.

Then it generates a direct clickable URL.

In Home Assistant, clicking it opens the device interface in a new browser tab.

Ideal for routers, switches, cameras, ESPs, APs, printers…
📊 Home Assistant Output

Each device entry includes:

    IP address

    MAC address

    Custom name (from oui)

    Vendor (if available)

    Ping status

    Best web port

    Clickable URL

All grouped in a single clean sensor, dashboard‑friendly.
🛠️ Architecture

    Single lightweight script

    Zero dependencies

    Fully local

    Works on HAOS, BusyBox, SSH add‑on

    Executes in a few hundred milliseconds

    Perfect for automations and Lovelace tiles

🧪 Tested On

    HAOS x86‑64

    HAOS Raspberry Pi

    HAOS supervised

    Standard home LANs (DHCP, Wi‑Fi, wired/wireless mix)

📦 Status

    ✔️ Fully working ARP + ICMP presence detection

    ✔️ Stable on HAOS (validated over several days)

    ✔️ Compatible with BusyBox environments

    ⏳ Additional convenience features planned

    🤝 Community contributions welcome

📄 Documentation

A complete PDF documentation will be added soon.

-    How to install on HAOS:

Just past this one-line on you ssh console:

`unzip -o <(curl -fsSL https://github.com/comdif/ha-tracknet/archive/refs/heads/main.zip) -d /tmp && mv /tmp/ha-tracknet-main/tracknet /config/custom_components/ && ha core restart`

-    How to install on other OS:

Just copy the tracknet directory in your HA custom-component directory.
