# Evidence Access Gaps

Use this reference when a page is reachable but a material value cannot be verified, or when the evidence surface itself is inaccessible. The correct output is a bounded evidence gap, not a guessed fact.

## Dynamic, animated, canvas, or delayed values

1. Wait for the page to settle and take two independent semantic or DOM readbacks.
2. Inspect accessible text, relevant DOM attributes, structured data, and a documented first-party endpoint when allowed.
3. Use visual capture only when the browser capability gate verified it and the visual state materially resolves the claim.
4. Require stable, matching values before recording a precise metric.
5. If the value remains unreadable, label it **unverifiable in this run**, exclude the number, and state whether a qualitative observation is still defensible.

Do not interpret a missing counter, blank node, animation start value, or failed selector as zero. Do not estimate a value from bar length, motion, or partial pixels.

## Login-only, private, regional, or closed surfaces

Examples include private Discord communities, App Store views that vary by region/account, login-walled comments, account-specific dashboards, and geo-restricted pages.

- Do not bypass access controls, robots rules, CAPTCHA, rate limits, or regional restrictions.
- Record whether the observation was anonymous, authenticated, user-provided, region-specific, or blocked.
- Use an official public API, authoritative first-party page, user handoff, or another original source when available.
- Separate a public metadata claim from what was actually observed inside the closed surface.
- Exclude inaccessible AI citations from the evidence chain; they may remain only as labeled leads.

## Claim status

Use one status per material claim:

- **Observed:** directly and stably read from the original surface.
- **Reported:** asserted by a named primary/authoritative source but not independently observed.
- **Inferred:** an explanation or translation supported by identified evidence.
- **Unverifiable:** access or rendering prevented reliable verification in this run.

Complete [../templates/evidence-access-gap.md](../templates/evidence-access-gap.md) whenever an unverifiable item could change a channel priority, positioning wedge, KPI baseline, comparison, or legal/cultural claim.

