# Deal Package Templates

Fill these from the conversation. Bracketed `[…]` items are slots; `[NEEDS CONFIRMATION]`
marks anything the prospect did not state. Keep the prospect's own language wherever you
can — restating their pain in their words is the single highest-leverage move.

---

## Proposal template (`01-proposal.md`)

```
# Proposal: [Outcome-framed title, e.g. "Cut onboarding time in half"]
Prepared for [Prospect name], [Company] · by [Founder name], [Business]
[Date] · Valid for 14 days

## The problem we discussed
[2–4 sentences restating their pain in their words, with the cost they mentioned.]

## What success looks like
[Their definition of done, framed as objectives — never as a guaranteed result.]

## Scope
**Included**
- [Deliverable 1]
- [Deliverable 2]

**Not included** (available as add-ons)
- [Out-of-scope item — naming these prevents scope creep]

## Approach
[3–5 step plan in plain language. Show you understood the work.]

## Options
| | Good | Better ⭐ (recommended) | Best |
|--|------|------------------------|------|
| Scope | [...] | [...] | [...] |
| Timeline | [...] | [...] | [...] |
| Revisions | [...] | [...] | [...] |
| Investment | [CUR X] | [CUR Y] | [CUR Z] |

**Recommended: Better** — [one sentence on why it fits what they told you].

## Timeline
[Start → milestone → delivery, tied to their stated deadline.]

## Next step
[One clear CTA: "Reply 'Better' and I'll send the agreement + deposit invoice today."]
```

---

## SOW / Contract template (`02-sow-contract.md`)

```
> ⚠️ DRAFT — not legal advice. Have qualified counsel review before signing.

# Statement of Work & Services Agreement
Between **[Founder / Business]** ("Provider") and **[Prospect / Company]** ("Client").
Effective date: [Date]

## 1. Services & deliverables
[Itemized from the chosen tier. Specific and bounded.]

## 2. Timeline & milestones
| Milestone | Deliverable | Target date |
|-----------|-------------|-------------|
| M1 | [...] | [...] |

## 3. Fees & payment
- Total fee: **[CUR total]** (Tier: [Better]).
- Deposit: **[pct]%** due on signing; non-refundable.
- Remainder invoiced per the schedule in `03-invoice-schedule.md`.
- Terms: Net [7/14]. Late balances accrue **1.5%/month**.

## 4. Revisions
[N] rounds of revision per deliverable included. Additional revisions billed at
[CUR rate]/hr.

## 5. Intellectual property
All deliverable IP transfers to Client upon **receipt of final payment**. Provider
retains the right to display the work in a portfolio unless Client opts out in writing.

## 6. Cancellation / kill fee
If Client cancels, the deposit is retained and Client pays for all work completed to the
cancellation date.

## 7. Term & termination
Either party may terminate for material breach with [N] days' written notice and a chance
to cure. Earned fees remain payable.

## 8. Independent contractor
Provider is an independent contractor, not an employee. Provider is responsible for own
taxes.

## 9. Acceptance
Signatures + dates for both parties.
```

---

## Follow-up sequence template (`04-followups.md`)

Tune the spacing to the deal's urgency. Each message is short, send-ready, and does one
job. Stop the sequence the moment they reply.

```
### Day 0 — Send the proposal
Subject: [Company] — proposal + next step
[2–3 sentences. Attach/link the proposal. Restate the one outcome they care about. Clear
CTA to pick a tier.]
→ Doing: deliver the proposal, make saying yes a one-word reply.

### Day 2 — Soft nudge
Subject: Re: [Company] — quick question
[1–2 sentences. "Did the Better option look right, or should we adjust scope to fit the
timeline?" Offer a fork, not just a ping.]
→ Doing: surface objections, keep it a conversation.

### Day 5 — Value-add
Subject: thought you'd find this useful
[Share one specific, relevant insight / resource / mini-idea tied to their problem. No
ask.]
→ Doing: stay top-of-mind by giving, not chasing.

### Day 9 — Break-up
Subject: should I close this out?
[1–2 sentences. "Happy to revisit when the timing's right — want me to close the file for
now?" Permission-to-close paradoxically prompts replies.]
→ Doing: create gentle urgency and free your own pipeline.
```

---

## Evidence ledger template (`05-evidence-ledger.md`)

This is the audit trail for the whole package. Keep excerpts short and map each major
recommendation back to the conversation or founder profile. If the evidence is missing,
write `[NEEDS CONFIRMATION]` instead of filling the gap.

```
# Evidence ledger: [Company] deal package

## Source
- Conversation: [transcript / email thread name]
- Founder profile: [profile file or placeholders used]

## Claim map
| Package claim | Source evidence | Used in | Confidence |
|---------------|-----------------|---------|------------|
| [Pain] | "[short quote]" | Scorecard, proposal | High |
| [Cost / value signal] | "[short quote]" | Pricing, proposal | High/Medium |
| [Timeline] | "[short quote]" | Proposal, SOW, follow-ups | High |
| [Authority] | "[short quote]" | Scorecard | High |
| [Budget] | "[short quote or NEEDS CONFIRMATION]" | Pricing | Medium |
| [Scope] | "[short quote]" | Proposal, SOW | High |

## Assumptions and confirmation checklist
- [ ] [NEEDS CONFIRMATION] [unsupported fact or assumption]

## Pricing rationale
[2-4 bullets explaining how the tier recommendation uses the transcript evidence,
pricing playbook, and founder rate/cost floor. Do not invent ROI.]
```

---

## CRM export template (`06-crm-update.json`)

Create strict JSON that can be pasted into a CRM, spreadsheet, or automation tool. Use
ISO dates and numeric deal values. Use `null` for unknown facts, not invented values.

```json
{
  "prospect": {
    "name": "[Prospect name]",
    "role": "[Role or null]",
    "company": "[Company]"
  },
  "deal": {
    "status": "qualified|caution|declined",
    "score": 0,
    "score_max": 18,
    "recommended_action": "Pursue|Pursue with caution|Decline",
    "recommended_tier": "[Good|Better|Best|null]",
    "deal_value": 0,
    "currency": "[CUR]",
    "biggest_risk": "[Risk]"
  },
  "next_step": {
    "owner": "[Founder name]",
    "action": "[Next action]",
    "due_date": "[YYYY-MM-DD or null]"
  },
  "follow_ups": [
    {"day": 0, "date": "[YYYY-MM-DD]", "purpose": "send proposal"}
  ],
  "needs_confirmation": [
    "[Open item]"
  ]
}
```

---

## Sendable email template (`07-sendable-email.md`)

Write the actual email the founder can send with the package. Keep it short and specific.
Reference the recommended tier, the next step, and any critical confirmation item.

```
# Sendable email: [Company] proposal

**To:** [Prospect name / email if known]
**Subject:** [Company] — proposal + next step

Hi [Name],

[2–4 short paragraphs. Restate the business outcome, point to the attached proposal/SOW,
recommend the tier, and ask for one clear reply or decision.]

[Optional: One sentence naming the biggest item to confirm before signing.]

Best,
[Founder name]
```
