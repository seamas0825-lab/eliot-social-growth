#!/usr/bin/env python3
"""Fail-closed workflow state guard for eliot-social-growth runs.

The guard does not decide research content. It makes skipped stages and
unreconciled branches visible, and blocks strategy or delivery assertions until
the recorded gates are complete.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised on unsupported hosts
    raise SystemExit("workflow_guard.py requires PyYAML; install scripts/requirements-test.txt") from exc


FAMILIES = (
    "official_baseline",
    "official_social_accounts",
    "target_native_performance",
    "search_intent_keywords",
    "native_high_performing_cases",
    "direct_competitors",
    "analogous_mechanisms",
    "user_voice_community",
    "authoritative_facts",
    "internal_or_real_user_evidence",
    "ai_research",
)
BASELINE_FAMILIES = ("official_baseline", "official_social_accounts", "target_native_performance")
SOCIAL_CONTENT_REQUIRED_FAMILIES = (
    "direct_competitors", "analogous_mechanisms",
    "search_intent_keywords", "native_high_performing_cases",
)
GROUP_BY_FAMILY = {
    "official_baseline": "brand-baseline-001",
    "official_social_accounts": "brand-baseline-001",
    "target_native_performance": "brand-baseline-001",
    "direct_competitors": "post-baseline-wave-001",
    "analogous_mechanisms": "post-baseline-wave-001",
    "search_intent_keywords": "post-baseline-wave-001",
    "native_high_performing_cases": "post-baseline-wave-001",
    "ai_research": "post-baseline-wave-001",
    "user_voice_community": "contextual-sequential-001",
    "authoritative_facts": "contextual-sequential-001",
    "internal_or_real_user_evidence": "contextual-sequential-001",
}
GROUP_SPECS = (
    ("brand-baseline-001", "single_surface_only", "official brand baseline, official social accounts, and target-native account behavior"),
    ("post-baseline-wave-001", "parallel_after_gate", "three independent EGO subtasks after the brand baseline: competitor/analogous, multi-AI, and keyword-to-native-performance"),
    ("contextual-sequential-001", "sequential_dependency", "community, authoritative, and internal evidence when their decision value remains after baseline"),
)
DISPOSITIONS = {"required", "planned", "excluded_by_user", "excluded_by_value_gate", "not_applicable"}
DONE_STATUSES = {"complete", "degraded", "excluded"}
PLACEHOLDER = re.compile(r"^(?:$|TODO\b|pending(?:\s|$)|.+\s\|\s.+$)", re.IGNORECASE)


def now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def blank(value):
    return value is None or (isinstance(value, str) and PLACEHOLDER.search(value.strip()) is not None)


def load_state(path: Path):
    if not path.exists():
        raise ValueError(f"state file does not exist: {path}")
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("state file must contain a YAML mapping")
    return value


def save_state(path: Path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(state, allow_unicode=True, sort_keys=False), encoding="utf-8")


def result(ok, errors=None, changed=False, **extra):
    payload = {"passed": bool(ok), "errors": errors or [], "changed": changed}
    payload.update(extra)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if ok else 1


def base_state(args, path: Path):
    exclusions = {}
    for item in args.exclude or []:
        if "=" not in item:
            raise ValueError("--exclude expects FAMILY=REASON")
        family, reason = item.split("=", 1)
        if family not in FAMILIES:
            raise ValueError(f"unknown branch family: {family}")
        exclusions[family] = ("excluded_by_user", reason.strip())

    inventory = []
    branches = []
    for family in FAMILIES:
        disposition, reason = exclusions.get(family, ("required", "Hard dependency until the blueprint review changes this disposition."))
        inventory.append({"family": family, "disposition": disposition, "reason": reason, "branch_ids": []})
        if disposition in {"required", "planned"}:
            branch_id = f"{family}-001"
            inventory[-1]["branch_ids"] = [branch_id]
            branches.append({
                "id": branch_id,
                "family": family,
                "disposition": disposition,
                "question": f"TODO: define the decision question for {family}",
                "capability_required": "TODO: name the required capability",
                "service_adapter": "TODO: name the adapter or open-web path",
                "capability_verified_date": "",
                "known_limitation": "",
                "fallback": "TODO: record the bounded fallback ladder",
                "dependency": "soft" if family == "native_high_performing_cases" else ("asynchronous_external" if family == "ai_research" else "independent"),
                "parallel_group_id": GROUP_BY_FAMILY.get(family, "parallel-research-001"),
                "time_or_source_budget": "TODO: set a bounded time or source budget",
                "entry_condition": "TODO: define the entry condition",
                "stop_rule": "TODO: define the stop rule",
                "expected_artifact": f"TODO: define the {family} evidence artifact",
                "status": "planned",
                "stable_session_id": "",
                "session_url": "",
                "exact_prompt_path": "",
                "source_ids": [],
                "conflicts": [],
                "decision_affected": "TODO: state which decision this branch can change",
                "branch_exit_gate": "pending",
                "changed_branches_or_beliefs": [],
                "included": True,
                "exclusion_reason": "",
            })

    branch_ids_by_family = {family: [item["id"] for item in branches if item["family"] == family] for family in FAMILIES}
    groups = []
    for group_id, mode, description in GROUP_SPECS:
        family_ids = [family for family, mapped_group in GROUP_BY_FAMILY.items() if mapped_group == group_id]
        group = {
            "id": group_id,
            "mode": mode,
            "branch_ids": [branch_id for family in family_ids for branch_id in branch_ids_by_family.get(family, [])],
            "task_space_ids": [],
            "owner_paths": [],
            "start_condition": "TODO: define the shared gate",
            "convergence_point": "TODO: define the sequential convergence point",
            "account_or_rate_limit": "TODO: record account/rate-limit boundary",
            "bundle_description": description,
            "subtasks": [],
        }
        if group_id == "post-baseline-wave-001":
            group["subtasks"] = [
                {
                    "id": "competitor-analog-001",
                    "label": "Direct competitors and analogous mechanisms",
                    "branch_ids": branch_ids_by_family.get("direct_competitors", []) + branch_ids_by_family.get("analogous_mechanisms", []),
                    "task_space_ids": [], "owner_paths": [],
                    "independence_rule": "Independent of the sibling AI and keyword-native subtasks after brand baseline exit.",
                },
                {
                    "id": "multi-ai-001",
                    "label": "Bounded multi-AI research",
                    "branch_ids": branch_ids_by_family.get("ai_research", []),
                    "task_space_ids": [], "owner_paths": [],
                    "independence_rule": "Use distinct AI jobs with distinct questions; converge sequentially after source verification.",
                },
                {
                    "id": "keyword-native-001",
                    "label": "Behavioral keyword map and native-platform performance",
                    "branch_ids": branch_ids_by_family.get("search_intent_keywords", []) + branch_ids_by_family.get("native_high_performing_cases", []),
                    "task_space_ids": [], "owner_paths": [],
                    "independence_rule": "The subtask may build the keyword map then trace it to native cases inside one task space; it is independent of the sibling subtasks.",
                },
            ]
        groups.append(group)

    return {
        "version": 2,
        "project": {
            "name": args.project,
            "task_type": args.task_type,
            "decision": args.decision,
            "decision_risk": args.risk,
            "decision_owner": args.owner,
            "success_signal": args.success_signal,
            "constraints": [],
            "non_negotiables": [],
            "observation_window": args.observation_window,
        },
        "workflow": {
            "mode": args.mode,
            "current_stage": "scope",
            "source_of_truth_path": str(path),
            "last_reconciled_at": now(),
            "reentry_check_completed": False,
            "checkpoints": {
                "blueprint_gate": "pending",
                "brand_baseline_gate": "pending",
                "branch_exit_gate_last_branch": "",
                "branch_exit_gate_status": "pending",
                "pre_convergence_completeness_gate": "pending",
                "pre_delivery_gate": "pending",
            },
            "forgotten_or_reopened_branches": [],
            "active_blockers": [],
        },
        "run_control": {
            "initialized": True,
            "blueprint_reviewed": False,
            "reentry_required": False,
            "reentry_reason": "",
            "strategy_writing_allowed": False,
            "delivery_allowed": False,
            "revision": 0,
            "last_user_update_at": "",
        },
        "preflight": {
            "detected_os": "", "detection_date": "",
            "required_browser_components": [], "present_browser_components": [],
            "missing_browser_components": [], "missing_component_reminder_sent": False,
            "browser_runtime_probe_status": "", "browser_runtime_probe_evidence": "",
            "difficulty_assessment": "", "recommended_mode": "",
            "recommendation_reason": "", "mode_choice_status": "",
            "relevant_social_platforms": [], "social_login_status": {},
            "social_login_reminder_status": "", "recommended_ai_services": [],
            "selected_ai_services": [], "ai_service_choice_status": "",
            "ai_login_status": {}, "ai_login_reminder_status": "",
        },
        "branch_inventory": inventory,
        "search_intent": {
            "audience_roles": [], "decision_situations": [], "query_families": [],
            "languages": [], "native_platform_probes": [], "open_web_probes": [],
            "query_to_case_source_ids": [], "repeated_mechanisms_stop_reached": False,
            "cross_platform_probe": {
                "target_platforms": [], "supplemental_platforms": [],
                "query_families_tested": [], "query_to_case_source_ids": [],
                "status": "pending", "limitation": "",
            },
        },
        "content_strategy_contract": {
            "applicable": args.task_type == "social_content_strategy",
            "competitor_data_complete": False,
            "keyword_psychology_complete": False,
            "keyword_to_native_performance_complete": False,
            "evidence_limits_complete": False,
            "research_to_calendar_change_log_complete": False,
            "competitor_artifact_path": "",
            "keyword_psychology_artifact_path": "",
            "keyword_performance_artifact_path": "",
            "evidence_limits_artifact_path": "",
            "research_to_calendar_change_log_path": "",
        },
        "parallelism": {
            "adapter": "TODO: select the browser/host adapter",
            "host_concurrency_available": False,
            "groups": groups,
        },
        "discovery_attempts": [],
        "external_jobs": [],
        "ai_value_gate": {
            "primary_source_faster": False, "real_user_faster": False,
            "internal_data_owns_answer": False, "cheap_test_faster": False,
            "reversible_judgment_safe": False, "ai_value_added": [],
            "result": "pending", "entry_path": "pending", "entry_path_verified": False,
            "internal_data_access": "pending", "internal_data_reason": "TODO: record internal data access",
            "reason": "TODO: record the AI value decision",
        },
        "browser_capability_gate": {
            "adapter": "", "adapter_version": "", "verified_date": "",
            "required_capabilities": [], "verified_capabilities": [],
            "failed_capabilities": [], "service_editor_probe": "not_required",
            "fallback_and_claim_restrictions": [], "result": "pending",
        },
        "beliefs": [], "language_lenses": [], "evidence_access_gaps": [],
        "branches": branches,
        "human_checkpoints": {
            key: {"status": "not_needed", "owner": "", "decision": ""}
            for key in ("decision", "taste", "contradiction", "reality")
        },
        "convergence": {
            "multi_ai_gate": "not_required", "claim_matrix_path": "",
            "shared_sources_deduplicated": False, "verified_consensus": [],
            "verified_divergence": [], "unverified_consensus": [],
            "single_branch_leads": [], "included_findings": [],
            "excluded_findings": [], "unresolved_uncertainties": [],
            "selected_direction": "", "rejected_directions": [],
            "next_experiment": "", "reversal_condition": "", "stop_reason": "",
        },
    }


def branch_map(state):
    return {item.get("id"): item for item in state.get("branches", []) if isinstance(item, dict) and item.get("id")}


def included_families(state):
    return {
        item.get("family") for item in state.get("branch_inventory", [])
        if item.get("disposition") in {"required", "planned"}
    }


def included_branch_ids_for_families(state, families):
    family_set = set(families)
    return [
        branch_id
        for item in state.get("branch_inventory", [])
        if item.get("family") in family_set and item.get("disposition") in {"required", "planned"}
        for branch_id in (item.get("branch_ids") or [])
    ]


def blueprint_errors(state):
    errors = []
    if state.get("version") != 2:
        errors.append("state version must be 2; reinitialize from schemas/run-state.yaml")
    project = state.get("project") or {}
    for key in ("name", "decision", "decision_risk", "success_signal", "observation_window"):
        if blank(project.get(key)):
            errors.append(f"project.{key} is empty or still a placeholder")
    if project.get("task_type") not in {"general", "social_research", "social_content_strategy"}:
        errors.append("project.task_type must be general, social_research, or social_content_strategy")
    workflow = state.get("workflow") or {}
    if workflow.get("mode") not in {"Light", "Standard", "Deep"}:
        errors.append("workflow.mode must be Light, Standard, or Deep")
    control = state.get("run_control") or {}
    if not control.get("initialized"):
        errors.append("run_control.initialized is false; run workflow_guard.py init")
    if not control.get("blueprint_reviewed"):
        errors.append("blueprint has not been explicitly reviewed; run approve --what blueprint")
    if control.get("reentry_required"):
        errors.append("reentry is required after a user/scope update; reconcile state before browsing")

    preflight = state.get("preflight") or {}
    if preflight.get("detected_os") not in {"macos", "windows", "linux", "other"}:
        errors.append("preflight.detected_os must record the detected operating system")
    for key in ("detection_date", "difficulty_assessment", "recommendation_reason"):
        if blank(preflight.get(key)):
            errors.append(f"preflight.{key} is empty or a placeholder")
    if preflight.get("recommended_mode") not in {"Light", "Standard", "Deep"}:
        errors.append("preflight.recommended_mode must be Light, Standard, or Deep")
    if preflight.get("mode_choice_status") not in {"confirmed", "preselected_by_user"}:
        errors.append("preflight.mode_choice_status must confirm the user's mode choice")
    required_components = preflight.get("required_browser_components") or []
    if not required_components:
        errors.append("preflight.required_browser_components must record the OS-specific browser path")
    accounted_components = set(preflight.get("present_browser_components") or []) | set(preflight.get("missing_browser_components") or [])
    unaccounted_components = [item for item in required_components if item not in accounted_components]
    if unaccounted_components:
        errors.append("preflight must classify every required browser component as present or missing")
    normalized_components = " ".join(required_components).lower()
    if preflight.get("detected_os") == "macos" and not ("ego lite" in normalized_components and "ego-browser" in normalized_components):
        errors.append("macOS preflight requires EGO Lite Browser and the ego-browser skill")
    if preflight.get("detected_os") == "windows" and not ("browser use" in normalized_components and "web-access" in normalized_components):
        errors.append("Windows preflight requires Browser Use and the eze-is/web-access skill")
    if preflight.get("missing_browser_components") and not preflight.get("missing_component_reminder_sent"):
        errors.append("preflight missing browser components require a user reminder")
    if preflight.get("browser_runtime_probe_status") not in {"pass", "degraded", "fail"}:
        errors.append("preflight.browser_runtime_probe_status must record the live browser/adapter probe")
    if blank(preflight.get("browser_runtime_probe_evidence")):
        errors.append("preflight.browser_runtime_probe_evidence must identify the harmless live invocation or detected failure")
    if not preflight.get("missing_browser_components") and preflight.get("browser_runtime_probe_status") != "pass":
        errors.append("preflight with all browser components present requires a passing live runtime probe")
    if preflight.get("ai_service_choice_status") not in {"confirmed", "declined", "preselected_by_user", "not_applicable"}:
        errors.append("preflight.ai_service_choice_status must record the user's optional AI choice")
    if preflight.get("selected_ai_services") and preflight.get("ai_login_reminder_status") not in {"not_needed", "sent", "user_declined_login"}:
        errors.append("preflight selected AI services need a recorded login check/reminder status")
    selected_ai = preflight.get("selected_ai_services") or []
    ai_login = preflight.get("ai_login_status") or {}
    if selected_ai and any(service not in ai_login for service in selected_ai):
        errors.append("preflight.ai_login_status must cover every selected AI service")
    if selected_ai and preflight.get("ai_login_reminder_status") == "not_needed" and any(ai_login.get(service) != "logged_in" for service in selected_ai):
        errors.append("preflight cannot skip the AI login reminder unless every selected service is visibly logged in")
    if project.get("task_type") in {"social_research", "social_content_strategy"}:
        platforms = preflight.get("relevant_social_platforms") or []
        if not platforms:
            errors.append("preflight.relevant_social_platforms is required for social tasks")
        login_status = preflight.get("social_login_status") or {}
        missing_platform_status = [platform for platform in platforms if platform not in login_status]
        if missing_platform_status:
            errors.append("preflight.social_login_status must cover every relevant social platform")
        if preflight.get("social_login_reminder_status") not in {"not_needed", "sent", "user_declined_login"}:
            errors.append("preflight.social_login_reminder_status must be recorded for social tasks")
        if preflight.get("social_login_reminder_status") == "not_needed" and any(login_status.get(platform) != "logged_in" for platform in platforms):
            errors.append("preflight cannot skip the social login reminder unless every relevant platform is visibly logged in")

    inventory = state.get("branch_inventory") or []
    seen = set()
    branches = branch_map(state)
    for item in inventory:
        family = item.get("family")
        disposition = item.get("disposition")
        if family not in FAMILIES:
            errors.append(f"unknown branch family: {family}")
            continue
        seen.add(family)
        if disposition not in DISPOSITIONS:
            errors.append(f"{family}: invalid disposition")
        if blank(item.get("reason")):
            errors.append(f"{family}: disposition reason is missing")
        ids = item.get("branch_ids") or []
        if disposition in {"required", "planned"} and not ids:
            errors.append(f"{family}: included disposition has no branch_ids")
        for branch_id in ids:
            if branch_id not in branches:
                errors.append(f"{family}: missing branch record {branch_id}")
    for family in set(FAMILIES) - seen:
        errors.append(f"branch_inventory is missing family {family}")
    if project.get("task_type") == "social_content_strategy":
        inventory_by_family = {item.get("family"): item for item in inventory}
        for family in SOCIAL_CONTENT_REQUIRED_FAMILIES:
            if (inventory_by_family.get(family) or {}).get("disposition") != "required":
                errors.append(f"{family}: social_content_strategy requires this family; use degraded branch status when access is limited")
        contract = state.get("content_strategy_contract") or {}
        if contract.get("applicable") is not True:
            errors.append("content_strategy_contract.applicable must be true for social_content_strategy")

    required_fields = (
        "family", "question", "capability_required", "service_adapter", "fallback",
        "dependency", "parallel_group_id", "time_or_source_budget", "entry_condition",
        "stop_rule", "expected_artifact", "decision_affected",
    )
    for branch in branches.values():
        if branch.get("family") not in FAMILIES:
            errors.append(f"{branch.get('id')}: unknown family")
        for key in required_fields:
            if blank(branch.get(key)):
                errors.append(f"{branch.get('id')}: {key} is empty or a placeholder")
        if branch.get("status") not in {"planned", "active", "waiting", "complete", "degraded", "blocked", "excluded"}:
            errors.append(f"{branch.get('id')}: invalid status")
        if branch.get("parallel_group_id") and branch.get("parallel_group_id") not in {
            group.get("id") for group in (state.get("parallelism") or {}).get("groups", [])
        }:
            errors.append(f"{branch.get('id')}: parallel_group_id is not declared")

    parallelism = state.get("parallelism") or {}
    if blank(parallelism.get("adapter")):
        errors.append("parallelism.adapter is empty or a placeholder")
    groups = parallelism.get("groups") or []
    if not groups:
        errors.append("parallelism.groups must contain the planned concurrency groups")
    for group in groups:
        for key in ("id", "mode", "start_condition", "convergence_point", "account_or_rate_limit"):
            if blank(group.get(key)):
                errors.append(f"parallel group {group.get('id')}: {key} is empty or a placeholder")
        if group.get("mode") not in {"parallel_now", "parallel_after_gate", "sequential_dependency", "single_surface_only"}:
            errors.append(f"parallel group {group.get('id')}: invalid mode")
        if parallelism.get("host_concurrency_available") and group.get("mode") in {"parallel_now", "parallel_after_gate"} and not group.get("task_space_ids"):
            errors.append(f"parallel group {group.get('id')}: EGO task_space_ids are required when concurrency is available")
        if group.get("mode") == "parallel_after_gate":
            subtasks = [item for item in (group.get("subtasks") or []) if item.get("branch_ids")]
            if len(subtasks) < 2:
                errors.append(f"parallel group {group.get('id')}: at least two independent subtasks are required")
            for subtask in subtasks:
                for key in ("id", "label", "independence_rule"):
                    if blank(subtask.get(key)):
                        errors.append(f"parallel subtask {subtask.get('id')}: {key} is empty or a placeholder")
                if parallelism.get("host_concurrency_available") and not subtask.get("task_space_ids"):
                    errors.append(f"parallel subtask {subtask.get('id')}: EGO task_space_ids are required")
    return sorted(set(errors))


def done_branch_errors(state, branch_id=None, require_exit=True):
    branches = branch_map(state)
    selected = [branches[branch_id]] if branch_id else list(branches.values())
    errors = []
    if branch_id and branch_id not in branches:
        return [f"unknown branch: {branch_id}"]
    for branch in selected:
        if branch.get("included") is False:
            continue
        status = branch.get("status")
        if status not in DONE_STATUSES:
            errors.append(f"{branch.get('id')}: status must be complete, degraded, or excluded")
        if require_exit and branch.get("branch_exit_gate") != "pass":
            errors.append(f"{branch.get('id')}: branch_exit_gate is not pass")
        if status in {"complete", "degraded"} and not branch.get("source_ids"):
            errors.append(f"{branch.get('id')}: complete/degraded branch needs source_ids")
        if status == "excluded" and blank(branch.get("exclusion_reason")):
            errors.append(f"{branch.get('id')}: excluded branch needs exclusion_reason")
    return sorted(set(errors))


def content_strategy_contract_errors(state):
    if (state.get("project") or {}).get("task_type") != "social_content_strategy":
        return []
    contract = state.get("content_strategy_contract") or {}
    errors = []
    required_flags = (
        "competitor_data_complete", "keyword_psychology_complete",
        "keyword_to_native_performance_complete", "evidence_limits_complete",
        "research_to_calendar_change_log_complete",
    )
    for key in required_flags:
        if contract.get(key) is not True:
            errors.append(f"content_strategy_contract.{key} must be true before calendar drafting")
    required_paths = (
        "competitor_artifact_path", "keyword_psychology_artifact_path",
        "keyword_performance_artifact_path", "evidence_limits_artifact_path",
        "research_to_calendar_change_log_path",
    )
    for key in required_paths:
        if blank(contract.get(key)):
            errors.append(f"content_strategy_contract.{key} must identify the completed artifact or section")
    return sorted(set(errors))


def pre_convergence_errors(state):
    errors = []
    errors.extend(blueprint_errors(state))
    errors.extend(done_branch_errors(state))
    post_baseline_ids = included_branch_ids_for_families(state, (
        "direct_competitors", "analogous_mechanisms", "search_intent_keywords",
        "native_high_performing_cases", "ai_research",
    ))
    if post_baseline_ids and (state.get("workflow") or {}).get("checkpoints", {}).get("brand_baseline_gate") != "pass":
        errors.append("brand_baseline_gate must pass before post-baseline parallel research can converge")
    search = state.get("search_intent") or {}
    if "search_intent_keywords" in included_families(state):
        for key in ("audience_roles", "decision_situations", "query_families", "languages"):
            if not search.get(key):
                errors.append(f"search_intent.{key} must be populated before convergence")
        if "native_high_performing_cases" in included_families(state) and not search.get("query_to_case_source_ids"):
            errors.append("search_intent.query_to_case_source_ids must trace keywords to original cases")
    if (state.get("project") or {}).get("task_type") == "social_content_strategy":
        cross = search.get("cross_platform_probe") or {}
        if cross.get("status") not in {"complete", "degraded"}:
            errors.append("search_intent.cross_platform_probe.status must be complete or degraded")
        if not cross.get("target_platforms"):
            errors.append("search_intent.cross_platform_probe.target_platforms must be recorded")
        if cross.get("status") == "complete":
            for key in ("supplemental_platforms", "query_families_tested", "query_to_case_source_ids"):
                if not cross.get(key):
                    errors.append(f"search_intent.cross_platform_probe.{key} must be populated for a complete probe")
        if cross.get("status") == "degraded" and blank(cross.get("limitation")):
            errors.append("degraded cross-platform probe needs a limitation")
        errors.extend(content_strategy_contract_errors(state))
    ai = state.get("ai_value_gate") or {}
    if blank(ai.get("reason")):
        errors.append("ai_value_gate.reason must record whether AI changes the decision")
    if ai.get("result") not in {"pending", "no_ai", "one_bounded_branch", "multiple_distinct_branches"}:
        errors.append("ai_value_gate.result is invalid")
    if ai.get("result") == "pending":
        errors.append("ai_value_gate.result is still pending; complete the AI Value Gate before convergence")
    if ai.get("entry_path") not in {"ego_browser", "api_connector", "open_web_only", "unavailable"}:
        errors.append("ai_value_gate.entry_path must record the actual AI entry path; do not infer unavailability from missing connectors")
    if ai.get("internal_data_access") not in {"available", "user_not_provided", "unavailable"}:
        errors.append("ai_value_gate.internal_data_access must be recorded separately from AI access")
    if ai.get("entry_path") == "ego_browser":
        browser = state.get("browser_capability_gate") or {}
        if not ai.get("entry_path_verified"):
            errors.append("EGO browser AI entry path must be verified with the live editor probe")
        if browser.get("result") not in {"pass", "degraded"}:
            errors.append("EGO browser AI entry path requires a PASS or defensible DEGRADED browser capability gate")
    if "ai_research" in included_families(state) and ai.get("result") == "no_ai":
        errors.append("ai_research is included in the blueprint but ai_value_gate.result is no_ai; reconcile the disposition or run the branch")
    convergence = state.get("convergence") or {}
    if ai.get("result") == "multiple_distinct_branches" and convergence.get("multi_ai_gate") not in {"pass", "provisional_test"}:
        errors.append("multiple AI branches require a completed convergence gate")
    jobs = state.get("external_jobs") or []
    for job in jobs:
        if job.get("status") in {"planned", "running", "active"}:
            errors.append(f"external job {job.get('id')} is still active; mark it waiting_noncritical or reconcile it")
        if job.get("status") in {"unresolved_timeout", "failed"} and blank(job.get("disposition_reason")):
            errors.append(f"external job {job.get('id')}: unresolved/failed job needs a disposition reason")
    return sorted(set(errors))


def calendar_errors(state):
    errors = []
    if (state.get("project") or {}).get("task_type") != "social_content_strategy":
        errors.append("calendar assertion is only valid for project.task_type social_content_strategy")
        return errors
    checkpoints = (state.get("workflow") or {}).get("checkpoints", {})
    if checkpoints.get("pre_convergence_completeness_gate") != "pass":
        errors.append("calendar drafting is blocked until the Pre-Convergence Completeness Gate passes")
    errors.extend(content_strategy_contract_errors(state))
    return sorted(set(errors))


def pre_delivery_errors(state):
    errors = pre_convergence_errors(state)
    workflow = state.get("workflow") or {}
    if workflow.get("checkpoints", {}).get("pre_convergence_completeness_gate") != "pass":
        errors.append("pre_convergence_completeness_gate must be pass before delivery")
    beliefs = state.get("beliefs") or []
    if not beliefs:
        errors.append("at least one first-order belief must be audited before delivery")
    for belief in beliefs:
        if belief.get("gate") not in {"pass", "provisional_test"}:
            errors.append(f"belief {belief.get('id')}: gate must be pass or provisional_test")
    convergence = state.get("convergence") or {}
    for key in ("selected_direction", "next_experiment", "reversal_condition"):
        if blank(convergence.get(key)):
            errors.append(f"convergence.{key} must be filled before delivery")
    return sorted(set(errors))


def audit_state(state):
    inventory = state.get("branch_inventory") or []
    declared = {item.get("family") for item in inventory if item.get("family") in FAMILIES}
    missing_families = sorted(set(FAMILIES) - declared)
    branches = branch_map(state)
    pending = sorted(
        branch_id for branch_id, branch in branches.items()
        if branch.get("included") is not False and branch.get("status") not in DONE_STATUSES
    )
    active_jobs = sorted(
        job.get("id") or "unnamed-job" for job in (state.get("external_jobs") or [])
        if job.get("status") in {"planned", "running", "active"}
    )
    ready_parallel = []
    for group in (state.get("parallelism") or {}).get("groups", []):
        if group.get("mode") not in {"parallel_now", "parallel_after_gate"}:
            continue
        ready = [branch_id for branch_id in group.get("branch_ids", []) if branch_id in pending]
        if len(ready) >= 2:
            ready_parallel.append({"group_id": group.get("id"), "branch_ids": ready})
    contract = content_strategy_contract_errors(state)
    reopened = (state.get("workflow") or {}).get("forgotten_or_reopened_branches") or []
    critical = []
    if missing_families:
        critical.append("branch inventory is missing required families")
    return {
        "critical_errors": critical,
        "missing_branch_families": missing_families,
        "pending_branches": pending,
        "active_external_jobs": active_jobs,
        "parallel_opportunities": ready_parallel,
        "forgotten_or_reopened_branches": reopened,
        "content_contract_gaps": contract,
    }


def gate(state, path: Path, name: str, branch_id=None):
    errors = []
    workflow = state.setdefault("workflow", {})
    checkpoints = workflow.setdefault("checkpoints", {})
    control = state.setdefault("run_control", {})
    if name == "blueprint":
        errors = blueprint_errors(state)
        if not errors:
            checkpoints["blueprint_gate"] = "pass"
            workflow["current_stage"] = "research"
            control["reentry_required"] = False
            control["reentry_reason"] = ""
            control["strategy_writing_allowed"] = False
            control["delivery_allowed"] = False
            workflow["reentry_check_completed"] = True
    elif name == "branch-exit":
        errors = done_branch_errors(state, branch_id, require_exit=False)
        if not branch_id:
            errors.append("--branch is required for gate branch-exit")
        if not errors:
            state_branch = branch_map(state)[branch_id]
            state_branch["branch_exit_gate"] = "pass"
            checkpoints["branch_exit_gate_last_branch"] = branch_id
            checkpoints["branch_exit_gate_status"] = "pass"
    elif name == "brand-baseline":
        errors = []
        if checkpoints.get("blueprint_gate") != "pass":
            errors.append("brand baseline gate requires the Blueprint Gate to pass first")
        baseline_ids = included_branch_ids_for_families(state, BASELINE_FAMILIES)
        if not baseline_ids:
            errors.append("brand baseline gate has no included official/social/native branches")
        for baseline_id in baseline_ids:
            errors.extend(done_branch_errors(state, baseline_id))
        if not errors:
            checkpoints["brand_baseline_gate"] = "pass"
            workflow["current_stage"] = "research"
    elif name == "pre-convergence":
        errors = pre_convergence_errors(state)
        if not errors:
            checkpoints["pre_convergence_completeness_gate"] = "pass"
            workflow["current_stage"] = "belief_audit"
            control["strategy_writing_allowed"] = True
            control["delivery_allowed"] = False
    elif name == "pre-delivery":
        errors = pre_delivery_errors(state)
        if not errors:
            checkpoints["pre_delivery_gate"] = "pass"
            workflow["current_stage"] = "delivery"
            control["delivery_allowed"] = True
    else:
        errors = [f"unknown gate: {name}"]
    if errors:
        return result(False, errors, gate=name)
    workflow["last_reconciled_at"] = now()
    save_state(path, state)
    return result(True, [], True, gate=name, current_stage=workflow.get("current_stage"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create a fresh run-state")
    init.add_argument("--state", required=True, type=Path)
    init.add_argument("--project", required=True)
    init.add_argument("--decision", required=True)
    init.add_argument("--risk", required=True, choices=("reversible", "costly_reversible", "hard_to_reverse"))
    init.add_argument("--success-signal", required=True)
    init.add_argument("--observation-window", required=True)
    init.add_argument("--mode", required=True, choices=("Light", "Standard", "Deep"))
    init.add_argument("--task-type", default="general", choices=("general", "social_research", "social_content_strategy"))
    init.add_argument("--owner", default="agent")
    init.add_argument("--exclude", action="append", help="FAMILY=REASON; repeatable")

    state_arg = sub.add_parser("gate", help="validate and record a workflow gate")
    state_arg.add_argument("--state", required=True, type=Path)
    state_arg.add_argument("--gate", required=True, choices=("blueprint", "branch-exit", "brand-baseline", "pre-convergence", "pre-delivery"))
    state_arg.add_argument("--branch")

    approve = sub.add_parser("approve", help="acknowledge blueprint review after inspecting the ledger")
    approve.add_argument("--state", required=True, type=Path)
    approve.add_argument("--what", required=True, choices=("blueprint",))

    reentry = sub.add_parser("reentry", help="mark a user/scope update that requires reconciliation")
    reentry.add_argument("--state", required=True, type=Path)
    reentry.add_argument("--reason", required=True)

    assertion = sub.add_parser("assert", help="fail if an action is not currently allowed")
    assertion.add_argument("--state", required=True, type=Path)
    assertion.add_argument("--action", required=True, choices=("research", "parallel-research", "ai", "strategy", "calendar", "delivery"))

    status = sub.add_parser("status", help="show compact state and missing gates")
    status.add_argument("--state", required=True, type=Path)

    audit = sub.add_parser("audit", help="show omissions, pending work, active jobs, and safe parallel opportunities")
    audit.add_argument("--state", required=True, type=Path)

    args = parser.parse_args()
    try:
        if args.command == "init":
            if args.state.exists():
                return result(False, [f"refusing to overwrite existing state: {args.state}"])
            save_state(args.state, base_state(args, args.state))
            return result(True, [], True, action="init", state=str(args.state), next="fill TODO fields, run approve, then gate blueprint")

        state = load_state(args.state)
        if args.command == "gate":
            return gate(state, args.state, args.gate, args.branch)
        if args.command == "approve":
            control = state.setdefault("run_control", {})
            control["blueprint_reviewed"] = True
            control["reentry_check_completed"] = True
            state.setdefault("workflow", {})["last_reconciled_at"] = now()
            save_state(args.state, state)
            return result(True, [], True, action="approve", what=args.what)
        if args.command == "reentry":
            workflow = state.setdefault("workflow", {})
            control = state.setdefault("run_control", {})
            control["reentry_required"] = True
            control["reentry_reason"] = args.reason
            control["blueprint_reviewed"] = False
            control["strategy_writing_allowed"] = False
            control["delivery_allowed"] = False
            control["revision"] = int(control.get("revision") or 0) + 1
            for branch in state.get("branches", []):
                if branch.get("included") is not False:
                    branch["status"] = "waiting"
                    branch["branch_exit_gate"] = "pending"
                    changed = branch.setdefault("changed_branches_or_beliefs", [])
                    marker = f"reentry revision {control['revision']} requires branch revalidation"
                    if marker not in changed:
                        changed.append(marker)
            workflow["reentry_check_completed"] = False
            workflow["current_stage"] = "scope"
            workflow.setdefault("checkpoints", {}).update({
                "blueprint_gate": "pending", "brand_baseline_gate": "pending", "branch_exit_gate_status": "pending",
                "pre_convergence_completeness_gate": "pending", "pre_delivery_gate": "pending",
            })
            workflow["last_reconciled_at"] = now()
            save_state(args.state, state)
            return result(True, [], True, action="reentry", revision=control["revision"])
        if args.command == "assert":
            control = state.get("run_control") or {}
            errors = []
            if control.get("reentry_required"):
                errors.append("reentry is required before this action")
            checkpoints = (state.get("workflow") or {}).get("checkpoints", {})
            if args.action == "research" and checkpoints.get("blueprint_gate") != "pass":
                errors.append("research is blocked until the Blueprint Gate passes")
            elif args.action == "parallel-research":
                if checkpoints.get("blueprint_gate") != "pass":
                    errors.append("parallel research is blocked until the Blueprint Gate passes")
                if checkpoints.get("brand_baseline_gate") != "pass":
                    errors.append("parallel research is blocked until the brand baseline gate passes")
                group = next((item for item in (state.get("parallelism") or {}).get("groups", []) if item.get("mode") == "parallel_after_gate"), None)
                subtasks = [item for item in (group or {}).get("subtasks", []) if item.get("branch_ids")]
                if len(subtasks) < 2:
                    errors.append("parallel research needs at least two independent subtasks")
                if (state.get("parallelism") or {}).get("host_concurrency_available") and any(not item.get("task_space_ids") for item in subtasks):
                    errors.append("parallel research needs one stable EGO task-space ID per subtask")
            elif args.action == "ai":
                ai = state.get("ai_value_gate") or {}
                browser = state.get("browser_capability_gate") or {}
                if checkpoints.get("blueprint_gate") != "pass":
                    errors.append("AI research is blocked until the Blueprint Gate passes")
                if checkpoints.get("brand_baseline_gate") != "pass":
                    errors.append("AI research is blocked until the brand baseline gate passes")
                if ai.get("entry_path") not in {"ego_browser", "api_connector", "open_web_only"}:
                    errors.append("AI research needs a recorded entry_path")
                if not ai.get("entry_path_verified"):
                    errors.append("AI research needs a live entry-path/editor probe")
                if ai.get("entry_path") == "ego_browser" and browser.get("result") not in {"pass", "degraded"}:
                    errors.append("EGO AI research needs a PASS or defensible DEGRADED browser capability gate")
            elif args.action == "calendar":
                errors.extend(calendar_errors(state))
            else:
                allowed = control.get("strategy_writing_allowed") if args.action == "strategy" else control.get("delivery_allowed")
                if not allowed:
                    errors.append(f"{args.action} is blocked until its workflow gate passes")
            return result(not errors, errors, gate="assert", action=args.action)
        if args.command == "status":
            workflow = state.get("workflow") or {}
            control = state.get("run_control") or {}
            return result(True, [], False, stage=workflow.get("current_stage"), checkpoints=workflow.get("checkpoints", {}), run_control=control, missing_branch_families=sorted(set(FAMILIES) - set(included_families(state)) - {item.get("family") for item in state.get("branch_inventory", []) if item.get("disposition") in DISPOSITIONS}))
        if args.command == "audit":
            audit_result = audit_state(state)
            return result(not audit_result["critical_errors"], audit_result.pop("critical_errors"), False, **audit_result)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return result(False, [str(exc)])


if __name__ == "__main__":
    sys.exit(main())
