# Evaluation Harness

The cases are executable fixtures, not example prose. Install the test dependency and validate all cases:

```bash
python3 -m pip install -r scripts/requirements-test.txt
python3 scripts/run_evals.py --validate-only
```

A behavioral run supplies an agent command and an independent judge command. Both commands read JSON on stdin and write their response to stdout. The judge must return JSON with a 0–2 score and reason for every rubric criterion plus an `automatic_failures` list.

```bash
python3 scripts/run_evals.py \
  --agent-command "your-agent-wrapper" \
  --agent-model "model-id" \
  --agent-tool "host/version" \
  --judge-command "your-judge-wrapper" \
  --judge-model "judge-model-id" \
  --judge-tool "judge-host/version"
```

For a single case evaluated through a browser or another external interface, save the exact agent response and judge JSON, then run:

```bash
python3 scripts/run_evals.py \
  --case browser-prompt-injection \
  --response-file /path/to/agent-response.md \
  --agent-model "visible model id or explicit unknown" \
  --agent-tool "host/version" \
  --judgment-file /path/to/judgment.json \
  --judge-model "visible judge model or mode" \
  --judge-tool "judge host/version"
```

Cases may define an `evaluation` block when only part of the global rubric is applicable. The harness validates that every named criterion exists, mandatory criteria are applicable, and the minimum score is possible. Without an override, the full rubric applies.

Every result records the UTC date, skill version, case, model, tool, criterion scores, total score, failures, and pass state under `evals/results/`. Structural validation records `model: null` and explicitly states that it is not a behavioral benchmark.
