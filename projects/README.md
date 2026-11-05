# MDMTMR project dossiers

Markdown dossiers for **My Data, My Tools, My Rules** (MDMTMR).
Maintainer can copy these into `github.com/pihme/my-data-my-tools-my-rules` so a plain Python static builder can generate the site (similar spirit to freigeist).

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
| `category` | yes | string | Tentative taxonomy label (not final) |
| `license` | yes | string | SPDX id; for source-available without SPDX use `LicenseRef-<Name>` (e.g. `LicenseRef-SourceFirst-1.1`) |
| `open_source` | yes | bool | `true` only for OSI-approved licenses; otherwise `false` |
| `type` | yes | string or list | `App` or `Server`; list both when applicable |
| `url` | yes | string | Official website |
| `repo` | yes | string | Source code repository URL |
| `source_url` | yes | string | Direct link to the project's LICENSE file (used to check the license) |
| `checked` | yes | date | Verification date (`YYYY-MM-DD`) |
| `note` | no | string | One short sentence for the project card (~120 characters max) |
| `corporate_note` | no | string | Optional corporate / org binding (info only, never exclusion) |
| `funding_note` | no | string | Optional brief funding note with source; funding is not decisive |
| `sources` | yes | list | URLs used for verification |

## Body sections

Free-form Markdown after the front matter. Keep each dossier short. Suggested headings:

1. Short neutral description (2–4 sentences)
2. `## Why it fits` — free private self-install
3. `## Getting started` — link to official install docs only
4. `## Notes` — caveats, labels, unverified items

## Admission rule (context)

Anything an individual can install for private use free of charge qualifies. Source-available / fair-use style licenses are allowed and labeled via `open_source: false` plus the SPDX/`LicenseRef-*` id.

## Status

Initial set: 24 candidates from the planning Page (checked 2026-11-05, Europe/Berlin). Taxonomy for `category` is tentative.
