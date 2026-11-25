# Jerga de Obra

Unfiltered Spanish for construction, welding, and trades jobsites — crew slang (*jerga*), not tourist textbook lines. Clever, funny, and as vulgar as the jobsite gets.

## Features
- Categories including **Jerga** (filthy & true), Safety, Tools, Welding, HVAC, Plumbing, Scaffolding, Heavy Equip
- Search across Spanish, English, and tips
- Mexican Spanish audio clips for every built-in phrase
- Flip cards, Drill (ES↔EN), favorites, spaced review
- First-run tips; add your own crew slang
- Offline-ready PWA
- High-vis safety yellow / black / white theme

## Run locally

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit `http://127.0.0.1:8000`.

## Deploy

The live site is meant to be:

https://glenngerbrick-ship-it.github.io/jerga-de-obra/

Push to `main` runs `.github/workflows/deploy-pages.yml`. GitHub Pages must be turned on once in the repo: **Settings → Pages → Source → GitHub Actions**. The deploy workflow cannot create the Pages site by itself.

If the GitHub repo is still named `jobsite-spanish`, rename it to `jerga-de-obra` in **Settings → General → Repository name** so the live URL matches the product name. GitHub keeps a redirect from the old repo URL.

## Regenerate audio

```bash
pip install edge-tts
python3 scripts/build_content.py
python3 scripts/assemble_html.py
```
