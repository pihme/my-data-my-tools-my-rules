---
name: Frigate
slug: frigate
category: Smart Home
license: MIT
open_source: true
type: Server
audience: enthusiast
url: https://frigate.video/
repo: https://github.com/blakeblackshear/frigate
source_url: https://github.com/blakeblackshear/frigate/blob/dev/LICENSE
checked: 2026-11-25
added: 2026-11-25
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-25
note: Local video recorder (NVR) for IP cameras with real-time object detection; integrates with Home Assistant.
summary: Frigate is a network video recorder for IP cameras that runs object detection on the camera feeds locally in real time. It records around the clock or keeps recordings based on detected objects, offers live view with low latency, re-streams camera feeds and talks to other systems over MQTT. It runs as a Docker container, and a separate integration connects it to Home Assistant.
corporate_note: Copyright holder in the LICENSE is Frigate, Inc., which owns the Frigate trademarks; Frigate+ is an optional paid subscription for custom-trained detection models.
funding_note: The README asks for donations through GitHub Sponsors.
fireworks_image: assets/fireworks/cf-frigate-b1.webp
fireworks_date: 2026-11
sources:
  - https://frigate.video/
  - https://github.com/blakeblackshear/frigate/blob/dev/LICENSE
  - https://github.com/blakeblackshear/frigate/blob/dev/README.md
  - https://github.com/blakeblackshear/frigate/blob/dev/TRADEMARK.md
  - https://docs.frigate.video/frigate/installation/
  - https://docs.frigate.video/frigate/hardware/
  - https://docs.frigate.video/plus/
---
## Why it fits

Frigate is licensed under the MIT License and runs entirely on your own hardware, so camera video and detections stay in your network. Frigate+ is an optional paid service and not needed to run it.

## Getting started

Prerequisites (from the official docs):

- A Linux host with Docker and Docker Compose
- IP cameras with an RTSP stream
- Recommended: a GPU or AI accelerator for object detection; storage for recordings
- Optional: Home Assistant with the Frigate integration

Steps (Docker Compose, as checked without a camera):

1. Generate a Compose file with the generator on the installation page for your hardware, and set the paths for config and recordings.
2. Start the container with `docker compose up -d`; without a config file Frigate creates a default one.
3. Read the generated admin password from the container log.
4. Open the web interface on port 8971 and log in as admin, then add your cameras in the configuration.

Watch out: the admin password is printed only once in the log. The ports table describes 8971 as "without TLS", but in our test it served HTTPS with a self-signed certificate. The image is large (6.3 GB for 0.18.3). The generator adds `privileged: true`, which says it may not be necessary; Frigate ran without it. Set `shm_size` according to the number and resolution of your cameras.

Official installation docs: <https://docs.frigate.video/frigate/installation/>

Recommended hardware: <https://docs.frigate.video/frigate/hardware/>

## Notes

Tested with Frigate 0.18.3 on 2026-11-25 without a camera: the web interface reported "No Cameras Configured" and "System is healthy"; recording and detection with a real camera were not tested. No logo is shown: Frigate's trademark policy says the logo generally cannot be used on other websites without permission.
