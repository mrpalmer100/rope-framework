# COMMISSION NUN-2 -- RESULTS: SYMMETRY-ALLOWED AT ORDER 4. THE COMFORTABLE ESCAPE IS CLOSED AND THE REMAINING QUESTION IS ONE NUMBER.

*Adjudicated 2026-08-11 after bar lock
(analysis/NUN2_rotational_symmetry_bars_LOCKED.md). Benchmark:
benchmarks/foundations/nun2_rotational_symmetry.py. The question an
external reviewer identified as the one to inspect BEFORE the expensive
coupling calculation. They were right to put it first.*

## N1 -- the point group

Three strand families along x, y, z at spacing a. That direction set is
invariant under the octahedral group **O_h** (48 elements: axis
permutations and sign flips), **not** under the full rotation group.

**An orientation-dependent energy is therefore generically allowed.**
Exact cancellation would require an identity BEYOND the lattice
symmetry -- the symmetry itself does not supply one.

## N2 -- the lowest allowed anisotropy, from group theory alone

Invariants of a unit axis under O_h, by order:

| order | invariant | status |
|---|---|---|
| 2 | n_x^2+n_y^2+n_z^2 | equals 1 on the unit sphere -- **no anisotropy** |
| **4** | **n_x^4+n_y^4+n_z^4** | **the first nontrivial cubic harmonic** |
| 6 | n_x^6+n_y^6+n_z^6 | higher |

Odd orders are killed independently, because the axis is defined only up
to sign (the two poles are equivalent, ELEC-091).

Evaluated on the symmetry directions:

| axis | sum n_i^4 |
|---|---|
| [100] | 1.0000 |
| [110] | 0.5000 |
| [111] | 0.3333 |

**Spread 0.667 -- nonzero.** The harmonic genuinely distinguishes
orientations; it does not vanish.

**VERDICT N2: SYMMETRY-ALLOWED AT ORDER 4. Mechanism (A), exact
cancellation by symmetry protection, is EXCLUDED** unless someone
produces a further non-symmetry identity.

## N3 -- the dynamical average

ELEC-068 registers that the electron has no static branch and exists
only as a rotating configuration, so mechanism (C) had to be checked.

**It does not work.** The order-4 invariant depends on the axis n alone,
not on the rotational phase about n. Rotating the configuration about
its own axis leaves n fixed and leaves the harmonic unchanged.
Averaging would require the AXIS ITSELF to tumble through many
orientations within a measurement time -- and ELEC-068 registers
rotation of the winding pattern, not axis tumbling. No claim supplies a
precession or tumbling rate.

**VERDICT N3: NOT AVERAGED. Mechanism (C) is available in principle but
UNREGISTERED**, and would need a carrier the corpus does not have.

## The consequence, which is what makes this brick worth its cost

Of the reviewer's three escapes:
- **(A) symmetry protection -- EXCLUDED.**
- **(C) orientation averaging -- UNREGISTERED**, would require a new
  carrier (axis tumbling rate).
- **(B) strong derived suppression -- the only one left standing.**

So the electron-axis question now reduces to a single number, in a form
fixed in advance rather than fitted afterwards:

    **E_pin(n) = C_pin * s^(-3/2) * [ sum_i n_i^4 - 3/5 ] * E_core**

with the bracket the normalized order-4 cubic harmonic (N2), the s^(-3/2)
scaling taken as FIXED INPUT per the bar and the reviewer's instruction
not to re-derive it alongside a prefactor, and **C_pin the one unknown.**

The reviewer's protocol is now fully specified: feed the registered
strand engine the ELEC-091 boundary geometry, extract C_pin at small s
with no adjustable normalization, and propagate with the fixed scaling.
Three outcomes are pre-named and must not blur: C_pin = 0 (would now
require an identity beyond symmetry, since symmetry has been shown not
to supply one); C_pin small with a derived reason; or C_pin ordinary,
in which case the seven-to-eight-order margin makes this a real
electron-sector failure rather than something to model around.

## Honest note on what this does NOT show

This is a statement about what the symmetry PERMITS, not about
magnitude. A permitted term can still have a coefficient of zero for
dynamical reasons, and permitted-at-order-4 already implies substantial
suppression for a nearly-isotropic object. **The commission closes an
escape; it does not create a problem.** The problem, if there is one,
is the coefficient -- unchanged from before, but now with the comfortable
symmetry exit removed and the target written down.

## Attribution and status of the reviewer's document

The reviewer's framing (three mechanisms, do the symmetry inspection
first, treat 3/2 as fixed input, no adjustable normalization) is adopted
in full and drove this commission's design. Their document predates
ELEC-095: the 39-58 eV figure and the 10^-8 suppression requirement they
reason from were WITHDRAWN by that claim, since the registered engine
contradicted the proxy's trend in the overlap. Their methodological
points survive that withdrawal intact; the numerical target does not.
Their correction to ELEC-094's overstatement -- that the two routes DO
share ELEC-074's sharp-boundary geometry, so the 3/2 agreement evidences
a universal consequence of the hard boundary rather than the proxy's
physical correctness -- is accepted and registered against ELEC-094.
