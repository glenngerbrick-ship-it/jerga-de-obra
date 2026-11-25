# Jobsite Spanish

Practical Spanish for construction, welding, and trades jobsites — the phrases crews actually yell, not tourist textbook lines.

## Features
- Category browsing (Safety, Tools, Welding, HVAC, Plumbing, Scaffolding, Heavy Equip, and more)
- Search across Spanish, English, and tips
- **Mexican Spanish audio clips** for every built-in phrase (plus device TTS fallback)
- **Flip cards** — tap to reveal, mark known, favorites, spaced “Again”
- Drill mode with ES→EN / EN→ES, Review / Favorites filters, streaks
- Favorites + spaced review (due phrases resurface)
- First-run tips / onboarding
- Add / delete your own crew slang (saved locally)
- Speak mode with speed control
- Offline-ready PWA (service worker + manifest)
- High-vis safety yellow / black / white theme

## Files
- `index.html` — app shell + UI
- `phrases.js` — phrase bank + audio paths (generated)
- `audio/` — Mexican Spanish MP3 clips
- `sw.js` — offline cache
- `manifest.json` — PWA manifest
- `icon.png` — app icon
- `scripts/build_content.py` — regenerate phrases + audio
- `scripts/assemble_html.py` — rebuild `index.html`

## Run locally

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit `http://127.0.0.1:8000`.

## Deploy
- **GitHub Pages:** push to `main` runs `.github/workflows/deploy-pages.yml`. In repo **Settings → Pages**, set Source to **GitHub Actions** once.
- **Cursor publish:** use the Publish control on the agent chat for a hosted preview.

## Regenerate audio

```bash
pip install edge-tts
python3 scripts/build_content.py          # skip existing clips
python3 scripts/build_content.py --force  # rebuild all clips
python3 scripts/assemble_html.py
```
