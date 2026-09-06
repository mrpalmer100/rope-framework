# WHY-WINDING STAGE 3 -- RUNBOOK (for any executor, incl. Opus 5)

Charter: analysis/WHYWIND_stage3_bars_LOCKED.md (locked; do not
amend without the author). Executor:
benchmarks/foundations/whywind_stage3.py.

## SEQUENCE
1. `python3 benchmarks/foundations/whywind_stage3.py --credential`
   -- must print eight seed lines. Session baseline (2026-08-28):
   5/3 seeds arrive at ~8e-4 RMS (nearly solved: the flat state is
   smooth and transfers exactly); 4/3 seeds arrive at 1.8e-2 (base)
   and ~1e-1 (probe) -- ROUGH BY NATURE: the deep 4/3 state carries
   the near-Nyquist mode under test, which the transfer perturbs.
   Rough 4/3 seeds are expected, not a fault.
2. Campaign, detached, budgeted:
   `setsid nohup python3 benchmarks/foundations/whywind_stage3.py
    --budget 3000 > /tmp/s3w.log 2>&1 < /dev/null &`
   Rerun the same line to resume; checkpoint /tmp/s3w_ckpt.pkl.
   Solve order: base pairs then probe pairs, 5/3 before... (fixed
   by the GRIDS/members iteration; do not reorder).
3. When all six... all EIGHT members gate (2 grids x 2 cells x 2
   members), the verdict block prints mechanically. Do not
   interpret partial output.

## LESSONS ALREADY INSTALLED (from the stage-1/2 ledgers; verify,
## don't rediscover)
- Rotate lock files if using flock; verify worker RSS before
  trusting a "running" pid; zombie setsid shells can hold locks.
- The f32-J floor sits at ~1e-4 RMS; the endgame switches to f64
  normal equations automatically (resumable_solve does this).
- Keep controls printing. A silent stall is a control not printed.
- Memory: dof 15554 fits the 3 GB container with the f32-J path;
  do NOT attempt 96x72 or 144x72 here (measured infeasible).

## CLOSE-OUT (standing rule)
Export /tmp/s3w_ckpt.pkl to analysis/ BEFORE reporting; append the
verdict block and the eight member metric lines to
analysis/WHYWIND_stage3_results.md; draft registration for the
author; grants reserved to the author; failures kept. If the run
ends S3-F-INSTRUMENT or a member refuses to gate, that outcome is
the deliverable -- record it and stop.
