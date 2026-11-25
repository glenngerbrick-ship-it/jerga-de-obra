# Jobsite Spanish

Practical Spanish for construction, welding, and trades jobsites — the phrases crews actually yell, not tourist textbook lines.

## Features
- Category browsing (Safety, Tools, Welding, and more)
- Search across Spanish, English, and tips
- **Flip cards** — tap to reveal, mark known, shuffle
- Drill mode with ES→EN / EN→ES, streaks, and score tracking
- Device TTS pronunciation (Mexican Spanish) with speed control
- Add / delete your own crew slang (saved locally)
- Speak mode to hear and save phrases
- Offline-ready PWA (service worker + manifest)
- High-vis safety yellow / black / white theme

## Files
- `index.html` — full app
- `sw.js` — offline cache
- `manifest.json` — PWA manifest
- `icon.png` — app icon

## Run
Open `index.html` in a browser, or serve the folder locally:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:8000`.
