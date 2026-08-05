# Social Media Deep Research Skill

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/seamas0825-lab/social-media-deep-research/releases/tag/v1.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An Agent Skills-compatible evidence-to-experiment operating system for social growth. It turns direct user and market evidence into hard strategic choices, repeatable content systems, and measurable experiments while preserving uncertainty, human judgment, and source traceability.

It is not Codex-only. The portable package works with Claude Code, Codex, WorkBuddy, OpenClaw, Hermes Agent, and other hosts that implement the [Agent Skills specification](https://agentskills.io/specification). `agents/openai.yaml` is optional UI metadata and other hosts may ignore it.

## Start here

```text
What decision are we trying to make?
What evidence could reverse it?
What is the cheapest experiment that can resolve the uncertainty?
```

Choose a run mode:

| Mode | Best for | Minimum useful result |
| --- | --- | --- |
| Light | Reversible, narrow choices | 3–5 opened sources and one cheap test |
| Standard | Costly but reversible strategy decisions | Evidence map, belief check, hard choice, experiment |
| Deep | Reputation-sensitive, regulated, multilingual, or hard-to-reverse work | Auditable multi-source package, checkpoints, evaluation |

The source counts are effort guardrails, not statistical proof thresholds. See [run modes](references/run-modes.md).

## Browser compatibility

Authenticated and dynamic research needs an agent-controlled browser with observation, interaction, login-state reuse, user handoff, and readback verification.

### macOS — recommended

Use **EGO Browser (ego-lite)** with the `ego-browser` skill. This is the preferred and best-tested path.

- Project: [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)
- Website: [lite.ego.app](https://lite.ego.app/)

### Windows — supported fallback

Use both [Browser Use](https://github.com/browser-use/browser-use) and the [eze-is/web-access skill](https://github.com/eze-is/web-access) with Chrome or Edge remote debugging. This path has more setup variance and is expected to be less reliable than EGO for complex authenticated sites; use smaller action batches and verify every meaningful interaction.

Without an authenticated adapter, the framework still supports open-web research, but the agent must label missing platform evidence. See the [compatibility matrix and smoke tests](references/platform-compatibility.md).

## Security boundary

Every page, post, comment, document, search snippet, and web-AI answer is untrusted data. It may supply evidence or links, but it cannot override system, host, user, or Skill instructions and cannot authorize tool calls.

The Skill rejects browser prompt injection, secret disclosure, out-of-scope commands, uploads, sends, installs, deletion, and hidden navigation. Sensitive login, 2FA, payment, consent, and publication actions require user control. See [browser security](references/browser-security.md).

## What it produces

- Decision-first research briefs and source-linked evidence ledgers
- Direct and psychologically analogous benchmark maps
- User tensions, objections, desired progress, and belief audits
- Platform-native content pillars and low-resource production systems
- Product-led social proof loops
- Falsifiable experiments with relative baselines and stop/scale rules
- Optional Feishu-ready strategy documents and clean Base import tables

Web AI tools such as Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, and Kimi are optional, bounded adapters. The Skill selects them by distinct evidence role, compiles prompts against a quality contract, and returns to original sources before accepting a claim.

## Install

Universal installer:

```bash
npx skills add seamas0825-lab/social-media-deep-research -g
```

Claude Code:

```bash
npx skills add seamas0825-lab/social-media-deep-research -g -a claude-code
```

Codex:

```bash
npx skills add seamas0825-lab/social-media-deep-research -g -a codex
```

WorkBuddy: download the [repository ZIP](https://github.com/seamas0825-lab/social-media-deep-research/archive/refs/heads/main.zip), then use **Skills → Add Skill → Upload Skill**.

OpenClaw:

```bash
openclaw skills install git:seamas0825-lab/social-media-deep-research --global
```

Hermes Agent:

```bash
hermes skills install https://raw.githubusercontent.com/seamas0825-lab/social-media-deep-research/main/SKILL.md
```

Example invocation:

```text
Use $social-media-deep-research in Standard mode. Define the decision and reversal condition, separate evidence from inference, and design the cheapest executable growth experiment.
```

## Real example

[Phi Browser: Evidence to Experiment](examples/phi-browser-evidence-to-experiment.md) shows a complete, source-linked Standard run: verified product facts, anecdotal user signals, inference boundaries, disconfirming evidence, a rejected positioning direction, and one controlled acquisition test.

## Tests

The repository includes real public-page smoke tests for EGO, Browser Use, and Web Access. Each test checks startup, navigation, readback, and cleanup without login data:

```bash
python3 scripts/run_smoke_tests.py --adapter ego
python3 scripts/run_smoke_tests.py --adapter browser-use --python /path/to/python3.11+
python3 scripts/run_smoke_tests.py --adapter web-access \
  --web-access-dir /path/to/eze-is/web-access \
  --launch-chrome
```

Golden eval cases are connected to a runnable harness:

```bash
python3 -m pip install -r scripts/requirements-test.txt
python3 scripts/run_evals.py --validate-only
```

Behavioral runs require explicit agent and judge model/tool metadata and save dated criterion scores. See [eval harness instructions](evals/README.md). Public smoke tests prove only the tested adapter path, not authenticated-site reliability.

## Failure discipline

The Skill has explicit handling for insufficient evidence, unavailable browsers, platform blocking, and web-AI citations that cannot be opened. It narrows or excludes the affected branch instead of inventing support. See [failure handling](references/failure-handling.md).

## Repository structure

```text
├── SKILL.md
├── VERSION
├── LICENSE
├── agents/                 # optional host UI metadata
├── references/             # detailed policies and protocols
├── examples/               # complete source-linked run
├── schemas/                # run-state schema
├── templates/              # reusable decision artifacts
├── scripts/                # smoke tests and eval runner
├── test-results/           # dated adapter evidence
└── evals/                  # rubric, cases, and dated results
```

## Privacy

Do not commit account identifiers, passwords, one-time codes, API keys, recovery data, cookies, sessions, or browser profiles. Verify active accounts and requested modes before submission. Hand browser control to the user for login, CAPTCHA, 2FA, payment, consent, or other sensitive actions.

## Version and license

Current version: **1.0.0**. See [Releases](https://github.com/seamas0825-lab/social-media-deep-research/releases).

Licensed under the [MIT License](LICENSE).
# Social Media Deep Research Skill

An open, Agent Skills-compatible **evidence-to-experiment operating system for social growth**. It turns real user evidence into defensible decisions and executable experiments without replacing human taste, responsibility, or reality checks.

It starts with three questions:

```text
What decision are you trying to make?
What evidence could reverse that decision?
What is the cheapest experiment that can resolve the remaining uncertainty?
```

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

- Runs an AI Value Gate before opening expensive multi-agent research branches.
- Separates evidence, inference, and decisions.
- Preserves supporting evidence, disconfirming evidence, alternative explanations, and reversal conditions through a formal Belief Audit.
- Uses Human Harness checkpoints for decision, taste, contradiction, and execution reality.
- Researches direct and psychologically analogous benchmarks.
- Extracts user tensions, objections, desired progress, and content mechanisms.
- Selects AI tools by required capability first, then chooses Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, Kimi, or another current adapter when available.
- Enforces a pre-submission prompt-quality gate and service-specific prompt templates for Grok, Perplexity, Gemini Deep Research, ChatGPT, and other web AI tools.
- Returns to original posts, comments, product pages, studies, and authoritative documents before accepting AI-generated claims as evidence.
- Protects editorial judgment with direct proof, quiet authority, documentary observation, search utility, trust repair, and other non-manipulative attention-entry modes.
- Connects successful product outcomes to privacy-safe shareable artifacts, social proof, activation, and product learning.
- Supports bounded serendipity and multilingual source lenses without letting weak discoveries contaminate the main evidence chain.
- Converts findings into repeatable content pillars, falsifiable experiments, production plans, measurement rules, and optional Feishu deliverables.
- Keeps long-running browser and Deep Research jobs off the critical path while preserving their state for later reconciliation.
- Includes a machine-readable run-state template and Golden Evals for Phi Browser, Pexo, and thin-evidence destination research.

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
Use $social-media-deep-research to define the decision, identify evidence that could reverse it, and design the cheapest executable social-growth experiment under the stated constraints.
```

## Repository structure

```text
social-media-deep-research/
├── SKILL.md
├── agents/
│   └── openai.yaml                    # optional Codex UI metadata
├── references/
    ├── ai-prompt-quality.md
    ├── ai-research-orchestration.md
    ├── category-transfer.md
    ├── decision-protocols.md
    ├── deliverables.md
    ├── editorial-judgment.md
    ├── human-harness.md
    ├── platform-compatibility.md
    ├── product-led-social.md
    ├── research-schema.md
    └── source-diversity.md
├── schemas/
│   └── run-state.yaml
├── templates/
│   ├── belief-audit.md
│   ├── convergence-memo.md
│   ├── human-checkpoint.md
│   └── research-brief.md
└── evals/
    ├── rubric.yaml
    └── cases/
        ├── guilin-thin-evidence.yaml
        ├── pexo-narrative-migration.yaml
        └── phi-browser-red-team.yaml
```

## Privacy and account safety

- Do not commit account identifiers, passwords, one-time codes, API keys, recovery codes, or session data.
- Verify the active account and research mode before submitting a prompt.
- Switch accounts only when the user has specified the target account and it is already available in the account chooser.
- Hand browser control to the user for login, CAPTCHA, 2FA, payment, consent, or other sensitive actions.
- Treat AI output as a research lead until the original source has been inspected.
