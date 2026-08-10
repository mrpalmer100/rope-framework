# COMMISSION Y RESULTS: CANONICAL ACTION vs ENERGY DRESSING (2026-08-06)
# Bars: charter Y (blind-first, linear/quadratic physics gate, second
# prediction as arbiter, scope cap two computations on the committed W
# solution). Verification: y_action_vs_energy.py (primary),
# y_eps4_robustness.py (convention and mesh audit). D_E reproduced to the
# committed 1.1051029 before any Y quantity was computed. All Y quantities
# were printed before their comparison lines.

## VERDICT: OUTCOME 3 (RECTIFICATION LEAD), SHARPENED.
## The 4/pi is NOT produced mechanically by the W solution (the physics gate
## falsifies the only internal rectification source the solver owns). But the
## second prediction, computed anyway as the charter demands, lands within 9%
## of the reviewer's eps_4 and moves the alpha residual from +179 ppm to
## -15 ppm under the profile-overlap convention. Close to the bar, not under
## it, and honestly convention-dependent. Not graduated. Not dead.

## PART 1 -- THE LINEAR/QUADRATIC GATE (the decisive negative)
The committed solution's strain is tiny everywhere: energy-median g = 1e-4,
energy-weighted response exponent n_bar = 2.0000, fraction of elastic energy
in the g > 1 linear regime = 0.0000. The elastic law eps = sqrt(1+g^2)-1 is
purely QUADRATIC on this solution. Therefore the solver's own physics
contains NO rectified linear response: there is no mechanism inside the W
solution by which the canonical action could differ from the energy by 4/pi.
The cycle integrals confirm this by reduction: computed numerically on the
solution, the linear/quadratic cycle ratio is exactly the trig identity
(<|cos|+|sin|>)/(<cos^2+sin^2>), carrying no profile content whatsoever. The
4/pi is not derived from this solution; it is a property a COUPLING would
have to impose (integral of |cos chi| dchi = 4 versus cos^2 dchi = pi in the
final angular closure). The prefactor question, 4 pi^3 versus pi^4, is
therefore EXTERIOR to the W solver and cannot be decided by it. Registered
as the sharp boundary of this route.

## PART 2 -- D_J
Under the charter's own gate, D_J = D_E on this solution: the canonical
momentum of a quadratic-regime rotating configuration carries no
rectification. The hypothesis "D_J/D_E = 4/pi falls out mechanically from
the W solution" is FALSIFIED, cleanly, by the gate the charter itself set.

## PART 3 -- THE SECOND PREDICTION (computed regardless, per charter)
Conditional frame: IF alpha couples to the rectified response (which Part 1
shows must be imposed by the coupling, not derived from the solver), the
rectified series (|cos|+|sin|) has exact harmonics h_m = 2(-1)^(m+1)/
(16 m^2 - 1), leading h_1 = 2/15. The 4-Omega drive was applied to the
linearized EL operator around f0 (numerical Jacobian, residual check 1e-11,
inertial (4 m Omega)^2 term included), unit-drive susceptibilities chi_m
computed, and the physically standard second-order correction formed:
Delta = (1/2) sum h_m^2 chi_m.

Results (mesh-converged across N = 2000/3000/4500, spread < 0.1%):
- Profile-overlap convention (rotational weight and plain norm agree to all
  digits shown, because f4_unit is very nearly proportional to f0):
  Delta = 1.939e-4, equivalent eps_4 = 15 Delta = 0.00291.
  Reviewer's proposed eps_4 = 0.00268. Agreement to 8.5%.
  1/alpha = 4 pi^3 D_E (1 - Delta) = 137.033937 -> residual -15.1 ppm.
- m = 1 only: -12.1 ppm (higher harmonics contribute ~3 ppm, same sign).
- Energy-pairing convention (the sign-definite second-order energy shift,
  normalized by the dressing excess E_el - LOG):
  Delta = 6.3e-4 -> residual -450 ppm (overshoots by ~3.5x).

Plain statement: the derived f4 correction has the right sign, the right
order, and under the overlap convention the right magnitude to within 9%,
compressing the residual 12x (from +179 ppm to -15 ppm). It does NOT close
to < ppm anywhere in the audited convention space, and the convention
dependence (a factor ~3 between defensible pairings) is itself a result:
the chain is missing the derivation that would FORCE one pairing.

## WHAT WOULD GRADUATE THIS (named for go-decision, NOT opened)
1. The coupling derivation: why alpha couples to the rectified linear
   response (fixing 4 pi^3 over pi^4 from the construction, not the fit).
   This is the same item the charter already named.
2. The pairing derivation: the same coupling derivation would fix which
   susceptibility pairing is physical, collapsing the -15 ppm / -450 ppm
   ambiguity to one number. If it selects the overlap pairing, the remaining
   gap is -15 ppm, and the question becomes whether the neglected pieces
   (harmonic cross terms, the 4pi double-cover bookkeeping, D_E's own
   sub-ppm error bar) are of that size.

## LADDER PLACEMENT
Outcome 1 (alpha cracked): NO. Outcome 2 (4/pi derived): NO, the gate
falsified the mechanical derivation. Outcome 4 (route dead): NO, the second
prediction performed too well to kill. Outcome 3: YES. Registered as
LEAD-2R (rectified-coupling lead): 1/alpha = 4 pi^3 D_E (1 - Delta) with
Delta derived from the f4 response, currently -15 ppm under the overlap
convention, gated on the coupling derivation named above.

## Depends on
Commission W (D_E = 1.1051029, reproduced), Commission Y charter, the
external review (alpha_idea.txt, not in package; its two numbers, 4/pi at
179 ppm and eps_4 ~ 0.00268, were the pre-stated comparisons).

## Scripts
explorations/y_action_vs_energy.py (gate, cycle integrals, first eps_4)
explorations/y_eps4_robustness.py (conventions P1/P2/P3, harmonics m=1..6,
mesh convergence)
