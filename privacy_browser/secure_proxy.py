#!/usr/bin/env python3
"""A minimal privacy-focused HTTP proxy starter.

Features:
- Forwards HTTP(S) requests from explicit proxy clients.
- Strips common identifying headers.
- Blocks localhost/private-network targets by default.

This is a starter implementation, not a complete circumvention tool.
"""

from __future__ import annotations

import argparse
import ipaddress
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import urllib.request

BLOCK_PRIVATE = True


def is_private_host(hostname: str) -> bool:
    try:
        infos = socket.getaddrinfo(hostname, None)
        for info in infos:
            ip = ipaddress.ip_address(info[4][0])
            if (
                ip.is_private
                or ip.is_loopback
                or ip.is_link_local
                or ip.is_multicast
                or ip.is_reserved
            ):
                return True
    except Exception:
        return True
    return False


class ProxyHandler(BaseHTTPRequestHandler):
    server_version = "SecureProxy/0.1"

    def do_CONNECT(self):
        self.send_error(405, "CONNECT tunnel not supported in starter build")

    def do_GET(self):
        self._handle_http()

    def do_POST(self):
        self._handle_http()

    def do_HEAD(self):
        self._handle_http()

    def log_message(self, fmt, *args):
        return

    def _handle_http(self):
        parsed = urlparse(self.path)
        if parsed.scheme not in ("http", "https"):
            self.send_error(400, "Only absolute http/https URLs are supported")
            return

        host = parsed.hostname
        if not host:
            self.send_error(400, "Missing host")
            return

        if BLOCK_PRIVATE and is_private_host(host):
            self.send_error(403, "Destination blocked by policy")
            return

        out_headers = {}
        for key, value in self.headers.items():
            lk = key.lower()
            if lk in {
                "proxy-connection",
                "connection",
                "x-forwarded-for",
                "forwarded",
                "via",
                "cf-connecting-ip",
                "true-client-ip",
            }:
                continue
            out_headers[key] = value

        out_headers["Connection"] = "close"

        body = None
        if self.command in {"POST", "PUT", "PATCH"}:
            content_length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(content_length) if content_length > 0 else None

        req = urllib.request.Request(
            self.path,
            data=body,
            headers=out_headers,
            method=self.command,
        )

        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                payload = resp.read()
                self.send_response(resp.status)
                for key, value in resp.getheaders():
                    if key.lower() in {"transfer-encoding", "connection", "keep-alive"}:
                        continue
                    self.send_header(key, value)
                self.send_header("Connection", "close")
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(payload)
        except Exception as exc:
            self.send_error(502, f"Upstream request failed: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Minimal privacy proxy starter")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument(
        "--allow-private-targets",
        action="store_true",
        help="Allow requests to private/localhost IP ranges (unsafe)",
    )
    args = parser.parse_args()

    global BLOCK_PRIVATE
    BLOCK_PRIVATE = not args.allow_private_targets

    with ThreadingHTTPServer((args.host, args.port), ProxyHandler) as httpd:
        print(f"Secure proxy listening on {args.host}:{args.port}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
