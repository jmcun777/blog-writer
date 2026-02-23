#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
[ -f "$DIR/.env" ] && source "$DIR/.env"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <rows.json>"
  exit 1
fi

JSON_PATH="$1"
if [ ! -f "$JSON_PATH" ]; then
  echo "JSON file not found: $JSON_PATH"
  exit 1
fi

: "${N8N_WEBHOOK_URL:?N8N_WEBHOOK_URL is required in .env}"
RUN_ID="${RUN_ID_PREFIX:-china-olympics}-$(date +%Y%m%d-%H%M%S)"

PAYLOAD=$(python3 - <<'PY' "$JSON_PATH" "$RUN_ID"
import json,sys,datetime
path=sys.argv[1]; run_id=sys.argv[2]
rows=json.load(open(path,encoding='utf-8'))
print(json.dumps({
  "task_name":"china_olympics_medalists",
  "run_id":run_id,
  "row_count":len(rows),
  "rows":rows,
  "sent_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()
},ensure_ascii=False))
PY
)

if [ -n "${N8N_AUTH_HEADER:-}" ]; then
  curl -sS -X POST "$N8N_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -H "$N8N_AUTH_HEADER" \
    -d "$PAYLOAD"
else
  curl -sS -X POST "$N8N_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD"
fi

echo
echo "[OK] sent run_id=$RUN_ID"
