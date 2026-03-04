# China Employee Termination: Pulse Triage-Ward Brief for Foreign Employers (Hourly Testing Run)

- For foreign employers, China termination execution is safer when cases are managed like a triage ward: classify risk early, assign treatment owners, and block discharge until criteria are met.
- Most avoidable failures still occur when legal, HR, manager, and payroll teams treat symptoms separately instead of one integrated case flow.
- A triage-ward format helps non-local leadership see which cases are stable, which are deteriorating, and which require immediate intervention.
- Negotiated exits can reduce friction, but only when settlement terms, payroll treatment, and communication records remain clinically consistent across the case file.
- City-level implementation variance remains material; local validation should remain a mandatory discharge hold.

## Plain-language legal baseline (first)

China is not an at-will termination market. Employer-initiated termination should align with a lawful route under the Labor Contract Law framework and be executed with coherent evidence and consistent process conduct. For foreign teams, the practical care pathway is:

1. Route legality intake check.
2. Evidence integrity diagnostics.
3. Communication + settlement consistency check.
4. Payroll + local validation readiness check.
5. Closure evidence discharge check.

State Council implementation regulations and SPC labor-dispute interpretation remain critical because disputes often test whether this pathway was followed consistently.

## Pulse triage board: 7 case controls

### Control T1 — Route diagnosis

**Stable when:** one canonical route rationale is documented and consistent.  
**Escalate when:** route wording drift or unsupported rationale appears.  
**Action:** pause case progression and reissue canonical route note.

### Control T2 — Evidence diagnostics

**Stable when:** chronology, ownership, and versions are coherent.  
**Escalate when:** contradiction or source ambiguity appears.  
**Action:** freeze employee-facing movement until reconciliation passes.

### Control T3 — Communication integrity

**Stable when:** approved script version is acknowledged and locked.  
**Escalate when:** delivery deviates from approved language.  
**Action:** enforce deviation approval workflow.

### Control T4 — Settlement coherence

**Stable when:** legal terms, payroll mapping, and manager explanation align.  
**Escalate when:** cross-channel mismatch appears.  
**Action:** revalidate single settlement source sheet.

### Control T5 — Payroll readiness

**Stable when:** treatment assumptions are validated before cutoff.  
**Escalate when:** unresolved assumptions remain near lock.  
**Action:** trigger stop/go with legal co-sign.

### Control T6 — Local validation

**Stable when:** city-level validation is completed and logged.  
**Escalate when:** local caveat remains unresolved.  
**Action:** hold release until local sign-off.

### Control T7 — Discharge integrity

**Stable when:** payment proof and archive checklist are complete.  
**Escalate when:** closure requested without evidence-complete pack.  
**Action:** block closure state change.

## Practical implications for foreign employers

For overseas leadership, the triage model converts broad progress updates into treatment-level decisions. It identifies where case condition is worsening, who owns remediation, and what must clear before movement resumes.

For operations teams, triage discipline reduces last-minute disruption near communication release, payroll lock, and closure.

## Daily triage cycle (20 minutes)

### Minute 0-4: T1-T2 case scan
- Refresh route/evidence stability.
- Apply immediate holds for high-risk deterioration.

### Minute 4-8: T3-T4 case scan
- Validate script/settlement coherence.
- Assign owners for escalated controls.

### Minute 8-12: T5-T6 case scan
- Validate payroll/local readiness before release.
- Trigger stop/go where needed.

### Minute 12-16: T7 case scan
- Validate discharge readiness for near-complete cases.

### Minute 16-20: leadership triage bulletin
- Report escalated controls with owner + ETA + next review time.

## SOP by role

### HR
1. Maintain triage board and ownership records.
2. Block progression on escalated controls.
3. Capture employee communication records.

### Legal
1. Own route and settlement legal coherence.
2. Co-sign high-risk stop/go decisions.
3. Validate control evidence quality.

### Manager
1. Provide date-stamped factual updates.
2. Use approved script only.
3. Escalate material changes immediately.

### Payroll/Finance
1. Validate settlement mapping and treatment assumptions.
2. Enforce payroll readiness control discipline.
3. Produce payment proof for discharge integrity.

### Compliance/Ops
1. Audit control transitions and reason codes.
2. Track repeated escalation patterns by city/team.
3. Verify closure evidence-pack integrity.

## Required document checklist

- Canonical route note
- Evidence chronology log
- Approved script version
- Settlement source sheet
- Payroll treatment mapping
- Local validation memo
- Payment proof + closure archive checklist

SLA baseline:
- route note within 1 business day,
- chronology pass within 2 business days,
- settlement/payroll sync before lock,
- closure archive within 2 business days after payment.

## Exception playbook

### T1 escalation (route)
- Stop progression.
- Reassess route on latest facts.
- Reissue canonical route note.

### T2 escalation (evidence)
- Freeze communication.
- Resolve chronology/ownership conflicts.
- Resume only after verified pass.

### T4 escalation (settlement)
- Use documented clarification path.
- Reconcile legal text and payroll mapping.
- Reapprove communication language.

### T5 escalation (payroll)
- Trigger stop/go before lock.
- Correct mapping and revalidate.
- Align employee-facing explanation.

### T6/T7 escalation (local/closure)
- Hold release/closure.
- Complete validation/evidence pack.
- Re-open only after completion.

## System implementation notes

Core fields:
- case_id
- city
- control_t1_to_t7_status
- route_status
- evidence_status
- script_status
- settlement_status
- payroll_status
- local_validation_status
- release_status
- unresolved_count
- closure_status

Control rules:
- immutable control logs,
- mandatory reason codes for escalated controls,
- auto-alert when unresolved_count > 1,
- release lock on unresolved T1-T6,
- closure lock on unresolved T7.

## Common mistakes and prevention

### Mistake: case marked stable without owner sign-off
**Prevention:** require owner approval artifact per control.

### Mistake: multiple document versions in circulation
**Prevention:** single-source policy for route/script/settlement docs.

### Mistake: escalated control without ETA
**Prevention:** owner + ETA required for every escalation.

### Mistake: local validation treated as advisory
**Prevention:** keep T6 as hard hold.

### Mistake: closure cleared on payment event only
**Prevention:** require T7 evidence-complete pass.

## What to do now (10 actions)

1. Add T1-T7 fields to active case tracker.
2. Reclassify open cases by stable/escalated control status.
3. Publish canonical route notes.
4. Resolve open chronology defects.
5. Lock script version control.
6. Standardize settlement source sheet.
7. Apply pre-lock T5 stop/go checks.
8. Assign local-validation owners for T6.
9. Shift leadership updates to escalated-control format.
10. Review weekly escalation-pattern trends and tune controls.

## What to watch next

- Continued dispute sensitivity to evidence/procedure continuity.
- Settlement/payroll mismatch pressure near lock windows.
- City-level implementation differences requiring explicit checks.
- Deadline pressure increasing unauthorized forward movement.

## FAQ

### 1) Is this legal advice?
No. This is an operations governance brief for decision support.

### 2) Can unilateral routes still be used?
Potentially yes, where legal/factual conditions support them; evidence quality remains decisive.

### 3) Why use a triage-ward model?
Because explicit severity and treatment ownership improve intervention timing and release discipline.

### 4) Is negotiated termination always lower risk?
No. It can help, but only with coherent control discipline.

### 5) What KPI should leadership start with?
Track **escalated-control resolution time** and **full-control-clear release rate**.

## Legal appendix (secondary depth)

This run is anchored to the Labor Contract Law, State Council implementation regulations, and SPC labor-dispute interpretation. These sources define route boundaries and dispute-facing standards for evidence/procedure consistency. Practitioner and market/business references translate legal structure into foreign-employer operational controls.

## Disclaimer

This content is informational only and does not constitute legal, tax, or employment advice. Employers should seek qualified local counsel and tax advisors for case-specific decisions.

## Sources

1. National People’s Congress — Labor Contract Law of the PRC (English): http://www.npc.gov.cn/zgrdw/englishnpc/Law/2007-12/13/content_1384064.htm (accessed 2026-03-04).  
2. State Council — Implementation Regulations of the Labor Contract Law (Decree No. 535): https://www.gov.cn/gongbao/content/2008/content_1124615.htm (accessed 2026-03-04).  
3. Supreme People’s Court — Interpretation on Application of Law in Labor Dispute Cases (Fa Shi [2020] No. 26): https://www.court.gov.cn/fabu/xiangqing/243981.html (accessed 2026-03-04).  
4. China Briefing / Dezan Shira — Employee Termination in China (updated 2025-10-17): https://www.china-briefing.com/news/employee-termination-in-china/ (accessed 2026-03-04).  
5. Littler — Key Recent Developments in China’s Employment Law: https://www.littler.com/news-analysis/asap/key-recent-developments-chinas-employment-law-china-us-comparative-perspective (accessed 2026-03-04).  
6. PwC Worldwide Tax Summaries — PRC Individual: Taxes on Personal Income: https://taxsummaries.pwc.com/peoples-republic-of-china/individual/taxes-on-personal-income (accessed 2026-03-04).
