# MDMTMR project dossiers

Markdown dossiers for **My Data, My Tools, My Rules** (MDMTMR).
These are the source files for the project pages of this site. A plain Python static builder generates the pages from them.

- `projects/<slug>.md` — one file per candidate
- `TEMPLATE.md` — blank template
- All prose is English
- Do not invent facts; if a claim is not checked against a primary source, write `unverified`

## Front matter schema

Exact field names (YAML):

| Field | Required | Type | Meaning |
| --- | --- | --- | --- |
| `name` | yes | string | Display name |
| `slug` | yes | string | Lowercase, no special characters; file is `projects/<slug>.md` |
| `category` | yes | string | Category label shown on the site |
| `license` | yes | string | SPDX id; for source-available without SPDX use `LicenseRef-<Name>` (e.g. `LicenseRef-SourceFirst-1.1`) |
| `open_source` | yes | bool | `true` only for OSI-approved licenses; otherwise `false` |
| `type` | yes | string or list | `App` or `Server`; list both when applicable (the site labels `Server` as "Self-host") |
| `audience` | yes | string | Who can run it for private use: `end-user` (apps and desktop applications you just install), `enthusiast` (Docker containers, home server, self-hosting with some setup), `expert` (needs deep ops knowledge, e.g. your own S3/object storage or mail server). One value; for borderline cases pick one |
| `url` | yes | string | Official website |
| `repo` | yes | string | Source code repository URL |
| `source_url` | yes | string | Direct link to the project's LICENSE file (used to check the license) |
| `demo` | no | string | URL of an official online demo or public instance run by the project, so readers can try it without installing; link from the project's own site or README |
| `demo_note` | no | string | One short line about the demo: login, reset interval, who runs it |
| `checked` | yes | date | Verification date (`YYYY-MM-DD`) |
| `note` | no | string | One short sentence for the project card (~120 characters max) |
| `summary` | no | string | Opening text on the dossier page (and on cards where space allows): 2-4 plain, factual sentences (~250-400 characters), no marketing superlatives. Shown instead of `note` where the layout has room |
| `corporate_note` | no | string | Optional corporate / org binding (info only, never exclusion) |
| `funding_note` | no | string | Optional one-sentence funding note; the source URL goes into `sources`; funding is not decisive and not proof of a license |
| `funders` | no | list | Funder slugs linking to the Funders page, e.g. `[futo, nlnet, ngi]` |
| `icon` | no | string | Path to the official logo, `assets/icons/<slug>.svg` or `.png`; only when its license/terms are documented in ASSETS.md |
| `icon_credit` | no | string | Credit/trademark line shown with the icon |
| `icon_source` | no | string | URL the icon file was taken from |
| `screenshot` | no | string | Path to an official screenshot, `assets/screenshots/<slug>.webp` (max 1600 px wide); only with a documented reuse license |
| `screenshot_credit` | no | string | Credit/license line shown with the screenshot |
| `screenshot_source` | no | string | URL the screenshot was taken from |
| `fireworks_image` | no | string | Path to the project's Code Fireworks render, `assets/fireworks/cf-<slug>-b1.png` (560×560 PNG, our own Gource render of the public repository); set together with `fireworks_date`; listed in ASSETS.md |
| `fireworks_date` | no | string | Snapshot month of the render (`YYYY-MM`); shown as "As of Nov 2026"; a fixed date, so the image never needs re-rendering |
| `sources` | yes | list | URLs used for verification |
| `setup_steps` | no | integer | Count of human actions in the official getting-started path that was checked |
| `setup_clarity` | no | integer 1–5 | How clear that path was (1 = unusable, 5 = copy-paste works and is well explained) |
| `setup_tested` | no | date | Date the path was hands-on checked (`YYYY-MM-DD`); omit all three `setup_*` fields when not checked |

## Body sections

Free-form Markdown after the front matter. Keep each dossier short. The `summary` field is the opening text; do not repeat it as a body paragraph. Suggested headings:

1. `## Why it fits` — free private self-install
2. `## Getting started` — short prerequisites list, 3-6 high-level steps, the official install-doc link, and optional short `Watch out:` lines for pitfalls in that official path
3. `## Notes` — caveats, labels, unverified items

## Admission rule (context)

Anything an individual can install for private use free of charge qualifies. Source-available / fair-use style licenses are allowed and labeled via `open_source: false` plus the SPDX/`LicenseRef-*` id.

## Status

30 dossiers (22 from the initial research, plus restic, Paperless-ngx, Beszel, Uptime Kuma, ONLYOFFICE, OpenCode, Pangolin and Jitsi Meet; checked 2026-11-05/06, Europe/Berlin). Categories: AI, Files, Media, Mobile, Office, Passwords, Server, Smart Home, Utilities.
