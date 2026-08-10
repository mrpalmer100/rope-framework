# COMMISSION B (v2): THE THREE-PIN PROBLEM
# (supersedes COMMISSION_B_two_lattice_reconciliation.md; issued after
# FND-REL-004 landed and before any B session ran)

## What changed since v1
Commission A registered FND-REL-004, and the two-pin problem became a
three-pin problem. The corpus now holds three independent pins on a
microscopic length, mutually incompatible under a one-lattice reading:

  PIN 1 (matter): the M-point calibration, a = 6.0e-17 m
         (FND-MATTER-044/049; the one spent calibration, pinned by m_e).
  PIN 2 (photon): the LHAASO tolerance, a <~ 9.4e-28 m on the lenient
         branch, ~2.5e-29 m on the QB-008 branch
         (FND-REL-004 + Amendment 1; an upper bound, not a value).
  PIN 3 (gravity): the induced-G selection, a = 8 l_P ~ 1.3e-34 m
         (GRV-075/095; conditional on the Sakharov reading).

Pin 2 sits strictly between Pins 1 and 3 and is inconsistent with Pin 1 by
at least eleven orders. Under a one-lattice reading, Commission A has
ALREADY fired FND-MATTER-049's reopening condition ("any independent pin
of the mesh disagreeing with the M-point beyond the zero-point band");
this commission then merely records the firing. The live question is
whether the one-lattice reading is forced.

## The question (restated for three pins)
Trace, claim by claim, which registered quantities each pin actually
depends on, and read off the dependency graph:

  Q1: does the FND-REL-004 dispersion operator's a and the M-point's a
      refer to the same registered primitive? (The operator came from
      FND-STRAND-001 + GRV-029 nearest-neighbor form; the M-point came
      through FND-017's invariance at the registered Sigma. Same lattice
      or different structures on it?)
  Q2: does the GRV-075 band coefficient's scale refer to that same
      primitive? (The band is the weave Hessian's; the Sakharov cutoff
      was flagged as possibly distinct by GRV-007.)
  Q3: if any pair separates, WHERE in the dependency graph does the
      letter a fork, and what physical statement licenses the fork?

Amendment 3 to FND-REL-004 supplies the one candidate fork already
visible: a as DISPERSIVE lattice spacing (what Pin 2 constrains) versus a
as COVERAGE/cell-face geometry (what Pin 1 was calibrated through). The
loaded-continuum picture, if it lands, makes that fork physical rather
than notational: a continuum of nearly-transparent strands has a coverage
scale but no Brillouin structure. This commission does NOT assume that
outcome; it tests whether the registered dependency graph already
contains the fork or whether the fork would be new physics.

## Pre-committed bars (v1 bars inherited, renumbered, extended)
- B1: verdicts read off the dependency graph, not asserted. For each pin,
  the session produces the explicit chain from the pin's number back to
  registered primitives, and the same-or-different verdict per pair
  (1-2, 1-3, 2-3) follows from whether the chains meet at one primitive
  length.
- B2: the output is a THREE-ROW allocation table (pin, value/bound,
  primitive it constrains, claims that use that primitive), auditable
  line by line, plus a flag list of every registered claim that uses "a"
  without disambiguation between forked roles.
- B3: if any pair shares one primitive, the corresponding contradiction
  is registered at full volume with no harmonizing language. Pair 1-2
  sharing a primitive means FND-MATTER-049 is declared REOPENED and the
  M-point terminus is downgraded accordingly. Pair 1-3 sharing means the
  original v1 contradiction. Pair 2-3 sharing is CONSISTENT as stated
  (a bound above a value) and is registered as the corpus's one
  concordant pair if it holds.
- B4 (softened before any session ran, decision logged): no new physics
  inside this commission. The loaded-continuum fork (Amendment 3) may be
  cited as a registered candidate wherever the dependency graph is
  ambiguous about whether the two roles of a were ever identified; the
  session is NOT required to prove non-identification before citing it.
  What remains forbidden is the strong move: declaring a fork VERIFIED on
  the strength of the candidate rather than the graph. If the graph is
  ambiguous, the registrable verdict for that pair is "ambiguous, with
  the loaded-continuum fork the named registered candidate," and the
  question transfers whole to the loaded-continuum commission.
  Construction stays there. Rationale for the softening: the strict
  reading asked the session to adjudicate a close graph question under
  full view of the stakes, which is exactly the contamination condition
  the seals exist to avoid; reporting ambiguity and transferring is the
  honest failure mode, and the bar now permits it by name.
- B5: FND-REL-004 and its three amendments are mandatory inputs to the
  session. Running B without them re-litigates a settled result.
- B6 (new): the session must state, for each contradiction registered,
  which resolution PATHS are already named in the corpus (loaded
  continuum for 1-2; GRV-007's a_grav distinction for 1-3) versus which
  would require unregistered physics -- a two-column paths table, named
  not executed.

## Seal
Unchanged from v1: the dependency question is target-free by
construction (same-or-different is wrong wherever it lands). Ask the
graph questions Q1-Q3 first, before any discussion of which allocation
the corpus would prefer. The stakes section of this document is the
contamination surface; a clean run receives the pins, the questions, and
the bars.

## Stopping rule
One dependency trace, one allocation table, one contradiction
registration per fired pair, one paths table. Ambiguity in any chain is
registered as the finding for that pair, with the specific missing
dependency named; it is not resolved by judgment.

## Registrable outcomes (all acceptable)
1. Full fork: three pins, two (or three) distinct primitive lengths, the
   allocation table becomes the corpus's structural statement of its own
   scales, GRV-007's caveat upgraded to claim, ambiguous-"a" flag list
   drives a notation cleanup pass.
2. One lattice: all three chains meet at one primitive; pairs 1-2 and
   1-3 both fire; FND-MATTER-049 reopens; the M-point survives only as a
   calibration of SOMETHING, with what it calibrated becoming the named
   open question.
3. Partial fork (most likely a priori): 1 forks from {2,3}, i.e. the
   coverage scale separates from the dispersive/gravitational scale.
   Registered with the concordance of pair 2-3 stated (bound above
   value, consistent), and the loaded-continuum commission inherits the
   burden of making the fork physical.
4. Undecidable from registered claims: registered as such, per v1 --
   and under softened B4 this is a first-class outcome, not a failure:
   the pair's verdict reads "ambiguous, loaded-continuum fork the named
   registered candidate," and the question transfers whole to that
   commission with the graph trace attached.

## Depends on
Everything in v1, plus: FND-REL-004 and Amendments 1-3, FND-STRAND-001,
GRV-029, FND-017, FND-MATTER-004, FND-MATTER-056 (the a^2 cell-face
usage), and the loaded-continuum commission's charter (for the paths
table only).
