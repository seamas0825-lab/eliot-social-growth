#!/usr/bin/env python3
"""Validate eval cases or run command-backed agent/judge evaluations."""

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CASE_FIELDS = {
    "id", "input", "known_facts", "hidden_traps", "required_behavior",
    "forbidden_behavior", "expected_decisions", "acceptable_uncertainties",
}


def load_yaml(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_case(case, path):
    missing = sorted(CASE_FIELDS - set(case or {}))
    if missing:
        raise ValueError(f"{path.name}: missing fields: {', '.join(missing)}")
    for field in CASE_FIELDS - {"id", "input"}:
        if not isinstance(case[field], list) or not case[field]:
            raise ValueError(f"{path.name}: {field} must be a non-empty list")
    evaluation = case.get("evaluation")
    if evaluation is not None:
        required = {"applicable_criteria", "minimum_total", "mandatory_twos"}
        missing_eval = sorted(required - set(evaluation))
        if missing_eval:
            raise ValueError(f"{path.name}: evaluation missing: {', '.join(missing_eval)}")
        if not isinstance(evaluation["applicable_criteria"], list) or not evaluation["applicable_criteria"]:
            raise ValueError(f"{path.name}: evaluation.applicable_criteria must be a non-empty list")


def run_command(command, stdin_text, timeout):
    result = subprocess.run(
        command, input=stdin_text, text=True, capture_output=True,
        timeout=timeout, shell=True, check=False,
    )
    if result.returncode:
        raise RuntimeError(f"command failed ({result.returncode}): {result.stderr[-2000:]}")
    return result.stdout


def evaluation_policy(rubric, case):
    all_criteria = [item["id"] for item in rubric["criteria"]]
    override = case.get("evaluation")
    if not override:
        return {
            "applicable_criteria": all_criteria,
            "minimum_total": rubric["pass_conditions"]["minimum_total"],
            "mandatory_twos": rubric["pass_conditions"]["mandatory_twos"],
        }
    unknown = sorted(set(override["applicable_criteria"]) - set(all_criteria))
    if unknown:
        raise ValueError(f"{case['id']}: unknown applicable criteria: {', '.join(unknown)}")
    if not set(override["mandatory_twos"]).issubset(set(override["applicable_criteria"])):
        raise ValueError(f"{case['id']}: mandatory_twos must be applicable")
    maximum = len(override["applicable_criteria"]) * 2
    if not 0 <= override["minimum_total"] <= maximum:
        raise ValueError(f"{case['id']}: minimum_total must be between 0 and {maximum}")
    return override


def score_result(rubric, case, judgment):
    policy = evaluation_policy(rubric, case)
    expected = policy["applicable_criteria"]
    raw_scores = judgment.get("scores", {})
    normalized = {}
    for criterion in expected:
        value = raw_scores.get(criterion)
        if not isinstance(value, dict) or value.get("score") not in (0, 1, 2):
            raise ValueError(f"judge result missing valid 0–2 score for {criterion}")
        normalized[criterion] = {"score": value["score"], "reason": str(value.get("reason", ""))}
    total = sum(value["score"] for value in normalized.values())
    automatic_failures = judgment.get("automatic_failures", [])
    mandatory = policy["mandatory_twos"]
    passed = (
        not automatic_failures
        and total >= policy["minimum_total"]
        and all(normalized[item]["score"] == 2 for item in mandatory)
    )
    return normalized, total, len(expected) * 2, automatic_failures, passed, policy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", help="Case id; repeatable. Defaults to all cases.")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--agent-command")
    parser.add_argument("--response-file", help="Use an existing agent response instead of --agent-command.")
    parser.add_argument("--agent-model")
    parser.add_argument("--agent-tool")
    parser.add_argument("--judge-command")
    parser.add_argument("--judgment-file", help="Use existing judge JSON instead of --judge-command.")
    parser.add_argument("--judge-model")
    parser.add_argument("--judge-tool")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--output")
    args = parser.parse_args()

    rubric_path = ROOT / "evals/rubric.yaml"
    rubric = load_yaml(rubric_path)
    case_paths = sorted((ROOT / "evals/cases").glob("*.yaml"))
    if args.case:
        selected = set(args.case)
        case_paths = [path for path in case_paths if path.stem in selected]
        missing = selected - {path.stem for path in case_paths}
        if missing:
            parser.error(f"unknown case(s): {', '.join(sorted(missing))}")

    cases = []
    for path in case_paths:
        case = load_yaml(path)
        validate_case(case, path)
        cases.append(case)

    now = dt.datetime.now(dt.timezone.utc)
    if args.validate_only:
        result = {
            "schema_version": 1,
            "run_type": "structural-validation",
            "skill_version": (ROOT / "VERSION").read_text().strip(),
            "run_at": now.isoformat(),
            "model": None,
            "tool": "scripts/run_evals.py --validate-only",
            "score": {"valid_cases": len(cases), "total_cases": len(cases), "passed": True},
            "case_ids": [case["id"] for case in cases],
            "note": "This validates eval wiring and schemas; it is not a behavioral model benchmark.",
        }
    else:
        required = ["agent_model", "agent_tool", "judge_model", "judge_tool"]
        missing = [name.replace("_", "-") for name in required if not getattr(args, name)]
        if missing:
            parser.error("behavioral runs require --" + ", --".join(missing))
        if bool(args.agent_command) == bool(args.response_file):
            parser.error("provide exactly one of --agent-command or --response-file")
        if bool(args.judge_command) == bool(args.judgment_file):
            parser.error("provide exactly one of --judge-command or --judgment-file")
        if (args.response_file or args.judgment_file) and len(cases) != 1:
            parser.error("file-backed behavioral runs require exactly one --case")
        results = []
        for case in cases:
            agent_prompt = json.dumps({"case": case, "rubric": rubric}, ensure_ascii=False)
            response = (
                Path(args.response_file).read_text(encoding="utf-8").strip()
                if args.response_file
                else run_command(args.agent_command, agent_prompt, args.timeout).strip()
            )
            policy = evaluation_policy(rubric, case)
            judge_input = json.dumps({
                "case": case,
                "rubric": rubric,
                "agent_response": response,
                "required_output": {
                    "scores": {criterion: {"score": "0|1|2", "reason": "traceable reason"} for criterion in policy["applicable_criteria"]},
                    "automatic_failures": [],
                },
            }, ensure_ascii=False)
            judgment = (
                json.loads(Path(args.judgment_file).read_text(encoding="utf-8"))
                if args.judgment_file
                else json.loads(run_command(args.judge_command, judge_input, args.timeout))
            )
            scores, total, maximum, failures, passed, policy = score_result(rubric, case, judgment)
            results.append({
                "case_id": case["id"], "scores": scores, "total": total,
                "maximum": maximum, "automatic_failures": failures,
                "passed": passed, "evaluation_policy": policy,
                "agent_response": response,
            })
        result = {
            "schema_version": 1,
            "run_type": "behavioral-evaluation",
            "skill_version": (ROOT / "VERSION").read_text().strip(),
            "run_at": now.isoformat(),
            "agent": {
                "model": args.agent_model, "tool": args.agent_tool,
                "command": args.agent_command,
                "response_file": Path(args.response_file).name if args.response_file else None,
            },
            "judge": {
                "model": args.judge_model, "tool": args.judge_tool,
                "command": args.judge_command,
                "judgment_file": Path(args.judgment_file).name if args.judgment_file else None,
            },
            "rubric": str(rubric_path.relative_to(ROOT)),
            "results": results,
            "score": {
                "passed_cases": sum(item["passed"] for item in results),
                "total_cases": len(results),
                "points": sum(item["total"] for item in results),
                "maximum": sum(item["maximum"] for item in results),
            },
            "passed": all(item["passed"] for item in results),
        }

    output = Path(args.output) if args.output else ROOT / "evals/results" / f"{now.date().isoformat()}-{result['run_type']}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("passed", result["score"].get("passed", False)) else 1


if __name__ == "__main__":
    sys.exit(main())
