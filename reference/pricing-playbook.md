# Pricing Playbook

The solo founder's pricing failure mode is anchoring on cost ("my time × rate") instead
of value ("what is solving this worth to them"). This playbook sets the anchor and the
tier spread.

## 1. Anchor on value, sanity-check on cost

- **Value anchor:** what is the prospect's pain costing them, from the transcript? Lost
  revenue, wasted hours, stalled launch, risk. Price as a fraction of that cost.
- **Cost floor:** estimate effort honestly (days × the founder's rate), then add a buffer
  for revisions and coordination. Never quote below this floor.
- If you have no value signal, price off the cost floor and label the value assumptions
  as `[NEEDS CONFIRMATION]`.

## 2. Always present three tiers (Good / Better / Best)

Three options out-convert one because they reframe the decision from "yes/no" to "which."

| Tier | Purpose | Construct it as |
|------|---------|-----------------|
| **Good** | The walk-away floor; makes Better look reasonable | Core deliverable only, longer timeline, minimal revisions |
| **Better** ⭐ | The one you recommend; where most should land | Core + the 1–2 things they actually need, sensible timeline |
| **Best** | The anchor; raises the ceiling and the average | Better + speed, extra scope, ongoing support/retainer |

- Spread the tiers roughly **1× / 1.6× / 2.5×** off the Good price unless transcript
  signals say otherwise. The Best tier's job is partly to make Better feel safe.
- Recommend **Better** explicitly. Don't make the prospect guess.

## 3. Payment structure defaults

- **Deposit: 30–50%** due on signing. Non-refundable to cover commitment. A solo founder
  who starts work before the deposit clears is financing the client's project.
- **Milestones:** split the remainder across 2–4 milestones tied to deliverables, not
  just dates. Default cadence 14 days.
- **Net terms:** Net 7 or Net 14. Avoid Net 30+ as a solo — it's an interest-free loan.
- **Late fee:** 1.5%/month on overdue balances; state it in the SOW so it's enforceable.
- **Kill fee:** if the client cancels mid-project, deposit is retained + payment for work
  completed to date. Protects you from being left holding sunk effort.
- **IP transfer on final payment**, not before. Leverage until you're paid in full.

## 4. Discounting

- Don't discount price; **reduce scope** instead (move them from Better to Good). This
  protects your rate and trains the client that your price reflects value.
- If you must discount to close, trade it for something: faster payment terms, a
  testimonial/case study, a referral, or a longer commitment.

## 5. Run the numbers, don't guess them

Once the tier and structure are chosen, the invoice schedule is produced **only** by
`scripts/invoice_schedule.py`. The script guarantees the line items sum to the total —
that arithmetic guarantee is part of what makes this skill's output trustworthy.
