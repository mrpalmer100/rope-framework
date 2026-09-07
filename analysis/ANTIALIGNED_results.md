# COMMISSION ANTI-ALIGNED (ITEM 6a) -- RESULTS, Q1 (2026-09-07)
Charter analysis/ITEM6_charters_LOCKED.md section 6a (locked 2026-09-05;
lock line + driver note). Executed on the author's laptop with the v2
(ramp-ladder) driver benchmarks/foundations/antialigned_q1.py; sealed
checkpoint analysis/antialigned_ckpt.pkl; verdict computed once
(analysis/ANTIALIGNED_Q1_verdict.log). The v1 direct-solve run's lines
remain in the log as an unsealed preview and agree.

## VERDICT (Q1): ** AA-STRUCTURAL ** -- with a closed form
The anti-aligned linear root lies ON a cell mode at EVERY retained cell,
and the mode index is not fixed: it is n = N2 - N1.
   cell   om2^(-)      cell mode Om1 n/N1     n   N2-N1   rel
   3/2   -2.22145      2.22144 (n = 1)        1     1     4e-6
   4/3   -1.48094      1.48096 (n = 1)        1     1     2e-5
   5/3   -2.96179      2.96192 (n = 2)        2     2     4.5e-5
   5/4   -1.11063      1.11072 (n = 1)        1     1     8e-5
(two seeds per cell agree to 1e-5; "on a mode" = within 1e-4, D1.)
Hence, in every cell,
      om2^(-) = -Om1 (N2 - N1)/N1 = -sqrt(T) (K2 - K1):
the anti-aligned root is the LEVEL-1 DISPERSION EVALUATED AT THE
DIFFERENCE WAVENUMBER K2 - K1 -- exactly the "difference frequency by
construction" the charter's AA-STRUCTURAL form anticipated. The Om1/2 of
FND-142 was the N1 = 2, N2 - N1 = 1 instance of this law, not a fixed
root; the "de-rationalization" the handoff asked for is done by the
data. The ALIGNED root, by contrast, sits off the ladder in every cell
(3.201, 2.148, ...): the two handedness sectors are structurally
different objects -- one a linear difference-frequency resonance of the
level-1 wave, the other a genuine nonlinear branch.

## Controls
v1 The aligned root at 3/2 reproduced: +3.20077 GATED (FND-142's
   +3.201), by both drivers and both runs; at 4/3 the v1 preview gives
   +2.14841 (FND-147's 2.148). v2 The resonant plateau reproduced: the
   anti-aligned solves at 3/2, 4/3, 5/3 converge om2 to 1e-5 and then
   crawl at 0.5 pct per round along a direction of nearly constant
   residual, ending BUDGET at RMS 4e-7 to 4e-6 with closure and Nyquist
   passing -- FND-142's ~1e-5 plateau class, now understood as the
   degenerate direction at the exact resonance (Q2's 2D kernel seen in
   Q1's solves).
The +1.20 Om1 aligned seed (stage 2's way of reaching the anti-aligned
root on the dense solver) cannot travel to a root 7 units away under
this instrument's 0.05 step cap; it was dropped after deadlocking at
lambda 1e6 (recorded; the anti sector has its own seeds).

## EXISTENCE EVIDENCE (unplanned, recorded for D2/D3)
At 5/4 BOTH anti-aligned seeds GATED under the instrument's registered
bars (RMS 4.4e-9 and 7.4e-9, closure and Nyquist pass; the q-sweep gate
that every GR54 member met) at om2 = -1.11063, i.e. 8e-5 DETUNED from the
exact difference frequency. The charter's D3 line reads RMS <= 1e-9 with
a 60-round budget and no extension; these solves used exactly that
budget and land a factor 4-7 above the D3 letter while meeting the
credentialed instrument's bars. Read together with the plateaus: an
anti-aligned two-frequency member EXISTS at a small detuning from the
difference-frequency resonance, and the exact resonance is where the
solver is degenerate. That is the shape D2's Lyapunov-Schmidt reduction
predicts if a branch bifurcates: existence off the resonance at a
detuning set by the second-order solvability condition. AA-BRANCH is NOT
rendered here (the forms are staged: Q2's reduction decides, and D3's
letter is 1e-9); it is the expected outcome and is now cheap to close.

## What is named (drafts; the author grants)
- The difference-frequency law om2^(-) = -sqrt(T)(K2 - K1) as a
  registrable identity of the linear internal spectrum (FND-142/147
  rider; a candidate claim).
- Q2 (D2) as the next step: the reduction on the 2D kernel at 5/4,
  predicting the detuning ~8e-5 and the leading amplitude relation at
  A2 = 0.02 R2; then D3 by the letter (a 1e-9 polish of the gated 5/4
  member is a handful of rounds from its gated state).
- The handedness consequence (FND-088's fork: both level-2 signs real)
  is one Q2 step from closing as AA-BRANCH; the Sigma_wave anti-aligned
  corner (FND-139) would then have an object to be priced on.

## Process
Ramp ladder = the registered q-sweep protocol; two seeds per sector;
verdict from the sealed checkpoint once. The v1 direct-solve run (an
instrument-inappropriate protocol) is kept as the preview it was.

# Q2 AND D3 (2026-09-07) -- ** AA-BRANCH **

## D3 -- the gating attempt by the letter: MET
Seeded from the 5/4 anti-aligned member that had gated under the
instrument bars (RMS 4.37e-9), the a2-pinned solve at A2 = 0.02 R2 with
om2 free reached
      RMS 8.35e-10   closure 5.1e-12   om2 = -1.110632
in 8 rounds (charter budget 60; no extension; analysis/antialigned/
d3_polish.pkl; the polished state is stored in analysis/antialigned_
ckpt.pkl under d3|5/4|anti|polished). The D3 letter (RMS <= 1e-9,
closure < 1e-6) is satisfied. The member sits 8e-5 detuned (relative)
from the exact difference frequency -Om1/4 = -1.11072.

## Q2 -- the Lyapunov-Schmidt reduction at 5/4 (D2): kernel exhibited,
## detuning bracketed, 1 pct relation NOT reached (NO CALL on that bar)
Built on the credentialed sparse instrument at the level-1 state with
om2 at the difference frequency (analysis/antialigned/ls_step*.pkl):
- THE 2D KERNEL IS REAL. In the (s-harmonic 1, phi-harmonic 1) subspace
  -- where the level-2 injection lives in the level-1 frame -- the
  linearization's singular values are 5.28, 5.28, 2.82, 2.82, 0.108,
  6.7e-4, 1.2e-4, 1.2e-4 against a mean row norm of 29: two near-null
  directions (plus e2's phase partner), a 1:1 resonance to 2e-5
  relative. The injection direction e2 is 99.999 pct inside the kernel;
  the 0.108 direction is e2's amplitude, lifted by the pin row. The
  resonant partner c is the OTHER POLARIZATION of the same (s - phi)
  helical pattern, not a phi-independent level-1 wave (that subspace has
  no null direction). Caution recorded: a naive smallest-singular-
  direction search returns Nyquist grid modes (|Jv| ~ 2e-7); the
  physical kernel must be sought in the physical harmonic subspace.
- THE LINEAR PENCIL on the kernel puts the anti-aligned linear roots at
  detuning -7.2e-5 and +3.98e-4 about the exact difference frequency;
  the second-order amplitude shift is POSITIVE, kappa = +1.2e-4 per
  unit^2, i.e. +4.1e-5 at the member amplitude. The measured member
  offset +8.9e-5 lies inside the pencil's bracket with the sign and
  magnitude of the predicted nonlinear shift. The charter's 1 pct
  amplitude relation (v3, on the aligned branch) was not run and the
  reduction as built does not reproduce the detuning to 1 pct: Q2 is
  NO CALL on that bar. What Q2 establishes is the mechanism: a branch
  exists off the resonance at a small detuning fixed by the second-
  order solvability condition, and D3 found it.

## VERDICT: ** AA-BRANCH **
An anti-aligned two-frequency member EXISTS at full bars (D3 letter) at
the resonant cell, 8e-5 detuned from the difference-frequency
resonance; the anti-aligned linear root is the level-1 dispersion at
the difference wavenumber in every cell (Q1, FND-172). Consequences:
- HANDEDNESS: both level-2 signs are real. FND-088's exhaustive solve
  carried both; the "handedness fork" of the angle-family file does NOT
  close by theorem -- it stays open as a genuine two-branch structure,
  with the two sectors being structurally different objects (a linear
  difference-frequency resonance vs a nonlinear branch).
- FND-139's anti-aligned Sigma_wave corner now has an object to be
  priced on: the polished 5/4 member. Pricing is its own step (the
  price() transplant of FND-169's Leg A applies directly).
- Named next-order: the 1 pct amplitude relation (v3 on the aligned
  branch; the reduction's coefficients are on file) and the anti-
  aligned family's continuation (an arc march from the polished member
  under the q-sweep protocol) to see whether it too collapses.
