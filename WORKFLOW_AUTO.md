# WORKFLOW_AUTO.md

## Continuous Quality Loop (User-approved)

1. Keep learning from high-performing reference sites (especially China Briefing) across multiple directories.
2. For each daily article cycle:
   - Research -> Outline -> Draft -> Humanization pass -> Score
3. Scoring policy:
   - If score < 85: revise before publish.
   - Publish and notify when score >= 85.
   - If score >= 90, send a second milestone-quality notification.
4. Prioritize reader retention mechanics:
   - fast value entry
   - short utility headings
   - coherent section flow
   - concrete data density
5. Avoid machine-writing artifacts and overlong intros.


## Sticky Topic Rule (Hourly Testing Mode)
- During hourly testing, do NOT pick random/new topics by default.
- Read `/home/tz/.openclaw/workspace-dev/CURRENT_TOPIC.md` and keep the same topic for iterative improvement each run.
- If user sends a new topic in chat, update `CURRENT_TOPIC.md` immediately and use that as the new optimization target for subsequent hourly runs.
