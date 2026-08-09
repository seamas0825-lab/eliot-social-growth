#!/usr/bin/env python3
"""Small behavioral regression suite for workflow_guard.py."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts/workflow_guard.py"


def invoke(*args):
    return subprocess.run(
        [sys.executable, str(GUARD), *args],
        text=True,
        capture_output=True,
        check=False,
    )


class WorkflowGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.state = Path(self.temp.name) / "run-state.yaml"
        init = invoke(
            "init", "--state", str(self.state), "--project", "demo",
            "--decision", "choose a content experiment", "--risk", "reversible",
            "--success-signal", "qualified inquiries", "--observation-window", "14 days",
            "--mode", "Standard", "--exclude", "official_baseline=user excluded website",
        )
        self.assertEqual(init.returncode, 0, init.stdout + init.stderr)

    def tearDown(self):
        self.temp.cleanup()

    def load(self):
        return yaml.safe_load(self.state.read_text(encoding="utf-8"))

    def save(self, value):
        self.state.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def test_blueprint_rejects_unresolved_template(self):
        result = invoke("gate", "--state", str(self.state), "--gate", "blueprint")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("placeholder", result.stdout)

    def test_ai_entry_is_pending_until_explicitly_verified(self):
        state = self.load()
        self.assertEqual(state["ai_value_gate"]["result"], "pending")
        self.assertEqual(state["ai_value_gate"]["entry_path"], "pending")
        self.assertEqual(state["ai_value_gate"]["internal_data_access"], "pending")

    def make_reviewable(self):
        state = self.load()
        state["run_control"]["blueprint_reviewed"] = True
        state["parallelism"]["adapter"] = "ego-browser"
        for group in state["parallelism"]["groups"]:
            group.update({
                "start_condition": "blueprint gate passes",
                "convergence_point": "sequential evidence convergence",
                "account_or_rate_limit": "one task space per independent branch",
            })
            for subtask in group.get("subtasks", []):
                subtask["independence_rule"] = subtask.get("independence_rule") or "Independent sibling task with sequential convergence."
        for branch in state["branches"]:
            branch.update({
                "question": f"What evidence changes the {branch['family']} decision?",
                "capability_required": "navigation and semantic readback",
                "service_adapter": "ego-browser or open-web fallback",
                "fallback": "search engine, platform-native search, then record gap",
                "time_or_source_budget": "14 days, 3-5 source cases",
                "entry_condition": "blueprint gate passes",
                "stop_rule": "stop when new cases repeat mechanisms",
                "expected_artifact": f"{branch['family']} evidence ledger",
                "decision_affected": state["project"]["decision"],
            })
        state["ai_value_gate"].update({
            "reason": "EGO Browser is available; one bounded browser-AI branch adds multilingual contradiction review.",
            "result": "one_bounded_branch",
            "entry_path": "ego_browser",
            "entry_path_verified": True,
            "internal_data_access": "user_not_provided",
            "internal_data_reason": "No private Insights, CRM, or DM export was provided.",
        })
        state["browser_capability_gate"].update({
            "adapter": "ego-browser",
            "adapter_version": "verified",
            "verified_date": "2026-08-10",
            "required_capabilities": ["navigation", "semantic_snapshot", "dom_evaluation", "textarea_input"],
            "verified_capabilities": ["navigation", "semantic_snapshot", "dom_evaluation", "textarea_input"],
            "result": "pass",
        })
        state["search_intent"].update({
            "audience_roles": ["agency buyer"],
            "decision_situations": ["select a China DMC partner"],
            "query_families": ["China DMC itinerary for agencies"],
            "languages": ["English"],
            "query_to_case_source_ids": ["source-native-001"],
        })
        self.save(state)

    def test_gates_authorize_then_revoke_after_reentry(self):
        self.make_reviewable()
        approved = invoke("approve", "--state", str(self.state), "--what", "blueprint")
        self.assertEqual(approved.returncode, 0, approved.stdout + approved.stderr)
        blueprint = invoke("gate", "--state", str(self.state), "--gate", "blueprint")
        self.assertEqual(blueprint.returncode, 0, blueprint.stdout + blueprint.stderr)

        state = self.load()
        for branch in state["branches"]:
            branch.update({"status": "complete", "source_ids": [f"source-{branch['id']}"], "branch_exit_gate": "pass"})
        self.save(state)
        for branch in state["branches"]:
            exited = invoke("gate", "--state", str(self.state), "--gate", "branch-exit", "--branch", branch["id"])
            self.assertEqual(exited.returncode, 0, exited.stdout + exited.stderr)
        baseline = invoke("gate", "--state", str(self.state), "--gate", "brand-baseline")
        self.assertEqual(baseline.returncode, 0, baseline.stdout + baseline.stderr)
        parallel = invoke("assert", "--state", str(self.state), "--action", "parallel-research")
        self.assertEqual(parallel.returncode, 0, parallel.stdout + parallel.stderr)
        state = self.load()
        convergence = state["convergence"]
        convergence.update({
            "selected_direction": "buyer-ready evidence cards",
            "next_experiment": "specification carousel versus generic inspiration",
            "reversal_condition": "zero qualified inquiries after 14 days",
        })
        state["beliefs"] = [{"id": "belief-001", "gate": "provisional_test"}]
        self.save(state)
        pre = invoke("gate", "--state", str(self.state), "--gate", "pre-convergence")
        self.assertEqual(pre.returncode, 0, pre.stdout + pre.stderr)
        strategy = invoke("assert", "--state", str(self.state), "--action", "strategy")
        self.assertEqual(strategy.returncode, 0, strategy.stdout + strategy.stderr)
        delivery = invoke("gate", "--state", str(self.state), "--gate", "pre-delivery")
        self.assertEqual(delivery.returncode, 0, delivery.stdout + delivery.stderr)
        self.assertEqual(invoke("assert", "--state", str(self.state), "--action", "delivery").returncode, 0)

        reentry = invoke("reentry", "--state", str(self.state), "--reason", "user changed audience and cadence")
        self.assertEqual(reentry.returncode, 0, reentry.stdout + reentry.stderr)
        self.assertTrue(all(item["status"] == "waiting" for item in self.load()["branches"]))
        blocked = invoke("assert", "--state", str(self.state), "--action", "delivery")
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("reentry", blocked.stdout)


if __name__ == "__main__":
    unittest.main()
