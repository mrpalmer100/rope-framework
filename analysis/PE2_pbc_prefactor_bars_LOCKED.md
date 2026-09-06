# COMMISSION PE-2 (ELEC-099) -- THE PBC AXIS-PINNING PREFACTOR (BARS, LOCKED)

*Locked 2026-08-11, before computing. The deciding computation. The
reviewer's protocol adopted in full, including their blinding order and
both of their added controls.*

## The form, fixed in advance and NOT fitted

    E_pin(n) = C_pin * s^(-3/2) * K(n) * E_core,
    K(n) = sum_i n_i^4 - 3/5

**C_pin is the ONLY free quantity.** The angular form is ELEC-096's, the
exponent is fixed input per ELEC-096/the reviewer. No angular fitting.

## Ordering (the reviewer's blinding discipline, binding)

**Before any orientation signal is read:**
1. establish the numerical projection floor from NULL calculations
   (isotropic inclusion -- no axis at all; the projection must return
   zero to within noise);
2. establish finite-cell behaviour across multiple L, fitting
   C_measured(L) = C_pin + A/L + ... and FREEZING the extrapolation
   procedure;
3. run the GLOBAL ROTATION CONTROL: rotate the entire system AND the
   periodic cell together. The projected coefficient must be invariant.
   **If it is not, an axis is being defined by the implementation rather
   than by the three-family physics, and the run is void.**

Only then may orientation-labelled results be read.

## The perturbative shortcut is CONDITIONAL, not assumed

ELEC-098 argued first-order sufficiency from stationarity. The reviewer
correctly notes that stationarity does not license it when contacts or
active constraints can change discontinuously. **Validate empirically**
on at least two representative orientations:
Delta E_perturbative vs Delta E_fully_relaxed. If the control fails, PBC
is retained and the relaxations are paid for -- the two innovations are
independent and must not be made to depend on each other.

## Verdict grammar (pre-committed)

- **C_PIN-MEASURED**: coefficient extracted, extrapolated, confronted
  against the 1e-6 eV degeneracy bar. Classify per the reviewer's three
  outcomes (zero / derived-small / ordinary).
- **C_PIN-BOUNDED**: signal below the projection floor. Report the
  UPPER BOUND and confront the bound. **This is an acceptable
  endpoint**, per the reviewer's instruction that the endpoint be a
  number or a bound.
- **VOID**: the global-rotation control fails.

## Standing rule, quoted from the reviewer and binding

"Don't let ELEC-099 become another infrastructure campaign." If the
computation runs, its endpoint is a number or a bound -- not a further
feasibility finding. If it cannot run at all, that is a VOID or a
bound, not a new campaign charter.
