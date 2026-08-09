# The Target-Free Question, and Why It Goes First

*A methodology note, written from a worked case in which it changed the answer.
Sealed commissions and their verdicts:
`SEALED_COMMISSION_fnd017_directional_reading.md`,
`SEALED_COMMISSION_2_fnd017_exclusion_and_doublecount.md`.
Registered results: FND-MATTER-058, 059, 060.*

---

## The problem this addresses

A construction misses its target by some factor. There is a candidate move
available that would close the gap. The move is not obviously wrong — it has a
real argument behind it, drawn from relations the corpus already owns.

This is the most dangerous configuration in derivation work, and it is dangerous
for a reason that ordinary care does not reach. The failure mode is *not* that
someone knowingly fits. It is that a correct sub-result, argued correctly, gets
applied where it does not belong, and the application is motivated by a gap the
arguer can see. Every individual step survives scrutiny. The conclusion is
wrong anyway.

Pre-committed bars do not catch this. Refusal discipline within a session does
not catch it. Target-blind sessions catch it only if the blindness holds, and
blindness is fragile: an answering session tracing a relation through a
repository will read the surrounding files, and once it has seen the gap it
cannot un-see it.

## The rule

**When a candidate factor is worth approximately what the gap needs, do not ask
whether the factor is right. Find the question whose answer is wrong wherever it
lands, and ask that one first.**

Such a question exists more often than one expects. It is usually a bookkeeping
question rather than a physical one: a units check, a double-count check, a
question about which primitive a calculation actually integrates against. Its
defining property is that neither of its answers is convenient — an error is an
error regardless of which direction it moves the result.

That property is what makes it robust to contamination. A session that knows the
target still cannot bias a question whose answers carry no differential
advantage. The blindness stops being load-bearing, which matters because
blindness is the part of the protocol most likely to fail in practice.

## The worked case

**The setup.** A mechanism for a suppression parameter landed at a gap of 2.08×
against a pre-committed bar of 2.00×. A missing factor of 3 was available: the
corpus registers `T0 = Sigma a^2/3`, and the 3 could be read as a per-direction
partition such that a displacing inclusion engages one share rather than the
full cell face. Worth exactly 3×. Would have landed the mechanism at 1.44×,
inside the bar.

**What was refused.** The factor, on the grounds that a reading settled by its
usefulness is not a reading. Registered as *permitted and refused*, with the
question sent out to a fresh session under seal.

**What went wrong with the first seal.** The answering session traced the
relation through the repository, read the surrounding analysis in the course of
doing so, and disclosed it unprompted. Void condition fired. It returned FORCED
— the convenient answer — with a tight argument: an inclusion does not
selectively evict one strand family while two thread through, so removal is
wholesale, exactly as an earlier polarization factor had been ruled forced.

**The split that saved the useful half.** Two halves of that verdict carried
contamination unequally. The *provenance* half — where does the 3 come from —
was mechanical: the tube radius cancels identically, and what survives is an
areal density whose numerator is the family count. Checkable by anyone,
independent of judgment, and it landed *against* the alternative the commission
had named as the crux. Registered (FND-MATTER-059). The *exclusion* half was
worth the gap and was not registered.

**The target-free question.** `Sigma = 3 T0/a^2` already contains the 3.
Pricing displaced strand-equivalents at `a^2/3` reintroduces it. So: does the
construction reach displaced content via `Sigma`, or via strand counts? If via
`Sigma`, the 3 is double-counted and the correct factor is 1. If via strand
counts, it enters once and the exclusion argument stands.

A double-count is an error wherever it lands. The question could not be biased.
It was asked first, ahead of the exclusion argument.

**The verdict, and why it vindicates the ordering.** The answer was neither
branch. The construction computes a *fraction* — displaced cross-section over
available cell area — and any content density cancels identically between
numerator and denominator. The 3 cannot enter *once*. The error was writing
`pi r^2/(a^2/3)`, which prices the numerator in strand-equivalents while leaving
the denominator a raw cell face: a mixing of units of account across the bar of
a fraction, and that mixing was the entire 3×.

The exclusion argument was **sound and proved the opposite of its conclusion**.
If an inclusion evicts all three families, the denominator must count all three
too. The `a^2/3` reading is the one that would require an inclusion to see a
single family's share.

The session answered against its own prior position and located its own error to
the line. That is what a genuinely target-free question buys.

## The second rule: a stopping condition, fixed in advance

Per-session refusal discipline protects against fitting *within* a session. It
does nothing about a sequence of individually-blind sessions continued until one
returns the convenient answer. That is a fit with extra steps, and it is
invisible from inside any single session — each one is clean.

Before the second seal ran, its terminal condition was written into the registry:
this is the last reframing, these outcomes close the question, no third
commission. The condition was honored when the verdict came back negative.

**A blind sequence without a pre-committed stopping rule is not blind.**

## The third rule: seal the right side

The residual open item in this case is target-side — the target's own
construction may convert through the same primitives. A session auditing it must
have the *mechanism* sealed out, not the target.

The asymmetry is not arbitrary. The failure mode being guarded against is a
target quietly adjusted to meet a construction, so the thing hidden is whichever
side would supply the motive.

## Summary

1. When a factor is worth what the gap needs, find the question whose answer is
   wrong wherever it lands, and ask it first.
2. Split a contaminated verdict by *how much contamination each half can carry*.
   Mechanical results survive; judgment calls do not.
3. Fix the stopping rule before the sequence runs, or the sequence is a search.
4. Seal the side that would supply the motive.

The case above produced two keepers and a negative. The negative is the one that
required all four rules.
