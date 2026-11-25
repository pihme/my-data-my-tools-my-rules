---
name: Backrest
slug: backrest
category: Server
license: GPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://garethgeorge.github.io/backrest/
repo: https://github.com/garethgeorge/backrest
source_url: https://github.com/garethgeorge/backrest/blob/main/LICENSE
checked: 2026-11-25
added: 2026-11-25
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-25
note: Web interface and scheduler for restic backups, as a single binary or a Docker container.
summary: Backrest is a web interface and scheduler for restic. It creates or imports restic repositories, runs backups, prune and check jobs on a cron schedule, lets you browse and restore files from snapshots, and sends notifications. It runs as a single binary on Linux, macOS, Windows and FreeBSD or in Docker, and downloads a suitable restic version if none is installed.
icon: assets/icons/backrest.svg
icon_credit: Backrest icon from the GPL-3.0 repository; used to identify the project
icon_source: https://github.com/garethgeorge/backrest/blob/main/webui/assets/favicon.svg
fireworks_image: assets/fireworks/cf-backrest-b1.webp
fireworks_date: 2026-11
role: Web UI for restic
works_with: [restic]
sources:
  - https://garethgeorge.github.io/backrest/
  - https://github.com/garethgeorge/backrest/blob/main/LICENSE
  - https://github.com/garethgeorge/backrest/blob/main/README.md
  - https://garethgeorge.github.io/backrest/introduction/getting-started
---
## Why it fits

Backrest is licensed under GNU GPL version 3 and free to use. It runs on your own machine and stores backups wherever restic can write, from a local disk to your own SFTP server or cloud storage you choose.

## Getting started

Prerequisites (from the official docs):

- Linux, macOS, Windows or FreeBSD, or any host with Docker
- A storage location for the restic repository (local path, SFTP, S3-compatible or other restic backends, or rclone remotes)
- restic is optional: Backrest uses a compatible installed version or downloads one into its data directory

Steps (Docker Compose, as checked):

1. Copy the Docker Compose block from the README and set the paths for data, config, cache, the folders to back up and local repositories.
2. Start the container with `docker compose up -d` and open the web interface on port 9898.
3. In the first-run dialog, set the instance ID and create a user name and password.
4. Add a repository ("Add Repo") and a backup plan ("Add Plan") with a schedule.

Watch out: until the first user is created in the web interface, there is no login, so anyone who can reach the port can configure the instance; the Compose example publishes port 9898 on all interfaces. The instance ID cannot be changed in the web interface after the first setup.

Official getting started guide: <https://garethgeorge.github.io/backrest/introduction/getting-started>

Installation (README): <https://github.com/garethgeorge/backrest#installation>

## Notes

Backrest is developed separately from restic by its own author; it wraps the restic command line, and its repositories are normal restic repositories. Tested with Backrest 1.14.1 and the bundled restic 0.19.1 on 2026-11-25. The Linux and macOS install script and the Homebrew tap were not tested.
