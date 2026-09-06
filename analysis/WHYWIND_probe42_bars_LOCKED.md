# WHY-WINDING PROBE 144x42 (option a) -- CONFOUND-FREE RESOLUTION
# PROBE: CHARTER (LOCKED 2026-08-29, before any solve)
# Authorized by the author ("Let's do c"; this is the second half).
# Adjudicates what stage 3 could not: same s-grid as the retained
# states (144), phi 36 -> 42 (Nyquist 18 -> 21). Feasibility of
# record: dof 18146; JtJ f64 2.63 GB against 3.7 GB available; the
# phase-resumable driver (whywind_stage3.py ledger) is the solver.

## OBJECTS
- REQUIRED: the deep 4/3 arc pair (2c states[11], states[12]),
  re-solved at 144x42 under their own A2 pins, stage-1 full bars.
- OPTIONAL CONTROL (run if the container cooperates): the matched
  5/3 pair, same treatment.
- Seeds: phi-only FFT zero-pad 36 -> 42 (s untouched -- the
  confound stage 3 could not avoid is absent by construction).

## LOCKED STATISTIC
BAND(17, 19) exactly as in the stage-3 charter (+-1 index, both
conjugates) on the pair tangent's pt spectrum.
  CREDENTIAL (no re-solve needed; computed on the RETAINED 144x36
  states with the same band function): F17(144x36) -- the reference.
  HIBAND42 = pt mass at |n_phi| in [19, 21] (the new headroom band).

## LOCKED VERDICT LINES
  P42-PHYSICAL: F17(144x42) >= 0.5 x F17(144x36) AND the dominant
      pt mode of the 144x42 tangent lies in the (17, 19) band AND
      HIBAND42 < 0.10.
  P42-ARTIFACT: F17(144x42) < 0.05.
  Between: P42-OPEN. No salvage; no post-hoc lines.

## CONSEQUENCES (in advance)
  P42-PHYSICAL: the amendment rider of WHYWIND_reprice_results.md
      is softened to record band location only; the mechanism
      question re-sharpens to why THIS mode.
  P42-ARTIFACT: the rider hardens; a full re-pricing of the
      FND-150..153 INTERPRETATION (not their rates or D bounds) is
      proposed to the author, and the full stage-3 replication of
      the Q-SWEEP columns goes to the queue head, flagged for the
      Opus 5 handoff.
Grants reserved to the author. Failures kept.
