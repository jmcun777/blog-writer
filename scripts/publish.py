#!/usr/bin/env python3
import json, os, re, html, datetime, pathlib, argparse


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
                out.append('</ul>'); in_ul=False
            out.append(f"<h1>{html.escape(s[2:].strip())}</h1>")
        elif s.startswith('## '):
            if in_ul:
                out.append('</ul>'); in_ul=False
            out.append(f"<h2>{html.escape(s[3:].strip())}</h2>")
        elif s.startswith('### '):
            if in_ul:
                out.append('</ul>'); in_ul=False
            out.append(f"<h3>{html.escape(s[4:].strip())}</h3>")
        elif s.startswith('- '):
            if not in_ul:
                out.append('<ul>'); in_ul=True
            out.append(f"<li>{html.escape(s[2:].strip())}</li>")
        else:
            if in_ul:
                out.append('</ul>'); in_ul=False
            # very light link handling [text](url)
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

    body_html = md_to_html(draft_text)
    cover_block = (
        f'<figure class="hero"><img src="./cover.jpg" alt="{html.escape(args.image_alt)}" '
        "onerror=\"this.style.display='none'\" loading=\"lazy\" /></figure>"
    )
    body_html = cover_block + body_html

    tpl = pathlib.Path(args.template).read_text(encoding='utf-8')
    canonical_url = f"{args.site_base_url.rstrip('/')}/{out_dir.as_posix().lstrip('./')}/"
    og_image = args.og_image or f"{args.site_base_url.rstrip('/')}/{out_dir.as_posix().lstrip('./')}/cover.jpg"

    page = (tpl.replace('{{META_TITLE}}', html.escape(title))
              .replace('{{META_DESCRIPTION}}', html.escape(args.meta_description))
              .replace('{{CANONICAL_URL}}', html.escape(canonical_url))
              .replace('{{OG_IMAGE}}', html.escape(og_image))
              .replace('{{BODY_HTML}}', body_html)
              .replace('{{LAST_REVIEWED}}', args.date))

    (out_dir / 'index.html').write_text(page, encoding='utf-8')

    # image prompt pack
    main_prompt = args.image_prompt or (
        f"Editorial hero image for an English article titled '{title}'. "
        "Scene: international HR/payroll team reviewing China employment compliance updates. "
        "Style: professional, clean, trustworthy, modern business publication. "
        "Composition: 16:9 horizontal hero with clear whitespace for headline. "
        "Color palette: blue, white, subtle gray. "
        "No text overlays, no watermark, no logos."
    )
    variants = [
        "Variant A (isometric): clean isometric office + compliance dashboard visuals, minimalistic details.",
        "Variant B (photo-realistic): realistic corporate meeting room, documents/laptop charts, natural lighting.",
        "Variant C (flat illustration): modern flat vector style, simple geometric shapes, editorial look."
    ]
    negative = "Negative prompt: no watermark, no blurry text, no propaganda symbols, no flags dominating the scene, no caricature."
    prompt_txt = "\n".join([main_prompt, "", *variants, "", "Aspect ratio: 16:9", negative])
    (out_dir / 'image_prompt.txt').write_text(prompt_txt, encoding='utf-8')
    (out_dir / 'image_alt.txt').write_text(args.image_alt, encoding='utf-8')

    # Add full prompt link (and short preview) inside article HTML
    prompt_preview = html.escape((prompt_txt[:260] + ('…' if len(prompt_txt) > 260 else '')))
    prompt_block = (
        '<section class="prompt"><h3>Image Prompt Pack</h3>'
        f'<p><a href="./image_prompt.txt" target="_blank">Open full image prompt (TXT)</a></p>'
        f'<p><code>{prompt_preview}</code></p>'
        '</section>'
    )
    page = page.replace('</article>', f'{prompt_block}</article>')

    try:
        src = json.loads(args.sources)
    except Exception:
        src = []
    (out_dir / 'sources.json').write_text(json.dumps(src, ensure_ascii=False, indent=2), encoding='utf-8')

    print(str(out_dir))


if __name__ == '__main__':
    main()
