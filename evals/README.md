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

Every result records the UTC date, skill version, case, model, tool, criterion scores, total score, failures, and pass state under `evals/results/`. Structural validation records `model: null` and explicitly states that it is not a behavioral benchmark.
