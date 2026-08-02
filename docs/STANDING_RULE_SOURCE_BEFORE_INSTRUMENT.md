# Standing rule: ask what sources the quantity before building the apparatus that measures it

Adopted 2026-08-01, after two branches were retired on the same failure mode.

## The rule

Before investing sessions in instrument, control, or solver quality for a
proposed effect, first answer, from the registry alone:

1. **What in the corpus sources the quantity the instrument would measure?**
   Name the claim. If nothing does, say so.
2. **What magnitude does that source predict?** An order of magnitude is
   enough. If the source cannot supply one, that is the answer.
3. **Is the predicted value observable in principle by the proposed
   instrument?** A derived value that lands in the instrument's null space is
   a structural obstruction, not a small effect.

This audit is cheap -- typically one session of reading plus an estimate --
and its outcomes are asymmetric. If a source exists, every later validation
gains a target magnitude and becomes a test of a prediction. If none exists,
the branch is closed before its most expensive component is built.

## Why it exists: two precedents

**The pilot-wave sub-quantum branch (ELEC-056).** Seven claims of genuine
work -- a flow uniqueness proof, a dynamical CHSH violation at 2.724, a
four-claim relaxation programme, a chaos-versus-transport discrimination --
were built while the layer's physical scale came from HBAR-005's 4.31 fm.
When that length was corrected (ELEC-054) and its nuclear consequence
excluded (ELEC-055), a machine-checked audit found the programme had NEVER
depended on the anchor: no claim carried it at any depth in 165-171 ancestors,
and no benchmark contained a single dimensionful constant. The mathematics
survived intact and the branch lost its only bridge to observation. Status:
validated mechanism, no empirical content.

**The gauge/Aharonov-Bohm branch (ROPE-SOURCE-AUDIT-001/002).** Five sessions
produced a validated ring solver, a diagnosed penetrable-core failure, a
validated straight excluded core, and a diagnosed curved-boundary failure --
all gauge-invariant to 1e-13, all correct, all checks that the instrument
reproduces textbook physics. One session of reading then found that nothing
in the corpus sources a flux, and worse, that the one topological circulation
the corpus DOES derive (2 pi N) lands exactly in the instrument's null space.
Status: validated instrument, no target.

## The cost that was paid

Roughly eight to nine sessions across the two branches, all of it competent
work, none of it wasted in the sense of being wrong -- but arriving after the
investment rather than before it. In both cases the closing question cost one
session and could have been asked first.

## The corollary

An instrument with no target is a legitimate artifact and should be retained
and labeled as such. What is NOT legitimate is describing such a branch, on a
front page or in a summary, as an active line of physics. Both branches above
carry explicit no-target status in their registrations for this reason.


---

## Companion rule: check forward before you rely (added 2026-08-01)

The rule above prevents building an instrument for a quantity nothing sources.
Its companion prevents building on a result something later revised.

**Before relying on any registered claim, run:**

    python tools/forward_check.py <CLAIM-ID>

It lists every later claim that names it, depends on it, or shares its sector
while using the corpus's revision vocabulary. Reading the hits is cheap.

**Why it exists.** On 1 August 2026 the corpus made this mistake twice in one
day. HBAR-010 was classified as surviving a sector retirement because it did not
use the retired *length* — it used the retired *relation*. And GRV-049 used a
luminosity law that GRV-047 had revised three claims earlier in the same sector,
under a title announcing the revision in capitals; the resulting number was wrong
by **63 orders of magnitude**. Both were caught by a human reading, not by any
tool, and in both cases the conclusion happened to survive — which is luck, not
method.

**The asymmetry that makes it worth doing.** `verify_corpus.py` and ELEC-065's
sweep both look DOWNSTREAM, asking what a changed claim affects. Neither looks
FORWARD, asking whether the claim you are about to use has itself been changed.
That is the direction errors actually travel when a corpus is being extended.
