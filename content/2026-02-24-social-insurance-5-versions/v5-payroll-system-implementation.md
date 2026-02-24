# Payroll System Implementation Guide (2026): China Social Insurance for Foreign Employees

## Key takeaways
- System design determines whether policy can be executed consistently.
- Required fields and validation rules should prevent incomplete payroll runs.
- Auditability is as important as calculation correctness.

## Data model requirements
Mandatory fields:
- Nationality / employee type
- City contribution code
- Social insurance participation flag
- Treaty exemption flag
- Certificate validity start/end date
- Decision approver ID

## Validation rules
- Block payroll finalization if mandatory SI fields are missing.
- If exemption flag = true, certificate fields must be populated.
- If certificate expired, auto-revert to standard contribution path.

## Monthly run controls
1. Parameter sync check (city base/rate).
2. Pre-run exception report.
3. Payroll run.
4. Post-run reconciliation.
5. Evidence export and archive.

## Integration notes
- HRIS -> payroll field mapping must be version-controlled.
- Vendor/API payload should include decision reason codes.
- Keep immutable log for field overrides.

## Error handling
- Mapping mismatch: fail-fast and alert payroll owner.
- Missing certificate: quarantine record and apply default contribution.
- Unexpected delta: create reconciliation ticket with due date.

## Sources
- Social Insurance Law (NPC): http://www.npc.gov.cn/zgrdw/englishnpc/Law/2009-02/20/content_1471106.htm
- Labor Contract Law (NPC): http://www.npc.gov.cn/zgrdw/englishnpc/Law/2007-12/13/content_1384064.htm
- PwC WTS: https://taxsummaries.pwc.com/peoples-republic-of-china/individual/other-taxes
