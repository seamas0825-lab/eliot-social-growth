# Social Media Deep Research Skill

An evidence-backed Codex skill for turning product, audience, competitor, social-platform, community, and user-psychology research into executable social-media positioning, content systems, experiments, and measurement plans.

## EGO Browser required

Authenticated and dynamic research workflows in this skill are designed to run with **EGO Browser (ego-lite)** and the `ego-browser` skill. EGO provides isolated agent task spaces while reusing the user's existing browser login state.

Before using authenticated research branches:

1. Install and configure EGO Browser and make the `ego-browser` CLI available.
2. Install the `ego-browser` skill in Codex.
3. Sign in to any AI research or social platforms you choose to use inside EGO.
4. Keep account selection under user control. This repository contains no credentials, account identifiers, tokens, or login secrets.

The social-media strategy framework can still be used without authenticated services, but EGO is required for the browser-driven AI orchestration described in `references/ai-research-orchestration.md`.

## What it does

- Separates evidence, inference, and decisions.
- Researches direct and psychologically analogous benchmarks.
- Extracts user tensions, objections, desired progress, and content mechanisms.
- Orchestrates distinct research roles across Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, and Kimi when available.
- Returns to original posts, comments, product pages, studies, and authoritative documents before accepting AI-generated claims as evidence.
- Converts findings into repeatable content pillars, falsifiable experiments, production plans, measurement rules, and optional Feishu deliverables.
- Keeps long-running browser and Deep Research jobs off the critical path while preserving their state for later reconciliation.

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/seamas0825-lab/social-media-deep-research.git ~/.codex/skills/social-media-deep-research
```

Then invoke it in Codex with a request such as:

```text
Use $social-media-deep-research to research this product and build an evidence-backed social media growth plan.
```

## Repository structure

```text
social-media-deep-research/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── ai-research-orchestration.md
    ├── category-transfer.md
    ├── deliverables.md
    └── research-schema.md
```

## Privacy and account safety

- Do not commit account identifiers, passwords, one-time codes, API keys, recovery codes, or session data.
- Verify the active account and research mode before submitting a prompt.
- Switch accounts only when the user has specified the target account and it is already available in the account chooser.
- Hand EGO control to the user for login, CAPTCHA, 2FA, payment, consent, or other sensitive actions.
- Treat AI output as a research lead until the original source has been inspected.
