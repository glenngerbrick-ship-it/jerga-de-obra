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

## Regenerate audio

```bash
pip install edge-tts
python3 scripts/build_content.py
python3 scripts/assemble_html.py
```
