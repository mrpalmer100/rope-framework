# The Number That Wasn't There

## Six commissions on gravity's coefficient, in plain language

Mark Palmer · with computational collaboration by Claude (Anthropic) ·
palmer100@gmail.com

This is the accessible account of the exact-D arc: six chartered
commissions (GRV-096 through GRV-101, August 2026) that set out to
measure one number and ended up correcting a flagship result,
discovering a new universal quantity, proving a structural theorem, and
producing a candidate physical principle. Everything here is registered
in the claim registry with locked bars and executable benchmarks; this
document adds no claims and softens none.

## The setup: what the number was supposed to be

In this framework, gravity is not fundamental. The vacuum is a woven
medium, and its modes are never still -- they carry an irreducible
zero-point jitter. When the medium is bent, the energy of that jitter
changes, and the medium pushes back. The push-back has been shown to
have exactly Einstein's tensor shape (the absorption exam, GRV-024/025):
bend the medium and its quantum hum responds the way general relativity
says spacetime responds. That shape result is the gravity sector's
crown jewel and it stands untouched through everything below -- in
fact it comes out of this arc sharper than it went in.

But a shape needs a size. The strength of the push-back is a
dimensionless coefficient, and the corpus's working formula for the
induced gravitational tension carried it as a constant called D, known
only within a factor bracket. GRV-095 named the obvious next step:
extract D exactly from the instrument that proved the shape. Precision,
not decision. Six sessions later, that sentence reads very differently.

## Commission 1 (GRV-096): the scale gives different weights

The first extraction was straightforward in design: compute the
relevant amplitude on bigger and bigger lattices, extrapolate to the
infinite-size limit, and check that the answer does not depend on
arbitrary choices of measurement protocol. The size-extrapolation was
beautiful -- sub-percent convergence. The protocol check failed
spectacularly: shifting which mass window you fit over moved the answer
by up to 29 percent, and changing the fitting basis moved it by up to
57 percent.

A number that depends on how you measure it is not yet a number. Under
the pre-committed bars, this registered as a failure and was kept, with
a diagnosis: two contributions in the data were nearly
indistinguishable over the accessible window.

## Commission 2 (GRV-097): there are two signals, and ours is the small one

The second commission built the protocol the first one's diagnosis
called for: a measurement window that scales toward the ideal limit,
dense sampling, a richer model, and -- the key addition -- a second,
independent extraction method based on third differences, which
annihilates every smooth polynomial contribution exactly and leaves
only the genuinely non-smooth signal.

The new instrument worked well enough to reveal that the disease was
never the protocol. The non-smooth content of the data has TWO terms,
and the one carrying the would-be D is nearly six times smaller than
its sibling across every window the lattice can legally reach. You
cannot weigh a mouse while an elephant stands on the scale. Four of
five bars fired; the failure was registered and kept; the elephant's
weight was measured on the way down (with a machine-exact internal
identity as the check), and the route forward was named: derive the
elephant from first principles and subtract it.

## Commission 3 (GRV-098): the limits do not commute

Deriving the sibling term meant moving from the lattice to the
continuum, where the two limits in the problem -- the probe wavelength
going long, and the mode mass going light -- can be taken in either
order. The commission discovered they give different answers. Taken in
the order every lattice protocol was forced to use, the continuum
machinery reproduces exactly what the lattice measured (the
reconciliation, accurate to 13 percent -- proof the machinery is
sound). Taken in the other order -- the order the actual definition of
D requires -- the coefficients come out 2.7 times different, and the
extraction destabilizes into a numerical cliff before the true limit
is reached.

Neither prior measurement was wrong. They were correct answers to a
different question than the one D asks. Third failure, kept, and the
residue was the best kind of open problem: one explicit, validated
integral whose behaviour in the final limit is a pencil-and-paper
question.

## Commission 4 (GRV-099): the number is zero, and the real signal is a logarithm

The asymptotic analysis was run with its predictions locked in advance,
and half of them were confirmed while the other half were refuted --
both registered. The confirmed half: the deep-infrared region
contributes no term of the form D was supposed to have. The refuted
half: the specific logarithm the analysis predicted does not exist
either. What DOES exist is a different logarithm -- an even one, of
the form (mass squared) times log(mass squared) -- sourced by both
halves of the response, with one half exactly solvable and serving as
an internal control that the method passed at the level of two parts
in ten thousand.

Then came the arc's keystone computation. That single derived
logarithm, held fixed rather than fitted, accounts for 82 to 88
percent of everything the lattice ever measured. The "two-term
structure," the protocol dependence, the non-commuting cliff -- all of
it was one logarithm wearing a disguise that the earlier fitting bases
could not see through. And the direct verdict on D itself: with the
logarithm properly modelled, the D-channel amplitude shrinks toward
zero in proportion to the probe wavelength. In the defining limit, D
is zero. The number the arc was hunting does not exist.

## Commission 5 (GRV-100): the logarithm is Einstein's, and the strength is not predictable

Two questions remained. Does the newly found logarithm have the right
shape to BE gravity? And what does a logarithm mean for a formula that
wanted a constant?

The shape test used the original absorption exam's own locked criterion
and returned the arc's most striking positive: the logarithm passes the
Einstein-pattern test one hundred times more cleanly than the original
verdict did. Retroactively this is no surprise -- the original numbers
were mostly this logarithm in disguise, so the pattern was always its
pattern. The covariant induced action is real, it lives in the
logarithm, and its slope is a derived universal constant of the medium.

The sobering half: a logarithm's absolute value depends on a reference
point, and over any honest range of reference points this one even
changes sign. So the theory predicts the SHAPE of induced gravity and
its RUNNING, but cannot predict its absolute strength from the loop
alone. The corpus's long-standing "scale problem" was thereby promoted
from an open item to a structural theorem about the mechanism. The
practical fallout splits cleanly in two: exclusion arguments that rest
on tens of orders of magnitude survive untouched (logarithms cannot
manufacture orders), while precision numbers inherit the reference
ambiguity -- most prominently the framework's famous scale selection.

## Commission 6 (GRV-101): auditing "eight Planck lengths" -- and finding one

The flagship number said: solve the induced-gravity formula against the
measured strength of gravity, and the medium's lattice spacing comes
out at eight Planck lengths -- the Planck scale emerging from the
framework's own arithmetic, never having been told about it. After
Commission 5, that number carried an unquantified condition, and the
house rules do not allow flagship numbers to carry unquantified
conditions. So it was audited, bars first.

The audit caught something no one predicted: a plain accounting slip.
The coefficient in the chain had been measured as a TOTAL over a
96-site ring and then used as if it were a per-site quantity. Doubling
the ring doubles it -- verified with the original claim's own code --
and the stowaway factor is the square root of 96, which is 9.8. The
famous "8" was almost entirely ring-size bookkeeping. Corrected, the
selection is 0.80 Planck lengths. One, not eight.

And here the arc hands back more than it took. The deep claim was
never the digit -- it was the CLASS: a dimensionless vacuum
coefficient, solved against measured gravity, lands the spacing at the
Planck scale unprompted. That survives on both calculational routes,
is structurally protected against reference-point games (the spacing
goes as the square root of the coefficient, and logarithms cannot move
square roots by orders), and is arguably stronger now: 0.80 is closer
to one Planck length than 7.8 was. The sub-Planck reading -- a lattice
at or finer than the Planck length -- is registered plainly as the
strong ontological statement it is.

One more gift fell out. Requiring gravity to attract rather than repel
turns out to select which half of the reference-point range is allowed:
the reference scale must sit above the medium's band gap. That is the
first physically motivated candidate for the very principle Commission
5 said was missing. It is registered as a candidate, not a conclusion
-- but the question "what fixes the logarithm's reference point?" now
has a live answer on the table.

## What the arc accomplished, in one place

Started with: a shape proof, a constant D known to a factor bracket,
and a headline of eight Planck lengths.

Ended with: the constant proven not to exist; a derived universal
logarithmic slope carrying Einstein's pattern a hundred times more
cleanly than before; a structural theorem that this mechanism predicts
gravity's shape and running but not its absolute strength; a corrected
flagship -- one Planck length, both routes agreeing in class; a
registered erratum with the exact factor named; a candidate physical
principle (positivity selects the reference half-line); and six claims
in the registry, three of them kept failures, each one explaining its
predecessor.

## Why the failures were the method

Three of the six commissions ended at their own kill conditions, and
none of those endings was wasted. The first failure located a
degeneracy; the second measured the confounding term and named the
subtraction; the third proved the limits do not commute and reduced
the problem to one integral; and the successes of commissions four
through six were built directly on those registered corpses. At no
point was a bar widened, a window re-chosen after the fact, or a
number dropped from the record. The arc is what the house discipline
looks like when it works: the wrong turns are not embarrassments to be
smoothed over -- they are the load-bearing steps, kept at full
strength, that made the right answer checkable.

Every number in this document is re-verified by a deterministic
benchmark shipped with the corpus: exact_d_extraction, exact_d_ordered,
exact_d_derived, exact_d_asymptotics, exact_d_interpretation, and
exact_d_scale, under benchmarks/gravity/. The charters, with bars
locked before computation and outcomes appended after, are in
docs/technical/COMMISSION_EXACT_D.md through COMMISSION_EXACT_D6.md.
