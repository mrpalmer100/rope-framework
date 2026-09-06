# COMMISSION YOD-2 -- RESULTS: THE DEBT IS NOT PAID. NARROWED TO ONE DETERMINABLE NUMBER, AND ELEC-091's RESOLUTION IS CONDITIONAL

*Adjudicated 2026-08-11 after bar lock
(analysis/YOD2_axis_pinning_bars_LOCKED.md). Benchmark:
benchmarks/foundations/yod2_axis_pinning.py. The debt ELEC-091 created
one commission ago, called in immediately.*

## Y1 -- the scale

The core is large compared to the mesh: r0/a = g = 82.6 (kappa=50) to
108.0 (kappa=250). Inherited conditionality stated per the bar -- g is
FND-044's residual and is not independently derived.

| kappa | a [m] | g = r0/a | r0 [m] |
|---|---|---|---|
| 50 | 1.630e-17 | 82.6 | 1.346e-15 |
| 250 | 9.533e-18 | 108.0 | 1.030e-15 |

## Y2/Y3 -- the two readings, and they disagree by 218 orders

An extended object couples to a periodic medium through its form factor
at the reciprocal-lattice wavevector G = 2 pi/a. The suppression depends
on whether the object is SMOOTH or SHARP-EDGED on the scale of a.

| kappa | reading | suppression | E_pin (x m_e c^2) | vs 1e-6 eV bar |
|---|---|---|---|---|
| 50 | exponential, exp(-2 pi g) | 4.0e-226 | 2.1e-220 eV | **PASS** by 214 orders |
| 250 | exponential | 2.0e-295 | 1.0e-289 eV | **PASS** |
| 50 | power law, (a/r0)^4 | 2.1e-08 | 1.1e-02 eV | **FAIL** by 1.1e4 |
| 250 | power law, (a/r0)^4 | 7.4e-09 | 3.8e-03 eV | **FAIL** |

## THE COMMISSION'S OWN ERROR, caught by its own bar

The bar stated: *"if only a bound is available, register a bound"* and
*"do NOT substitute a plausible form."* **The exponent 4 in the power-law
row is not derived from anything.** It was chosen as a plausible form
factor falloff for a hard-edged object, which is exactly what the bar
forbade. The row is therefore ILLUSTRATIVE, not evaluative, and the FAIL
it produces cannot be registered as a falsification -- it would be a
falsification of a number this commission invented.

Reported rather than deleted, because the illustration carries real
information: **if the sharp-edge reading holds with any exponent near 4,
the pinning is four orders too large** and ELEC-091's resolution fails.
The question is live, not comfortable.

## VERDICT: UNDERSPECIFIED -- the debt is NOT paid

The registered inputs do not determine which reading applies, and the
corpus has no claim giving the form factor of ELEC-074's hard-edged
core at the reciprocal-lattice scale.

**Missing carrier, named:** the asymptotic form factor of a core with a
boundary of the type ELEC-074 derived. This is not a new primitive and
not an experiment -- it is a computation on an object the corpus already
has in closed form (the exact profile p(x) = x^-2/sqrt(1-x^-4)). It is
the next brick and it is cheap.

## What this does to ELEC-091

**ELEC-091's charge-fixes-spin resolution is now explicitly
CONDITIONAL** on the axis being unpinned, and that condition is unproven
rather than merely unstated. The claim's own T3 argument -- that
GRV-020's breaking leaves the axis free in laboratory space -- is a
statement about the SYMMETRY of the internal sector; it does not by
itself establish that the ambient mesh exerts no orienting torque on an
extended core. Those are different claims and this commission separates
them.

If the form-factor computation returns the exponential regime, the
resolution is safe by two hundred orders and the matter is closed
forever. If it returns a power law of order 4, the corpus predicts a
spin-state splitting ~1e-2 eV that spectroscopy excludes, and ELEC-091's
resolution -- and with it the two-orientations reading of spin --
fails.

**That is a genuine falsifier, sharply stated, and it was created by
this sector's own progress rather than imported.** The corpus should
want it computed quickly.

## Honest note on the bar

The confrontation bar (1e-6 eV) was set conservatively on purpose so a
failure could not be blamed on aggressiveness. It did not have to work
that way round: the exponential reading passes by two hundred orders,
so the bar's exact value is irrelevant to that branch, and the power-law
branch fails by four orders, so it would fail a bar ten thousand times
looser. **The verdict is insensitive to the bar**, which is the
condition under which a bar was worth locking.
