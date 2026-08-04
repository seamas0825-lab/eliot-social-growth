# Operational deliverables

Choose only what the task needs. Keep strategy and execution linked by stable IDs.

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
11. Sources and evidence limitations.

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
- hook variants;
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

Each planned item needs a visible payoff and a follow reason.

## Platform packaging matrix

For each platform specify:

- opening frame and hook style;
- target duration range;
- pacing and subtitle density;
- caption depth;
- cover/profile-grid behavior;
- CTA type;
- native interaction features;
- primary success signal;
- what can be reused from the master asset.

Do not require separate shoots unless the platform genuinely demands different source material.

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
