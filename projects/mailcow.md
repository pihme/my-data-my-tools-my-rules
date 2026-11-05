---
name: mailcow
slug: mailcow
category: Email (tentative)
license: GPL-3.0-only
open_source: true
type: Server
audience: expert
url: https://mailcow.github.io/mailcow-dockerized-docs/
repo: https://github.com/mailcow/mailcow-dockerized
source_url: https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
checked: 2026-11-05
note: Dockerized mail server stack for self-hosted email.
summary: mailcow: dockerized is a complete mail server suite in Docker containers. It combines Postfix, Dovecot, SOGo groupware, Rspamd spam filtering and ClamAV behind a web admin interface and handles mail, calendars and contacts for your own domains. Running a mail server means managing DNS records, IP reputation and deliverability, which needs solid ops experience.
sources:
  - https://mailcow.github.io/mailcow-dockerized-docs/
  - https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
  - https://docs.mailcow.email/getstarted/install/
  - https://docs.mailcow.email/getstarted/prerequisite-dns/
  - https://docs.mailcow.email/getstarted/prerequisite-system/
  - https://github.com/mailcow/mailcow-dockerized/blob/master/README.md
---

mailcow (mailcow: dockerized) is a mail server suite packaged with Docker Compose (MTA, MDA, web UI, and related services). LICENSE is GPL version 3.

## Why it fits

You can deploy it on your own VPS or hardware for private mail without a proprietary mail-suite license.

## Getting started

Prerequisites (from the official docs):

- A dedicated server or VPS (x86_64 or ARM64; OpenVZ, Virtuozzo and LXC are not supported) with at least 6 GiB RAM plus 1 GiB swap and 20 GiB disk
- Docker 24 or newer with the Compose plugin, plus git, openssl, curl and jq
- A domain with DNS records you control: A/AAAA, MX, reverse DNS (PTR), and later SPF, DKIM and DMARC
- Open mail and web ports, including 25, 80, 443, 465, 587 and 993, and a correct system time

Steps:

1. Prepare DNS and the server as described on the two prerequisite pages.
2. Clone the mailcow-dockerized repository.
3. Run generate_config.sh and enter your mail hostname.
4. Start the stack with docker compose up -d.
5. Log in to the web UI, change the default admin password and add your domain and mailboxes.

Official install guide: <https://docs.mailcow.email/getstarted/install/>

DNS prerequisites: <https://docs.mailcow.email/getstarted/prerequisite-dns/>

System prerequisites: <https://docs.mailcow.email/getstarted/prerequisite-system/>

## Notes

Operating email on the public internet also requires domain/DNS and operational care (deliverability); that is outside license scope.
