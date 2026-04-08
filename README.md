# My-OS: Direct-to-Desktop Web OS + Native Roadmap

My-OS now **boots directly into the desktop UI** so users land in the OS immediately, with Scramjet Browser opened by default.

## Quick start

```bash
python3 -m http.server 8080
```

Open `http://127.0.0.1:8080` and you will be dropped straight into My-OS.

## Included

- Direct boot overlay -> desktop handoff (`index.html`, `app.js`, `styles.css`)
- Scramjet Browser as default app window
- GitHub Pages static deployment compatibility
- Linux Windows app/game compatibility launcher (`scripts/launch_windows_app.sh`)
- Native OS architecture plan (`docs/architecture.md`)

## GitHub Pages deploy

1. Push repo to GitHub.
2. Settings -> Pages -> Deploy from branch.
3. Select default branch + `/ (root)`.
4. Save.

`.nojekyll` is included.
