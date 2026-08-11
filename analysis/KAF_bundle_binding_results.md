# COMMISSION KAF -- RESULTS: UNBOUND-PREDICTED, THE EXPOSURE CLAUSE FIRES

*Evaluated 2026-08-11 after bar lock (analysis/KAF_bundle_binding_bars_LOCKED.md).
Benchmark: benchmarks/foundations/kaf_bundle_binding.py.*

## Q1 -- sign: NO BINDING at registered strains, under BOTH quartic readings

The full partial-overlap family (f in [0,1], 100001 points, minimum taken,
nothing chosen by hand) has its minimum at f = 0 (fully separated) for
k = 2, 3, 4 at the registered strain bound x = 0.04:

    sigma_k / sigma_1 = k exactly, both signs of the quartic.

The reason is structural, not marginal: the quadratic term prices coherent
overlap at k^2 while separation prices at k, so overlap costs (k^2 - k) x/2;
the softening quartic's gain, (k^4 - k) x^2/8, can only win at

    x > 4 / (k^2 + k + 1)  =  0.571 (k=2), 0.308 (k=3), 0.190 (k=4)

i.e. 14x / 8x / 5x above the registered tube-strain domain (FND-040
dominance clause). Inside the domain where the expansion is licensed, the
mechanism REPELS parallel windings; the stiffening counter-reading repels
harder. The sign conflict SCALE-001's C6 flagged is immaterial here: both
readings give the same verdict, disclosed per the locked bar.

## Q2 -- the bracket: MISS

Prediction sigma_2/sigma_1 = 2.000 against the pre-committed SU(6) k = 2
bracket [1.600, 1.767]: 13.2 percent past the upper edge. No free parameter
existed to move it; none is invented now.

## Q3 -- the (N, k) form: the ontology has NO N-CARRIER

Declared before the bracket was read, per the locked bar: the registered
inputs are T0, x, and the winding count k. The number of colours appears
nowhere in the registered mechanism -- which is exactly WHY the grant was
made (FND-050: no N-dependence in the derivations) -- and the derived law is
therefore N-independent: sigma_k = k sigma_1. The data's binding fraction is
explicitly N-DEPENDENT and vanishing at large N:

    b_k(N) = 1 - sigma_k/(k sigma_1):
    SU(4) k=2: 0.333 (Casimir) / 0.293 (sine)
    SU(6) k=2: 0.200 / 0.134
    SU(8) k=2: 0.143 / 0.076   -- b ~ (k-1)/(N-1) at Casimir.

The very feature that motivated the grant (the mechanism never mentions N)
is the feature the data refuses: real k-string binding carries 1/N structure.

## VERDICT: UNBOUND-PREDICTED -- Failed-and-kept, falsification channel HIT

Per the pre-committed grammar and FND-050's chosen exposure: the registered
strand-medium mechanism, claimed SU(N)-universal by the grant, predicts free
bundles (sigma_k = k sigma_1) at every registered strain, against a resolved
record showing 8-33 percent binding across SU(4/6/8). SU(3) retreat is
refused in advance by the grant itself. This is the corpus's first
registered falsification-channel hit under FND-050, and it is registered at
full volume, not softened.

## What it does and does not kill (scope, stated precisely)

- It does NOT touch the SU(3) calibrations (Sigma_eff and the chain
  conditional on it): those are measurements, scoped by FND-050 itself.
- It does NOT kill FND-037's recruitment or FND-040's softening as SU(3)
  single-source statements: Casimir scaling and the one resolved
  single-source violation (negative, Anzai-Kiyo-Sumino direction) remain
  matched. The hit is specifically against the mechanism's claimed
  N-universal COMPLETENESS: as universalized, it lacks the inter-tube
  attraction the k-string sector measures.
- The YOD sanity gate ("softening implies attraction") is CORRECTED: the
  gate's reasoning compared quartic gains without the quadratic overlap
  cost; at registered strains the quadratic wins by an order of magnitude.
  Annotation filed against FND-048.

## The inverted demand (registered, the MATTER046 grammar)

A rescue must DERIVE, blind, from registered or newly registered structure:
an inter-tube attraction producing binding fraction b_k(N) that (i) is
positive at tube strains x <= 0.04, (ii) decreases with N and vanishes as
N -> infinity, (iii) has magnitude ~(k-1)/(N-1) at moderate N, and (iv)
discriminates sine from Casimir at O(1/N^2), where the two laws differ.
The 1/N structure is the demand's teeth: the medium must carry adjoint-like
content (a registered carrier that counts colours) or the ontology must
register a new attraction channel. Either is a GRANT-level acquisition and
goes to the author.

## Standing consequence for the grant

FND-050 stands as made -- the grant is not retracted by its own exposure
firing; that would be bar-shopping in reverse. What changes is the ledger:
the corpus now owes either (a) the derived 1/N attraction channel, or (b)
the author's explicit acknowledgment that the universalized mechanism is
INCOMPLETE as a theory of gauge vacua, with the incompleteness localized to
inter-tube forces. Which -- and whether any new primitive is adopted to
pursue (a) -- is Mark's call, named and priced here, decided by him.
