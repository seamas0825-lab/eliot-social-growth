# Social Media Deep Research Skill

An open, Agent Skills-compatible workflow for turning product, audience, competitor, social-platform, community, and user-psychology research into executable social-media positioning, content systems, experiments, and measurement plans.

It is not Codex-only. The core `SKILL.md` and relative references can be installed in Claude Code, Codex, WorkBuddy, OpenClaw, Hermes Agent, and other hosts that support the [Agent Skills specification](https://agentskills.io/specification). The `agents/openai.yaml` file is optional Codex UI metadata and is ignored by other hosts.

## Browser requirements

Authenticated and dynamic research branches require an agent-controlled browser with login-state reuse, observation, interaction, user handoff, and result verification.

### macOS — recommended

Use **EGO Browser (ego-lite)** with the `ego-browser` skill. This is the preferred and best-tested path.

- EGO Lite project: [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)
- Official website: [lite.ego.app](https://lite.ego.app/)

### Windows — supported fallback

Use both:

- [Browser Use](https://github.com/browser-use/browser-use)
- [eze-is/web-access](https://github.com/eze-is/web-access)

The Windows path is supported but is expected to be less reliable than macOS plus EGO for complex authenticated and highly dynamic sites. Use smaller action batches, allow more setup time, and verify every meaningful interaction.

Baseline Windows setup:

1. Install Python 3.11+ and Browser Use with `uv add "browser-use[core]"` or `pip install "browser-use[core]"`.
2. Install Web Access with `npx skills add eze-is/web-access`.
3. Install Node.js 22+.
4. Enable remote debugging in Chrome at `chrome://inspect/#remote-debugging` or Edge at `edge://inspect/#remote-debugging`.
5. Sign in to required sites manually and test observation, interaction, screenshot/readback, and handoff before a long research job.

Browser Use and Web Access are complementary capabilities; follow both upstream projects' current setup instructions. The strategy framework can still run with open-web sources when no authenticated browser is available, but the agent must label the missing evidence.

## What it does

- Separates evidence, inference, and decisions.
- Researches direct and psychologically analogous benchmarks.
- Extracts user tensions, objections, desired progress, and content mechanisms.
- Orchestrates distinct research roles across Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, and Kimi when available.
- Enforces a pre-submission prompt-quality gate and service-specific prompt templates for Grok, Perplexity, Gemini Deep Research, ChatGPT, and other web AI tools.
- Returns to original posts, comments, product pages, studies, and authoritative documents before accepting AI-generated claims as evidence.
- Converts findings into repeatable content pillars, falsifiable experiments, production plans, measurement rules, and optional Feishu deliverables.
- Keeps long-running browser and Deep Research jobs off the critical path while preserving their state for later reconciliation.

## Install

### Universal installer

For hosts supported by the open `skills` CLI:

```bash
npx skills add seamas0825-lab/social-media-deep-research -g
```

### Claude Code

```bash
npx skills add seamas0825-lab/social-media-deep-research -g -a claude-code
```

Manual location: `~/.claude/skills/social-media-deep-research`.

### Codex

```bash
npx skills add seamas0825-lab/social-media-deep-research -g -a codex
```

### WorkBuddy

Download the [repository ZIP](https://github.com/seamas0825-lab/social-media-deep-research/archive/refs/heads/main.zip), then choose **Skills → Add Skill → Upload Skill** and import the local package. Enable the skill for the task.

### OpenClaw

```bash
openclaw skills install git:seamas0825-lab/social-media-deep-research --global
```

### Hermes Agent

```bash
hermes skills install https://raw.githubusercontent.com/seamas0825-lab/social-media-deep-research/main/SKILL.md
```

Hermes retrieves the support files explicitly referenced by `SKILL.md`.

Then invoke the skill through the host's natural-language or slash-command mechanism, for example:

```text
Use $social-media-deep-research to research this product and build an evidence-backed social media growth plan.
```

## Repository structure

```text
social-media-deep-research/
├── SKILL.md
├── agents/
│   └── openai.yaml                    # optional Codex UI metadata
└── references/
    ├── ai-prompt-quality.md
    ├── ai-research-orchestration.md
    ├── category-transfer.md
    ├── deliverables.md
    ├── platform-compatibility.md
    └── research-schema.md
```

## Privacy and account safety

- Do not commit account identifiers, passwords, one-time codes, API keys, recovery codes, or session data.
- Verify the active account and research mode before submitting a prompt.
- Switch accounts only when the user has specified the target account and it is already available in the account chooser.
- Hand browser control to the user for login, CAPTCHA, 2FA, payment, consent, or other sensitive actions.
- Treat AI output as a research lead until the original source has been inspected.
