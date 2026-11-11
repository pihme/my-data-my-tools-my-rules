---
name: Ollama
slug: ollama
category: AI
license: MIT
open_source: true
type: [App, Server]
audience: end-user
url: https://ollama.com/
repo: https://github.com/ollama/ollama
source_url: https://github.com/ollama/ollama/blob/main/LICENSE
checked: 2026-11-11
added: 2026-11-11
note: Runs open language models on your own computer; local API for other tools, optional cloud models.
summary: Ollama runs open-weight language models on your own computer. It ships as a desktop app for macOS and Windows and as a command-line tool and background service for Linux, and serves a local API on port 11434 that tools such as Open WebUI or OpenCode can use. Ollama, Inc. also offers optional cloud models that need an account; they can be switched off.
corporate_note: Developed by Ollama, Inc. (Toronto, Canada; owner of the Ollama trademark applications at the USPTO). LICENSE copyright line reads "Copyright (c) Ollama". Optional cloud models need an Ollama account and usage credits or a paid plan.
icon: assets/icons/ollama.svg
icon_credit: Ollama logo from the docs folder of the MIT-licensed repository; used to identify the project
icon_source: https://github.com/ollama/ollama/blob/main/docs/ollama-logo.svg
sources:
  - https://ollama.com/
  - https://github.com/ollama/ollama/blob/main/LICENSE
  - https://docs.ollama.com/quickstart
  - https://docs.ollama.com/linux
  - https://docs.ollama.com/macos
  - https://docs.ollama.com/windows
  - https://docs.ollama.com/cloud
  - https://docs.ollama.com/faq#how-do-i-disable-ollama-cloud-features
  - https://ollama.com/terms
  - https://tsdr.uspto.gov/statusview/sn98310169
---
## Why it fits

Ollama is MIT-licensed and free. Local models run entirely on your own hardware, so prompts and answers stay on your machine; the optional cloud models are a separate, paid service you do not have to use.

## Getting started

Prerequisites (from the official docs):

- macOS Sonoma (14) or newer (Apple silicon with GPU support, Intel CPU only), Windows 10 22H2 or newer, or Linux
- On a minimal Debian or Ubuntu system, install `zstd` before the Linux script (`sudo apt install zstd`); `install.sh` exits with "requires zstd" without it
- Disk space for models: the docs say they "can be tens to hundreds of GB"; the quickstart model `gemma4:e2b` is 4.6 GB
- Memory: the quickstart recommends 8 GB of free VRAM or unified memory for that model; with less, Ollama falls back to system RAM and gets slower

Steps:

1. Download Ollama for macOS or Windows from ollama.com/download, or on Linux run the install script `curl -fsSL https://ollama.com/install.sh | sh`.
2. Open the app. On Linux with systemd, the install script starts a service. Without systemd, run `ollama serve` yourself — the script may still print that the API is now available even when no server is running.
3. Download and chat with a local model: `ollama run gemma4:e2b` (type `/bye` to leave).
4. Optional: point other tools at the local API on `http://localhost:11434`.

Watch out: the first-run setup offers to sign in for cloud models; choose a local model instead. To run local-only, set `OLLAMA_NO_CLOUD=1` or `"disable_ollama_cloud": true` in `~/.ollama/server.json` and restart.

Official docs: <https://docs.ollama.com/quickstart>

Linux install: <https://docs.ollama.com/linux>

## Notes

Local versus cloud: per the official docs, cloud models run on Ollama's servers, need an account and usage credits or a paid plan, and Ollama states it does not train on cloud prompts. Local-only mode turns off cloud models and web search. The Linux one-step install pipes a script into `sh`; a manual tarball install and a systemd unit are documented on the same page. Speed of local models depends heavily on GPU and memory.
