#!/usr/bin/env python3
"""Solo Deal Desk — deterministic invoice schedule generator.

Produces a payment schedule whose line items ALWAYS sum exactly to the total
(rounding remainder is absorbed into the final milestone). Pure Python 3.8+
standard library — no third-party dependencies, so it runs on any installer's
machine on day one.

Example:
    python3 invoice_schedule.py --total 12000 --currency USD \\
        --deposit-pct 30 --milestones 3 --start 2026-06-22 --cadence-days 14
"""
import argparse
import datetime
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENTS = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to 2 decimal places, half-up."""
    return Decimal(value).quantize(CENTS, rounding=ROUND_HALF_UP)


def build_schedule(total, deposit_pct, milestones, start, cadence_days):
    total = money(total)
    deposit = money(total * Decimal(deposit_pct) / Decimal(100))
    remaining = total - deposit

    items = []
    if deposit > 0:
        items.append({
            "label": "Deposit (due on signing)",
            "date": start.isoformat(),
            "amount": deposit,
        })

    if milestones > 0:
        per = money(remaining / Decimal(milestones))
        # Final milestone absorbs any rounding remainder so the sum is exact.
        last = remaining - per * (milestones - 1)
        date = start
        for i in range(1, milestones + 1):
            date = date + datetime.timedelta(days=cadence_days)
            amount = per if i < milestones else last
            items.append({
                "label": f"Milestone {i}",
                "date": date.isoformat(),
                "amount": amount,
            })

    return total, items


def render_markdown(currency, total, items):
    lines = []
    lines.append(f"| # | Invoice | Due date | Amount ({currency}) |")
    lines.append("|---|---------|----------|--------------------:|")
    for idx, it in enumerate(items, 1):
        lines.append(f"| {idx} | {it['label']} | {it['date']} | {it['amount']:,} |")
    total_items = sum((it["amount"] for it in items), Decimal("0"))
    lines.append(f"| | **Total** | | **{total_items:,}** |")
    ok = total_items == total
    check = "✓ matches contract total" if ok else "✗ MISMATCH"
    lines.append("")
    lines.append(
        f"_Verification: line items sum to {currency} {total_items:,} "
        f"vs. contract total {currency} {total:,} — {check}._"
    )
    return "\n".join(lines), ok


def main(argv=None):
    p = argparse.ArgumentParser(description="Deterministic invoice schedule generator.")
    p.add_argument("--total", required=True, help="Total contract value, e.g. 12000")
    p.add_argument("--currency", default="USD")
    p.add_argument("--deposit-pct", type=Decimal, default=Decimal("30"),
                   help="Deposit as a percent of total (default 30). Use 0 for none.")
    p.add_argument("--milestones", type=int, default=3,
                   help="Number of post-deposit milestone invoices (default 3).")
    p.add_argument("--start", default=datetime.date.today().isoformat(),
                   help="Project start / signing date, YYYY-MM-DD (default today).")
    p.add_argument("--cadence-days", type=int, default=14,
                   help="Days between milestone invoices (default 14).")
    p.add_argument("--json", action="store_true", help="Print JSON only.")
    args = p.parse_args(argv)

    try:
        start = datetime.date.fromisoformat(args.start)
    except ValueError:
        p.error(f"--start must be YYYY-MM-DD, got {args.start!r}")
    if not (0 <= args.deposit_pct <= 100):
        p.error("--deposit-pct must be between 0 and 100")
    if args.milestones < 0:
        p.error("--milestones must be >= 0")
    try:
        total, items = build_schedule(
            args.total, args.deposit_pct, args.milestones, start, args.cadence_days
        )
    except (InvalidOperation, ValueError):
        p.error(f"--total must be a number, got {args.total!r}")

    payload = {
        "currency": args.currency,
        "total": str(total),
        "items": [
            {"label": it["label"], "date": it["date"], "amount": str(it["amount"])}
            for it in items
        ],
        "sum_matches_total": sum((it["amount"] for it in items), Decimal("0")) == total,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0 if payload["sum_matches_total"] else 1

    table, ok = render_markdown(args.currency, total, items)
    print(table)
    print()
    print("```json")
    print(json.dumps(payload, indent=2))
    print("```")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
