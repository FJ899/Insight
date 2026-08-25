#!/usr/bin/env python3
"""Mechanical integrity checks for Insight.

This checker enforces only repository properties that can actually be proven.
Open methodological/evidence limitations remain visible warnings rather than being
silently converted into PASS.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_FILES = (
    "START.md",
    "STATUS.md",
    "TODO.md",
    "OPERATING_PROTOCOL.md",
    "control/frozen_artifacts.json",
    "control/known_limitations.json",
    "experiments/ARX-001/STATUS.md",
    "experiments/ARX-001/REGISTRY.md",
    "experiments/HOT-001/STATUS.md",
    "experiments/HOT-001/HOT-001_PROTOCOL_v1.0.md",
    "experiments/HOT-001/HOT-001_PROTOCOL_v1.1.md",
    "schemas/START_RECORD_v1.md",
    "schemas/START_RECORD_v1.1.md",
)

HOT_BPM160_CHAIN = (
    "experiments/HOT-001/HOT-001_PROTOCOL_v1.0.md",
    "experiments/HOT-001/START_RECORDS/HOT-001-BPM160-01_FROZEN.md",
    "experiments/HOT-001/RUN_INPUTS/HOT-001-BPM160-01_PRIMARY_PROMPT.md",
    "experiments/HOT-001/RAW/HOT-001-BPM160-01_PRIMARY_TRANSCRIPT_RAW.md",
    "experiments/HOT-001/EVALUATIONS/HOT-001-BPM160-01_PRE_SEMANTIC_EVALUATION.md",
    "experiments/HOT-001/DECISIONS/HOT-001-BPM160-01_HUMAN_SEMANTIC_DECISION.md",
    "experiments/HOT-001/RESULTS/HOT-001-BPM160-01_FINAL_RECONCILIATION.md",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def check_required_files(root: Path) -> Iterable[Finding]:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            yield Finding("ERROR", "STRUCTURE_MISSING", f"missing required file: {relative}")


def check_frozen_artifacts(root: Path) -> Iterable[Finding]:
    manifest_path = root / "control/frozen_artifacts.json"
    if not manifest_path.is_file():
        return
    payload = load_json(manifest_path)
    if not isinstance(payload, dict) or payload.get("version") != 1:
        yield Finding("ERROR", "FROZEN_MANIFEST_FORMAT", "frozen_artifacts.json must have version=1")
        return
    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        yield Finding("ERROR", "FROZEN_MANIFEST_EMPTY", "frozen artifact manifest has no artifacts")
        return

    seen: set[str] = set()
    for item in artifacts:
        if not isinstance(item, dict):
            yield Finding("ERROR", "FROZEN_ENTRY_FORMAT", "frozen artifact entry is not an object")
            continue
        relative = item.get("path")
        expected = item.get("git_blob_sha1")
        if not isinstance(relative, str) or not isinstance(expected, str):
            yield Finding("ERROR", "FROZEN_ENTRY_FORMAT", "entry requires path and git_blob_sha1")
            continue
        if relative in seen:
            yield Finding("ERROR", "FROZEN_DUPLICATE", f"duplicate frozen artifact: {relative}")
            continue
        seen.add(relative)
        path = root / relative
        if not path.is_file():
            yield Finding("ERROR", "FROZEN_MISSING", f"frozen artifact missing: {relative}")
            continue
        actual = git_blob_sha1(path.read_bytes())
        if actual != expected:
            yield Finding("ERROR", "FROZEN_DRIFT", f"{relative} expected={expected} actual={actual}")

    for relative in HOT_BPM160_CHAIN:
        if relative not in seen:
            yield Finding("ERROR", "FROZEN_CHAIN_UNPINNED", f"BPM160 evidence artifact not pinned: {relative}")


def check_known_limitations(root: Path) -> Iterable[Finding]:
    path = root / "control/known_limitations.json"
    if not path.is_file():
        return
    payload = load_json(path)
    if not isinstance(payload, dict) or payload.get("version") != 1:
        yield Finding("ERROR", "LIMITATIONS_FORMAT", "known_limitations.json must have version=1")
        return
    items = payload.get("limitations")
    if not isinstance(items, list):
        yield Finding("ERROR", "LIMITATIONS_FORMAT", "limitations must be a list")
        return

    status_text = (root / "STATUS.md").read_text(encoding="utf-8") if (root / "STATUS.md").is_file() else ""
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            yield Finding("ERROR", "LIMITATION_ENTRY_FORMAT", "limitation entry is not an object")
            continue
        lim_id = item.get("id")
        state = item.get("state")
        summary = item.get("summary")
        if not all(isinstance(v, str) and v for v in (lim_id, state, summary)):
            yield Finding("ERROR", "LIMITATION_ENTRY_FORMAT", "entry requires id, state, summary")
            continue
        if lim_id in seen:
            yield Finding("ERROR", "LIMITATION_DUPLICATE", f"duplicate limitation id: {lim_id}")
            continue
        seen.add(lim_id)
        if state not in {"OPEN", "MITIGATED", "CLOSED"}:
            yield Finding("ERROR", "LIMITATION_STATE", f"invalid state for {lim_id}: {state}")
        if state == "OPEN":
            yield Finding("WARN", lim_id, summary)
        if lim_id not in status_text:
            yield Finding("ERROR", "LIMITATION_NOT_SURFACED", f"STATUS.md does not surface {lim_id}")


def check_hot_run_consistency(root: Path) -> Iterable[Finding]:
    run_id = "HOT-001-BPM160-01"
    for relative in HOT_BPM160_CHAIN[1:]:
        path = root / relative
        if not path.is_file() or relative.endswith("PRIMARY_PROMPT.md"):
            continue
        if run_id not in path.read_text(encoding="utf-8"):
            yield Finding("ERROR", "RUN_ID_MISMATCH", f"{relative} lacks RUN_ID {run_id}")

    hot_status = root / "experiments/HOT-001/STATUS.md"
    if hot_status.is_file():
        text = hot_status.read_text(encoding="utf-8")
        for relative in HOT_BPM160_CHAIN[1:]:
            local_name = Path(relative).name
            if local_name not in text and "PRIMARY_PROMPT" not in local_name:
                yield Finding("ERROR", "STATUS_CHAIN_GAP", f"HOT status does not name {local_name}")


def check_protocol_v11_guards(root: Path) -> Iterable[Finding]:
    protocol = root / "experiments/HOT-001/HOT-001_PROTOCOL_v1.1.md"
    if not protocol.is_file():
        return
    text = protocol.read_text(encoding="utf-8")
    for phrase in (
        "PRIMARY PROMPT HYGIENE",
        "must not contain HOT methodology",
        "native platform export",
        "interaction shape",
        "NOT FROZEN",
    ):
        if phrase not in text:
            yield Finding("ERROR", "V11_GUARD_MISSING", f"v1.1 missing guard: {phrase}")


def run_checks(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for checker in (
        check_required_files,
        check_frozen_artifacts,
        check_known_limitations,
        check_hot_run_consistency,
        check_protocol_v11_guards,
    ):
        findings.extend(checker(root))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Insight repository integrity and evidence debt.")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--strict-warnings", action="store_true", help="treat OPEN limitations as failures")
    args = parser.parse_args(argv)

    findings = run_checks(Path(args.root).resolve())
    for finding in findings:
        print(f"{finding.severity} {finding.code}: {finding.message}")
    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARN" for f in findings)
    print(f"SUMMARY errors={errors} warnings={warnings}")
    return 1 if errors or (args.strict_warnings and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
