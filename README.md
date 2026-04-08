# My-OS: Web Desktop + OS Roadmap

This project now ships as a **GitHub Pages-friendly web desktop** while keeping the broader goal of a Linux-based operating system with Windows app compatibility.

## What you get

- A web desktop shell (`index.html`) that looks and behaves like a lightweight operating system UI.
- A built-in **Scramjet Browser** app slot in the desktop environment.
- Existing Linux compatibility launcher to run Windows apps/games via Wine or Proton.
- OS architecture roadmap in `docs/architecture.md`.

## Run locally

Open `index.html` in a browser, or serve it:

```bash
python3 -m http.server 8080
```

Then visit `http://127.0.0.1:8080`.

## Deploy to GitHub Pages

1. Push this repo to GitHub.
2. In **Settings → Pages**, set source to:
   - **Deploy from branch**
   - branch: `main` (or your default)
   - folder: `/ (root)`
3. Save. GitHub Pages will publish the web desktop.

The `.nojekyll` file is included for static asset compatibility.

## Windows app and game support (Linux runtime)

Use the compatibility launcher:

```bash
bash scripts/launch_windows_app.sh ./SomeApp.exe
```

Environment options:
- `COMPAT_TOOL=auto|wine|proton`
- `PROTON_PATH=/path/to/proton`
- `WINEPREFIX=~/.local/share/myos/wineprefix`

## Important note

A full Windows-scale OS cannot be fully implemented as a static website. This repo keeps both:
1. a runnable GitHub Pages desktop experience, and
2. a real OS development path via documentation and compatibility tooling.
