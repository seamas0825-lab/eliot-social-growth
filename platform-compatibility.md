# Platform Compatibility

Use this reference to install and run the skill across Agent Skills-compatible hosts and operating systems. The canonical package is the directory containing `SKILL.md` and its relative `references/` files.

**Skill version:** 1.4.0
**Compatibility verified:** 2026-08-10
**License:** MIT

## Contents

- [Open Agent Skills format](#open-agent-skills-format)
- [Host installation](#host-installation)
- [Browser runtime matrix](#browser-runtime-matrix)
- [Silent startup detection](#silent-startup-detection)
- [Windows setup](#windows-setup)
- [Smoke tests](#smoke-tests)
- [Capability adaptation](#capability-adaptation)

## Open Agent Skills format

Keep the core workflow host-neutral. Require only:

- a host that discovers a `SKILL.md` file with `name` and `description` frontmatter;
- access to relative reference files;
- open-web research tools for baseline research;
- an authenticated browser adapter for dynamic platforms and web AI services;
- local file or document tools only when the requested deliverable requires them.

Treat `agents/openai.yaml` as optional Codex UI metadata. Other hosts may ignore it without affecting the skill workflow.

## Host installation

Prefer the host's current official installer. Verify paths against current documentation when they may have changed.

| Host | Supported installation path | Invocation |
| --- | --- | --- |
| Claude Code | Install globally with `npx skills add seamas0825-lab/eliot-social-growth -g -a claude-code`, or place the repository at `~/.claude/skills/eliot-social-growth`. | Ask Claude to use the skill or invoke `/eliot-social-growth`. |
| Codex | Install with `npx skills add seamas0825-lab/eliot-social-growth -g -a codex`, or clone into the active Codex skills directory. | Ask the agent to use `$eliot-social-growth`. |
| WorkBuddy | Download the GitHub repository as a local skill package, then use **Skills → Add Skill → Upload Skill**. Enable it for the task. | Ask WorkBuddy to use `eliot-social-growth`. |
| OpenClaw | Run `openclaw skills install git:seamas0825-lab/eliot-social-growth --global`, or place it under a configured OpenClaw skill root. | Ask naturally or invoke `/skill eliot-social-growth`. |
| Hermes Agent | Run `hermes skills install https://raw.githubusercontent.com/seamas0825-lab/eliot-social-growth/main/SKILL.md`; Hermes also retrieves explicitly referenced support files. | Invoke `/eliot-social-growth` or ask naturally. |
| Other compatible agents | Use `npx skills add seamas0825-lab/eliot-social-growth -g` when supported, or copy the full directory into the host's documented skill root. | Use the host's natural-language or slash-command mechanism. |

Sources:

- Agent Skills specification: https://agentskills.io/specification
- Claude Code skills: https://code.claude.com/docs/en/slash-commands
- WorkBuddy skills: https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market
- OpenClaw skills: https://docs.openclaw.ai/skills
- Hermes Agent skills: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/work-with-skills.md
- Universal `skills` CLI: https://github.com/vercel-labs/skills

## Browser runtime matrix

| Environment | Required browser path | Verification baseline | Confidence policy |
| --- | --- | --- |
| macOS | EGO Browser plus the `ego-browser` skill | EGO 0.4.5.9 skill runtime; public-page navigation and readback smoke test. | Preferred. Use isolated task spaces, inherited login state, explicit handoff, and readback verification. |
| Windows | Browser Use plus `eze-is/web-access` | Adapter smoke passed with Browser Use 0.13.7 and Web Access commit `7af34af` on 2026-08-06. This validates both adapter APIs, not Windows host behavior; run the same tests on the target Windows machine. | Supported fallback. Expect more setup variance and lower reliability on complex authenticated sites than macOS plus EGO. Use smaller action batches and verify after every meaningful interaction. |
| Linux or another host | A browser adapter with observation, interaction, authenticated state, user handoff, and verification | Host-specific smoke test required. | Proceed only when the adapter exposes the required capabilities. Otherwise use open-web sources and label evidence gaps. |

## Silent startup detection

Run this check before presenting the mode choices or formally initializing research state:

1. Detect the operating system from the host environment.
2. Inspect the available Skill/tool catalog instead of assuming installation from documentation.
3. On macOS, require EGO Lite Browser runtime access and the `ego-browser` Skill. The first harmless EGO invocation is the runtime check; do not run redundant `which`, version, or package probes when the EGO Skill says the runtime is ready.
4. On Windows, require Browser Use, the `eze-is/web-access` Skill, and an intended Chrome/Edge remote-debugging path. Verify each adapter with its supported smoke test.
5. Record `detected_os`, required components, present components, missing components, and detection date in run state.
6. If nothing is missing, continue silently. Do not remind the user to install or enable something already present.
7. If a component is missing, tell the user only what is missing and how to enable/install it. Do not block open-web planning, but block any dynamic/authenticated branch that depends on the missing capability.

After the browser path is available, identify only the social and AI services relevant to the chosen workflow. If a service is visibly logged in, record it and do not remind the user. Otherwise remind once that the user must log in manually; never request credentials or session exports.

EGO resources:

- Project: https://github.com/citrolabs/ego-lite
- Website: https://lite.ego.app/

Windows resources:

- Browser Use: https://github.com/browser-use/browser-use
- Web Access skill: https://github.com/eze-is/web-access

## Windows setup

Use the current upstream instructions. The expected baseline is:

1. Install Python 3.11 or newer for Browser Use, then follow its current official installation instructions.
2. Install Web Access with `npx skills add eze-is/web-access` into the active host agent.
3. Install Node.js 22 or newer for Web Access.
4. Use Chrome or Edge. Open `chrome://inspect/#remote-debugging` or `edge://inspect/#remote-debugging` and enable remote debugging for the intended browser instance.
5. Sign in to required sites manually. Never place passwords, cookies, session exports, recovery codes, or one-time codes in the skill.
6. Run the adapter smoke test and [mandatory browser capability gate](references/browser-capability-gate.md) before starting any authenticated or dynamic branch.

Browser Use and Web Access are complementary capabilities, not an implied automatic integration. Follow each project's current setup and expose their tools through the host agent before relying on them.

## Smoke tests

Run from the skill root before every authenticated or dynamic research job:

```bash
python3 scripts/run_smoke_tests.py --adapter ego
python3 scripts/run_smoke_tests.py --adapter browser-use --python /path/to/python3.11+
python3 scripts/run_smoke_tests.py --adapter web-access \
  --web-access-dir /path/to/eze-is/web-access \
  --launch-chrome
```

The runner writes a JSON record under `test-results/` with the date, platform, adapter/tool version, duration, status, redacted output, and parsed capability details when available. Then run the gate against the capabilities required by the branch. A public-page pass does not prove authenticated-site reliability or a target service's current editor surface.

```bash
python3 scripts/browser_capability_gate.py test-results/smoke-YYYY-MM-DD.json \
  --adapter ego --require navigation --require semantic_snapshot \
  --require dom_evaluation --require textarea_input --require contenteditable_input
```

After the adapter gate, perform the target service's disposable write/readback/clear probe described in [references/browser-capability-gate.md](references/browser-capability-gate.md).

Smoke tests use `https://example.com`, temporary browser profiles where applicable, and no login data. Read [references/browser-security.md](references/browser-security.md) before extending them.

## Capability adaptation

Map workflow intent instead of copying tool syntax:

| Workflow intent | Required capability |
| --- | --- |
| Preserve authenticated research state | Isolated browser session, profile, or controlled logged-in browser |
| Inspect a dynamic page | Semantic page snapshot, accessibility tree, DOM extraction, screenshot, or equivalent |
| Act safely | Element or coordinate interaction with post-action verification |
| Ask the user to intervene | Explicit browser-control handoff or a hard stop with precise instructions |
| Resume a long job | Stable session, tab, task, or conversation identifier |
| Verify a result | Direct page readback, exported artifact, API readback, or original-source URL |

Do not claim cross-agent compatibility for a workflow that silently depends on a missing tool. Label the unsupported branch and continue with the best evidence available.
