# ROPE-SOURCE-AUDIT-001 — Can the current corpus source a nontrivial holonomy?

## Question

Before further curved-core mesh work, determine whether any existing rope degree of freedom supplies the Aharonov–Bohm phase

\[
\theta_{AB}=q\Phi/\hbar
\]

without imposing \(\Phi\), \(q\), or an explicit linking-number term by hand.

## Corpus findings

### 1. A gauge connection exists mathematically, but its physical identification is not derived

GG-001 through GG-004 establish the bundle/connection/curvature language and gauge invariance. GG-005 explicitly keeps the statement that the rope physically instantiates the electromagnetic connection at **Modeled**, not Derived. These claims supply a mathematical place for holonomy, but not a strand-level source or its magnitude.

### 2. FND-013 supplies integer internal circulation, not a calibrated AB flux

FND-013 derives the discrete identity

\[
\oint d\theta = 2\pi N,
\]

with unit defect winding and no smooth zero-defect flux. This is a dimensionless phase-circulation result. The corpus does not derive a map from that circulation to physical magnetic flux \(\Phi\) in the AB coupling.

Moreover, under the most direct identification, a unit winding gives \(\theta_{AB}=2\pi N\) for a unit-coupled probe. Because the validated AB spectrum is periodic under \(\theta\to\theta+2\pi\), an integer unit is spectrally equivalent to zero. A nontrivial AB response would require an additional ingredient: fractional effective coupling, fractional flux, an offset such as half flux, or a different representation. None is derived in the current corpus.

### 3. Transported linking is a current mechanism, not a spontaneous flux source

EM-008 and EM-014 show that transported linking can consistently represent current and that a rotating helix can pump one linking unit per turn. Their registered scope is a mechanical realization of an already-prescribed current. They do not derive a persistent current in the static linked electron/atom geometry, nor do they select its rate.

### 4. The dynamical Maxwell model takes the source current as input

EM-010 evolves a supplied current \(J\) into an Ampere-like field. The current is external to the field evolution; the benchmark does not show the rope configuration self-generating \(J\). Thus it cannot close the source loop for \(\Phi\).

### 5. Helical handedness fixes type and sign only

The circulation and screw benchmarks support the possibility and sign of a circulating response. They do not determine its absolute magnitude. The corpus itself states that the field dictionary remains Modeled partly because the absolute calibration and some dynamical terms are inputs.

### 6. The observable phase cannot currently be calculated

Even if an internal circulation were identified with magnetic flux, the observable AB phase needs \(q\Phi/\hbar\). The corpus does not presently derive all three quantities in one closed chain for this system. In particular, the absolute quantum-action scale remains an acknowledged open boundary in the programme.

## Verdict

**NO_NONTRIVIAL_HOLONOMY_SOURCE_IN_CURRENT_CORPUS**

The current corpus contains:

- a valid gauge-geometric language;
- integer winding and defect circulation;
- a modeled electromagnetic identification;
- mechanisms for transporting linking when a current is prescribed.

It does **not** contain a derivation that makes a static rope configuration generate a nonzero, non-integer AB phase. The most direct topological assignment gives an integer \(2\pi\) phase and is therefore spectrally trivial.

## Consequence

Further curved-core mesh development cannot presently test a rope prediction, because the target holonomy has no derived source or magnitude. ROPE-VALIDATION-001 through 004 remain useful instrument work, but the physical gauge branch should be paused.

The branch should resume only if the framework derives at least one of:

1. a persistent circulation/current selected by the rope ground state;
2. a non-integer effective phase per unit winding;
3. a dynamically selected fractional or offset flux;
4. a framed/twisted degree of freedom whose action coupling fixes \(q\Phi/\hbar\);
5. a justified new nonlocal coupling, clearly labeled as an added postulate or phenomenological term.

## Recommended next action

Do not begin conforming-mesh or cut-cell work yet. Register the sourcing gap as an explicit Open dependency. The cheapest constructive follow-up is an analytic and corpus-level audit of whether twist, framing, or the existing screw-current dynamics can support a stable persistent circulation in a closed rope without external drive. If that audit is negative, cancel the physical AB branch rather than extending the instrument further.
