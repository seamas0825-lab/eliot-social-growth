# Failure Handling

Failures are evidence about access and confidence. Do not hide them by substituting invented facts or unverifiable AI summaries.

## Evidence is insufficient

**Signal:** only isolated comments, copied summaries, or nonrepresentative examples are available.

**Response:** label sample and retrieval limits; state what cannot be inferred; narrow the decision; use an analogous case only as a hypothesis; propose a cheap live test or interview. Do not claim prevalence or consensus.

## Browser adapter is unavailable

**Signal:** EGO, Browser Use, or Web Access cannot start, observe, interact, or preserve the required authenticated state.

**Response:** run the relevant smoke test once; preserve the error and adapter version; continue open-web branches; omit authenticated claims; give the user the smallest setup or handoff action. Do not repeatedly retry or silently switch to an unauthenticated proxy source.

## Platform blocks access

**Signal:** login wall, CAPTCHA, rate limit, geo restriction, robots restriction, or anti-automation block prevents direct inspection.

**Response:** do not bypass the control. Request user handoff when allowed, try an official API or authoritative public source, or exclude the branch. Record the blocked URL, date, and resulting evidence gap.

## A web-AI citation cannot be opened

**Signal:** the citation is missing, broken, inaccessible, unrelated, or does not support the generated claim.

**Response:** downgrade the statement to an unverified lead and exclude it from the evidence chain. Search for the original primary source independently. Cite the original source, not the AI conversation, when verification succeeds.

## Reporting template

```text
Failure type:
Adapter/source and version:
URL or branch:
Observed date:
Error or access boundary:
What evidence is now missing:
Fallback used:
Decision impact:
Next safe action:
```
