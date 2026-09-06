# WHY-WINDING STAGE 3 (TARGETED) -- RESULTS: S3-F-INSTRUMENT
# (the credential line refused adjudication; the cross-grid record it
# produced is the product, and it points one way)
# Executed 2026-08-28/29 under analysis/WHYWIND_stage3_bars_LOCKED.md.
# Benchmark: benchmarks/foundations/whywind_stage3.py.
# State: analysis/whywind_stage3_ckpt.pkl (all eight members).

## VERDICT: ** S3-F-INSTRUMENT ** (mechanical)
S3-CRED required F17(96x36) >= 0.20 on the 4/3 tangent; measured
0.042. The baseline did not reproduce the (n=17, m=19) story, so the
locked rules refused any PHYSICAL/ARTIFACT call. (The 5/3 half of the
credential passed: beat-ladder top mode at both grids.)

## THE EIGHT MEMBERS (all full-bar; the campaign's credential)
  grid   cell  member  RMS       clos      A2         om2
  96x36  4/3   prev    9.14e-09  3.77e-07  0.0050380  2.22681
  96x36  4/3   deep    8.97e-09  1.96e-07  0.0050464  2.22684
  96x36  5/3   prev    1.38e-11  9.11e-11  0.0051481  4.32544
  96x36  5/3   deep    1.60e-11  1.49e-10  0.0051922  4.32725
  96x54  4/3   prev    6.59e-09  9.92e-07  0.0050381  2.22621
  96x54  4/3   deep    5.12e-09  3.67e-07  0.0050464  2.22648
  96x54  5/3   prev    4.53e-09  4.60e-11  0.0051482  4.32530
  96x54  5/3   deep    4.85e-09  8.10e-11  0.0051923  4.32711

## THE CROSS-GRID SPECTRAL RECORD (displays; now spanning three grids)
4/3 tangent, dominant pt modes:
  144x36 (retained states): +-(m=19, n=17), 74 pct -- n at
          phi-Nyquist-1 (18)
  96x36  (re-solved):       (m=+45, n=-9) 42 pct, (m=+45, n=+15)
          25 pct -- m at s-Nyquist-3 (48); (17,19) band: 0.042
  96x54  (re-solved):       beat ladder (1,-1) 43 pct, (2,-2) 21 pct,
          (4,-4)/(3,-3) 11 pct each -- the high-harmonic content GONE
5/3 tangent, dominant pt modes:
  144x36: beat ladder (n=k, m=-2k), 25/16/7 pct
  96x36:  beat ladder, 47/31/15/5 pct
  96x54:  beat ladder, 47/31/15/5 pct -- IDENTICAL to 96x36 to three
          figures
The flat cell's spectrum is grid-invariant. The collapsing cell's
high-harmonic winding content sits at whichever grid edge is nearest
and dissolves when the phi band opens: the classic signature of
GRID-SCALE CONTENT CHASING THE NYQUIST, not of a physical mode
holding its harmonic index.

## A SECOND RESOLUTION-SENSITIVITY, FOUND IN THE MEMBER TABLE
om2 at matched members, source (144x36) vs re-solved (96-grids):
  4/3: 2.2154 -> 2.2262..2.2268  (+0.50 pct; the branch moves from
       0.27 pct BELOW Om1/2 = 2.22144 to 0.23 pct ABOVE it)
  5/3: 4.3287 -> 4.3271..4.3273  (-0.03 pct)
The 4/3 cell's om2 drifts 15x more than the 5/3 cell's under the
same s-reduction, and the drift CROSSES the Om1/2 line. The brick-1
proximity coincidence (om2 0.27 pct off Om1/2) is therefore WITHIN
the discretization drift of the collapsing branch: its evidential
weight, already reduced by brick 2a, is reduced further.

## WHY F-INSTRUMENT AND NOT ARTIFACT (stated carefully)
The charter's credential exists because the baseline members are
RE-SOLVED states, not the retained originals: an s-reduction that
reshuffles tangent content invalidates the comparison the probe was
designed to make. That is exactly what happened -- so the run cannot
DISTINGUISH "the (17,19) mode is phi-grid artifact" from "the 4/3
deep tangent's content is generically unstable under ANY grid
change". Both readings, however, share the operative conclusion:
THE 4/3 DEEP-END WINDING CONTENT IS NOT GRID-STABLE, while the 5/3
content is. No registered claim is re-priced by this stage (its
locked scope); but the interpretation of FND-150..153's deep-end
f_dir now carries a REGISTERED DOUBT, and the re-pricing commission
contemplated in the charter's consequences is recommended to the
author as OWED.

## INSTRUMENT LEDGER (this stage; all annotated at code sites)
- Rounds-cap budget exits mis-marked as failures; fixed (budget exit
  vs stall distinguished; sweeps resume open members).
- Container reaps workers on a ~10-min cadence, silently; watchdog
  relaunch + rolling checkpoints installed.
- pgrep -f matches the monitoring shell itself; liveness by ps.
- 15554-dof jac build exceeds the reap window: livelock; fixed with
  a chunk-resumable disk-memmap jac (numerics identical).
- Normal-matrix accumulation also exceeds the window; fixed with a
  phase-resumable LM driver (f64 accumulation on disk, damped
  Cholesky, f64-residual acceptance; solver path differs from
  gn_exact -- bars judge the state, not the path). The driver gated
  all four probe members in 10-12 rounds each.
- Feasibility correction of record: 144x54 is NOT memory-feasible
  here (JtJ f64 = 4.35 GB vs 3.7 GB available); the largest
  confound-free follow-up grid is 144x42 (dof 18146, JtJ 2.63 GB,
  phi-Nyquist 21).

## FOLLOW-UP OPTIONS (unchartered; the author's call)
  (a) CONFOUND-FREE PROBE: re-solve the deep 4/3 pair at 144x42
      (same s-grid as the retained states; phi-Nyquist 21). If
      (17,19) is physical it survives; if artifact, it migrates
      into 18..21 or dissolves. Thin headroom band, but the
      s-confound is gone entirely. ~2 members, feasible with the
      phase-resumable driver.
  (b) RE-PRICING COMMISSION over FND-150..153's interpretation:
      recompute f_dir/V_pt on the retained 144x36 profile with the
      pt content split into a resolved band (|n| <= 12, say --
      bar to be locked) and a Nyquist band, and re-state the
      registered mechanism sentence against the resolved band
      only. Desk-cheap; no solves.
  (c) Both, (b) first.
Recommendation recorded: (c). Grants reserved to the author.
Failures kept.
