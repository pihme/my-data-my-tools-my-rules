---
name: Pi-hole
slug: pi-hole
category: Server
license: EUPL-1.2
open_source: true
type: Server
audience: enthusiast
url: https://pi-hole.net/
repo: https://github.com/pi-hole/pi-hole
source_url: https://github.com/pi-hole/pi-hole/blob/master/LICENSE
checked: 2026-11-11
added: 2026-11-11
note: DNS server for your home network that blocks ads and trackers for every device using it.
summary: Pi-hole is a DNS server for your home network that blocks ads and trackers for every device that uses it. It runs on a Raspberry Pi, any small Linux machine or in Docker, needs a fixed IP address, and includes a web interface for block lists and query logs. Devices use it once your router hands out its address as DNS server.
corporate_note: Copyright holder in the LICENSE files is Pi-hole, LLC; "Pi-hole" and the Pi-hole logo are trademarks under its brand guidelines.
sources:
  - https://pi-hole.net/
  - https://github.com/pi-hole/pi-hole/blob/master/LICENSE
  - https://github.com/pi-hole/FTL/blob/master/LICENSE
  - https://github.com/pi-hole/web/blob/master/LICENSE
  - https://docs.pi-hole.net/main/prerequisites/
  - https://docs.pi-hole.net/main/basic-install/
  - https://docs.pi-hole.net/main/post-install/
  - https://docs.pi-hole.net/docker/
  - https://pi-hole.net/trademark-rules-and-brand-guidelines/
---
## Why it fits

Pi-hole is free and EUPL-licensed and runs entirely on your own hardware. DNS lookups for your whole network go through a machine you control instead of your provider's resolver.

## Getting started

Prerequisites (from the official docs):

- A supported Linux system (Alpine, Armbian, Debian, CentOS Stream, Fedora, Raspberry Pi OS or Ubuntu), or Docker
- At least 2 GB free disk space (4 GB recommended) and 512 MB RAM
- A static IP address for the machine (a DHCP reservation is fine)
- Port 53 free (no other DNS server running); web interface on 80/443

Steps:

1. Run the installer: `curl -sSL https://install.pi-hole.net | bash` (or download/clone and run `basic-install.sh` to read it first).
2. Follow the installer prompts.
3. Set or note the web interface password (`pihole setpassword`).
4. Configure your router so DHCP clients get the Pi-hole address as DNS server (or use Pi-hole's own DHCP server, or set DNS per device).
5. Open the web interface and check that queries arrive and are blocked.

Watch out: the host itself does not use Pi-hole after installation unless you configure it; if it does and Pi-hole fails, the host loses DNS. Firewall rules in the docs restrict access to the local network.

Official install docs: <https://docs.pi-hole.net/main/basic-install/>

Docker: <https://docs.pi-hole.net/docker/>

## Notes

License: Pi-hole core, FTL (the DNS resolver) and the web interface are each EUPL-1.2 per their LICENSE files; the core LICENSE excludes commits made to master before version 3.0, which keep their earlier licenses. The one-step install pipes a script into bash; the docs offer alternatives to review the code first. Logo not shown: the Pi-hole brand guidelines allow the word mark but not the logo for supporting the project (pi-hole.net/trademark-rules-and-brand-guidelines).
