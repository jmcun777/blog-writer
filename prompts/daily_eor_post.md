# Daily EOR Blog Task Prompt

You are producing one daily blog post for China-Payroll.com.

## Objective
Write one factual, readable English article for overseas readers interested in China employment/payroll compliance, with high EOR relevance.

## Workflow
1. Pick ONE topic with strongest EOR decision relevance (not just keyword volume).
2. Research and collect at least 3 reliable sources (prefer official/primary sources).
3. Cross-check critical claims and flag uncertainty.
4. Draft article in human-like professional English.
5. Generate image prompt pack for manual image creation in external AI tools.
6. Build HTML page into repo.
7. If `.pipeline/APPROVE_AUTOPUBLISH` exists, commit+push. Otherwise stop at pending-review and report artifacts path.

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

## Draft format (draft.md)
- Title
- Executive summary (4-6 bullets)
- What changed
- Policy and market context
- Why it matters for foreign employers / EOR buyers
- Practical scenarios (at least 2)
- What to do now (step-by-step action checklist)
- FAQ (5-8 Q&A)
- Disclaimer
- Sources

## Length and SEO requirements
- Target 1,400-2,000 words per article.
- Use one primary keyword plus related terms naturally (no keyword stuffing).
- Write meaningful section headings that match search intent.
- Avoid thin content and generic filler.

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
