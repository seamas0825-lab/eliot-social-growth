# Workflow Control and Branch Completeness

Use this reference for every substantial Standard or Deep run. Its purpose is to prevent branch loss, context drift, duplicated browsing, and premature strategy writing.

The companion `scripts/workflow_guard.py` is the executable contract for this
reference. A prose checklist does not count as a gate. The guard must be run
against the persisted state before browsing, after every branch, before
convergence, and before delivery; a non-zero exit is a hard stop.

## Treat run state as the workflow source of truth

Before browsing, copy `schemas/run-state.yaml` into the task workspace and fill the project, workflow, branch inventory, dependencies, fallbacks, and checkpoints. Do not keep the only copy of the plan in conversation memory.

Prefer `workflow_guard.py init` because it creates all branch families and
marks unresolved fields as `TODO`, which the Blueprint Gate rejects. This makes
an omitted branch visible instead of allowing an empty checklist to pass.

On every continuation, compaction, handoff, or return from a long-running branch:

1. Read the current run state first.
2. Restate the active decision and current stage internally.
3. Reconcile completed, active, waiting, excluded, and missing branches.
4. Resume the next dependency-ready branch; do not rebuild the workflow from memory.

If the user changes scope, evidence, audience, constraints, or success signals,
run `workflow_guard.py reentry` first. That resets the relevant gates and
blocks strategy and delivery until the revised blueprint is reviewed and
re-approved.

## Build the branch blueprint before research

For Light runs, record the decision, two source roles, one contradiction path, and one experiment. For Standard and Deep runs, consider every branch family below and give it one explicit disposition:

- `required`: hard dependency; strategy cannot proceed without completion or a defensible degraded result;
- `planned`: useful soft or independent branch;
- `excluded_by_user`: outside explicit user scope;
- `excluded_by_value_gate`: cannot change the decision or a cheaper truth owner exists;
- `not_applicable`: structurally irrelevant, with a reason.

Never leave a candidate branch absent or silently unexecuted.

| Branch family | Default consideration | Typical evidence or decision role |
| --- | --- | --- |
| Official website/product baseline | Required unless unavailable, irrelevant, or excluded by the user | Official website/product reality, first-party documents, current offer, brand claims |
| Official social accounts | Required for social/account work unless unavailable, irrelevant, or excluded by the user | First-party profile promise, cadence, current creative and conversion surfaces |
| Target native-account performance | Required for account/content audits when access exists | Original posts, formats, public metrics, comments, cadence, profile promise, conversion path |
| Search-intent and keyword map | Required consideration for editorial, SEO, discovery, trend, or content-planning work | Audience jobs, anxieties, questions, native-language queries, autocomplete/platform search terms |
| Native high-performing cases | Required consideration for content strategy | Search keywords on the target platform, open original posts, compare visible performance in context |
| Direct competitors | Required consideration for positioning and content-system decisions | Same buyer, category, offer, market, or business model |
| Analogous mechanisms | Required consideration when direct cases are thin or repetitive | Same tension, proof, trust, identity, or follow reason in another category |
| User voice and community | Include when vocabulary, objection, anxiety, or buyer intent could change the decision | Comments, Reddit, forums, reviews, interviews, sales/support language |
| Authoritative facts | Required when law, policy, safety, technical limits, pricing, or unstable facts affect the claim | First-party or authoritative sources |
| Internal evidence or one real user | Prefer when it owns conversion, product truth, constraints, or execution reality | Insights, CRM, DMs, interviews, performance data, team capacity |
| AI research | Include only after the AI Value Gate | Bounded source discovery, contradiction, multilingual coverage, long-context synthesis, structured extraction |

For every included branch record:

```text
Branch ID and family:
Question and decision affected:
Source role and target surface:
Required capability:
Dependency: hard / soft / independent / asynchronous external
Owner or execution path:
Time or source budget:
Entry condition and stop rule:
Fallback ladder:
Expected artifact:
Status and stable session/job IDs:
```

## Build search intent before searching for hits

When the task concerns content, discovery, positioning, or trends, create a bounded search map before collecting examples:

1. Name the audience roles and decision situations.
2. Generate query families from desired progress, anxieties, objections, alternatives, geography, product/category terms, and native platform vocabulary.
3. Translate only after identifying the evidence language; preserve original-language queries.
4. Probe a small set through search-engine discovery, platform-native search/autocomplete/hashtags, and community language where available.
5. Use validated queries to find original high-performing social cases. Open each original post and record query, URL, date, account context, first frame/line, visible metrics, comments, and access limits.
6. Call a case `high-performing` only relative to observable account or comparable context. Do not invent an absolute viral threshold or infer saves, shares, reach, or conversion from unlabeled values.

Stop expanding keywords when new queries repeat the same mechanisms or cannot change the experiment.

## Plan browser parallelism explicitly

EGO supports multiple isolated task spaces and tabs. Use that capability only for independent work.

Before browsing, group branches into:

- `parallel_now`: independent, no shared mutable surface, and safe under account/rate limits;
- `parallel_after_gate`: start after a shared adapter or authentication gate passes;
- `sequential_dependency`: requires another branch's output;
- `single_surface_only`: same editor/account flow or action state; do not race.

When the host supports concurrency, give each independent branch its own EGO task space, tab set, owner, and stable ID. Never let two agents control the same task space. When concurrency is unavailable, round-robin across preserved task spaces instead of reopening or duplicating work.

Use parallelism for official-account inspection, competitor discovery, analogous cases, search-intent probes, community language, and bounded AI branches when they do not depend on one another. Keep authentication handoffs, sensitive actions, belief convergence, and final strategy selection sequential.

## Pass four workflow integrity checkpoints

### Checkpoint 1: Blueprint gate

Before broad research:

- decision, risk, success signal, constraints, and reversal condition exist;
- every branch family has a disposition and reason;
- every included branch records its owned question/decision, dependency, owner or execution path, time or source budget, entry condition, stop rule, fallback ladder, expected artifact, and parallel group;
- hard dependencies and stable session/job identifiers are planned;
- explicit user exclusions are preserved.

If any included branch omits one of these fields, the Blueprint Gate is `FAIL`; do not start broad browsing. A branch-name list or generic research checklist is not a valid blueprint.

Record the review explicitly with `workflow_guard.py approve --what blueprint`,
then run `workflow_guard.py gate --gate blueprint`. The command must return
success before dynamic browsing or broad research starts.

### Checkpoint 2: Branch-exit gate

After every branch:

- save direct sources, dates, evidence/inference separation, conflicts, and limitations;
- set status to complete, degraded, excluded, or waiting;
- record whether the branch changed another branch, belief, or experiment;
- audit the blueprint for newly missing or obsolete work.

Do not start strategy drafting merely because one productive branch finished.
Run `workflow_guard.py gate --gate branch-exit --branch BRANCH_ID` for each
included branch. A completed branch without a passing exit gate is still
incomplete.

### Checkpoint 3: Pre-convergence completeness gate

Before belief audit or strategy selection:

- every hard dependency is complete, defensibly degraded, or explicitly blocked;
- every planned branch is complete or excluded with a reason;
- official baseline, target-native behavior, keyword/high-performing-case discovery, direct competitors, analogous mechanisms, internal/user truth, and AI were each either handled or explicitly ruled out;
- long-running jobs have a stable ID, current state, timeout/hedge decision, and inclusion plan;
- multi-AI sources are ready for deduplication.

If a branch was forgotten, reopen it. If it no longer has decision value, exclude it explicitly. Do not silently skip it.

Run `workflow_guard.py gate --gate pre-convergence` before belief audit,
strategy selection, or calendar drafting. This command checks the branch
ledger, keyword-to-case path, AI decision/convergence, external-job states,
and branch exit gates together.

### Checkpoint 4: Pre-delivery gate

Before final delivery:

- every material recommendation traces to evidence or is labelled a test;
- the belief gate, convergence artifact, experiment, owners, metrics, risks, and stop rules are complete;
- created artifacts and external links are verified;
- run state contains no active or unexplained planned branch.

Run `workflow_guard.py gate --gate pre-delivery` and then
`workflow_guard.py assert --action delivery` immediately before final output.
The same `assert` command with `--action strategy` is required immediately
before writing a strategy or content calendar.

## Use the branch ledger to control scope, not inflate it

Completeness means every branch was considered and dispositioned. It does not mean every branch must run. Exclude branches when they cannot change the decision, duplicate stronger evidence, violate the user's scope, or cost more than the next reversible test. Record the reason so that efficiency is distinguishable from forgetting.
