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
- Structure:
  1) What changed
  2) Why it matters for employers using EOR/PEO-like setups
  3) What companies should do next

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
