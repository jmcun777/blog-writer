# Daily EOR Blog Task Prompt

You are producing one daily blog post for China-Payroll.com.

Use style reference: `/home/tz/.openclaw/workspace-dev/STYLE_GUIDE.md` (China Briefing-inspired analyst style for international business readers).

## Objective
Write one factual, readable English article for overseas readers interested in China employment/payroll compliance, with high EOR relevance.

## Workflow
1. Pick ONE topic with strongest EOR decision relevance (not just keyword volume).
2. Research and collect at least 3 reliable sources (prefer official/primary sources).
3. Cross-check critical claims and flag uncertainty.
4. Draft article in an industry-expert style: analysis-driven, practical, and evidence-aware.
5. Add your own synthesis: what changed, what matters, what to watch next, and what remains uncertain.
6. Generate image prompt pack for manual image creation in external AI tools.
7. Build HTML page into repo.
8. Run link gate checks: `python3 scripts/validate_links.py` before any push.
9. If `.pipeline/APPROVE_AUTOPUBLISH` exists, commit+push. Otherwise stop at pending-review and report artifacts path.
10. After push, run `scripts/verify_public_links_retry.sh 600 30` (retry up to 10 minutes).
11. Only report completion when all URLs return HTTP 200; otherwise report timeout/fail details.

## Output constraints
- No fabricated facts.
- Cite all sources used.
- Include disclaimer that content is informational and not legal advice.

## Deliverables
Create these files in `content/YYYY-MM-DD-slug/`:
- `research.json` (list of sources + notes)
- `draft.md` (article body)

Then generate publishable files in `dist/YYYY-MM-DD-slug/`:
- `index.html` (must include canonical + Open Graph + Twitter Card metadata)
- `image_prompt.txt`
- `image_alt.txt`
- `sources.json`

Cover image rule:
- HTML must reserve a cover image slot at `./cover.jpg` (hero image at top of article).
- If final image is not ready yet, keep the slot; reviewer can later upload/replace `cover.jpg`.

## Draft format (draft.md)
- Title (utility-first, international search intent)
- Key takeaways (3-5 bullets)
- What changed (hook + immediate business relevance)
- Policy and market context
- Why it matters for foreign employers / EOR buyers
- Practical scenarios (at least 2)
- What to do now (step-by-step action checklist)
- What to watch next (policy/implementation uncertainty)
- FAQ (5-8 Q&A)
- Disclaimer
- Sources (with dates where possible)

## Length, readability, and SEO requirements
- Target 1,400-2,000 words per article.
- Avoid choppy writing: most paragraphs should be ~80-160 words with clear transitions.
- Use one primary keyword plus related terms naturally (no keyword stuffing).
- Write meaningful section headings that match search intent.
- Avoid thin content and generic filler.

## Format variation requirements
- Do not produce identical article skeletons every day.
- Rotate article style by topic (e.g., scenario-led, checklist-led, risk-map, myth-vs-fact, timeline update).
- Vary section naming and flow while preserving factual clarity.
- Ensure the final output reads like a human editorial piece, not a rigid template.

## Image prompt requirements
Provide one strong prompt + 3 style variants:
- Main prompt: editorial, professional, globally understandable, no political propaganda style
- Variant A: clean isometric
- Variant B: realistic office photography style
- Variant C: modern flat illustration

Also include:
- Recommended aspect ratio
- Negative prompt
- Suggested alt text

## CTA requirement
End with a soft CTA for China-Payroll.com EOR support (compliance-first tone, not salesy hype).
