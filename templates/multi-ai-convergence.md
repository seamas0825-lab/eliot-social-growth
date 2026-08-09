# Multi-AI Convergence Gate

Complete this artifact after two or more AI-service branches and before a strategy recommendation.

## Branch register

| Branch ID | Service/model/mode | Verified capability | Date | Assigned role | Branch type | Conversation/job ID | Retrieval limit | Selection state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use `distinct_research_role` or `latency_hedge` for branch type. A latency hedge answering the same bounded question is not independent corroboration. Record `selected_to_unblock`, `new_evidence_only`, `excluded_redundant`, or `unresolved_timeout` as its selection state.

## Claim matrix

| Claim ID | Decision affected | Branches making claim | Original source IDs/URLs | Shared-source deduplicated? | Verification | Relationship | Uncertainty | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use these controlled values:

- **Verification:** verified / partly verified / unverified
- **Relationship:** verified consensus / verified divergence / unverified consensus / single-branch lead
- **Disposition:** adopt / narrow / test / reject

## Decision matrix

| Decision | Supporting verified claims | Strongest contradiction | Access/language/sample gap | Belief gate ID | Outcome | Reversal condition |
| --- | --- | --- | --- | --- | --- | --- |

## Mandatory rules

- Model vote count is not confidence. Several systems repeating one source count as one evidence path.
- The fastest prose response does not win; only a source-adequate branch with openable, decision-relevant originals may unblock convergence.
- A primary job and its latency hedge count as one evidence role unless they recover distinct verified sources.
- Shared or circular URLs must be deduplicated before labeling consensus.
- Primary behavioral or authoritative evidence outranks model agreement.
- Unverified consensus remains a lead, not a fact.
- Preserve genuine disagreement; do not average it into a vague middle position.
- A material decision must trace to verified original sources or be labeled a reversible test.

```text
Convergence gate: PASS / PROVISIONAL-TEST / BLOCKED
Included decisions:
Rejected decisions:
Unresolved claims:
Next verification or experiment:
Owner and date:
```
