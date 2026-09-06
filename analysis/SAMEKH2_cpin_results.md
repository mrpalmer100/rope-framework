# COMMISSION SAMEKH-2 -- RESULTS: NOT FITTED. THE BOX ADEQUACY CHECK FAILS AND THE DECIDING COMPUTATION IS OUT OF REACH HERE.

*Adjudicated 2026-08-11 after bar lock
(analysis/SAMEKH2_cpin_bars_LOCKED.md). Benchmark:
benchmarks/foundations/samekh2_cpin.py. Form fixed by ELEC-096; the 3/2
exponent treated as fixed input and not re-derived, per the reviewer's
instruction.*

## What was run

Relaxations on the registered engine at nine orientations spanning the
order-4 cubic harmonic K(n) = sum_i n_i^4 - 3/5, at s = 2, 3, 4, 5, with
the relaxed energy REGRESSED on K(n) rather than reduced to
max-minus-min (MEM-2's cruder estimator).

| s | amplitude | \|amp\|/E | R^2 of the K-fit |
|---|---|---|---|
| 2.0 | -1.073e+00 | 5.29e-02 | 0.178 |
| 3.0 | -1.411e+00 | 7.56e-02 | 0.196 |
| 4.0 | +9.454e-01 | 5.68e-02 | 0.108 |
| 5.0 | +3.139e+00 | 2.10e-01 | 0.549 |

Noise floor at this box, measured before any signal was read: 2.19e-01.

## THE RESULT IS NOT USABLE, AND THE BAR SAYS WHY

Three independent symptoms, any one of which is disqualifying:

1. **R^2 = 0.11 to 0.55.** The order-4 harmonic explains between a
   ninth and a half of the orientation variance. The fixed form does
   not describe this data.
2. **The amplitude changes SIGN** between s = 3 and s = 4, and the
   trend is non-monotonic. A physical anisotropy amplitude does not do
   that.
3. **The box adequacy check -- which the bar required and which I ran
   only after seeing the numbers -- FAILS outright.** At the feasible
   grid (strand offsets at +-1 cell) an inclusion of half-length
   s = 2..5 cells EXTENDS BEYOND THE STRAND GRID. This is not an
   inclusion embedded in a medium; it is an object protruding from a
   medium too small to contain it. Every row above is therefore
   measuring boundary artifact, not bulk anisotropy.

**VERDICT: not C_PIN-MEASURED, not FORM-WRONG, not PRE-ASYMPTOTIC.**
The data cannot support any of those readings because it is not a valid
measurement. Registered as **INFEASIBLE-AT-ACCESSIBLE-SCALE.**

**The low R^2 must NOT be read as evidence against ELEC-096's order-4
form.** A protruding inclusion breaks the very symmetry the harmonic
classifies. ELEC-096's group theory is untouched by this failure.

## The honest cost accounting

Adequacy requires the strand grid to extend beyond the inclusion, i.e.
nrings >= s:

| nrings (covers s <=) | strands | cost vs the MEM-2 run |
|---|---|---|
| 1 | 27 | 1x |
| 2 | 75 | 3x |
| 3 | 147 | 5x |
| 4 | 243 | 9x |
| 6 | 507 | 19x |
| 8 | 867 | 32x |

And that is only the *adequacy* floor. MEM-2 established that s <= 3 is
pre-asymptotic; reaching a turnover plausibly needs s ~ 8-15, i.e.
30-100x the MEM-2 cost, at nine orientations, with a noise floor
measured per box and a convergence study on top. The wall-clock in this
environment already exceeded the limit at a box too small to be valid.

**The deciding computation is real, well-posed, and out of reach here.**

## What this commission does establish

- **The estimator is right and should be reused.** Projecting onto
  ELEC-096's harmonic is the correct measurement of C_pin; MEM-2's
  max-minus-min mixes harmonics and should not be used again.
- **The adequacy criterion is now explicit: nrings >= s.** Any future
  attempt that violates it is measuring boundary artifact, and this
  claim is the reason to check first rather than after.
- **The cost is quantified**, so the author can decide whether to spend
  it elsewhere or provision for it.

## My own procedural failure, registered

The bar required demonstrating box adequacy BEFORE reporting any signal.
I ran the scan first and the adequacy check afterwards, and the check
invalidated the scan. Had I obeyed my own bar's ordering, no invalid
numbers would have been produced at all. Logged, because the ordering
requirement exists precisely to prevent a session from becoming attached
to numbers it should never have generated.

## Status of the electron-axis question

Unchanged from ELEC-096. Symmetry protection excluded, orientation
averaging unregistered, C_pin the one unknown -- and now known to be
**not extractable at accessible scale**, with the required box size
stated. It is an infrastructure problem, not a physics problem, and
that is a materially different thing to record.
