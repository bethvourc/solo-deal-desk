#!/usr/bin/env python3
"""Smoke-check the Solo Deal Desk demo package.

Validates the hackathon demo artifacts without third-party dependencies:
- required files exist
- Acme CRM JSON is valid
- invoice schedule command succeeds and confirms exact totals
- stale dates from the old demo timeline are gone
"""
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACME = ROOT / "examples" / "deal-packages" / "acme-onboarding"
BRIGHTCART = ROOT / "examples" / "deal-packages" / "brightcart-analytics-decline"


REQUIRED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "submission-summary.md",
    ROOT / "founder-profile.example.md",
    ROOT / "examples" / "run-demo.md",
    ROOT / "examples" / "sample-discovery-call.md",
    ROOT / "examples" / "bad-fit-discovery-call.md",
    ACME / "00-scorecard.md",
    ACME / "01-proposal.md",
    ACME / "02-sow-contract.md",
    ACME / "03-invoice-schedule.md",
    ACME / "04-followups.md",
    ACME / "05-evidence-ledger.md",
    ACME / "06-crm-update.json",
    ACME / "07-sendable-email.md",
    ACME / "README.md",
    BRIGHTCART / "00-scorecard.md",
    BRIGHTCART / "README.md",
]


def fail(message):
    print(f"FAIL: {message}")
    return 1


def check_required_files():
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))
    print("PASS: required files exist")
    return 0


def check_crm_json():
    path = ACME / "06-crm-update.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"CRM JSON is invalid: {exc}")

    checks = [
        payload["deal"]["score"] == 17,
        payload["deal"]["deal_value"] == 14000,
        payload["deal"]["currency"] == "USD",
        len(payload["follow_ups"]) == 4,
        len(payload["needs_confirmation"]) == 3,
    ]
    if not all(checks):
        return fail("CRM JSON parsed but expected demo values did not match")
    print("PASS: CRM JSON is valid and matches expected demo values")
    return 0


def check_invoice_math():
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "invoice_schedule.py"),
        "--total",
        "14000",
        "--currency",
        "USD",
        "--deposit-pct",
        "40",
        "--milestones",
        "3",
        "--start",
        "2026-06-24",
        "--cadence-days",
        "7",
    ]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        return fail("invoice_schedule.py failed: " + result.stderr.strip())
    expected = "line items sum to USD 14,000.00 vs. contract total USD 14,000.00"
    if expected not in result.stdout:
        return fail("invoice verification line was not found")
    print("PASS: invoice schedule verifies exact total")
    return 0


def check_stale_dates():
    stale = ["2026-06-29", "2026-07-29", "June 29", "July 29"]
    hits = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json", ".py"}:
            continue
        if path == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for token in stale:
            if token in text:
                hits.append(f"{path.relative_to(ROOT)} contains {token}")
    if hits:
        return fail("stale demo timeline found: " + "; ".join(hits))
    print("PASS: no stale demo dates found")
    return 0


def check_package_text():
    checks = [
        (ACME / "README.md", "05-evidence-ledger.md"),
        (ACME / "README.md", "06-crm-update.json"),
        (ACME / "README.md", "07-sendable-email.md"),
        (ROOT / "SKILL.md", "06-crm-update.json"),
        (ROOT / "SKILL.md", "07-sendable-email.md"),
        (ROOT / "examples" / "run-demo.md", "python3 scripts/demo_check.py"),
        (ROOT / "submission-summary.md", "solo revenue desk"),
    ]
    for path, needle in checks:
        if needle not in path.read_text(encoding="utf-8"):
            return fail(f"{path.relative_to(ROOT)} missing expected text: {needle}")
    print("PASS: package text references new artifacts")
    return 0


def main():
    checks = [
        check_required_files,
        check_crm_json,
        check_invoice_math,
        check_stale_dates,
        check_package_text,
    ]
    failures = sum(check() for check in checks)
    if failures:
        print(f"\n{failures} check(s) failed.")
        return 1
    print("\nAll Solo Deal Desk demo checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
