#!/usr/bin/env bash
set -euo pipefail

BASE="https://jmcun777.github.io/blog-writer"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Checking review page..."
code=$(curl -o /dev/null -s -w '%{http_code}' "$BASE/review.html?ts=$(date +%s)")
[[ "$code" == "200" ]] || { echo "FAIL: review.html => $code"; exit 2; }

echo "Checking article links from local dist..."
count=0
while IFS= read -r d; do
  b=$(basename "$d")
  c=$(curl -o /dev/null -s -w '%{http_code}' "$BASE/dist/$b/?ts=$(date +%s)")
  if [[ "$c" != "200" ]]; then
    echo "FAIL: $b => $c"
    exit 3
  fi
  echo "OK: $b"
  count=$((count+1))
done < <(find "$ROOT/dist" -mindepth 1 -maxdepth 1 -type d | sort)

echo "PASS: $count article URLs are publicly reachable"
