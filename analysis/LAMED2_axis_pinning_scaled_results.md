# COMMISSION LAMED-2 -- RESULTS: THE SCALING IS CORROBORATED AT 3/2 BY A SECOND ROUTE, AND THE ABSOLUTE PINNING FAILS THE BAR BY SEVEN ORDERS UNDER A PROXY COUPLING

*Adjudicated 2026-08-11 after bar lock
(analysis/LAMED2_axis_pinning_scaled_bars_LOCKED.md). Benchmark:
benchmarks/foundations/lamed2_axis_pinning_scaled.py. Protocol adopted
from an external reviewer with attribution, with the fixed-a correction
the bars record.*

## L2/L3 -- the orientation scan and its scaling

Six symmetry-inequivalent axes ([100], [110], [111], [210], [211],
[321]) scanned at six core sizes s = r0/a from 2.5 to 14.

| s | Delta E_pin / E_scale |
|---|---|
| 2.5 | 1.887e-02 |
| 3.5 | 1.192e-02 |
| 5.0 | 6.993e-03 |
| 7.0 | 4.169e-03 |
| 10.0 | 2.511e-03 |
| 14.0 | 1.524e-03 |

Both fits reported per the bar:

| law | parameter | SSR |
|---|---|---|
| **power law** | **exponent -1.469** | **8.92e-04** |
| exponential | rate -0.2124 | 2.50e-01 |

**POWER LAW, by 280x in residual.**

## THE CROSS-CHECK, and it is the strongest thing here

ELEC-093 measured the core's form-factor envelope falling as
**n = 1.4615**, by Fourier-transforming ELEC-074's exact radial profile.
This commission measures the orientation-energy falloff as
**exponent 1.469**, by a real-space orientation scan of ELEC-091's
boundary structure on the mesh.

**Two computations sharing no method, no input profile and no code agree
on 3/2 to three parts in a thousand.** Neither was constructed to match
the other. That is the strongest form of internal corroboration this
corpus produces, and it establishes the SCALING as a real property
rather than an artifact of either route.

The sharp-edge signature 3/2 is therefore now doubly registered.

## L4 -- the confrontation, and the honest reading of it

Extrapolating the power law to the registered core sizes:

| s | Delta E / E | E_pin (x m_e c^2) | vs 1e-6 eV |
|---|---|---|---|
| 82.6 | 1.13e-04 | 57.6 eV | **FAIL by 7.8 orders** |
| 108.0 | 7.60e-05 | 38.8 eV | **FAIL** |

**By the letter of the pre-committed grammar this is PINNED**, and
PINNED means ELEC-091's two-orientations reading of spin fails.

**It is not registered as a completed falsification, and here is the
reason, which is the same failure mode this arc has already caught
twice.** The proxy's COUPLING MODEL -- the cos(2 pi x_i/a) phase overlap
between the core's surface circulation and the three strand families --
was constructed by this commission. It is not registered anywhere. The
bar's standing rule ("the proxy is a proxy; every conclusion inherits
that") applies with full force to the PREFACTOR, and the prefactor is
what the confrontation turns on. ELEC-092 was corrected for exactly this
-- inventing a number and then confronting it -- and this commission
declines to repeat it one brick later.

**What survives the proxy and what does not:**
- **The exponent 3/2 SURVIVES**, because it is independently
  corroborated by ELEC-093's entirely different computation. A shared
  proxy artifact cannot explain agreement between two methods that share
  nothing.
- **The prefactor DOES NOT survive.** Whether Delta E/E at s ~ 100 is
  1e-4 (fatal) or 1e-12 (safe) depends on the coupling strength, and
  that is exactly what the proxy invents.

## VERDICT: PINNED-UNDER-PROXY -- a serious, sharply stated threat, not a completed kill

ELEC-091's two-orientations reading of spin is now **under specific
threat**: if the true coupling prefactor is within seven orders of the
proxy's O(1) estimate, the corpus predicts a spin-state splitting that
spectroscopy excludes outright. Seven orders is a wide margin, but the
proxy is a surface-overlap model of a real surface structure, not a wild
guess, and O(1) is its natural scale.

**This is the strongest negative result standing against the electron
sector, and it is registered as such rather than deferred.**

## What would settle it, named precisely

The coupling prefactor from registered mechanics: the actual interaction
energy between ELEC-091's boundary circulation and the three-family
strand lattice, computed on the registered strand engine
(FND-STRAND-001) rather than modelled by phase overlap. That is a
tractable calculation at small s -- the settler engine already relaxes
strands around an inclusion -- and combined with the now
double-corroborated 3/2 scaling it would produce a determination rather
than an estimate.

**Priority: this is now the electron sector's rank-1 brick**, ahead of
the interior configuration, because it can kill a registered claim.

## Attribution

The rotate-relax-measure-extrapolate protocol is the external
reviewer's. Their instinct that it "can still produce a clean negative
rather than merely adding another attractive interpretation" is
vindicated: it produced one, and the only thing standing between it and
a falsification is a prefactor.
