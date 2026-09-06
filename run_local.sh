#!/usr/bin/env bash
set -u
DRV="$1"; NAME=$(basename "$DRV" .py); mkdir -p logs
PY=${PY:-python3}; export SJ_MEMO=${SJ_MEMO:-1}; fails=0
while true; do
  "$PY" -u "$DRV" >> "logs/$NAME.log" 2>&1; rc=$?
  tail -2 "logs/$NAME.log"
  if [ $rc -ne 0 ]; then fails=$((fails+1)); [ $fails -ge 3 ] && { echo "[$NAME] failing -- see logs/$NAME.log"; exit 1; }; sleep 2; continue; fi
  fails=0
  grep -qE "COMPLETE|REFUSED|RESOLVED|run the verdict" "logs/$NAME.log" && { echo "[$NAME] done"; break; }
  ls -t /tmp/sjjac_* 2>/dev/null | tail -n +3 | xargs -r rm
done
