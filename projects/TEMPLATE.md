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
checked: 2026-11-05
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-06
# optional; omit all three setup_* fields when the getting-started path was not hands-on checked
note: Optional card blurb, max about 120 characters.
summary: Optional card paragraph, 2-4 plain factual sentences (about 250-400 characters), no superlatives.
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
sources:
  - https://example.org/
  - https://github.com/example/project/blob/main/LICENSE
---

Short neutral description (2–4 sentences). No marketing language.

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
