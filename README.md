# Joesavat Donovan — Cyber Security & Researcher

Static, single-file portfolio built with HTML, CSS, and vanilla JavaScript. No frameworks, no build step, no server-side rendering.

## What is this?

A dark-mode cybersecurity practitioner portfolio showcasing:

- **Cyber Security & Researcher** — homepage hero with core message
- **Case Studies** — technical breakdowns of offensive security engagements (start from [project-1.html](project-1.html))
- **Write-ups** — CTF and research write-ups in a markdown-documentation style (start from [writeup-1.html](writeup-1.html))
- **Lab** — live self-hosted tools linked from the homepage and the fullscreen menu dropdown: [osint-harian](https://cingmen.github.io/osint-harian/) (daily public-data tracker) and [PhishQuest](https://cingmen.github.io/phisquest/) (anti-phishing training game)

## Structure

- `index.html` — homepage with hero, marquee, capabilities, tech arsenal, case studies, write-ups, lab, and contact
- `osint-harian/`, `phisquest/` — not part of this repo; each is its own GitHub Pages project site served under the same domain, so they deploy independently
- `project-1.html` — sample case study page (numbered 01-04 blocks, terminal/code placeholders, next-project link)
- `writeup-1.html` — CTF write-up page with clickable code blocks and table of contents
- `404.html` — custom 404 page in the same design language
- `sitemap.xml`, `robots.txt` — static SEO files
- GitHub Actions workflow in `.github/workflows/jekyll-gh-pages.yml` for GitHub Pages deployment

## Design

- Dark theme (#0a0a0a background, #f0f0f0 text, #ccff00 accent)
- Typography: Syne (headings), Space Grotesk (body), Space Mono (terminal/label)
- Custom cursor with smooth follow and hover ring (disabled on touch devices)
- Scroll progress bar, IntersectionObserver fade-up reveals, noise grain overlay
- Fullscreen clip-path menu overlay on the homepage, with a native `<details>` Lab dropdown (works without JS)

## Local development

No build step. Just open any file in a browser, or serve locally:

```bash
python3 -m http.server 8000
```

Changes are visible immediately — reload to see updates.

## License

Personal portfolio. Content and images are my own; third-party assets retain their respective licenses.
