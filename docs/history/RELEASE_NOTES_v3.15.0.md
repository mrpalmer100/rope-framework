# RELEASE NOTES v3.15.0 (2026-08-10)
## THE ELECTROMAGNETIC ARC

One session after the unification release, this release banks something the
programme had never had: a complete, chartered, zero-free-parameter
reconstruction of the electromagnetic sector — direction, carrier, sign,
normalization, and magnetism — ending in four new numbered predictions with
their kill conditions on their faces.

## Headline

**555 registered claims** (114 Derived, 395 Modeled, 4 EFT-constrained,
4 Conjecture, 6 Open, 32 Failed-and-kept); **531 code-backed, all passing.**
Heartbeats: 10/10 validation, 75/75 physics+EM regression, 6/6 reproduction.

## The five commissions (each with bars locked before computation)

### N — The direction of E (EM-RECON-024, Derived)
The gap: the corpus committed E's magnitude, split, and curl partner, but its
DIRECTION was committed nowhere (the EM-RECON-019 trace). Under the
operational definition the static sector already owned — E is force per
winding — the angular-averaged linear response of the azimuth-blind contact
form is a scalar times the identity: E points along the carrier's transverse
center-line displacement. The necessity clause unified two registered kills:
no center-line displacement, no force, no polarization — the bare screw's
F = 0 IS the state-count kill seen from the force side.

### K — The carrier (EM-RECON-025, Modeled)
The collective transverse displacement of the fully-dynamical mesh is a
symmetry-protected gapless Goldstone pair. The exact two-strand computation
puts the O(g) crossing mass entirely on the relative (optical) branch; the
center-of-mass branch runs at omega^2 = (T0/mu) q^2 at every crossing
strength. FND-REL-005's mass kill is located as a frozen-background artifact
— the escape is in the operator's eigenvectors, not in argument. Costs on the
face: the coverage-vs-dispersive fork becomes MANDATORY; the bending condition
B <= T0 a^2/12 stands as the live falsifier. GRV-102 (the Corollary-1
tension) resolves in structure: allocation had over-reached to identification;
winding = charge stands untouched.

### THETA — The electric sign (EM-RECON-026, Modeled)
The q-linear force derived from the momentum-flux (Blasius) integral,
residues shown: F = rho (v_rel x Gamma), Gamma = q kappa_0 by pi_1 = Z.
E identified: E = rho kappa_0 (v x zhat). The static sign rule (like windings
repel, q1 q2, 1/r) is REPRODUCED from momentum conservation — independently
confirming EM-015's energy-minimization route. The relative-velocity split
yields the exact Lorentz structure F = q(E + v_d x B'): electricity and
magnetism as two halves of one Magnus formula.

### IOTA — The normalization (EM-RECON-027, Modeled)
Two independent routes — wave-energy bookkeeping under the registered bridge,
and static Gauss consistency — fix the identical identity
kappa_0^2 eps0 rho = 1, whence kappa_0 = c/sqrt(eps0 SIGMA). Coulomb emerges
with no residual factor. No new constant exists to find: kappa_0 is exactly
as pinned as SIGMA, and the registered Schwinger-form bound propagates to
kappa_0 <= ~26-50 SI. One SIGMA measurement locks every magnitude at once.

### LAMBDA — The magnetic sector (EM-RECON-028, Modeled)
The commission that could have killed the arc: a constant B' in the Lorentz
split implies ether drag on any moving charge. It cancels as a COMPUTED
IDENTITY — the Magnus axis is the winding's own line direction, so the net
drag on a closed winding is the closed integral of the tangent: identically
zero, exhibited on a trefoil. The same topology that quantizes charge
protects free motion. Faraday applied to the derived E forces
mu_0 = 1/(eps0 c^2) from the carrier's own dispersion (|B| = |E|/c emergent),
and the structure lands on EM-009/012 as agreement between independent routes.

## New predictions (EM-RECON-029; paper Predictions 28-31)
- **P28, the Sign Lock**: quadratic photon LIV, at any level, must be
  SUBLUMINAL. One bit, zero parameters. Any superluminal quadratic signal
  kills EM-RECON-025.
- **P29, the Linked Cutoff**: E_QG2/E_max >= sqrt(3) exactly — a measured
  dispersion scale X requires vacuum opacity above X/sqrt(3). No other
  framework links these observables.
- **P30, the Massive Partner**: the optical branch at >= ~2e11 GeV; all
  accelerator nulls to date are predicted; a discovery below kills.
- **P31, the One-Number Lock**: one PVLAS-class SIGMA measurement fixes
  kappa_0, every field magnitude, and the vacuum density simultaneously —
  plus the QUANTIFIED internal falsifier: rho >= 4.5e7 kg/m^3 must not
  gravitate uniformly, or the framework dies on cosmology by ~33 orders.
- Gated candidate (unnumbered until chartered): linear optical response of
  neutral topological defects.

## Documentation
The QPT paper carries the five-commission postscript; the plain-language
guide gains "Which way does light push?"; guide/topics/light.md — the page
whose unregistered prose exposed the original gap — now cites the registered
claims; roadmaps regenerated from claims.yaml.

## Corrections within the cycle (all Mark's catches, logged)
The predictions numbering collision (26/27 reuse -> renumbered 28-31);
the THM-006 second falsification (sign bar violated and kept locked, the
failure geography's move registered); the validate.yml workflow restored
(it was lost locally, not retired — solver heartbeats preserved).

## Honesty ledger
- The arc's grade is Modeled where the effective-medium step enters (ideal-
  fluid treatment at wavelengths >> a); Derived where it does not (024).
- Underived and named: full covariance of the defect sector; beyond-plane-
  wave B bookkeeping; SIGMA's value — the single gate.
- The three-pin coverage/dispersive fork is now mandatory, not interpretive.
- Every commission's charter, with bars locked before computation, is in
  docs/commissions/ (N, K, THETA, IOTA, LAMBDA).
