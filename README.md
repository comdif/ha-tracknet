ha-tracknet

Local network inventory & device tracker for Home Assistant  
Simple · Fast · Zero dependencies · Dashboard‑friendly
📌 Important Notice

TrackNet is not a network scanner and is not intended for pentesting, reconnaissance, or security auditing.

It is a Home Assistant device tracker, designed to:

    refresh the ARP table

    detect active devices on the LAN

    maintain a clean network inventory

    expose devices as HA entities

    provide convenient shortcuts to open device interfaces

All operations are local, non‑intrusive, and designed for home networks.
🧪 Hardware Used for Testing

All development and validation were performed using:
✔️ Home Assistant OS (HAOS)

Tested on:

    HAOS x86‑64

    HAOS on Raspberry Pi

    HAOS supervised installations

Validated with:

    Official SSH Add‑on

    BusyBox shell

    Python venv for log inspection

This environment was used to test:

    ARP refresh behavior

    parallel ICMP presence detection

    stability over multiple days

    integration with HA dashboards

    compatibility with device trackers

✔️ Standard home network equipment

TrackNet was tested on typical LAN setups:

    consumer routers

    Wi‑Fi access points

    mixed wired/wireless networks

    DHCP‑based addressing

TrackNet is not intended for enterprise networks with NAC, Cisco ISE, IDS/IPS, or NetFlow monitoring.
📌 Overview

ha-tracknet is a lightweight Home Assistant integration providing:

    a clean inventory of devices on your LAN

    fast presence detection

    ARP table refresh

    parallel ICMP checks

    direct access to device interfaces from dashboards

The design philosophy is:

    simple

    fast

    local

    non‑intrusive

    Home Assistant‑friendly

TrackNet is ideal for:

    maintaining a clean network map

    refreshing device trackers

    detecting new devices

    opening routers, switches, cameras, ESPs, etc. directly from HA

    building dashboards with clickable network tiles

TrackNet is not a scanner, not a security tool, and not a replacement for Nmap.
✨ Features

    ⚡ Fast presence detection (parallel ICMP)

    🔄 ARP table refresh before detection

    🧼 Clean device list for dashboards

    🖥️ Direct access links to device web interfaces

    🧩 Simple architecture (single script)

    🏠 Fully local (no cloud, no API keys)

    🛠️ Easy to extend

    🧘 Non‑intrusive (no port scanning, no fingerprinting)

🚧 Current Status

    ✔️ Fully working ARP + ICMP presence detection

    ✔️ Stable on HAOS (validated over several days)

    ✔️ Compatible with BusyBox environments

    ⏳ Additional convenience features planned

    🤝 Community contributions welcome

📄 Documentation

A complete PDF documentation will be added soon.

Christian, ce README est propre, cohérent, aligné avec ton style, et surtout fidèle à la vraie nature de TrackNet.

Maintenant, tu me balances tes nou