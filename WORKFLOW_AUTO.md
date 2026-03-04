# WORKFLOW_AUTO.md

## Continuous Quality Loop (User-approved)

1. Keep learning from high-performing reference sites (especially China Briefing) across multiple directories.
2. For each daily article cycle:
   - Research -> Outline -> Draft -> Humanization pass -> Score
3. Scoring policy:
   - If score < 85: revise before publish.
   - Publish only when score >= 85.
   - If score >= 90, send a second milestone-quality notification.
4. Delivery gate (anti-404):
   - Do not send user-facing link notifications until public URL is confirmed HTTP 200.
   - If the page is still propagating, keep retrying verification and notify only after online confirmation.
5. Auto-remediation rule (critical):
   - If the same operational error appears 2 runs in a row, automatically attempt a fix in the same run (do not wait for user command).
   - Typical auto-fixes include: auth refresh/rebind, retry with backoff, restart failed step, switch to safer edit/write path, or reduce parallel load when fork/resource limits appear.
   - Report what was auto-fixed and whether it resolved the issue.
6. Prioritize reader retention mechanics:
   - fast value entry
   - short utility headings
   - coherent section flow
   - concrete data density
7. Readability format rule (critical):
   - Use clear H2-led section structure for main body.
   - Avoid overly mechanical account-style writing and excessive raw data stacking.
   - Reduce numbered-list density (1/2/3/4 style) and avoid repetitive numeric sequencing tone.
   - Keep evidence useful, but prioritize publishable narrative flow and article-like readability over data-dump formatting.
5. Audience-fit rule (foreign readers new to China):
   - lead with clear legal/regulatory introduction and context
   - explain core local law concepts in plain business English first
   - keep heavy operational playbooks as secondary/optional sections
6. Avoid machine-writing artifacts and overlong intros.


## Repository Boundary Rule (Critical)
- Do NOT sync website backup repositories/data into `blog-writer` by default.
- Treat `web-sites-backup/` and similar backup directories as separate repos/workspaces.
- Only sync backup content into `blog-writer` if the user explicitly requests it.

## Sticky Topic Rule (Hourly Testing Mode)
- During hourly testing, do NOT pick random/new topics by default.
- Read `/home/tz/.openclaw/workspace-dev/CURRENT_TOPIC.md` and keep the same topic for iterative improvement each run.
- If user sends a new topic in chat, update `CURRENT_TOPIC.md` immediately and use that as the new optimization target for subsequent hourly runs.

## Anti-Template Variation Rule
- Do NOT repeat the same article skeleton every run.
- Rotate among formats for the same topic:
  1) decision-tree format
  2) scenario/case format
  3) checklist format
  4) myth-vs-fact format
  5) cost/risk matrix format
- Do not always use the exact same timeline pattern (e.g., D-14 to D+7) in every article.
- Keep core facts consistent, but vary framing, heading labels, and narrative entry point.

## Pulse-Benchmark Mode (Enabled)
- Benchmark writing style against ChatGPT Pulse-like daily briefings.
- Use a two-layer output model:
  1) Pulse-style daily brief (primary): headline-driven, news-desk tone, impact-first, concise action steps.
  2) Legal depth appendix (secondary): regulations, legal basis, caveats.
- Before drafting, aggregate multi-source updates and cluster into themes; do not write from a single-source mindset.
- Enforce source mix each run: official/legal + practitioner + market/business context + practical interpretation.
- Add dual scoring per run:
  - Quality score (accuracy/clarity/decision value)
  - Pulse-similarity score (structure, tone, readability, briefing feel)
- If Pulse-similarity is weak, revise style before publish.

