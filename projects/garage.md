---
name: Garage
slug: garage
category: Cloud/Files (tentative)
license: AGPL-3.0-only
open_source: true
type: Server
audience: expert
url: https://garagehq.deuxfleurs.fr/
repo: https://git.deuxfleurs.fr/Deuxfleurs/garage
source_url: https://github.com/deuxfleurs-org/garage/blob/main-v2/LICENSE
checked: 2026-11-05
note: Lightweight S3-compatible object storage for self-hosting.
summary: Garage is an S3-compatible object storage server designed for self-hosting on modest hardware spread across several locations. It replicates data between nodes so that a cluster survives the loss of a machine or a site. It is written in Rust and developed by the French non-profit Deuxfleurs. Running it well needs S3 and cluster administration knowledge.
corporate_note: Deuxfleurs association.
funding_note: FUTO microgrant (July 2024); NLnet funded Garage through the NGI0 Entrust Fund (EU Next Generation Internet).
funders: [futo, nlnet, ngi]
icon: assets/icons/garage.svg
icon_credit: Garage logo from the Garage repository (AGPL-3.0); used to identify the project
icon_source: https://git.deuxfleurs.fr/Deuxfleurs/garage/src/branch/main-v2/doc/logo/garage-notext.svg
sources:
  - https://garagehq.deuxfleurs.fr/
  - https://git.deuxfleurs.fr/Deuxfleurs/garage
  - https://github.com/deuxfleurs-org/garage/blob/main-v2/LICENSE
  - https://garagehq.deuxfleurs.fr/documentation/quick-start/
  - https://futo.tech/grants
  - https://nlnet.nl/project/Garage/
---

Garage is a distributed object-storage system with an S3-compatible API, aimed at self-hosted and geo-distributed setups. Canonical repository is on git.deuxfleurs.fr; a GitHub mirror exists under deuxfleurs-org/garage. It is licensed under the GNU AGPL version 3.

## Why it fits

You can run your own object store without a paid software license for private use.

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

Official quick start: <https://garagehq.deuxfleurs.fr/documentation/quick-start/>

## Notes

License file on the canonical forge: <https://git.deuxfleurs.fr/Deuxfleurs/garage/src/branch/main/LICENSE>.
