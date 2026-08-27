# Q-SWEEP STAGE 1 -- q = 5/3 COLUMN RUNBOOK
# Written 2026-08-23 so any competent operator (human or model) can
# execute the remaining column without this session's context.

## WHAT THIS IS

The q-sensitivity probe (charter:
analysis/QSWEEP_stage1_bars_LOCKED.md, READ IT FIRST -- bars,
amendment 1, and the interpretation rules are locked and binding).
The q = 4/3 column is COMPLETE: branch exists (two gated members),
11-point rate profile, hi march closed under the unreached-target
clause with the rigorous bound D(4/3) >= 5.56 (see
q['hi_unreached'] in the checkpoint). The q = 5/3 column runs the
IDENTICAL protocol; the locked rules then fire on D(4/3) and
D(5/3) together. Do not interpret anything by hand: the rules block
prints the verdict mechanically.

## HOUSE DISCIPLINE (non-negotiable)

- Bars were locked before computing; deviations are recorded in
  daylight in the bars doc or at their code sites with reasons.
- Members cite only if they pass ALL gates (RMS < 1e-8, closure
  < 1e-6, geometry floors, pin where applicable). Rates cite only
  full-bar members.
- Failures stay on the record. Never delete a failed attempt;
  mark it (see q4/3's pre_v5_failed_attempt and
  fine_pin_abandoned for the pattern).
- All grants are the author's. Draft registrations; never register
  without his word.

## THE MACHINE

- Repo: /home/claude/rope/rope (unpacked from the author's zip).
- Benchmark: benchmarks/foundations/qsweep_stage1.py. Every solver
  lesson of the campaign is annotated IN THIS FILE at its site;
  read the annotations before changing anything.
- Checkpoint: /tmp/qsweep_ckpt.pkl -- per-round, per-rung,
  per-member persistence. A killed run resumes losing at most one
  solver round. NEVER edit it while a process is alive (a race
  once resurrected stale state; kill first, verify pgrep count 0,
  then edit).
- Launch (the container reaps detached runs at nearly every tool
  boundary; expect ~1 solve round per call):
    cd /home/claude/rope/rope && setsid flock -n /tmp/qsweep.lock \
      python3 benchmarks/foundations/qsweep_stage1.py \
      >> /tmp/qsweep.log 2>&1 < /dev/null & sleep 270; \
      tail -2 /tmp/qsweep.log
- Code changes: ALWAYS via a patcher file (write /home/claude/
  patch_*.py with create_file, run it in a tiny bash call).
  Heredocs get reaped mid-write and have corrupted the file before
  (a reversed splice once left two gn_lean definitions; check
  grep -c after every patch).
- Memory: 4 GB hard. The solver is built around it (f32 J, blocked
  f64 dsyrk, in-place Cholesky). Do not add dense n x n f64
  temporaries at n = 15554.

## THE SOLVER (gn_lean), AS PROVEN

lm_round-faithful Marquardt: lam * diag(JtJ) damping, exact
Cholesky steps, f64 monotone acceptance, degenerate-basin guard
(A2 >= 0.3 * pin), lam PERSISTED across reaps, closure-aware stop
(gate-facing solves run until RMS AND closure bars), and the
registered FORCING escalation (3 rounds < 25% cumulative ->
alternate exact / deep-lsmr steps; record so far: 5 firings, 5
breakthroughs). Rung ladders on EVERY pin jump (40/70% of the gap):
rungless jumps build closure debt that compounds into a soft bottom
band where exact steps inflate to r/sigma and stall -- measured
five times, never once survived. Do not remove the rungs.

## THE q = 5/3 SEQUENCE (state machine; the code drives itself,
## you mostly relaunch and watch)

1. LEVEL-1 (bar v2): closed-form seed, one or two rounds; check
   the printed [q5/3 level-1 ... PASS]. If HALT, the cell
   construction is wrong -- stop and investigate QGrid(ns, npn,
   3, 5); level-1 physics does not know q.
2. RAMP: m2 injection at the first sub-pin, rung ladder
   0.15/0.3/0.55/0.8 to member 1 (A2 = 0.0018792, gated), then
   runged jump to member 2 (0.0046979, gated). Expect the same
   convergence shape as q4/3: warm-up full steps, lam to floor,
   productive quarter-steps, escalation if it crawls, one
   99%-class Newton snap into the gate. Record om2 per member (the
   cell variable; q4/3 gave 2.1484 -> 2.2154).
3. FINE PIN: the code SKIPS the 0.0063 a2 pin only if you mark
   q['fine'] = None first. RECOMMENDED: mark it None immediately
   (patcher on the ckpt, processes dead), because the q4/3 record
   proved the a2 pin goes blind where dA2/ds shrinks (registered
   q=3/2 never a2-pinned its 0.0063 either); the arc march is the
   faithful route.
4. P3 RATES: arc pairs, ds = 0.08, lo budget 6 around 0.0048,
   then the hi march toward 0.0063. Every gated step prints one
   (A2, dA2/ds) point. ~5 calls per point early; the march
   self-brakes as the rate falls (step dA2 = rate * ds).
5. STOP RULE FOR THE HI MARCH (author-authorized economics): if
   the rate is collapsing and D(5/3)-so-far crosses 5 with the
   decline monotone, close under the unreached-target clause
   exactly as q4/3 did (copy the q['hi_unreached'] pattern with
   the D lower bound and reason; the bound is rigorous because a
   monotonically declining rate at the target is <= the last
   measured rate). If instead the rate HOLDS ~flat past ~0.0055,
   keep marching -- that is the S1-SPLIT branch of the tree, the
   most surprising outcome, and worth the budget; consult the
   author.
6. RULES: rerun the benchmark once both columns carry rates; the
   rules block prints D per column and the verdict form
   (S1-CELL / S1-BRANCH / S1-SPLIT / NO CALL). It handles the
   unreached-target D via nearest(); quote the D values as lower
   bounds where the closure records say so.
7. CLOSE-OUT: export /tmp/qsweep_ckpt.pkl to
   analysis/qsweep_stage1_ckpt.pkl, write
   analysis/QSWEEP_stage1_results.md (trajectories, both D values
   with their status, om2 cell variables, instrument record),
   update SESSION_CHANGES.md, bump version, DRAFT the registration
   and present it for the author's grant.

## KNOWN NUMBERS FOR CROSS-CHECK (q4/3, all gated)

  member 1: A2 0.0018792  RMS 1.89e-9  clos 1.5e-7  om2 2.14842
  member 2: A2 0.0046979  RMS 1.74e-10 clos 1.5e-8  om2 2.21540
  rate profile: 5.806e-4 @ 0.004721 falling to 1.045e-4 @ 0.005042
  (11 points, compounding decline: -2% steps steepening to -32%);
  D(4/3) >= 5.56 (unreached-target closure at best A2 0.005042).
  Registered q=3/2 reference: 6.5e-4 -> 6.8e-5, D ~ 9.6.

## WHAT NOT TO DO

- Do not "fix" a stall by weakening a gate. Gates are bars.
- Do not a2-pin into the small-dA2/ds region.
- Do not run two instances (flock guards, but verify).
- Do not trust f32 vectors at small spectral gaps (FND-146 lesson);
  the f64 arbiter check is in the SVD machinery if needed.
- Do not interpret; the rules block interprets.
