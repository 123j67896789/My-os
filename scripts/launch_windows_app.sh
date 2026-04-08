#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 /path/to/app.exe [extra args...]" >&2
  exit 1
fi

APP_PATH="$1"
shift || true

if [[ ! -f "$APP_PATH" ]]; then
  echo "Error: file not found: $APP_PATH" >&2
  exit 1
fi

COMPAT_TOOL="${COMPAT_TOOL:-auto}"
WINEPREFIX="${WINEPREFIX:-$HOME/.local/share/myos/wineprefix}"

mkdir -p "$WINEPREFIX"
export WINEPREFIX

run_wine() {
  if ! command -v wine >/dev/null 2>&1; then
    echo "Error: wine is not installed." >&2
    return 1
  fi
  echo "[my-os] Launching via Wine"
  exec wine "$APP_PATH" "$@"
}

run_proton() {
  local proton_bin="${PROTON_PATH:-}"

  if [[ -z "$proton_bin" ]]; then
    if command -v proton >/dev/null 2>&1; then
      proton_bin="$(command -v proton)"
    fi
  fi

  if [[ -z "$proton_bin" || ! -x "$proton_bin" ]]; then
    echo "Error: Proton binary not found. Set PROTON_PATH." >&2
    return 1
  fi

  echo "[my-os] Launching via Proton"
  exec "$proton_bin" run "$APP_PATH" "$@"
}

case "$COMPAT_TOOL" in
  wine)
    run_wine "$@"
    ;;
  proton)
    run_proton "$@"
    ;;
  auto)
    if command -v wine >/dev/null 2>&1; then
      run_wine "$@"
    elif command -v proton >/dev/null 2>&1 || [[ -n "${PROTON_PATH:-}" ]]; then
      run_proton "$@"
    else
      echo "Error: neither Wine nor Proton found. Install one of them first." >&2
      exit 1
    fi
    ;;
  *)
    echo "Error: invalid COMPAT_TOOL='$COMPAT_TOOL' (expected: auto|wine|proton)" >&2
    exit 1
    ;;
esac
