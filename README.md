# Joesavat Donovan — SECURE_ID://ROOT

Personal security portfolio of **Joesavat Donovan**, a cybersecurity practitioner working across
offensive security, threat intelligence, malware analysis and vulnerability research.

This repository is the whole website: hand-written HTML, CSS and vanilla JavaScript with **no
framework, no build step, no bundler and no runtime third-party requests**. Every font, script,
image and icon is served from this repository.

Live site: <https://cingmen.github.io/>

## What is in here

| Path | Purpose |
| --- | --- |
| `index.html` | Homepage — hero, about, capabilities, arsenal & certifications, case studies, write-ups, lab, contact, fullscreen menu |
| `projects/blackgate-perimeter-breach.html` | Case study 01 — BlackGate perimeter breach (web/network) |
| `projects/operation-nightshade-ad-red-team.html` | Case study 02 — Operation Nightshade (Active Directory red team) |
| `projects/iot-botnet-telemetry-study.html` | Case study 03 — IoT botnet telemetry study (malware research) |
| `writeups/htb-lame-samba-usermap-script.html` | CTF write-up — HackTheBox Lame: Samba `usermap_script` to root |
| `404.html` | Custom not-found page (served by GitHub Pages for any missing path) |
| `feed.xml` | RSS 2.0 feed of published write-ups |
| `sitemap.xml`, `robots.txt` | Static SEO files |
| `site.webmanifest` | Web app manifest (name, theme colour, icons) |
| `assets/fonts/` | Self-hosted WOFF2 subsets (Syne, Space Grotesk, Space Mono) |
| `assets/js/` | Locally bundled Motion runtime used for the hero entrance |
| `assets/diagrams/` | Seven hand-generated SVG figures used by the case studies and write-up |
| `assets/thumbs/` | Case-study hover previews |
| `assets/og-*.png` | Per-page Open Graph share images (1200×630) |
| `assets/icons/` | PWA / touch icons |
| `tools/` | Python scripts that generate brand assets and check the site |
| `.github/workflows/` | GitHub Pages deployment and site checks |

### Live sub-projects linked from the homepage

Two tools are separate GitHub Pages project sites served under the same domain:

- [osint-harian](https://cingmen.github.io/osint-harian/) — daily deterministic tracker of public data
  (BMKG, OFAC, CISA, NVD, WHO, USGS, news RSS) with a published diff per run.
- [PhishQuest](https://cingmen.github.io/phisquest/) — Indonesian anti-phishing training game with
  email, SMS and WhatsApp scenarios plus a CLI mode.

They live in their own repositories. Nothing in this repository needs to change when they deploy;
the homepage only links to `/osint-harian/` and `/phisquest/`.

## Design & engineering notes

- Dark palette (`#0a0a0a` background, `#f0f0f0` text, `#ccff00` accent), Syne for headings,
  Space Grotesk for body copy, Space Mono for labels and terminal blocks.
- Fullscreen menu is a keyboard-accessible modal: focus moves to the first link on open,
  Tab/Shift+Tab wrap inside it, `main`/`footer` are `inert` while it is open, and Esc closes it and
  returns focus to the menu button.
- Respects `prefers-reduced-motion`; the custom cursor only activates for fine pointers.
- Progressive enhancement: content is visible without JavaScript, the menu dropdown is a native
  `<details>` element, and the hero entrance falls back to visible text if Motion fails.
- No analytics, no cookies, no external CDNs.

## Local development

There is nothing to install or compile. Open any page directly, or serve the folder:

```bash
python3 -m http.server 8000
# http://localhost:8000/
```

## Checks

`tools/check_site.py` validates the static site without dependencies beyond the Python standard
library:

```bash
python3 tools/check_site.py
```

It fails on broken local links, missing anchors, duplicate `id`s, images without `alt`, pages
without a single `h1` or meta description, feed entries that point at pages or anchors that do not
exist, and sitemap URLs that do not resolve to a file (the 404 page must stay out of the sitemap).
The same script runs in CI via `.github/workflows/site-checks.yml` on every push and pull request.

Asset generation (macOS, needs Pillow and the system fonts referenced in each script):

```bash
python3 tools/make_case_images.py   # case-study thumbnails + OG images
python3 tools/make_diagrams.py      # SVG figures used in case studies
python3 tools/make_brand_assets.py  # write-up OG image + PWA/touch icons
```

## Deployment

Every push to `main` triggers `.github/workflows/jekyll-gh-pages.yml`, which uploads the repository
root as a static artifact and deploys it to GitHub Pages. There is no Jekyll build; the workflow
name is historical. `main` is the only deployed branch.

## Content notes

- Case studies use redacted identifiers; the techniques, tooling and remediation steps are real.
- The two "soon" items in the write-up list intentionally have no pages yet and are marked
  `aria-disabled`; the RSS feed only lists write-ups that actually exist.
- The PGP block offers a public key on request instead of publishing an unverified key.

## License

Personal portfolio. Code, copy, diagrams and images are the author's own unless noted otherwise.
