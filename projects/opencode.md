---
name: OpenCode
slug: opencode
category: AI
license: MIT
open_source: true
type: App
audience: enthusiast
url: https://opencode.ai/
repo: https://github.com/anomalyco/opencode
source_url: https://github.com/anomalyco/opencode/blob/dev/LICENSE
checked: 2026-11-05
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-06
note: Free, open-source AI coding agent; needs an AI model (some hosted ones are free, local is possible).
summary: OpenCode is an open-source AI coding agent that runs in the terminal, with a desktop app and web interface as alternatives. The tool itself is free under MIT, but it needs an AI model: you connect a hosted provider or a local model server such as Ollama or LM Studio. OpenCode's own service offers some hosted models free for a limited time; paid plans are optional.
corporate_note: Developed by Anomaly (copyright notice on opencode.ai; the repository moved from github.com/sst/opencode to github.com/anomalyco/opencode). Anomaly sells optional pay-as-you-go model access (OpenCode Console) and OpenCode Go subscriptions (Go USD 10/month, Go Plus USD 40/month, Go Teams USD 20 per member/month, per the docs).
icon: assets/icons/opencode.svg
icon_credit: OpenCode logo from the brand folder of the MIT-licensed repository (brand guidelines at opencode.ai/brand); used to identify the project
icon_source: https://github.com/anomalyco/opencode/blob/dev/packages/console/app/src/asset/brand/opencode-logo-light-square.svg
screenshot: assets/screenshots/opencode.webp
screenshot_credit: Screenshot from the OpenCode repository, MIT
screenshot_source: https://github.com/anomalyco/opencode/blob/dev/packages/web/src/assets/lander/screenshot.png
sources:
  - https://opencode.ai/
  - https://github.com/anomalyco/opencode/blob/dev/LICENSE
  - https://github.com/anomalyco/opencode/blob/dev/README.md
  - https://opencode.ai/v2/docs/
  - https://opencode.ai/v2/docs/models/
  - https://opencode.ai/v2/docs/console/models/
  - https://opencode.ai/v2/docs/console/go/
  - https://opencode.ai/docs/providers/
  - https://opencode.ai/brand
---

OpenCode is an AI coding agent: it reads your code, runs tools and edits files in your project, driven by a large language model you choose. The repository LICENSE is the MIT License.

## Why it fits

The agent is free and open source and runs on your own machine. Whether your use is entirely free and self-run depends on the model: local models keep everything on your hardware, free hosted models cost nothing but send code to a provider, and paid providers are optional.

## Getting started

Prerequisites (from the official docs):

- A modern terminal on macOS, Linux or Windows (a desktop app is also offered)
- An AI model. OpenCode itself is free, but it does nothing without one. Options: (a) some hosted models offered free by OpenCode for a limited time (terms and the list can change); (b) a local model server such as Ollama, LM Studio or vLLM, which needs strong hardware (plenty of RAM or GPU memory) to be practical; (c) optional paid providers or OpenCode subscriptions
- A project directory with your code

Steps:

1. Install OpenCode with the official install script, Homebrew or npm, as shown in the docs.
2. Start opencode in your project directory.
3. Connect a provider with /connect, or configure a local model server such as Ollama.
4. Pick a model with /models and start working in the terminal UI.

Official docs (current version): <https://opencode.ai/v2/docs/>

Models and local providers: <https://opencode.ai/v2/docs/models/>

## Notes

Model dependence: per the official docs, OpenCode works with many hosted providers and discovers local models from Ollama, LM Studio and vLLM automatically. In practice, local models work but need strong hardware (enough RAM or GPU memory for the model) to be pleasant to use. OpenCode's own model service lists several models as free "for a limited time" (for example Big Pickle, GLM-5.3-Flash Free and DeepSeek V4.1 Flash Free at the time of checking); availability, regions and data handling differ per model (some providers use the free period to collect feedback, others state zero retention; some, such as Crouton Alpha Free and Pulse Alpha Free, are not available in the European Union), and the list can change at any time. Free models can be hidden with `OPENCODE_DISABLE_FREE_MODELS=1`. OpenCode Console (pay-as-you-go) and OpenCode Go (subscription) are optional. The current docs describe OpenCode 2 (`opencode.ai/v2/docs`); OpenCode 1 docs remain at `opencode.ai/docs`. Not tested with a model provider here.
