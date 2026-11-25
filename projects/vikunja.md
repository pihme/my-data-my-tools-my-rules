---
name: Vikunja
slug: vikunja
category: Office
license: AGPL-3.0-or-later
open_source: true
type: Server
audience: enthusiast
url: https://vikunja.io/
repo: https://github.com/go-vikunja/vikunja
source_url: https://github.com/go-vikunja/vikunja/blob/main/LICENSE
demo: https://try.vikunja.io/
demo_note: Public demo instance linked from the README.
checked: 2026-11-25
added: 2026-11-25
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-25
note: Self-hosted to-do lists and projects with list, Kanban, table and Gantt views.
summary: Vikunja is a self-hosted task manager for personal to-do lists and team projects. Tasks live in projects that can be shown as a list, Kanban board, table or Gantt chart, with labels, due dates, reminders, sharing and CalDAV access. It runs as a single binary or in Docker with SQLite, MySQL or PostgreSQL, and the web interface is included.
corporate_note: vikunja.io and the paid hosted service vikunja.cloud are run by Konrad Langenberg Software (Lübeck) per the imprint; organisations can buy Vikunja Pro for extra features.
funding_note: The README asks for support via GitHub Sponsors, Buy Me a Coffee and sticker sales and lists the hosted version and Vikunja Pro as paid offers.
icon: assets/icons/vikunja.svg
icon_credit: Vikunja logo from the AGPL-3.0 repository; used to identify the project
icon_source: https://github.com/go-vikunja/vikunja/blob/main/frontend/src/assets/logo.svg
fireworks_image: assets/fireworks/cf-vikunja-b1.webp
fireworks_date: 2026-11
sources:
  - https://vikunja.io/
  - https://github.com/go-vikunja/vikunja/blob/main/LICENSE
  - https://github.com/go-vikunja/vikunja/blob/main/README.md
  - https://vikunja.io/imprint/
  - https://vikunja.io/docs/installing/
  - https://vikunja.io/docs/full-docker-example/
  - https://github.com/go-vikunja/vikunja/blob/main/pkg/license/license.go
---
## Why it fits

Vikunja is licensed under the GNU AGPL version 3 or later and is free to self-host. According to the comments in its license-check code, the free version is fully functional; a paid license key only unlocks optional features for organisations.

## Getting started

Prerequisites (from the official docs):

- A server with Docker and Docker Compose (a single binary and packages are also available)
- A database: SQLite for small setups, or PostgreSQL or MySQL/MariaDB
- A folder for uploaded files that the container user (UID 1000) can write to

Steps (the "Example without any proxy" from the full Docker example):

1. Create the `files` folder and give it to UID 1000 (`chown 1000`).
2. Copy the Compose example and set the service secret, the public URL and the database password.
3. Start the stack with `docker compose up -d` and open the web interface on port 3456.
4. Register an account and log in, then create a project and your first task.

Watch out: registration is open by default; turn it off in the configuration once your accounts exist if the instance can be reached from the internet. The PostgreSQL example omits `POSTGRES_DB`, which works because the database name defaults to the user name.

Official installation docs: <https://vikunja.io/docs/installing/>

Full Docker example: <https://vikunja.io/docs/full-docker-example/>

## Notes

Tested with Vikunja v2.8.0 and PostgreSQL 18 on 2026-11-25. The desktop app in the `desktop/` folder is licensed GPL-3.0-or-later. The README notes that LLM-assisted coding tools are used in parts of the development. Vikunja Pro (admin panel, audit logs, time tracking per the README) and the hosted vikunja.cloud are optional paid offers and not needed for private use.
