# Blog Production Spec (China-Payroll.com)

## Goal
Create daily English blog posts for overseas readers (HR/Finance/Founders) who need trustworthy China employment and payroll information, and may become Employer of Record (EOR) customers.

## Topic Rule (Primary)
Choose topics by **EOR business relevance first**, then SEO optimization.

Priority themes:
1. China employer risk and compliance changes
2. Payroll/tax/social insurance operational impact for foreign employers
3. Hiring, termination, severance, and labor dispute exposure
4. Practical employer actions and timelines

## Source & Fact Rule
- Minimum 3 independent sources per article
- Prefer official or primary sources where available
- Include publication/update date for each source
- Clearly label uncertainty or unresolved interpretations
- Add disclaimer: informational only, not legal advice

## Writing Rule
- Audience: non-Chinese English readers
- Use plain, professional English and explain local terms
- Avoid exaggerated certainty and avoid AI-generic filler language
- Target length: **1,400-2,000 words** (short posts are not acceptable unless explicitly requested)
- Readability baseline:
  - avoid overly short, choppy paragraphs
  - most body paragraphs should be ~80-160 words
  - use examples, transitions, and practical context so sections feel human-written
- Style variation rule (avoid mechanical sameness):
  - rotate between article shapes (explainer, checklist-led, myth-vs-fact, scenario-led, timeline-led)
  - not every post should use identical heading phrasing/order
  - vary opener style (news hook, practical pain point, data point)
- SEO quality baseline:
  - one primary keyword + 4-8 related keywords used naturally
  - descriptive H2/H3 headings
  - FAQ section with 5-8 Q&A
  - practical checklist and examples
- Structure guidance (flexible, not rigid template):
  - include policy change, business impact, scenarios, action checklist, and FAQ
  - allow section order to vary by topic for natural flow

## Required Output Files
For each post (under `dist/YYYY-MM-DD-slug/`):
- `index.html` (final publishable post)
- `image_prompt.txt` (prompt for external image generation)
- `image_alt.txt` (accessibility alt text)
- `sources.json` (source list and metadata)

## HTML Requirements
- Clean article layout
- Meta title + meta description
- H1 + ToC + section headings
- FAQ section
- CTA section for China-Payroll.com EOR services
- Last reviewed date

## Publishing
- Default mode: generate artifacts first, then human review
- Auto-publish is allowed only when `.pipeline/APPROVE_AUTOPUBLISH` exists in repo root
- If approval file is missing, do **not** push; return pending-review summary
- Once approved, commit and push to `master`
- Publish through GitHub Pages
