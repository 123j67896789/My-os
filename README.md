# My-OS (Starter Kit)

This repository now contains a **realistic starting point** for building a modern desktop operating system project with:

- a long-term architecture plan for a Windows-class OS,
- a practical Windows application compatibility launcher (via Wine/Proton), and
- a privacy-oriented proxy browser bootstrap for users in high-surveillance environments.

> Important: building a full Windows replacement takes a large team and years of work. This project is intentionally scoped as a strong foundation you can evolve.

## What is included

1. **Architecture blueprint**: `docs/architecture.md`
2. **Windows app/game launcher script**: `scripts/launch_windows_app.sh`
3. **Privacy proxy browser starter**:
   - `privacy_browser/secure_proxy.py`
   - `privacy_browser/README.md`

## Quick start

### 1) Launch a Windows `.exe`

```bash
bash scripts/launch_windows_app.sh ./SomeApp.exe
```

Optional environment variables:

- `COMPAT_TOOL=wine|proton|auto` (default: `auto`)
- `PROTON_PATH=/path/to/proton`
- `WINEPREFIX=~/.local/share/myos/wineprefix`

### 2) Run the privacy proxy

```bash
python3 privacy_browser/secure_proxy.py --host 127.0.0.1 --port 8080
```

Then set your browser proxy to `127.0.0.1:8080`.

## Security note

The proxy starter is intentionally conservative:

- strips identifying headers,
- blocks local/private destination ranges by default,
- allows only HTTP/HTTPS target schemes.

This is a foundation, **not** a full anti-censorship product. Harden further before real-world high-risk use.
