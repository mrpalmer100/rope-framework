# COMMISSION SHIN -- RESULTS: ESCAPE-CLOSED-BY-THEOREM; THE CEILING IS THE SPACING

*Adjudicated 2026-08-11 after bar lock
(analysis/SHIN_operator_ceiling_bars_LOCKED.md). Benchmark:
benchmarks/foundations/shin_operator_ceiling.py. The bar required the
whole admissible class be bounded, not one alternative operator tested.*

## C1 -- periodicity, arbitrary coupling range

For the most general translation-invariant transverse dynamics on the
mesh -- couplings J_n between sites n spacings apart, any range,
including infinite --

    mu omega^2(k) = sum_n 2 J_n (1 - cos(n k a)),

and omega^2(k + 2pi/a) - omega^2(k) = 0 identically (symbolic). A
continuous periodic function on a compact domain attains a finite
maximum. **Long-range coupling does not evade the ceiling; it only
reshapes the band.**

This locates the ceiling's true cause, and it is not what FND-REL-004's
derivation might have suggested: the ceiling is a consequence of
DISCRETENESS, not of the nearest-neighbour approximation. Replacing the
operator cannot help, because every operator in the class is periodic in
k with the same period.

## C2 -- operator norm, arbitrary or disordered couplings

Dropping translation invariance too (the disordered case, which C1 does
not cover), the Gershgorin bound gives omega_max^2 <= max row sum of the
dynamical matrix divided by the site mass. With tension-type couplings
J ~ T0/a and site mass ~ rho a, this is omega_max ~ sqrt(z) c/a with z
an effective coordination -- so for ANY arrangement, ordered or not,

    **E_max ~ hbar c / a, up to an O(1) structural factor.**

| kappa | a [m] | hbar c/a | coordination factor needed for 1.4 PeV |
|---|---|---|---|
| 50 | 1.630e-17 | 1.21e10 eV | 1.34e10 |
| 250 | 9.533e-18 | 2.07e10 eV | 4.58e9 |

Reaching the anchor energy at fixed spacing requires the
coupling-to-mass ratio to rise by a billion-fold. T0 and mu are not
free: they are pinned by the m_e calibration and FND-017's invariance.

## VERDICT: ESCAPE-CLOSED-BY-THEOREM

Proposal 3 fails, and it fails in the strongest available way -- not by
one operator missing, but by a bound over the entire admissible class.
The result is STRONGER than FND-REL-004's: that claim excluded one mesh
with one operator; this one shows the ceiling is E_max ~ hbar c/a for
every operator, every coupling range, ordered or disordered.

**The one-line statement the corpus should carry from here:** the
photon ceiling tracks the mesh spacing and nothing else. Any fix must
change a LENGTH; no fix can change the dynamics.

## What remains (stated, not proposed -- naming is the author's)

- Proposal 1: strand substructure 8.3 orders below the measured d_c --
  a new primitive at the ontology's base, and it must explain why the
  electron anchor (ELEC-021's Lambda = E_inf d_c, GRV-094) does not see
  it.
- Proposal 2: the observed PeV quanta are not collective mesh modes --
  a second carrier, owing two polarizations and a coupling.
- Route (c): register the limitation in KNOWN_LIMITATIONS at full
  volume.

This commission proposes none of them. What it establishes is that the
cheap route is gone: the remaining fixes all cost either a primitive or
an admission, and the corpus should choose knowing that.

## Consolation, stated precisely and not as comfort

The same theorem that closes the escape also SHARPENS the framework's
one genuinely distinctive high-energy prediction: E_max ~ hbar c/a is
now a class-level statement, so any future determination of the mesh
spacing is a hard, parameter-free prediction of the photon ceiling --
and conversely, the observed 1.4 PeV photons are a hard LOWER BOUND on
the medium's fineness: a <= hbar c / E_obs = 1.4e-22 m, which is five
orders below the mesh spacing and three below the measured strand
thickness. That inequality is the cleanest form of the problem and
should replace looser statements of it.
