# Solo Deal Desk — submission summary

## Problem

Solo founders lose warm deals in the hours after a discovery call. A larger company has
sales, solutions, pricing, legal, finance, and CRM operations. A one-person company has one
person trying to qualify, price, propose, contract, invoice, follow up, and update the
pipeline before momentum dies.

## What the skill does

Solo Deal Desk turns one sales-call transcript or lead email thread into an auditable deal
package:

- FIT-BUST qualification scorecard with a pursue/caution/decline recommendation.
- Tailored proposal with Good / Better / Best tiers.
- SOW/contract draft with payment terms and legal-review disclaimer.
- Deterministic invoice schedule whose line items sum exactly to the contract total.
- Follow-up sequence, CRM update JSON, and sendable proposal email.
- Evidence ledger mapping major claims back to the source conversation.

## Why it is different

This is not just a proposal writer. It is a solo revenue desk:

- It stops bad leads before they consume unpaid founder time.
- It refuses to invent facts and flags missing deal data as `[NEEDS CONFIRMATION]`.
- It makes pricing math verifiable with a zero-dependency script.
- It creates workflow artifacts a founder can actually use: CRM JSON and sendable email.
- It gives judges and clients an evidence ledger showing where each claim came from.

## Demo path

1. Run the Acme example from `examples/sample-discovery-call.md`.
2. Show the scorecard pause: 17 / 18, Pursue, budget is the biggest risk.
3. Continue to the full package and show the proposal, invoice schedule, evidence ledger,
   CRM JSON, and sendable email.
4. Run `python3 scripts/demo_check.py`.
5. Optionally show `examples/bad-fit-discovery-call.md` to demonstrate the decline path.

## Verifiable proof

For the Acme example:

- Recommended tier: Better
- Deal value: USD 14,000
- Core handoff: 2026-07-15
- Invoice verification: line items sum to USD 14,000.00 vs. contract total USD 14,000.00
- Open confirmations: exact budget, training audience, reusable Notion checklist
