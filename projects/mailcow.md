---
name: mailcow
slug: mailcow
category: Email (tentative)
license: GPL-3.0-only
open_source: true
type: Server
url: https://mailcow.github.io/mailcow-dockerized-docs/
repo: https://github.com/mailcow/mailcow-dockerized
source_url: https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
checked: 2026-11-05
note: Dockerized mail server stack for self-hosted email.
summary: "mailcow: dockerized is a complete mail server suite packaged with Docker Compose, including SMTP and IMAP servers, spam filtering, webmail, and an admin web interface. It lets you run email for your own domains instead of using a hosted provider. Running a mail server needs a server with a static IP address, correct DNS records, and ongoing maintenance."
audience: Expert
sources:
  - https://mailcow.github.io/mailcow-dockerized-docs/
  - https://github.com/mailcow/mailcow-dockerized/blob/master/LICENSE
  - https://docs.mailcow.email/getstarted/install/
---

mailcow (mailcow: dockerized) is a mail server suite packaged with Docker Compose (MTA, MDA, web UI, and related services). LICENSE is GPL version 3.

## Why it fits

You can deploy it on your own VPS or hardware for private mail without a proprietary mail-suite license.

## Getting started

Official install docs: <https://docs.mailcow.email/getstarted/install/>

## Notes

Operating email on the public internet also requires domain/DNS and operational care (deliverability); that is outside license scope.
