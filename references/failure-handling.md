# Failure Handling

Failures are evidence about access and confidence. Do not hide them by substituting invented facts or unverifiable AI summaries.

## Direct URL or profile fails: use the discovery ladder

**Signal:** a company website, official account, TikTok/Instagram profile, post URL, or competitor page fails to load, resolves incorrectly, or exposes an empty shell.

**Response:** stop repeating the same navigation after one verified retry. Preserve the URL and error, then move down this ladder:

1. Search the open web for the exact brand, handle, domain, page title, and `site:`-restricted query.
2. Use the target platform's native search for the brand, handle variants, display name, keywords, hashtags, and recent posts.
3. Inspect first-party cross-links from an accessible official profile, app listing, press page, verified account, or platform result.
4. Use an allowed official API, embed, RSS/feed, public share page, or authenticated user handoff when available.
5. Use search snippets, caches, mirrors, directories, or AI results only to discover candidate originals. Do not treat them as evidence until the original or authoritative source opens and supports the claim.
6. If the original remains inaccessible, complete an evidence-access gap, restrict the claim, and continue independent branches.

For competitor discovery, try both company/domain queries and platform-native account search before concluding that no account exists. For TikTok, Instagram, YouTube, or another native surface, search by handle, brand name, category term, language variant, hashtag, and visible post keyword. Verify account ownership through first-party cross-links, consistent identity, or another authoritative signal; name similarity alone is insufficient.

Record each attempt as `method`, `query or URL`, `observed result`, `source status`, and `next fallback`. Discovery resilience is not permission to bypass login, CAPTCHA, rate limits, geo controls, robots restrictions, or private surfaces.

## Evidence is insufficient

**Signal:** only isolated comments, copied summaries, or nonrepresentative examples are available.

**Response:** label sample and retrieval limits; state what cannot be inferred; narrow the decision; use an analogous case only as a hypothesis; propose a cheap live test or interview. Do not claim prevalence or consensus.

## Browser adapter is unavailable

**Signal:** EGO, Browser Use, or Web Access cannot start, observe, interact, or preserve the required authenticated state.

**Response:** run the relevant smoke test once; preserve the error and adapter version; continue open-web branches; omit authenticated claims; give the user the smallest setup or handoff action. Do not repeatedly retry or silently switch to an unauthenticated proxy source.

## Platform blocks access

**Signal:** login wall, CAPTCHA, rate limit, geo restriction, robots restriction, or anti-automation block prevents direct inspection.

**Response:** do not bypass the control. Request user handoff when allowed, try an official API or authoritative public source, or exclude the branch. Record the blocked URL, date, and resulting evidence gap.

Do not confuse one blocked URL with an exhausted branch. Use the discovery ladder first when search-engine or platform-native discovery remains allowed. Stop only after the planned fallback budget is exhausted or the branch no longer has decision value.

## Platform-native search is incomplete

**Signal:** native search returns sparse, personalized, region-limited, or irrelevant results.

**Response:** vary audience-language queries, spelling, handle, hashtag, buyer problem, category vocabulary, and time window; then cross-check with open-web `site:` search. Preserve the exact queries and distinguish “not retrieved” from “does not exist.” Open candidate original posts before recording performance or comments.

Do not claim that the first visible results are top-performing, representative, or exhaustive. Use account-relative comparisons or clearly labelled material cases.

## A page value cannot be verified

**Signal:** an animated counter, canvas rendering, delayed value, inaccessible Discord/App Store surface, account/region state, or selector drift prevents stable readback.

**Response:** follow [evidence-access-gaps.md](evidence-access-gaps.md), attempt two stable readbacks and allowed first-party fallbacks, then complete [../templates/evidence-access-gap.md](../templates/evidence-access-gap.md). Never treat missing data as zero or estimate a precise value. Exclude the value when it remains unverifiable.

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
