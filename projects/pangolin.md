---
name: Pangolin
slug: pangolin
category: Server
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://pangolin.net/
repo: https://github.com/fosrl/pangolin
source_url: https://github.com/fosrl/pangolin/blob/main/LICENSE
checked: 2026-11-06
note: Self-hosted tunneled reverse proxy to reach home services through your own VPS, no open ports at home.
summary: Pangolin is a self-hosted reverse proxy and VPN that makes services in your home network reachable from outside without opening ports there. A small connector at home opens outbound WireGuard tunnels to a Pangolin server with a public IP, usually a rented VPS. Access is controlled with logins and per-resource rules. It is not based on Tailscale.
corporate_note: "Developed by Fossorial, Inc., which also sells Pangolin Cloud and Enterprise Edition licenses. A self-hosted server keeps the control plane and traffic on your own infrastructure."
funding_note: FUTO microgrant (May 2025), listed on FUTO's grants page.
funders: [futo]
fireworks_image: assets/fireworks/cf-pangolin-b1.webp
fireworks_date: 2026-11
sources:
  - https://pangolin.net/
  - https://github.com/fosrl/pangolin/blob/main/LICENSE
  - https://github.com/fosrl/pangolin/blob/main/README.md
  - https://pangolin.net/fcl
  - https://docs.pangolin.net/about/how-pangolin-works
  - https://docs.pangolin.net/about/pangolin-cloud-vs-self-hosted
  - https://docs.pangolin.net/self-host/quick-install
  - https://docs.pangolin.net/self-host/dns-and-networking
  - https://github.com/fosrl/newt/blob/main/LICENSE
  - https://github.com/fosrl/gerbil/blob/main/LICENSE
  - https://futo.tech/grants
---
## Why it fits

The self-hosted Community Edition is licensed under AGPL-3.0 and free to run. Server, connectors and access rules stay on machines you control, so no third-party tunnel service such as Cloudflare Tunnel is needed.

## Getting started

Prerequisites (from the official docs):

- A Linux server with root access and a public IP address, usually a small VPS
- A domain whose DNS records point to that server
- An email address for Let's Encrypt certificates and the admin login
- Open ports on that server: 80 and 443 (TCP), 51820 and 21820 (UDP)
- A machine in your home network for the site connector (binary or Docker container)

Steps:

1. Download the installer on the server and run it with root privileges.
2. Choose Community Edition and enter your base domain, dashboard domain and email; keep tunneling (Gerbil) enabled.
3. Open the initial setup page, paste the setup token from the Pangolin container logs and create the admin account and an organization.
4. Create a site in the dashboard and run the shown connector command on a machine in your home network.
5. Add resources for the services you want to reach and grant users access.

Watch out: The server becomes part of your security boundary because your home network tunnels out to it; expose only the ports the docs list.

Official install docs: <https://docs.pangolin.net/self-host/quick-install>

## Notes

License: the repository is dual-licensed. Files without a license header and files marked AGPL-3 are under AGPL-3.0 (the LICENSE names version 3 without an "or later" clause); these make up the Community Edition, which is OSI open source. Files marked with a Fossorial Commercial License header form the Enterprise Edition, which is proprietary and not OSI open source. Per the docs, the Enterprise Edition is free for personal use and for organizations under USD 100,000 annual revenue but needs a license key. `open_source: true` applies to the Community Edition only.

Pangolin is not based on Tailscale and does not use Tailscale's coordination servers. It builds its own WireGuard tunnels with the Gerbil server component and the Newt site connector, both AGPL-3.0. Pangolin Cloud, a managed service run by Fossorial, is optional.

The repositories of the desktop and mobile clients use the same mixed AGPL-3.0 and Fossorial Commercial License scheme as the server.

No logo is included: Fossorial's terms of service reserve its name and logos as trademarks, and the repository states no separate license for the logo files.
