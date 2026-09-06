# WHY-WINDING PROBE 144x42 -- RESULTS: NO VERDICT; REFUSAL RECORDED
# Executed 2026-08-29 under WHYWIND_probe42_bars_LOCKED.md.
# Benchmark: benchmarks/foundations/whywind_probe42.py (+ the
# resumable_lm amendments in whywind_stage3.py, ledger-annotated).
# State: analysis/whywind_probe42_ckpt.pkl.

## OUTCOME
  p42|4/3|prev:  GATED. RMS 6.81e-09, clos 3.15e-07, A2 on pin,
                 om2 2.22712 (again above Om1/2; see stage-3 note).
  p42|4/3|deep:  ** REFUSES TO GATE. ** Recorded after two bounded
                 attempts, per the plan agreed with the author:
                 (1) f32-jac campaign: limit cycle at RMS 2.3e-07,
                     step rejections in the small-damping window its
                     gated sibling passed through;
                 (2) f64-jac endgame (option (ii), 10-round budget):
                     RMS crept 2.3e-07 -> 2.0e-07 while the state
                     SLID OFF ITS CONSTRAINTS -- A2 drifted to
                     0.0050447 (pin 0.0050464), closure degraded to
                     6.8e-05 (bar 1e-06). The weighted objective
                     trades constraint satisfaction against field
                     residual: a residual valley, not a solution
                     approach.
  The P42 verdict lines therefore CANNOT RENDER (the required pair
  never existed at full bar). Per the standing runbook rule, the
  refusal is the deliverable. No spectrum was computed on any
  144x42 state; the F17 reference was never taken; nothing was
  peeked.

## THE FINDING THIS LEAVES (proposed for registration)
The q = 4/3 deep member now shows GRID FRAGILITY on five
independent instruments, none of which was designed to find it:
  1. Spectral seed transfer roughness (stage-3 credential: 1e-1 RMS
     arrival vs the flat cell's 8e-4);
  2. Tangent spectrum chasing the nearest grid edge across
     144x36 / 96x36 / 96x54 (stage-3 record);
  3. om2 placement drifting +-0.5 pct and crossing Om1/2 under
     grid change (stage-3 member table; reconfirmed here: the
     GATED prev member's om2 moved to 2.22712);
  4. The registered winding demand living entirely in the
     phi-Nyquist band (RP-FALLS, re-pricing);
  5. Refusal of the deep member itself to re-solve at full bar on
     a phi-refined grid, under two Jacobian precisions, while its
     arc-pair sibling gated on the same grid in 11 rounds.
The flat q = 5/3 cell is unremarkable on every one of these axes.
Whether the deep 4/3 state is a discretization object (an artifact
of the 144x36 grid that has no 144x42 counterpart at this pin) or
a physical state whose short-wavelength structure defeats this
container's solver cannot be separated HERE. Both readings agree
on the operative point: THE DEEP-END COLLAPSE PHENOMENOLOGY OF
FND-150..153 IS NOT GRID-ROBUST, and its interpretation must say
so. The amendment rider of WHYWIND_reprice_results.md HARDENS
accordingly (rider text unchanged; its OPEN clause now points at
this refusal rather than at a pending probe).

## QUEUE CONSEQUENCE (per the charter's spirit; the author decides)
Full stage-3 resolution replication of the Q-SWEEP columns moves to
the queue head, flagged for the Opus 5 handoff WITH a hardware
note: this container's 3.7 GB / reap-window regime is the binding
constraint; the refusal should be retried once on a machine where
144x54+ is feasible before being treated as state-intrinsic.

## OPTIONAL CONTROL (running at close-out)
The 5/3 pair at 144x42 gated effortlessly on the same grid and
solver that refused the 4/3 deep member -- the contrast credential:
  p42|5/3|prev:  GATED, 9 rounds. RMS 4.57e-09, clos 1.49e-10,
                 A2 on pin, om2 4.32669 (drift 0.03 pct).
  p42|5/3|deep:  GATED, 9 rounds. RMS 4.80e-09, clos 1.35e-10,
                 A2 on pin, om2 4.32855 (drift 0.03 pct).
The flat cell re-solves anywhere, including at the pin amplitude
where the collapsing cell's member refuses.

Grants reserved to the author. Failures kept.
