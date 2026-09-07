#!/usr/bin/env bash
# self-contained launcher: loops the driver with the venv python until it prints a terminal line
DRV="$1"; NAME=$(basename "$DRV" .py); mkdir -p logs
PY=$HOME/rope-venv/bin/python; export SJ_MEMO=${SJ_MEMO:-1}
pkill -f "$NAME" 2>/dev/null; sleep 1
nohup bash -c '
  fails=0
  while true; do
    "'"$PY"'" -u "'"$DRV"'" >> "logs/'"$NAME"'.log" 2>&1; rc=$?
    if [ $rc -ne 0 ]; then fails=$((fails+1)); [ $fails -ge 3 ] && { echo "['"$NAME"'] failing -- see logs/'"$NAME"'.log" >> "logs/'"$NAME"'.log"; exit 1; }; sleep 2; continue; fi
    fails=0
    grep -qE "COMPLETE|REFUSED|RESOLVED|run the verdict" "logs/'"$NAME"'.log" && exit 0
    ls -t /tmp/sjjac_* 2>/dev/null | tail -n +3 | xargs rm -f
  done' > /dev/null 2>&1 &
echo "launched $DRV -> logs/$NAME.log"
