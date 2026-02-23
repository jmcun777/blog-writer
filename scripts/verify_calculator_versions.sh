#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BASE="https://jmcun777.github.io/blog-writer"
files=(
  calculator-shanghai.html
  calculator-shanghai-style-1.html
  calculator-shanghai-style-2.html
  calculator-shanghai-style-3.html
  calculator-shanghai-style-4.html
)

for f in "${files[@]}"; do
  local_v=$(grep -oP 'name="calc-version" content="\K[^"]+' "$ROOT/$f" | head -n1 || true)
  remote_html=$(curl -sL "$BASE/$f?ts=$(date +%s)")
  remote_v=$(printf '%s' "$remote_html" | grep -oP 'name="calc-version" content="\K[^"]+' | head -n1 || true)
  code=$(curl -o /dev/null -s -w '%{http_code}' "$BASE/$f?ts=$(date +%s)")
  if [[ "$code" != "200" ]]; then
    echo "FAIL $f http=$code"
    exit 2
  fi
  if [[ -z "$local_v" || -z "$remote_v" || "$local_v" != "$remote_v" ]]; then
    echo "FAIL $f version mismatch local=$local_v remote=$remote_v"
    exit 3
  fi
  echo "OK $f version=$local_v"
done

echo "PASS all calculator pages version-matched and reachable"
