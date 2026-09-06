# COMMISSION MEM-2 -- RESULTS: THE ENGINE MEASURES A REAL ORIENTATION ENERGY AND CONTRADICTS THE PROXY'S TREND. ELEC-094's EXTRAPOLATION IS WITHDRAWN.

*Adjudicated 2026-08-11 after bar lock
(analysis/MEM2_coupling_prefactor_bars_LOCKED.md). Benchmark:
benchmarks/foundations/mem2_coupling_prefactor.py. Engine: FND-STRAND-001
as registered -- inextensible curves by exact projection, bending
KB = 0.6, finite contact Ac/(1+(r/sigma)^4) with AC = 1.0, SIG = 0.30,
all unchanged. NO coupling model was introduced.*

## Noise floor, established before any Delta E was read

Three seeds at [100], s = 2.0: 31.280151, 31.277364, 31.311726.
**Convergence spread = 3.44e-02.** Reported first, per the bar, so no
signal could be claimed against an unmeasured floor.

## M1/M2 -- the orientation scan

| s | [100] | [110] | [111] | Delta E | Delta E/E | vs noise |
|---|---|---|---|---|---|---|
| 1.5 | 31.733110 | 31.217330 | 31.193594 | 5.40e-01 | 1.72e-02 | SIGNAL (16x) |
| 2.0 | 31.280151 | 32.717188 | 31.502187 | 1.44e+00 | 4.51e-02 | SIGNAL (42x) |
| 3.0 | 29.137519 | 30.561759 | 30.882186 | 1.75e+00 | 5.78e-02 | SIGNAL (51x) |

**The registered engine produces a genuine orientation-dependent energy**
-- 16x to 51x above its own convergence noise. This is the first
measurement of the quantity from registered mechanics rather than from a
model, and it is the thing MEM-2 was chartered to get.

## AND IT CONTRADICTS THE PROXY

ELEC-094's phase-overlap proxy gave Delta E/E **falling** with s
(1.89e-02 at s = 2.5 down to 1.52e-03 at s = 14, a clean power law at
exponent 1.469). The registered engine gives Delta E/E **rising** over
1.5 -> 3.0 (1.72e-02 -> 5.78e-02).

**The trends disagree in sign over the range where both were computed.**

## What that means, stated carefully

The accessible engine range (s <= 3) is NOT the asymptotic regime: the
inclusion's half-length is 1.5-3 cells while the strand offsets sit at
+-1 cell, so the object is comparable to the mesh rather than large
compared with it. The 3/2 falloff is an ASYMPTOTIC statement, and
nothing here refutes it at large s.

**But that is precisely the problem.** ELEC-094's proxy claimed the
falling power law already at s = 2.5-14, i.e. starting inside the range
the engine can check -- and where they overlap, the engine says the
opposite. So the proxy is not merely uncertain in its prefactor, as
ELEC-094 conceded; **it is unvalidated in its trend at the only sizes
where validation is currently possible.**

**ELEC-094's extrapolation to s = 82.6-108.0 is therefore WITHDRAWN.**
The 39-58 eV figure, and with it the "PINNED-UNDER-PROXY" threat to
ELEC-091's spin reading, does not survive contact with the registered
engine. It should not be quoted.

**What survives ELEC-094:** the 3/2 exponent as a property of
ELEC-074's form factor, corroborated by ELEC-093 through an independent
route. That was always the part that did not depend on the coupling
model, and it stands.

## VERDICT: PREFACTOR-MEASURED (small s), EXTRAPOLATION UNSUPPORTED

Per the pre-committed grammar this is not PINNED and not UNPINNED. The
prefactor is measured where the engine reaches, the confrontation
cannot be made, and the honest statement is that **the spin-degeneracy
question is reopened, not resolved.**

ELEC-091's two-orientations reading of spin is neither refuted (the
threat is withdrawn) nor secured (no unpinning is demonstrated). It sits
exactly where ELEC-092 left it, minus one false alarm.

## What would settle it, and why it is harder than it looked

Reaching the asymptotic regime on the registered engine means s >> 1
with strand offsets resolving many cells -- an O(10^6-10^7) node
relaxation at multiple orientations, which ELEC-094's own feasibility
note already priced as out of reach here. The realistic routes:

1. **Push the engine as far as s allows** (s = 5, 8, 12 with a larger
   offset grid) and look for the turnover where the rising small-s
   behaviour becomes the falling asymptotic one. If a turnover exists
   and is located, the asymptotic branch can be anchored to a measured
   point rather than to a proxy.
2. **Derive the asymptotic coupling analytically** from the registered
   contact energetics, rather than measuring it -- the contact kernel
   Ac/(1+(r/sigma)^4) is in closed form and its multipole expansion
   about an anisotropic inclusion is a tractable calculation.

Route 2 is the better brick: it produces a prefactor with provenance
rather than an extrapolation with a proxy.

## Disclosure

This commission was chartered to firm up ELEC-094 and instead undercut
it. That is registered as the outcome. Two commissions in a row have now
produced results that corrected the one before them -- ELEC-093 against
ELEC-092, and MEM-2 against ELEC-094 -- which is the arc's method
working as intended, and also a signal that this sector should slow
down and prefer derivations over models.
