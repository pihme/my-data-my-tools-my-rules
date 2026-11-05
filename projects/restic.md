---
name: restic
slug: restic
category: Backup
license: BSD-2-Clause
open_source: true
type: App
audience: enthusiast
url: https://restic.net/
repo: https://github.com/restic/restic
source_url: https://github.com/restic/restic/blob/master/LICENSE
checked: 2026-11-05
setup_steps: 5
setup_clarity: 3
setup_tested: 2026-11-06
note: Encrypted, deduplicated command-line backups to disks, SFTP or cloud storage.
summary: restic is a command-line backup program for Linux, macOS, Windows and BSD. It stores encrypted, deduplicated snapshots in a repository on a local disk, an SFTP server, or S3-compatible and other cloud storage. You can restore single files or whole snapshots. restic has no built-in scheduler, so regular backups are set up with cron, systemd timers or Task Scheduler.
funding_note: The project README states that AppsCode sponsors the backend integration tests for Google Cloud Storage and Azure Blob Storage.
sources:
  - https://restic.net/
  - https://github.com/restic/restic/blob/master/LICENSE
  - https://github.com/restic/restic/blob/master/README.md
  - https://restic.readthedocs.io/en/stable/020_installation.html
  - https://restic.readthedocs.io/en/stable/040_backup.html
---

restic is a backup program that runs on your own computer and writes encrypted, deduplicated snapshots to a repository you choose. The repository LICENSE is the BSD 2-Clause License.

## Why it fits

Free to install and run for private backups; the storage target can be your own disk or server, so no third-party service is required.

## Getting started

Prerequisites (from the official docs):

- A Linux, macOS, Windows or BSD computer and a terminal
- A place for the backup repository: a local or USB disk, an SFTP server, or S3-compatible or other supported cloud storage
- A way to schedule runs, such as cron, a systemd timer or Windows Task Scheduler

Steps:

1. Install restic from your package manager or as an official binary.
2. Create a repository with restic init and store the password safely.
3. Run your first backup with restic backup <paths>.
4. Check that a restore works with restic restore or by mounting a snapshot.
5. Schedule regular backups and a forget/prune policy with your system scheduler.

Official installation docs: <https://restic.readthedocs.io/en/stable/020_installation.html>

Backing up and scheduling: <https://restic.readthedocs.io/en/stable/040_backup.html>

## Notes

CLI only; graphical front ends are separate community projects and are not covered here.
