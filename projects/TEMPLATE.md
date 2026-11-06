---
name: Project Name
slug: project-name
category: Category
license: SPDX-or-LicenseRef
open_source: true
type: App
# type can also be a list, e.g. [App, Server]
audience: enthusiast
# audience: end-user (just install an app) | enthusiast (Docker/home server, some setup) | expert (deep ops knowledge, e.g. own object storage or mail server)
url: https://example.org/
repo: https://github.com/example/project
source_url: https://github.com/example/project/blob/main/LICENSE
demo: https://demo.example.org/
demo_note: Optional; login, reset interval, who runs it.
# demo fields are optional; only official demos linked from the project's site or README
checked: 2026-11-05
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-06
# optional; omit all three setup_* fields when the getting-started path was not hands-on checked
note: Optional card blurb, max about 120 characters.
summary: Opening text shown as the dossier lead (and on cards where space allows): 2-4 plain factual sentences (about 250-400 characters), no superlatives.
corporate_note: Optional org binding (info only).
funding_note: Optional one-sentence funding note (source URL in sources).
funders: [futo]
# optional; funder slugs for the Funders page
icon: assets/icons/project-name.svg
icon_credit: Logo (c) Project, license or trademark line
icon_source: https://github.com/example/project/blob/main/logo.svg
screenshot: assets/screenshots/project-name.webp
screenshot_credit: Screenshot from the project repository, license
screenshot_source: https://github.com/example/project/blob/main/docs/screenshot.png
# icon/screenshot fields are optional; use only assets cleared in ASSETS.md
fireworks_image: assets/fireworks/cf-project-name-b1.webp
fireworks_date: 2026-11
# optional; both together; our own Code Fireworks render, listed in ASSETS.md
sources:
  - https://example.org/
  - https://github.com/example/project/blob/main/LICENSE
---
<!-- The `summary` front-matter field is the opening text on the page; do not add a duplicate intro paragraph here. -->

## Why it fits

Explain free private self-install in one or two sentences.

## Getting started

Prerequisites (from the official docs):

- What you need (device, OS, Docker, domain, RAM ...)

Steps:

1. Three to six high-level steps.
2. ...

Watch out: Optional one-line tip when the official guide has a known pitfall; omit if none.

Official install docs: <https://example.org/docs/install>

## Notes

Caveats, license labels, or `unverified` items.
