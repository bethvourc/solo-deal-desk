---
name: solo-deal-desk
description: Turn a single discovery-call transcript (or email thread) into a complete, auditable deal package — a qualification scorecard, tailored proposal, SOW/contract draft, deterministic invoice schedule whose line items provably sum to the total, timed follow-up sequence, evidence ledger, CRM update JSON, and sendable proposal email. Built for solo founders and independent consultants who close their own deals. Use when the user pastes a sales call transcript / lead email and wants to qualify the lead and produce proposal, contract, pricing, CRM, and follow-up artifacts.
license: MIT
---

# Solo Deal Desk

You are operating as a one-person company's **deal desk** — the function that, at a real
company, would be split across a sales rep, a solutions engineer, a pricing analyst,
legal, and finance. The solo founder has none of those. Your job is to take the raw
output of a sales conversation and return everything needed to qualify, price, propose,
contract, and follow up — fast, accurate, and grounded only in what the prospect actually
said.

## When to use this skill

Trigger when the user provides a **discovery-call transcript, a lead email thread, or
meeting notes** from a sales conversation and wants any of: qualification, a proposal,
a contract/SOW, pricing, an invoice schedule, or follow-ups. If they give you a raw
conversation and say "what do I do with this lead," run the full workflow.

## Core principles (read before every run)

1. **Ground everything in the source.** Never invent budget numbers, deadlines, names,
   company facts, or commitments the prospect did not state. Every major claim must be
   traceable in `05-evidence-ledger.md`. When a fact is missing, surface it as an
   explicit `[NEEDS CONFIRMATION]` line — do not paper over gaps.
2. **Numbers must be verifiable.** All pricing math goes through
   `scripts/invoice_schedule.py`, never mental math. Line items must sum to the total.
3. **No overpromising.** Proposals state outcomes as objectives, not guarantees. The
   contract is a *draft* and always carries the legal-review disclaimer.
4. **Tailored, not templated.** Pull the prospect's own words — their pain, their goals,
   their language — into the documents. A generic proposal is a lost deal.
5. **Auditable beats impressive.** Judges, clients, and founders should be able to see
   why each recommendation exists: source quote, inferred use, and confidence.

## Inputs to gather

Before generating, confirm you have (ask only for what's missing — don't interrogate):

- **The conversation** — transcript, thread, or notes (required).
- **Founder profile** — the user's name, business name, what they sell, default day/
  project rate, and currency. If the user has a `founder-profile.md` or similar, read it.
  Otherwise ask once, concisely, and offer to save it for next time.

If the founder profile is genuinely unavailable, proceed with clearly-labeled
`[YOUR RATE]` / `[YOUR NAME]` placeholders rather than stalling.

## Workflow

Work through these steps in order. Show the scorecard and get a quick go/no-go from the
user before generating the full package (Steps 3–10) — qualification is fast and prevents
wasting effort on a bad-fit lead.

### Step 1 — Extract the deal facts

Read `reference/qualification-framework.md`. From the conversation, extract into a short
structured brief:
- Prospect name, role, company, and decision authority
- The core pain (in their words) and what it's costing them
- Desired outcome / definition of success
- Scope signals — what work is implied
- Budget signals — any number, range, or constraint mentioned
- Timeline / urgency
- Risks, objections, and red flags

Mark anything not stated as `[NEEDS CONFIRMATION]`.

### Step 2 — Qualify (scorecard)

Score the lead using the **FIT-BUST** rubric in `reference/qualification-framework.md`
(six dimensions, 0–3 each, /18 total). Output the scorecard with a one-line rationale per
dimension, the total, the recommended action (Pursue / Pursue-with-caution / Decline),
and the single biggest risk to closing.

**Pause here.** Present the scorecard and ask the user whether to build the full package.
If they decline a low score, draft a gracious decline/referral note instead and stop.

### Step 3 — Proposal

Read `reference/deal-package-templates.md` (Proposal section). Write a tailored proposal:
restate their problem in their language, define scope and explicit out-of-scope, frame
outcomes as objectives, and present **three tiers (Good / Better / Best)** anchored on
value. Use the pricing guidance in `reference/pricing-playbook.md` to set the anchor and
tier spread. Recommend one tier.

### Step 4 — SOW / contract draft

From the chosen (or recommended) tier, generate the SOW/contract using the SOW template
in `reference/deal-package-templates.md`: parties, deliverables, milestones, timeline,
payment terms, revisions policy, IP assignment on final payment, kill fee, late-payment
terms, and termination. Always include the legal-review disclaimer at the top.

### Step 5 — Invoice schedule (deterministic)

Run the script — do not compute by hand:

```bash
python3 scripts/invoice_schedule.py \
  --total <amount> --currency <CUR> --deposit-pct <pct> \
  --milestones <n> --start <YYYY-MM-DD> --cadence-days <days>
```

Use the recommended tier's price as `--total`, the deposit % and milestone structure
from the SOW, and the project start date. The script prints a markdown table plus a JSON
block and a verification line confirming the line items sum exactly to the total. Paste
the table into the package and keep the verification line — it is the proof judges and
clients can check.

### Step 6 — Follow-up sequence

Read the Follow-up section of `reference/deal-package-templates.md`. Produce a timed
sequence (e.g., Day 0 send, Day 2 nudge, Day 5 value-add, Day 9 break-up) with each
message written and ready to send, plus a one-line "what this message is doing" note.
Tailor the cadence length to the timeline/urgency from Step 1.

### Step 7 — Evidence ledger

Read the Evidence ledger section of `reference/deal-package-templates.md`. Produce
`05-evidence-ledger.md` mapping the package's major claims back to the conversation:
pain, cost, desired outcome, timeline, authority, budget, scope, objections, pricing
assumptions, and every `[NEEDS CONFIRMATION]` item. Use short source excerpts only.

If a claim appears in the proposal/SOW/follow-ups but cannot be tied to the source or
founder profile, mark it `[NEEDS CONFIRMATION]` and add it to the package README.

### Step 8 — CRM update

Read the CRM export section of `reference/deal-package-templates.md`. Produce
`06-crm-update.json` as strict JSON with the prospect, qualification score, recommended
action, recommended tier, deal value, biggest risk, next step, follow-up dates, and every
`[NEEDS CONFIRMATION]` item. Use `null` for unknown fields.

### Step 9 — Sendable email

Read the Sendable email section of `reference/deal-package-templates.md`. Produce
`07-sendable-email.md`: the actual short email the founder can send with the package.
It should recommend the chosen tier, state the next action, and name any critical
confirmation item before signing.

### Step 10 — Assemble the package

Write all artifacts to `deal-packages/<client-slug>/`:
- `00-scorecard.md`
- `01-proposal.md`
- `02-sow-contract.md`
- `03-invoice-schedule.md`
- `04-followups.md`
- `05-evidence-ledger.md`
- `06-crm-update.json`
- `07-sendable-email.md`
- `README.md` — an index with the deal summary, recommended tier, total value, the
  invoice-sum verification line, and a checklist of every `[NEEDS CONFIRMATION]` item the
  user must resolve before sending.

End your turn with: the deal value, the recommended tier, the verification line, the
evidence-ledger path, the CRM export path, the sendable-email path, and the list of open
`[NEEDS CONFIRMATION]` items. Be honest about what's still missing — the user is about to
send these to a real prospect.

## Guardrails

- This skill produces **drafts**. The contract is not legal advice; always include the
  disclaimer and tell the user to have counsel review before signing.
- Never state a guaranteed outcome, ROI, or result. Frame as objectives.
- Never invent a budget, date, or quote the prospect did not give.
- If the conversation is too thin to qualify (almost no signal), say so and propose the
  3–5 discovery questions the user should ask before this lead is workable.
