# COMMISSION PE-2 (ELEC-099) -- RESULTS: C_pin IS MEASURED, LARGE, AND ORDINARY. THE ELECTRON-AXIS DEGENERACY IS IN SERIOUS TROUBLE.

*Adjudicated 2026-08-11 after bar lock
(analysis/PE2_pbc_prefactor_bars_LOCKED.md). Benchmark:
benchmarks/foundations/pe2_pbc_prefactor.py. The reviewer's protocol
including their blinding order and both added controls.*

## The controls, run FIRST as the blinding order required

**Null calculation** (isotropic inclusion -- no axis exists, so the
projection must vanish):

| L | null projection |
|---|---|
| 6.0 | -3.19e-16 |
| 8.0 | -2.03e-16 |

**Machine zero.** The projection estimator has no intrinsic axis.

**Noise floor** (three seeds, s = 1.5, L = 8): amplitudes -3.7600e+01,
-3.7631e+01, -3.7626e+01 -> **floor = 3.15e-02**.

**Global rotation control** (the reviewer's addition -- rotate system AND
cell together): unrotated -3.7600e+01, rotated -3.7625e+01,
|diff| = 2.52e-02 against a floor of 3.15e-02. **PASS.** No axis is
being defined by the implementation.

## The perturbative shortcut FAILS its control -- the reviewer was right to demand one

ELEC-098 argued first-order sufficiency from stationarity at a relaxed
configuration. The reviewer warned that stationarity does not license it
when contacts or active constraints can change discontinuously.

The single-relaxation scan returns R^2 = 0.46 and |amp|/E = 0.92 -- an
"anisotropy" of order the total energy, which is not an anisotropy at
all but configuration mismatch: the strands are relaxed for [100] and
then evaluated with the inclusion rotated to [111], which is **not a
small perturbation**. Hellmann-Feynman does not apply across finite
rotations.

**Registered: the perturbative shortcut is rejected.** Per the bar, PBC
is retained and the relaxations are paid for. ELEC-098's separation of
the two innovations is what made this recoverable -- exactly as the
reviewer anticipated.

## The measurement: fully relaxed orientation scan under PBC

Six symmetry-inequivalent axes, each **fully relaxed** in the periodic
cell (L = 8, s = 1.5), projected onto ELEC-096's pre-fixed K(n):

energies: 23.3572, 24.7916, 27.5456, 24.0352, 25.2120, 24.7365

| quantity | value |
|---|---|
| K-projection amplitude | **-5.2273** |
| R^2 of the fixed angular form | **0.7098** |
| mean E | 24.9464 |
| **anisotropy fraction \|amp\|/E** | **2.10e-01** |
| signal / noise floor | **166** |

Three things to note. **(1) The signal is unambiguous** -- 166x the
measured floor, with a null that is machine zero and a rotation control
that passes. **(2) R^2 = 0.71 on an angular form fixed in advance and
never fitted** is substantial support for ELEC-096's order-4 harmonic
being the leading invariant: a wrong form would not capture 71 percent
of the variance across six axes. **(3) The anisotropy is 21 percent of
the interaction energy.** That is not a suppressed coupling.

## VERDICT: C_PIN-MEASURED, and it is the reviewer's outcome (3) -- ORDINARY COUPLING

Against the reviewer's three pre-named outcomes:

- **C_pin = 0** (exact cancellation): excluded. The signal is 166x the
  floor.
- **C_pin small with a derived reason**: excluded at this s. An
  anisotropy fraction of 0.21 is O(1), not O(10^-8).
- **C_pin ordinary**: **this is what was found.**

The reviewer stated the consequence in advance and it should be quoted
as they wrote it: *"If the coefficient survives and produces excessive
splitting, that's a genuine problem for the current electron
construction... rather than something worth rescuing with increasingly
elaborate modeling."*

**An O(1) prefactor with the registered s^(-3/2) scaling leaves the
predicted splitting many orders above the 1e-6 eV degeneracy bar at
s = 82.6-108.** The electron-axis degeneracy that ELEC-091's
two-orientations reading of spin requires is not supported by the
registered mechanics as they stand.

## What is NOT concluded, and why the verdict stops short of a kill

Two conditionalities are real and are stated rather than buried:

1. **The measurement is at s = 1.5, deep in the pre-asymptotic regime**
   MEM-2 identified. The s^(-3/2) law is asymptotic, and propagating an
   O(1) prefactor measured at s = 1.5 across nearly two decades to
   s ~ 100 assumes the law holds from here. It may not. **A measurement
   of C_pin on the asymptotic branch remains the honest completion.**
2. **The inclusion is a proxy for the core's anisotropy** -- a prolate
   rigid segment, not ELEC-091's boundary circulation with two polar
   defects. The coupling is the registered contact energetics (not
   modelled, which is the advance over ELEC-094), but the OBJECT is
   still a stand-in.

Neither conditionality points toward safety: both would have to work
strongly in the framework's favour to rescue eight orders.

## Registered consequence

**ELEC-091's two-orientations reading of spin is now under a measured
threat rather than a modelled one.** ELEC-094's threat was withdrawn
because its coupling was invented; this one uses the registered contact
mechanics, passes a null, a noise floor and a rotation control, and
supports an angular form that was fixed before the data existed.

The electron sector's honest position: **the microscopic weave appears
to pin the electron axis at ordinary strength, and the corpus does not
currently have a mechanism that frees it.** Mechanism (A) was excluded
by symmetry (ELEC-096); mechanism (C), orientation averaging by axis
tumbling, remains unregistered and is now the only named escape.

## Attribution

Protocol, blinding order, the global-rotation control and the demand for
a perturbative control are all the reviewer's. The perturbative control
they insisted on is precisely the one that failed, and their instruction
that ELEC-099 end in a number or a bound rather than another
infrastructure finding is what kept this commission from becoming one.
