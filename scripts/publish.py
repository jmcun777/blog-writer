#!/usr/bin/env python3
import json, re, html, datetime, pathlib, argparse, hashlib


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    in_ul = False
    for ln in lines:
        s = ln.strip()
        if not s:
            if in_ul:
                out.append('</ul>')
                in_ul = False
            continue
        if s.startswith('# '):
            if in_ul:
                out.append('</ul>'); in_ul = False
            out.append(f"<h1>{html.escape(s[2:].strip())}</h1>")
        elif s.startswith('## '):
            if in_ul:
                out.append('</ul>'); in_ul = False
            out.append(f"<h2>{html.escape(s[3:].strip())}</h2>")
        elif s.startswith('### '):
            if in_ul:
                out.append('</ul>'); in_ul = False
            out.append(f"<h3>{html.escape(s[4:].strip())}</h3>")
        elif s.startswith('- '):
            if not in_ul:
                out.append('<ul>'); in_ul = True
            out.append(f"<li>{html.escape(s[2:].strip())}</li>")
        else:
            if in_ul:
                out.append('</ul>'); in_ul = False
            esc = html.escape(s)
            esc = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', r'<a href="\2">\1</a>', esc)
            out.append(f"<p>{esc}</p>")
    if in_ul:
        out.append('</ul>')
    return '\n'.join(out)


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')[:80] or 'post'


def pick_prompt_pack(title: str):
    t = title.lower()
    if 'minimum wage' in t:
        scene = 'HR compensation planning meeting with salary benchmark charts and city map pins across China'
        motifs = 'payroll sheets, contract clauses, calendar markers'
    elif 'social insurance' in t:
        scene = 'finance and payroll operations team reviewing contribution base dashboards in a modern office'
        motifs = 'benefit icons, compliance checklist, monthly reports'
    elif 'iit' in t or 'tax' in t:
        scene = 'tax season preparation desk with multilingual guidance materials and payroll analytics dashboard'
        motifs = 'calculator, secure documents, process flow graphics'
    elif 'dispute' in t:
        scene = 'risk-control workshop with HR and legal teams reviewing case folders and prevention checklists'
        motifs = 'evidence timeline, policy binder, meeting whiteboard'
    else:
        scene = 'global operations team evaluating workforce model options for China market entry'
        motifs = 'decision matrix, org chart, legal policy documents'

    style_pool = [
        ('editorial illustration', 'clean composition, magazine quality, subtle shadows'),
        ('cinematic photo-realistic', 'natural office light, depth of field, modern corporate look'),
        ('isometric business infographic', 'precise geometry, neutral palette, data-storytelling feel'),
        ('premium flat vector', 'bold hierarchy, uncluttered shapes, high-contrast readability')
    ]
    idx = int(hashlib.md5(title.encode()).hexdigest(), 16) % len(style_pool)
    style, details = style_pool[idx]

    main_prompt = (
        f"Create a 16:9 hero image for article title: '{title}'. "
        f"Scene: {scene}. Include motifs: {motifs}. "
        f"Style: {style}; {details}. "
        "Audience is Western business readers. Tone should feel credible, practical, and contemporary. "
        "Leave clean whitespace on left/top area for headline overlay. "
        "No text in image, no logos, no watermarks."
    )

    variants = [
        "Variant A: add subtle human presence (2-4 professionals), emphasize collaboration and decision-making.",
        "Variant B: data-first composition with dashboards/charts as visual anchors, minimal people.",
        "Variant C: risk-and-compliance narrative visual (checklists, timeline cards, policy docs) with premium editorial look."
    ]
    negative = "Negative prompt: no propaganda style, no flags dominating frame, no blurry text blocks, no cartoon faces, no watermark."
    return main_prompt, variants, negative


def write_cover_svg(out_dir: pathlib.Path, title: str):
    words = title.split()
    subtitle = ' '.join(words[:8])
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1d4ed8"/>
      <stop offset="55%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <circle cx="1350" cy="120" r="180" fill="white" fill-opacity="0.08"/>
  <circle cx="1480" cy="760" r="220" fill="white" fill-opacity="0.06"/>
  <rect x="90" y="100" width="1420" height="700" rx="28" fill="white" fill-opacity="0.1"/>
  <text x="130" y="220" font-family="Inter,Arial,sans-serif" font-size="34" font-weight="600" fill="white" fill-opacity="0.92">China Payroll Insight</text>
  <foreignObject x="130" y="270" width="1300" height="360">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Inter,Arial,sans-serif;color:white;font-size:58px;font-weight:800;line-height:1.15;letter-spacing:-0.01em;">{html.escape(title)}</div>
  </foreignObject>
  <text x="130" y="700" font-family="Inter,Arial,sans-serif" font-size="30" fill="white" fill-opacity="0.95">{html.escape(subtitle)}</text>
</svg>'''
    (out_dir / 'cover.svg').write_text(svg, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--draft', required=True)
    ap.add_argument('--template', default='templates/post.html')
    ap.add_argument('--dist-root', default='dist')
    ap.add_argument('--date', default=datetime.date.today().isoformat())
    ap.add_argument('--slug', default='')
    ap.add_argument('--meta-description', default='Practical update for overseas employers on China payroll and labor compliance.')
    ap.add_argument('--image-prompt', default='')
    ap.add_argument('--image-alt', default='Business professionals reviewing payroll and compliance documents in a modern office setting.')
    ap.add_argument('--sources', default='[]')
    ap.add_argument('--site-base-url', default='https://jmcun777.github.io/blog-writer')
    ap.add_argument('--og-image', default='')
    args = ap.parse_args()

    draft_text = pathlib.Path(args.draft).read_text(encoding='utf-8')
    title = 'China Employment & Payroll Update'
    for ln in draft_text.splitlines():
        if ln.startswith('# '):
            title = ln[2:].strip()
            break

    slug = args.slug or slugify(title)
    out_dir = pathlib.Path(args.dist_root) / f"{args.date}-{slug}"
    out_dir.mkdir(parents=True, exist_ok=True)

    main_prompt, variants, negative = pick_prompt_pack(title) if not args.image_prompt.strip() else (args.image_prompt.strip(), [], "Negative prompt: no watermark.")
    prompt_txt = "\n".join([main_prompt, "", *variants, "", "Aspect ratio: 16:9 (1600x900 recommended)", negative])
    (out_dir / 'image_prompt.txt').write_text(prompt_txt, encoding='utf-8')
    (out_dir / 'image_alt.txt').write_text(args.image_alt, encoding='utf-8')
    write_cover_svg(out_dir, title)

    body_html = md_to_html(draft_text)
    cover_block = (
        f'<figure class="hero"><img src="./cover.svg" alt="{html.escape(args.image_alt)}" loading="lazy" />'
        '<figcaption>Suggested hero visual for editorial review. You can replace with a generated JPG/PNG using the prompt pack.</figcaption></figure>'
    )
    body_html = cover_block + body_html

    tpl = pathlib.Path(args.template).read_text(encoding='utf-8')
    canonical_url = f"{args.site_base_url.rstrip('/')}/{out_dir.as_posix().lstrip('./')}/"
    og_image = args.og_image or f"{args.site_base_url.rstrip('/')}/{out_dir.as_posix().lstrip('./')}/cover.svg"

    prompt_preview = html.escape((prompt_txt[:260] + ('…' if len(prompt_txt) > 260 else '')))
    prompt_block = (
        '<section class="prompt"><h3>Image Prompt Pack</h3>'
        '<p><a href="./image_prompt.txt" target="_blank">Open full image prompt (TXT)</a></p>'
        f'<p><code>{prompt_preview}</code></p>'
        '</section>'
    )

    page = (tpl.replace('{{META_TITLE}}', html.escape(title))
              .replace('{{META_DESCRIPTION}}', html.escape(args.meta_description))
              .replace('{{CANONICAL_URL}}', html.escape(canonical_url))
              .replace('{{OG_IMAGE}}', html.escape(og_image))
              .replace('{{BODY_HTML}}', body_html)
              .replace('{{LAST_REVIEWED}}', args.date))
    page = page.replace('</article>', f'{prompt_block}</article>')
    (out_dir / 'index.html').write_text(page, encoding='utf-8')

    try:
        src = json.loads(args.sources)
    except Exception:
        src = []
    (out_dir / 'sources.json').write_text(json.dumps(src, ensure_ascii=False, indent=2), encoding='utf-8')

    print(str(out_dir))


if __name__ == '__main__':
    main()
