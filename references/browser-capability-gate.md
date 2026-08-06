# Mandatory Browser Capability Gate

Run this gate before every authenticated, dynamic-platform, or web-AI branch. A prior successful run, documentation, a helper registry, or a remembered selector is not sufficient: browser and site interfaces drift independently.

## Gate sequence

1. Declare the capabilities the branch requires: navigation, semantic snapshot, DOM evaluation, visual capture, authenticated state, user handoff, file upload, or editor input.
2. Run the adapter smoke test on a harmless public page.
3. Verify each required helper by checking availability **and invoking it harmlessly**. Record both results when a diagnostic registry disagrees with runtime behavior.
4. On each target service, discover the currently visible editable surface from live DOM/accessibility state. Consider visible `textarea`, `[contenteditable=true]`, and appropriate text inputs; do not rely on one permanent selector.
5. Insert a disposable marker, read it back from the same visible surface, clear it, and verify the surface is empty. Only then submit a real prompt.
6. Verify the visible account, model/mode, research feature, and authentication state. Use user handoff for login, CAPTCHA, 2FA, consent, payment, or ambiguous account selection.
7. Record PASS, DEGRADED, or FAIL before starting the branch.

## Gate result

```text
Adapter and version:
Verified date:
Target service and URL:
Required capabilities:
Navigation: pass/fail + proof
Semantic readback: pass/fail + proof
DOM evaluation: pass/fail + proof
Visual capture: pass/fail/not required + proof
Visible editor discovered: element/role, without sensitive contents
Disposable write/readback/clear: pass/fail
Authentication and mode: pass/fail/user handoff
Fallback and claim restrictions:
Gate: PASS / DEGRADED / FAIL
```

- **PASS:** every required capability is verified live.
- **DEGRADED:** a named fallback preserves the decision, and the evidence or claims that cannot be supported are explicitly restricted.
- **FAIL:** block the branch. Use open-web evidence, a verified adapter, or user handoff.

Visual capture is required only when the decision depends on visual state that semantic/DOM inspection cannot verify. A semantic-only path may be DEGRADED for visual metrics and still PASS for text-source discovery.

## Runtime observations, not permanent selectors

Observed on 2026-08-06 with EGO 0.4.5.9:

| Surface | Live observation |
| --- | --- |
| Perplexity | Visible contenteditable editor |
| ChatGPT | Visible contenteditable editor despite earlier runs exposing a textarea-like path |
| Grok | Both a visible textarea and visible contenteditable surface |
| Gemini | Visible contenteditable editor |

These observations document drift; they are not a selector contract. Re-probe on every substantial run. When multiple visible surfaces exist, confirm which one owns the disposable marker and the enabled submit control.

The same EGO runtime exposed `captureScreenshot` as an invokable function even though `help('captureScreenshot')` returned `Unknown helper`. Treat diagnostic output as one signal, not proof of availability or absence. Conversely, a named helper is not verified until a harmless invocation succeeds.

## Input safety

- Never paste the real prompt until disposable write/readback/clear passes.
- Never include secrets in a probe marker.
- Do not use clipboard fallbacks that could overwrite user data unless the user authorized them.
- Verify post-action state after submission; an empty editor alone does not prove the prompt was sent.
- If the page changes during the probe, rediscover the surface instead of retrying a stale selector.

