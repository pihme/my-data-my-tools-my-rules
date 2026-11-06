---
name: mailcow
slug: mailcow
category: Server
license: GPL-3.0-only
open_source: true
type: Server
audience: expert
url: https://mailcow.github.io/mailcow-dockerized-docs/
repo: https://github.com/mailcow/mailcow-dockerized
source_url: https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
demo: https://demo.mailcow.email/
checked: 2026-11-05
setup_steps: 9
setup_clarity: 3
setup_tested: 2026-11-06
note: Dockerized mail server stack for self-hosted email.
summary: mailcow: dockerized is a complete mail server suite in Docker containers. It combines Postfix, Dovecot, SOGo groupware, Rspamd spam filtering and ClamAV behind a web admin interface and handles mail, calendars and contacts for your own domains. Running a mail server means managing DNS records, IP reputation and deliverability, which needs solid ops experience.
fireworks_image: assets/fireworks/cf-mailcow-b1.webp
fireworks_date: 2026-11
sources:
  - https://mailcow.github.io/mailcow-dockerized-docs/
  - https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
  - https://docs.mailcow.email/getstarted/install/
  - https://docs.mailcow.email/getstarted/prerequisite-dns/
  - https://docs.mailcow.email/getstarted/prerequisite-system/
  - https://github.com/mailcow/mailcow-dockerized/blob/master/README.md
  - https://mailcow.email/
---
## Why it fits

It is licensed under GPL version 3. You can deploy it on your own VPS or hardware for private mail without a proprietary mail-suite license.

## Getting started

Prerequisites (from the official docs):

- A dedicated server or VPS (x86_64 or ARM64; OpenVZ, Virtuozzo and LXC are not supported) with at least 6 GiB RAM plus 1 GiB swap and 20 GiB disk
- Docker 24 or newer with the Compose plugin, plus git, openssl, curl and jq
- A domain with DNS records you control: A/AAAA, MX, reverse DNS (PTR), and later SPF, DKIM and DMARC
- Open mail and web ports, including 25, 80, 443, 465, 587 and 993, and a correct system time

Steps:

1. Install the required packages on a supported dedicated server or VPS.
2. Install Docker and the Compose plugin as described in the system prerequisites.
3. Clone the mailcow-dockerized repository.
4. Run generate_config.sh and enter your mail hostname.
5. Review and edit mailcow.conf if needed.
6. Pull the images with docker compose pull.
7. Start the stack with docker compose up -d.
8. Create the DNS records (A/AAAA, MX, PTR, SPF, DKIM and DMARC) as documented.
9. Log in to the web UI, change the default admin password and add your domain and mailboxes.

Official install guide: <https://docs.mailcow.email/getstarted/install/>

DNS prerequisites: <https://docs.mailcow.email/getstarted/prerequisite-dns/>

System prerequisites: <https://docs.mailcow.email/getstarted/prerequisite-system/>

## Notes

Operating email on the public internet also requires domain/DNS and operational care (deliverability); that is outside license scope.
