# Solo Deal Desk live demo

Use this script when showing the skill to judges or a new installer.

## 1. Start from the sample call

Prompt the agent:

> Run Solo Deal Desk on `examples/sample-discovery-call.md`. Use
> `founder-profile.example.md` as the founder profile for this demo.

## 2. Show the qualification pause

Expected first output:

- Prospect: Jordan Lee, Head of Operations, Acme Tools
- FIT-BUST score: 17 / 18
- Recommendation: Pursue
- Biggest risk: exact budget is not confirmed

Tell the agent:

> Go ahead and build the full package.

## 3. Show the generated package

Expected files:

- `00-scorecard.md`
- `01-proposal.md`
- `02-sow-contract.md`
- `03-invoice-schedule.md`
- `04-followups.md`
- `05-evidence-ledger.md`
- `06-crm-update.json`
- `07-sendable-email.md`
- `README.md`

Expected demo outcome:

- Recommended tier: Better
- Deal value: USD 14,000
- Core handoff: 2026-07-15, before the mid-July Q3 account wave
- Open confirmations: exact budget, training audience, reuse of existing Notion checklist

## 4. Verify the invoice math live

From the skill directory, run:

```bash
python3 scripts/invoice_schedule.py --total 14000 --currency USD \
  --deposit-pct 40 --milestones 3 --start 2026-06-24 --cadence-days 7
```

Expected verification:

`_Verification: line items sum to USD 14,000.00 vs. contract total USD 14,000.00 — ✓ matches contract total._`

## 5. Show the differentiator

Open `05-evidence-ledger.md` and point to:

- Pain and cost are quoted from the transcript.
- Timeline and authority are quoted from the transcript.
- Budget is correctly marked as a partial signal, not invented.
- Pricing rationale is separated from source evidence.

The demo message: Solo Deal Desk is not just writing a proposal. It is turning a warm
sales conversation into an auditable revenue package a solo founder can send quickly.

## 6. Run the smoke check

```bash
python3 scripts/demo_check.py
```

Expected result: all checks pass, including required artifact presence, invoice math,
CRM JSON validity, and stale-date detection.
