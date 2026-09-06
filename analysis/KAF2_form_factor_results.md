# COMMISSION KAF-2 -- RESULTS: THE FORM FACTOR IS A POWER LAW, AND THE QUESTION IT WAS COMPUTED FOR TURNS OUT TO BE THE WRONG QUESTION

*Adjudicated 2026-08-11 after bar lock
(analysis/KAF2_form_factor_bars_LOCKED.md). Benchmark:
benchmarks/foundations/kaf2_form_factor.py.*

## The computation, done as chartered

ELEC-074's exact energy density e(x) = sqrt(1 + p(x)^2) - 1 with
p(x) = x^-2/sqrt(1 - x^-4) was Fourier-transformed in 3D. The edge
singularity at x = 1 (p ~ (x-1)^(-1/2)) was desingularized exactly by
the substitution x = 1 + t^2; cutoff independence was demonstrated
(S stable to 6 figures across cutoffs 40/60/90).

**A first pass sampled S(q) at scattered points and produced garbage** --
both fits at SSR ~2.6 and a meaningless 1.1x "discrimination". The
reason is that S(q) OSCILLATES in sign, so scattered sampling catches
near-zeros. The bar's ambiguity clause applied and the result was
discarded rather than rounded toward a regime. The envelope was then
extracted from 1500 dense samples (96 local maxima) and fitted properly:

| law | parameter | SSR |
|---|---|---|
| **power law** | **n = 1.4615** | **1.28e-03** |
| exponential | k = -0.0106 | 4.33e+00 |

**POWER LAW, better by a factor 3400.** The measured exponent
n = 1.46 sits at the sharp-edge prediction of 3/2 -- which is what an
inverse-square-root edge singularity gives, so the number is understood
and not merely fitted.

**REGIME: SHARP.** ELEC-074's hard boundary does dominate the
high-q behaviour, exactly as ELEC-092 feared and contrary to the
comfortable branch.

## AND THEN THE COMPUTATION INVALIDATES ITS OWN USE

Having established the form factor, applying it to the pinning question
exposes an error in how that question was framed -- in ELEC-092, and
inherited here:

**ELEC-074's profile is RADIAL, hence spherically symmetric. A
spherically symmetric density has S(q) depending only on |q|. The
orientation energy is a sum over reciprocal-lattice vectors of
S(|G|) V(G), and rotating a spherically symmetric object changes no
term in that sum. THE ORIENTATION ENERGY IS IDENTICALLY ZERO,
regardless of whether S falls exponentially or as a power law.**

So the 218-order dichotomy ELEC-092 set up was between two answers to a
question the registered profile cannot pose. The form factor's regime is
real and now measured, but it does not decide the pinning, because the
object it describes is isotropic.

## What actually decides the pinning

The core's anisotropy is the **two polar defects** ELEC-091 derived from
the hairy-ball theorem. Those are not part of ELEC-074's radial profile
-- they live in the tangential direction field on the boundary sphere,
which is a separate structure. **The orientation energy is sourced by
the pole structure alone**, and no registered claim gives its density
profile.

## VERDICT: UNDERSPECIFIED, with the target relocated

The debt ELEC-091 created remains unpaid, but it is no longer the debt
ELEC-092 described. The missing carrier is named precisely:

**the density profile of the two polar defects on the core boundary** --
their size, their strength, and how their contribution to S(q) depends
on the axis direction relative to the mesh.

That is a smaller object than "the interior configuration" and a
different one from "the core's form factor". It is the correct next
brick.

## Two things this commission establishes on the way

1. **The core's form factor is a power law with n = 3/2** (measured
   1.4615), the sharp-edge signature. This is a permanent registered
   property of ELEC-074's object and will matter wherever the core
   couples to short-wavelength structure -- it is not wasted work.
2. **ELEC-092's framing was wrong** and is corrected: it treated the
   radial form factor as the pinning quantity. The correction is
   registered against a claim of this same session, one commission old,
   which is the third in-session correction of this arc.

## What ELEC-091's spin reading now rests on

Not the comfortable branch, and not the fatal one -- on an unbuilt
computation. The two-orientations reading of spin is **neither rescued
nor refuted** by this commission. It awaits the polar-defect profile.
Anyone quoting ELEC-091's spin picture should quote this conditionality
with it.
