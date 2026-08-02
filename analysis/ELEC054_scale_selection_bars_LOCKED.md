# ELEC-054 — Standing-wave scale selection: locked bars (before computation)

## The problem, stated exactly
The surviving hbar route (HBAR-001) gives S = pi T A^2 / (2c), with L CANCELLING.
So hbar fixes ONE number: the amplitude A_hbar = sqrt(2 hbar c / (pi T0)).
Everything else about the mode is free. The open problem is therefore not
"derive hbar" but: WHY DOES THE MEDIUM OSCILLATE AT THAT AMPLITUDE?
Currently A is read backward out of hbar. A solution runs forward: medium
properties -> preferred amplitude -> hbar as consequence.

## The target, in the medium's own units (computed and fixed here)
A_hbar / w = 59.60 (Sigma-route, T0 = 1700) or 70.85 (lattice-anchored,
T0 = 1203), with w = a/sqrt(3) exactly (ELEC-053, scale-set invariant).
KEY STRUCTURAL FACT, locked before testing: the ratio is NOT invariant across
the two registered scale sets (they differ by 19%). Therefore ANY mechanism
producing a PURE NUMBER for A/w would DISCRIMINATE between the scale sets --
i.e. would select Sigma from theory, doing what the corpus has been waiting
on polarimetry to do. That is the payoff structure of this problem.

## Locked candidate list (no candidate may be added after results are seen)
M1 RELATIVISTIC CEILING: linear-string transverse speed v_max = A omega with
   omega = pi c / L. Demand v_max <= c. Test whether this selects A, and
   report what it constrains if it does not.
M2 AMPLITUDE = SPACING (HBAR-003 Q2 restated): A = w.
M3 THERMAL/EQUIPARTITION: A from an energy scale in the medium.
M4 ANHARMONIC TURNING POINT: the inter-strand potential U = C/w^2
   (HBAR-007/008) departs harmonic at excursion ~ w.
M5 COLLECTIVE COUNT: hbar = n S_1, S_1 = pi T w^2/(2c), n an INTEGER strand
   count. Test integrality AND state the precision needed to test it.

## Locked verdict rules
B1 A candidate SELECTS only if it yields A/w from medium properties alone,
   within the 7% scale uncertainty, WITHOUT hbar as input. Reproducing the
   target by algebra that already contains hbar is a RESTATEMENT, not a
   selection, and must be labelled so.
B2 NUMEROLOGY IS INADMISSIBLE, declared in advance: a numerical coincidence
   between A/w and any constant combination counts for NOTHING unless it
   arises from a stated mechanism. No post hoc constant-hunting.
B3 Any constraint a failed candidate DOES yield (bounds on L, on the patch,
   on precision) is registered as a positive byproduct with its propagation.
B4 Expected outcome is a negative. If all five fail, the claim registers the
   failure and the SHARPENED TARGET: what a mechanism must produce.
