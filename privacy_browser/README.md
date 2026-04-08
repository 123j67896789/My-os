# Privacy Browser Proxy Starter

This folder provides a minimal HTTP proxy service intended as a building block for a surveillance-resistant browsing workflow.

## Run

```bash
python3 secure_proxy.py --host 127.0.0.1 --port 8080
```

Configure your browser's manual proxy to `127.0.0.1:8080` for HTTP traffic.

## What it does

- Requires absolute proxy URLs (`http://...` or `https://...`).
- Strips a set of identifying forwarding headers.
- Blocks local/private destination ranges by default.
- Supports GET/POST/HEAD starter paths.

## Limitations

- `CONNECT` tunneling is not yet implemented.
- No traffic obfuscation/pluggable transport yet.
- No built-in anti-fingerprinting user-agent management yet.

## Next hardening steps

1. Implement CONNECT with policy checks and audited socket tunneling.
2. Add upstream SOCKS5 chaining support.
3. Add per-site isolation and stronger header normalization.
4. Add integration tests for leak prevention.
