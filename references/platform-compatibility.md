# Platform Compatibility

Use this reference to install and run the skill across Agent Skills-compatible hosts and operating systems. The canonical package is the directory containing `SKILL.md` and its relative `references/` files.

**Skill version:** 1.0.1  
**Compatibility verified:** 2026-08-06  
**License:** MIT

## Contents

- [Open Agent Skills format](#open-agent-skills-format)
- [Host installation](#host-installation)
- [Browser runtime matrix](#browser-runtime-matrix)
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
| Claude Code | Install globally with `npx skills add seamas0825-lab/social-media-deep-research -g -a claude-code`, or place the repository at `~/.claude/skills/social-media-deep-research`. | Ask Claude to use the skill or invoke `/social-media-deep-research`. |
| Codex | Install with `npx skills add seamas0825-lab/social-media-deep-research -g -a codex`, or clone into the active Codex skills directory. | Ask the agent to use `$social-media-deep-research`. |
| WorkBuddy | Download the GitHub repository as a local skill package, then use **Skills → Add Skill → Upload Skill**. Enable it for the task. | Ask WorkBuddy to use `social-media-deep-research`. |
| OpenClaw | Run `openclaw skills install git:seamas0825-lab/social-media-deep-research --global`, or place it under a configured OpenClaw skill root. | Ask naturally or invoke `/skill social-media-deep-research`. |
| Hermes Agent | Run `hermes skills install https://raw.githubusercontent.com/seamas0825-lab/social-media-deep-research/main/SKILL.md`; Hermes also retrieves explicitly referenced support files. | Invoke `/social-media-deep-research` or ask naturally. |
| Other compatible agents | Use `npx skills add seamas0825-lab/social-media-deep-research -g` when supported, or copy the full directory into the host's documented skill root. | Use the host's natural-language or slash-command mechanism. |

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
6. Test observation, navigation, input, screenshot or readback, and manual handoff before starting a long research branch.

Browser Use and Web Access are complementary capabilities, not an implied automatic integration. Follow each project's current setup and expose their tools through the host agent before relying on them.

## Smoke tests

Run from the skill root before a long authenticated research job:

```bash
python3 scripts/run_smoke_tests.py --adapter ego
python3 scripts/run_smoke_tests.py --adapter browser-use --python /path/to/python3.11+
python3 scripts/run_smoke_tests.py --adapter web-access \
  --web-access-dir /path/to/eze-is/web-access \
  --launch-chrome
```

The runner writes a JSON record under `test-results/` with the date, platform, adapter/tool version, duration, status, and redacted output. A public-page pass proves only that the adapter can start, navigate, read back, and clean up in the tested environment. It does not prove authenticated-site reliability.

Smoke tests use `https://example.com`, temporary browser profiles where applicable, and no login data. Read [browser-security.md](browser-security.md) before extending them.

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
