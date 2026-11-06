---
name: Jitsi Meet
slug: jitsi-meet
category: Office
license: Apache-2.0
open_source: true
type: Server
audience: enthusiast
url: https://jitsi.org/jitsi-meet/
repo: https://github.com/jitsi/jitsi-meet
source_url: https://github.com/jitsi/jitsi-meet/blob/master/LICENSE
demo: https://meet.jit.si/
demo_note: Public service run by 8x8; starting a meeting needs a Google, Facebook or GitHub account.
checked: 2026-11-06
setup_steps: 6
setup_clarity: 3
setup_tested: 2026-11-06
note: Browser-based video meetings you can run on your own server.
summary: Jitsi Meet is a video conferencing platform that runs in the browser, with mobile apps for Android (including F-Droid) and iOS. It offers screen sharing, chat, polls, reactions and virtual backgrounds. You can use the public meet.jit.si service or run your own instance from Debian packages or the official Docker setup.
corporate_note: Since 2018 the Jitsi team and technology belong to 8x8, a cloud communications company that also sells Jitsi as a Service; the code remains Apache-2.0.
icon: assets/icons/jitsi-meet.png
icon_credit: Jitsi Meet app icon from the jitsi-meet repository, Apache-2.0 repository license; used to identify the project
icon_source: https://github.com/jitsi/jitsi-meet/blob/master/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png
sources:
  - https://jitsi.org/jitsi-meet/
  - https://github.com/jitsi/jitsi-meet
  - https://github.com/jitsi/jitsi-meet/blob/master/LICENSE
  - https://github.com/jitsi/docker-jitsi-meet/blob/master/LICENSE
  - https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker
  - https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-requirements
  - https://jitsi.org/blog/we-have-a-new-home-and-it-wont-impact-you/
  - https://jitsi.org/about/
---
## Why it fits

Jitsi Meet is a free, self-hostable alternative to Zoom or Google Meet: on your own instance, meetings run on your server, and guests join from a browser without an account.

## Getting started

Prerequisites (from the official docs):

- A server with Docker and Docker Compose v2; for small meetings about 4 GB RAM (8 GB suggested), 4 dedicated CPU cores and about 20 GB disk
- A domain name for real use, set as `PUBLIC_URL`
- Port `10000/udp` open for media, plus the web ports

Steps:

1. Download and unzip the latest docker-jitsi-meet release (do not clone the repository).
2. Copy `env.example` to `.env` and set at least `CONFIG` and `PUBLIC_URL` (plus `JVB_ADVERTISE_IPS` on a LAN or behind NAT).
3. Run `./gen-passwords.sh` to set strong passwords.
4. Create the config directories exactly as listed in the Docker guide, including `storage/*` and `tmp/*` (default base `~/.jitsi-meet-cfg`).
5. Start the stack with `docker compose up -d`.
6. Open `https://localhost:8443` and accept the self-signed certificate warning; use HTTPS, not port 8000, or audio and video will not work.

Watch out: behind NAT or in a LAN, set `JVB_ADVERTISE_IPS` to the host's IP addresses, otherwise audio and video may not connect.

Official install docs: <https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker>

## Notes

The public meet.jit.si service is run by 8x8 and, per the project README, needs a Google, Facebook or GitHub account to start a meeting; your own instance does not. The getting-started path was checked hands-on on 2026-11-06 with release `stable-11248-3`: the web UI and a room's join page loaded; a full call with audio and video was not tested. The steps above are enough with the linked Docker guide, but not to follow on their own.
