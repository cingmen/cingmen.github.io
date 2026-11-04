# Joesavat Donovan — SECURE_ID://ROOT

**Offensive Security · Threat Intelligence · Malware Analysis · Vulnerability R&D**

[**Live Portfolio → cingmen.github.io**](https://cingmen.github.io/) · [**RSS Feed**](https://cingmen.github.io/feed.xml) · [**LinkedIn**](https://linkedin.com/in/joesavatdonovan) · [**joesavat@gmail.com**](mailto:joesavat@gmail.com)

<p align="center">
  <a href="https://cingmen.github.io/">
    <img src="assets/og-home.png" alt="Joesavat Donovan — Cyber Security & Researcher" width="720" />
  </a>
</p>

## About

I am **Joesavat Donovan**, a cybersecurity practitioner working with an offense-first mindset: model the adversary, chain small failures to prove real business impact, and translate every finding into durable fixes and detections.

- **Offensive Security** — External perimeter assessments, web/API exploitation (OWASP WSTG / PTES), and assumed-breach Active Directory red teaming.
- **Defensive & Purple Team** — MITRE ATT&CK detection engineering, SIEM telemetry gap analysis, Sigma rules, and incident response playbooks.
- **Malware Analysis & Vulnerability R&D** — Reverse engineering (Ghidra, profiled QEMU sandboxes), C2 protocol analysis, custom PoCs, and zero-FP YARA rules.

**Highlights on the site:**
- **Case Studies:** [BlackGate Perimeter Breach](https://cingmen.github.io/projects/blackgate-perimeter-breach.html) (Web/Network) · [Operation Nightshade](https://cingmen.github.io/projects/operation-nightshade-ad-red-team.html) (AD Red Team) · [IoT Botnet Telemetry Study](https://cingmen.github.io/projects/iot-botnet-telemetry-study.html) (Malware Research)
- **Write-ups:** [HTB — Lame: Samba `usermap_script` to root](https://cingmen.github.io/writeups/htb-lame-samba-usermap-script.html) (`CVE-2007-2447`)
- **Live Lab Tools:** [osint-harian](https://cingmen.github.io/osint-harian/) (daily public-data diff tracker) · [PhishQuest](https://cingmen.github.io/phisquest/) (Indonesian anti-phishing training game)

---

## About This Repository

Source code for **[cingmen.github.io](https://cingmen.github.io/)** — built with pure HTML, CSS, and vanilla JavaScript. **Zero frameworks, zero build step, zero trackers, and zero third-party network requests** (all WOFF2 fonts, SVG figures, and scripts are self-hosted).

```text
cingmen.github.io/
├── index.html                        # Homepage — hero, capabilities, arsenal, work, lab, contact
├── projects/                         # Technical case studies (SEO-slugged HTML)
├── writeups/                         # CTF walkthroughs & security research notes
├── 404.html                          # Custom 404 page
├── assets/                           # Self-hosted WOFF2 fonts, SVG diagrams, thumbnails, OG cards
├── tools/                            # Static site verifier (check_site.py) & asset generators
└── feed.xml, sitemap.xml, robots.txt # RSS 2.0 feed & search engine indexing files
```

### Local Development & Checks

```bash
python3 -m http.server 8000     # Serve locally at http://localhost:8000/
python3 tools/check_site.py     # Validate links, anchors, alt text, feed & sitemap (runs in CI)
```

---

## Contact

Available for **penetration testing engagements, red/purple team exercises, security research, and engineering roles**.  
Reach out at **[joesavat@gmail.com](mailto:joesavat@gmail.com)** *(PGP public key fingerprint available on request)*.
