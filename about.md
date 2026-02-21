---
layout: null
title: Comprehensive Profile
permalink: /about/
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} - {{ site.title | default: "Developer Documentation" }}</title>
    
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg: #050505;
            --card-bg: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.08);
            --accent: #6366f1; 
            --text-main: #ffffff;
            --text-dim: #94a3b8;
            --glass: blur(12px);
        }

        * { box-sizing: border-box; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            background-image: radial-gradient(circle at 50% -20%, #1e1b4b, transparent);
            color: var(--text-main);
            margin: 0;
            display: flex;
            justify-content: center;
            line-height: 1.6;
            padding-top: 5rem;
        }

        /* Standardized Global Navigation */
        .floating-nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgba(5, 5, 5, 0.85);
            backdrop-filter: var(--glass);
            border-bottom: 1px solid var(--border);
            z-index: 1000;
            display: flex;
            justify-content: center;
            padding: 1rem 1.5rem;
        }

        .nav-container {
            max-width: 1000px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-brand { color: var(--text-main); font-weight: 800; text-decoration: none; letter-spacing: -0.5px; font-size: 1.2rem; }
        .nav-links { display: flex; gap: 1.5rem; }
        .nav-links a { color: var(--text-dim); text-decoration: none; font-weight: 600; font-size: 0.9rem; }
        .nav-links a:hover { color: var(--text-main); }

        .container {
            max-width: 1000px;
            width: 100%;
            padding: 2rem 1.5rem 4rem 1.5rem;
        }

        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; }
        .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 28px; padding: 2rem; backdrop-filter: var(--glass); }

        .profile-main { grid-column: span 2; }
        .location-card { grid-column: span 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;}
        .skills-card { grid-column: span 3; }
        .experience-card { grid-column: span 3; }

        h1 { font-size: 3rem; margin: 0 0 1rem 0; letter-spacing: -2px; font-weight: 800; line-height: 1.1; }
        h2 { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--accent); margin-top: 0; margin-bottom: 1.5rem; }
        p { color: var(--text-dim); font-size: 1.1rem; }

        .skill-tags { display: flex; flex-wrap: wrap; gap: 10px; }
        .tag { background: rgba(99, 102, 241, 0.1); color: var(--text-main); padding: 8px 16px; border-radius: 20px; font-size: 0.9rem; border: 1px solid rgba(99, 102, 241, 0.2); display: flex; align-items: center; gap: 8px; }

        .timeline-item { border-left: 2px solid var(--border); padding-left: 20px; margin-bottom: 20px; position: relative; }
        .timeline-item::before { content: ''; position: absolute; left: -6px; top: 6px; width: 10px; height: 10px; background: var(--accent); border-radius: 50%; }
        .timeline-title { font-weight: 600; color: var(--text-main); font-size: 1.2rem; }
        .timeline-date { font-size: 0.85rem; color: var(--accent); margin-bottom: 5px; display: block; }

        @media (max-width: 850px) {
            .grid { grid-template-columns: 1fr; }
            .profile-main, .location-card, .skills-card, .experience-card { grid-column: span 1; }
        }
    </style>
</head>
<body>

    <nav class="floating-nav">
        <div class="nav-container">
            <a href="/" class="nav-brand">Research Log</a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about/">Profile</a>
                <a href="/blog/">Archive</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="grid">
            
            <section class="card profile-main">
                <h2>The Engineer</h2>
                <h1>Systematic Construction and Empirical Design.</h1>
                <p>My objective is to engineer software that processes data efficiently and presents information clearly. I construct digital architecture strictly through observable testing and measurable performance metrics, eliminating unverified methodologies.</p>
                <p>By avoiding heavy commercial frameworks where possible, I ensure that the foundational code remains secure, significantly fast, and completely understandable for future maintenance.</p>
            </section>

            <section class="card location-card">
                <i data-lucide="map-pin" style="width: 48px; height: 48px; color: var(--accent); margin-bottom: 1rem;"></i>
                <h3 style="margin: 0; font-size: 1.5rem;">Bandung</h3>
                <p style="margin: 5px 0 0 0; font-size: 1rem;">West Java, Indonesia</p>
                <p style="font-size: 0.8rem; margin-top: 15px; color: var(--accent);">Operational Base</p>
            </section>

            <section class="card skills-card">
                <h2>Technical Competencies</h2>
                <div class="skill-tags">
                    <span class="tag"><i data-lucide="code"></i> Hypertext Markup Language</span>
                    <span class="tag"><i data-lucide="palette"></i> Cascading Style Sheets</span>
                    <span class="tag"><i data-lucide="file-json"></i> JavaScript Programming</span>
                    <span class="tag"><i data-lucide="server"></i> Backend Architecture</span>
                    <span class="tag"><i data-lucide="database"></i> Relational Database Management</span>
                    <span class="tag"><i data-lucide="search"></i> Search Engine Optimization</span>
                    <span class="tag"><i data-lucide="git-branch"></i> Version Control Integration</span>
                </div>
            </section>

            <section class="card experience-card">
                <h2>Professional Timeline</h2>
                
                <div class="timeline-item">
                    <span class="timeline-date">2023 — Present</span>
                    <div class="timeline-title">Independent Software Developer</div>
                    <p style="font-size: 0.95rem; margin-top: 5px;">Designing high-performance static websites and robust server architecture. Focusing entirely on measurable loading speed reductions and structural code integrity.</p>
                </div>

                <div class="timeline-item">
                    <span class="timeline-date">2021 — 2023</span>
                    <div class="timeline-title">Systems Application Engineer</div>
                    <p style="font-size: 0.95rem; margin-top: 5px;">Maintained legacy code systems while systematically converting them to modern syntax standards. Reduced server response latency through rigorous database indexing.</p>
                </div>
                
            </section>

        </div>
        
        <footer style="text-align: center; margin-top: 3rem; color: var(--text-dim); font-size: 0.8rem;">
            &copy; 2026 — Engineered in Bandung
        </footer>
    </div>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>