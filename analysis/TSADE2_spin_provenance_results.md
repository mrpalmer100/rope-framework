# COMMISSION TSADE-2 (ELEC-100) -- SPIN PROVENANCE AUDIT: THE SPIN MACHINERY NEVER DEPENDED ON THE AXIS

*Adjudicated 2026-08-11. The reviewer's ELEC-100, run before spending
another compute cycle, exactly as they advised. Registry sweep plus
dependency trace; no new computation.*

## The question

Trace every registered claim responsible for spin-1/2, 4pi return,
two-state behaviour and spin-statistics, and determine which -- if any --
requires ELEC-091's core axis to represent spin.

## The dependency trace

Claims depending on the axis chain {ELEC-088, 089, 090, 091}:

    ELEC-089, 090, 091, 092, 093, 094, 095, 096, 097, 099

**Every one is from this session's own core arc. Nothing else in the
corpus depends on the axis at all.**

The spin machinery, checked individually:

| claim | grade | depends on axis? | its actual base |
|---|---|---|---|
| QB-020 (Tsirelson as a theorem) | Derived | **no** | QB-011/013/019 |
| QB-025 (junction, half-angle law) | Derived | **no** | QB-005/023/024 |
| QB-026 (knot-proxy Stern-Gerlach) | Modeled | **no** | QB-023/024/025 |
| QB-031 (frame transport law) | Modeled | **no** | **GRV-020**, QB-029/030 |
| QB-011, QB-023, GRV-045, QGATE-010 | -- | **no** | -- |

**Zero of them reference the axis**, and the reason is structural rather
than lucky: they predate ELEC-090/091 by many sessions. A result derived
before an object existed cannot depend on it.

## Where spin actually lives

The trace points somewhere specific. QB-031's frame transport law rests
on **GRV-020** -- the same internal-azimuth symmetry theorem that gives
the winding its circle-valued Goldstone. QB-025's spinor structure is
the polarization state on the Poincare sphere; QB-020's is the
Pauli/quaternion algebra the Hopf machinery natively carries.

**Spin in this corpus is carried by the internal azimuth and the Hopf/
spinor machinery, not by the orientation of a geometric axis in space.**
That was true before ELEC-090 and remains true after ELEC-099.

## VERDICT: the reviewer's outcome (1)

**ELEC-099 killed an interpretation, not a mechanism.** The
two-orientations reading of spin was an attractive picture proposed one
commission after the axis was derived; it was registered as "suggestive,
not derived" at the time, and it is now retired. Nothing else moves.

## What is retired and what is kept -- the reviewer's separation, adopted

**RETIRED:** *the two orientations of the ELEC-091 axis constitute the
electron's two degenerate spin states.* It has a direct mechanical
problem: an O_h substrate gives different orientations appreciably
different energies (ELEC-099), so a freely degenerate two-state axis is
not available.

**KEPT, untouched:** the axis itself. ELEC-090/091 derived it from
topology -- the tangent field on the hard-core boundary must have zeros
of total index 2, and matching to the exterior winding fixes the field
as azimuthal with two polar defects. **That derivation never mentioned
spin and does not need it.** The axis is geometric structure of the
charged defect, and ELEC-099 says it is *pinned* structure.

The reviewer's additional point stands and is registered: two
orientations of a classical axis were never sufficient for spin-1/2
anyway. **Spin-1/2 requires the spinor transformation structure**, which
the corpus obtains from the Hopf machinery -- not from a binary-looking
geometry.

## Correction to ELEC-099's language, adopted

The reviewer objects to phrasing the discrepancy as a measured
eight-order exclusion while two extrapolations remain unvalidated.
Accepted. The two statements are now separated:

- **STATED LOUDLY (established):** the registered microscopic mechanics
  exhibits ORDINARY AXIS PINNING -- anisotropy fraction 0.21 at 166x the
  floor, R^2 = 0.71 on a pre-fixed harmonic, all controls passed.
- **STATED CONDITIONALLY (extrapolated):** that this implies a specific
  splitting for the physical electron. That still rides on s = 1.5 being
  extendable to s ~ 100 and on the prolate proxy standing in for the
  circulating boundary.

## Tumbling is NOT chartered

The reviewer is right that "maybe it tumbles" would violate the corpus's
own source-before-instrument rule. Before any tumbling commission, six
things must be supplied: what torques it, why it persists in the ground
state, its derived frequency, why it averages the cubic anisotropy, why
it adds no observable dynamics, and whether it yields spinor/4pi
behaviour. **None is registered. Tumbling remains an unregistered
escape, not a next brick.**

## Methodological note

The reviewer proposed the pinning test precisely *because* ELEC-090's
new axis looked enticingly like spin. The test did what a good falsifier
should: **it stopped a visually compelling geometric feature from being
promoted into physics before the mechanics supported it.** The corpus
lost an attractive picture and kept everything that was actually
derived.
