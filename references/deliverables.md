# Operational deliverables

Choose only what the task needs. Keep strategy and execution linked by stable IDs.

## Contents

- [Strategy memo](#strategy-memo)
- [Research database](#research-database)
- [First-month plan](#first-month-plan)
- [Mandatory social-content evidence contract](#mandatory-social-content-evidence-contract)
- [Platform packaging matrix](#platform-packaging-matrix)
- [Convergence memo](#convergence-memo)
- [Product-led social loop](#product-led-social-loop)
- [Spreadsheet standards](#spreadsheet-standards)
- [Feishu CLI handoff](#feishu-cli-handoff)
- [Final answer](#final-answer)

## Strategy memo

Use this compact structure:

1. Decision and executive conclusion.
2. Audience, market, and operating constraints.
3. Positioning and profile promise.
4. Direct and analogous benchmark findings.
5. Dominant audience tensions and psychology.
6. Recurring content system.
7. Production and distribution design.
8. First experiment cycle.
9. Metrics and decision rules.
10. Compliance and credibility boundaries.
11. Disconfirming evidence, reversal conditions, and rejected alternatives.
12. Sources and evidence limitations.

Lead with choices and rejected alternatives, not a research diary.

## Research database

Recommended tables:

### Evidence cases

Use the case schema from `research-schema.md`.

### User tensions

Fields:

- tension ID;
- segment;
- situation;
- desired progress;
- anxiety/objection;
- current workaround;
- source count;
- representative source links;
- content implication;
- confidence;
- status.

### Content experiments

Fields:

- experiment/content ID;
- platform;
- audience;
- pillar;
- hypothesis;
- attention-entry variants;
- proof/payoff;
- participants/location/props;
- source mechanism IDs;
- production effort;
- risk and approval;
- publish date/status;
- primary and diagnostic metrics;
- continue/revise/stop rule;
- result and next action.

### Performance review

Fields vary by platform but typically include:

- views or reach;
- early retention;
- average watch percentage;
- completion rate;
- likes;
- comments;
- shares;
- saves;
- profile visits;
- follows;
- clicks, trials, leads, or sales where relevant;
- qualitative comment signal;
- decision;
- follow-up experiment ID.

## First-month plan

Design around content mechanisms and production batches rather than calendar slots alone.

Include:

- pillar quotas;
- shoot/creation days grouped by shared inputs;
- a master-asset specification;
- platform packaging variants;
- approval and consent checklist;
- release cadence;
- comment-reply workflow;
- weekly decision checkpoint.

Each planned item needs a credible payoff and a follow reason. Do not force an exaggerated attention entry when direct proof, quiet authority, documentary observation, or search utility better serves the brand.

## Mandatory social-content evidence contract

Do not generate a final content calendar until the guard's `calendar` assertion passes. The deliverable must contain or directly link to:

1. a competitor and adjacent-account table with classification basis, profile/account context, opened original posts, dates, visible labelled metrics, mechanism, and limitations;
2. an audience-psychology and keyword map connecting role, situation, desired progress, anxiety/objection, and likely query language;
3. a keyword-to-original-native-post performance map on the target platform, plus a clearly separated supplemental-platform probe when available;
4. an evidence-limit section covering private metrics, personalization, inaccessible posts, account-relative comparison, cross-platform transfer, language/sample bias, and unstable factual claims;
5. a research-to-calendar change log showing exactly which research finding changed a topic, opening, proof, format, CTA, cadence, or measurement choice.

The final calendar must trace every priority item to at least one evidence mechanism or label it a provisional test. A complete row still includes the user's requested execution fields—such as topic, on-asset text or script, caption, tags, format, asset needs, CTA, measurement, and approval risk—but formatting completeness cannot substitute for the five research prerequisites.

## Platform packaging matrix

For each platform specify:

- opening frame and attention-entry style;
- target duration range;
- pacing and subtitle density;
- caption depth;
- cover/profile-grid behavior;
- CTA type;
- native interaction features;
- primary success signal;
- what can be reused from the master asset.

Do not require separate shoots unless the platform genuinely demands different source material.

## Convergence memo

Use `templates/convergence-memo.md` for material decisions. Preserve:

- the decision and selected option;
- evidence included and excluded, with reasons;
- strongest disconfirming evidence and alternative explanation;
- rejected directions and trade-offs;
- unresolved uncertainty and reversal condition;
- the cheapest next experiment;
- the human judgment still required, if any.

## Product-led social loop

When a product creates visible outcomes, include:

- activation event and successful outcome;
- privacy-safe shareable artifact;
- why a user would share and permit brand amplification;
- how the artifact proves value without overstating causality;
- social-to-product attribution event;
- how recurring community requests enter templates, demos, onboarding, or product discovery.

## Spreadsheet standards

Maintain two variants when both presentation and Base import are needed:

1. **Human-facing workbook:** title bands, instructions, formulas, frozen panes, validation, visual hierarchy.
2. **Base-import workbook:** one normalized table per sheet, field names in row 1, no merged title rows, no decorative blocks, predictable data types.

Verify human-facing workbooks visually and scan formulas for errors. After Base import, verify:

- table names;
- field names and types;
- expected row presence;
- select options;
- sample records;
- import task completion state.

Never assume a successful upload means a correct schema.

## Feishu CLI handoff

When requested:

- import documents with `drive +import --type docx`;
- import a clean `.xlsx` as Base with `drive +import --type bitable`;
- run imports to the same location serially;
- preserve and poll import tickets instead of starting duplicates;
- use `base +table-list`, `base +field-list`, and a small `base +record-list` readback to verify;
- distinguish test imports from final deliverables and avoid leaving ambiguous titles.

Use the relevant Feishu skills for exact authentication and command requirements.

## Final answer

Report:

- the decision and what changed because of research;
- completed deliverables;
- verified external links or locations;
- important limitations and live risks;
- the immediate next operational action.

Do not make the user reconstruct the plan from commentary or research logs.
