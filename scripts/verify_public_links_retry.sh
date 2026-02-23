#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MAX_WAIT_SECONDS="${1:-600}"   # default 10 min
INTERVAL_SECONDS="${2:-30}"    # default 30 sec

start=$(date +%s)

while true; do
  echo "[verify] running public link check..."
  if "$ROOT/scripts/verify_public_links.sh"; then
    echo "[verify] PASS: all public links are reachable"
    exit 0
  fi

  now=$(date +%s)
  elapsed=$((now - start))
  if (( elapsed >= MAX_WAIT_SECONDS )); then
    echo "[verify] FAIL: timeout after ${elapsed}s waiting for all public links to return 200"
    exit 1
  fi

  remaining=$((MAX_WAIT_SECONDS - elapsed))
  echo "[verify] not ready yet; retrying in ${INTERVAL_SECONDS}s (remaining ${remaining}s)"
  sleep "$INTERVAL_SECONDS"
done
