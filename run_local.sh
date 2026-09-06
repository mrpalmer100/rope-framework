#!/usr/bin/env bash
# Local runner for ROPE 54-grid marches (MacBook, no reap window).
# Usage: ./run_local.sh benchmarks/foundations/gr54a_43.py
# Runs the driver repeatedly (one unit of work per invocation) until it
# prints a COMPLETE / REFUSED / verdict line. Logs to logs/<driver>.log.
# Then send analysis/<name>_ckpt.pkl back to the session for the
# verdict step. Requires: python3, numpy, scipy, pyyaml.
set -u
DRV="$1"; NAME=$(basename "$DRV" .py); mkdir -p logs
export SJ_MEMO=${SJ_MEMO:-1}          # 16 GB: full memos are fine
while true; do
  python3 -u "$DRV" 2>&1 | tee -a "logs/$NAME.log" | tail -3
  if grep -qE "COMPLETE|REFUSED|RESOLVED|run the verdict" "logs/$NAME.log"; then
    echo "[$NAME] done -- send analysis/ckpt back to the session"; break
  fi
  ls -t /tmp/sjjac_* 2>/dev/null | tail -n +3 | xargs -r rm   # prune J memos
done
