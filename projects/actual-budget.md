---
name: Actual Budget
slug: actual-budget
category: Finances
license: MIT
open_source: true
type: [App, Server]
audience: end-user
url: https://actualbudget.org/
repo: https://github.com/actualbudget/actual
source_url: https://github.com/actualbudget/actual/blob/master/LICENSE.txt
demo: https://demo.actualbudget.org/
demo_note: Official demo linked from the install docs; data stays in your browser.
checked: 2026-11-11
added: 2026-11-11
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-11
note: Local-first envelope budgeting app; optional self-hosted sync server; bank sync optional with your own keys.
summary: Actual Budget is a local-first app for envelope budgeting. It runs as a desktop app on Windows, macOS and Linux without any server, or as a self-hosted sync server that serves the web app and syncs budgets between devices, with optional end-to-end encryption. Bank sync is optional and needs your own API keys from a third-party provider.
funding_note: Community project funded through Open Collective (fiscal host Open Source Collective) and GitHub Sponsors.
icon: assets/icons/actual-budget.png
icon_credit: Actual Budget app icon from the MIT-licensed repository; used to identify the project
icon_source: https://github.com/actualbudget/actual/blob/master/packages/desktop-client/public/apple-touch-icon.png
sources:
  - https://actualbudget.org/
  - https://github.com/actualbudget/actual/blob/master/LICENSE.txt
  - https://github.com/actualbudget/actual/blob/master/README.md
  - https://actualbudget.org/docs/install/
  - https://actualbudget.org/docs/install/docker
  - https://actualbudget.org/docs/config/https
  - https://actualbudget.org/docs/advanced/bank-sync
  - https://actualbudget.org/download/
  - https://opencollective.com/actual
---
## Why it fits

MIT-licensed and free. The desktop app works fully offline without any account, and the optional sync server is one you run yourself; there is no vendor cloud you have to use.

## Getting started

Prerequisites (from the official docs):

- Desktop route: Windows, macOS or Linux (installers, Microsoft Store, Flathub and AppImage on actualbudget.org/download)
- Server route: a machine with Docker (or the Server CLI / Node.js), port 5006, a data folder
- HTTPS for the server when it is used from other devices; not needed on localhost

Steps:

1. Desktop: install the app for your system from the download page and create a budget; done.
2. Server: start the container with the `docker run` command from the Docker docs (`-p 5006:5006`, `-v <data>:/data`, image `actualbudget/actual-server:latest`).
3. Open http://<server>:5006 and set the server password.
4. Create a new budget or import one (YNAB4/nYNAB importers and file imports are built in).
5. Optional: connect the desktop app or other browsers to the server to sync.

Watch out: the server password cannot be recovered; losing it means losing access to the budget. For use beyond localhost, set up HTTPS (docs: Activating HTTPS). The "docker-compose.yml included in the actual repository" mentioned in the Docker docs is `packages/sync-server/docker-compose.yml`, not the development file at the repo root.

Official install docs: <https://actualbudget.org/docs/install/>

## Notes

Hosting options: the docs and README also list paid third-party hosting (PikaPods, where part of the fee goes to the project, and Fly.io); both are optional. Bank sync is optional and works only with the server: you sign up with a provider and use your own API keys (Enable Banking for European banks; GoCardless Bank Account Data is listed as no longer accepting new accounts; SimpleFIN for North America; Akahu, Pluggy.ai). Per the docs, bank-sync keys are stored on the server and not covered by end-to-end encryption. The browser-only web app keeps data only in the browser and is not recommended for long-term use. LICENSE.txt is the MIT text with "Copyright James Long" (the original author).
