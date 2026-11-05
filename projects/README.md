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
| `summary` | no | string | Card paragraph, 2–4 sentences: what it is, what it replaces or helps with, how you run it. Neutral, facts from the project's own site or repo, US spelling. Falls back to `note` |
| `audience` | no | string | `End user`, `Enthusiast` or `Expert` (editorial estimate of the experience needed to run it) |
| `icon` | no | map | Project logo, only if its license or brand guidelines allow use in a catalog: `file` (in `assets/projects/<slug>/`), `credit`, `license`, `source` (URL), optional `note` (e.g. trademark terms). Shown unmodified; without it the card shows a letter tile |
| `screenshots` | no | list of maps | Only screenshots published under a reusable license: `file` (16:10 WebP in `assets/projects/<slug>/`), `caption`, `credit`, `license`, `source` |
| `funding` | no | list of maps | `funder` (must match `name` in `funders/<slug>.md`), `what`, optional `when`, `source` (grant page or project announcement). Funding is not decisive and says nothing about the license |
| `funding_note` | no | string | Optional free-text funding note with source (prefer `funding`) |
| `sources` | yes | list | URLs used for verification |

Example of the map and list fields:

```yaml
icon:
  file: "icon.svg"
  credit: "Example Project contributors"
  license: "CC-BY-SA-4.0"
  source: "https://github.com/example/project/blob/main/logo.svg"
screenshots:
  - file: "screenshot-1.webp"
    caption: "Main window"
    credit: "Example Project contributors"
    license: "GPL-3.0-only (repository license)"
    source: "https://github.com/example/project/tree/main/screenshots"
funding:
  - funder: "NLnet"
    what: "NGI0 Entrust grant"
    when: "2023-04 to 2024-07"
    source: "https://nlnet.nl/project/Example/"
```

Logo and screenshot decisions (used or not, and why) are tracked in [MEDIA.md](MEDIA.md). Screenshots are framed to 16:10 (letterboxed on a neutral background, never stretched or cropped into the content) and skipped if the source is too small to stay sharp.

## Body sections

Free-form Markdown after the front matter. Keep each dossier short. Suggested headings:

1. Short neutral description (2–4 sentences)
2. `## Why it fits` — free private self-install
3. `## Getting started` — prerequisites, 3–6 numbered steps (fenced code blocks allowed) and the official install docs link
4. `## Notes` — caveats, labels, unverified items

## Admission rule (context)

Anything an individual can install for private use free of charge qualifies. Source-available / fair-use style licenses are allowed and labeled via `open_source: false` plus the SPDX/`LicenseRef-*` id.

## Status

Initial set: 24 candidates from the initial research (checked 2026-11-05, Europe/Berlin). Taxonomy for `category` is tentative.
