---
name: Garage
slug: garage
category: Server
license: AGPL-3.0-only
open_source: true
type: Server
audience: expert
url: https://garagehq.deuxfleurs.fr/
repo: https://git.deuxfleurs.fr/Deuxfleurs/garage
source_url: https://github.com/deuxfleurs-org/garage/blob/main-v2/LICENSE
checked: 2026-11-05
setup_steps: 4
setup_clarity: 3
setup_tested: 2026-11-06
note: Lightweight S3-compatible object storage for self-hosting.
summary: Garage is an S3-compatible object storage server designed for self-hosting on modest hardware spread across several locations. It replicates data between nodes so that a cluster survives the loss of a machine or a site. It is written in Rust and developed by the French non-profit Deuxfleurs. Running it well needs S3 and cluster administration knowledge.
corporate_note: Deuxfleurs association.
funding_note: FUTO microgrant (July 2024); NLnet funded Garage through the NGI0 Entrust Fund (EU Next Generation Internet).
funders: [futo, nlnet, ngi]
icon: assets/icons/garage.svg
icon_credit: Garage logo from the Garage repository (AGPL-3.0); used to identify the project
icon_source: https://git.deuxfleurs.fr/Deuxfleurs/garage/src/branch/main-v2/doc/logo/garage-notext.svg
fireworks_image: assets/fireworks/cf-garage-b1.webp
fireworks_date: 2026-11
sources:
  - https://garagehq.deuxfleurs.fr/
  - https://git.deuxfleurs.fr/Deuxfleurs/garage
  - https://github.com/deuxfleurs-org/garage/blob/main-v2/LICENSE
  - https://garagehq.deuxfleurs.fr/documentation/quick-start/
  - https://futo.tech/grants
  - https://nlnet.nl/project/Garage/
---
## Why it fits

The canonical repository is on git.deuxfleurs.fr, with a GitHub mirror under deuxfleurs-org/garage, and the software is licensed under GNU AGPL version 3. You can run your own object store without a paid software license for private use.

## Getting started

Prerequisites (from the official docs):

- A Linux machine with the Garage binary or Docker
- Free ports 3900-3903 (S3 API, RPC, web and admin endpoints)
- Basic familiarity with S3 tools and the command line
- For real use: several nodes, ideally in different locations; a single node is only for testing

Steps:

1. Install the Garage binary or pull the official Docker image.
2. Write a garage.toml configuration with data and metadata paths and an RPC secret.
3. Start the server and use the garage CLI to assign a cluster layout.
4. Create a bucket and an access key, then connect an S3 client.

Watch out: in the official Docker quick-start snippet, put a line continuation (`\`) after the image name so `/garage server --single-node --default-bucket` runs inside the container; without it those flags run on the host and the node stays without a role.

Official quick start: <https://garagehq.deuxfleurs.fr/documentation/quick-start/>

## Notes

License file on the canonical forge: <https://git.deuxfleurs.fr/Deuxfleurs/garage/src/branch/main/LICENSE>.
