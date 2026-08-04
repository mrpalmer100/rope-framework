# FND-STRAND-026 — antibunching formalized against the QB pin

Date: 2026-08-04. Commission: FND-STRAND-025's first queued consequence.
The QB campaign pinned every classical local field model at g2(0) >= 1
(the Cauchy-Schwarz bound on intensity correlations) against the
measured ~0.18, and cornered the only classical escape to instantaneous
constraint propagation, with QB-009 demonstrating sufficiency for
g2 ~ 0 in a conservation toy. Tonight the pin, the measurement, and the
grant are joined into one formal statement.

## T1 — the faithfulness theorem (detection inherits source statistics)

Under Grant 3 plus the Born law, a beamsplitter measurement of g2 is a
MULTINOMIAL SAMPLER of the source's quantum number n. For source
distribution p(n), splitter transmittance tau, and arm efficiencies
eta_A, eta_B, the delivered counts are the thinned variables
n_A ~ Thin(n; tau eta_A), n_B ~ Thin(n; (1-tau) eta_B), and

    g2_cross(0) = <n_A n_B> / (<n_A><n_B>) = <n(n-1)> / <n>^2

EXACTLY — independent of tau, eta_A, eta_B. Proof: for multinomial
thinning of a common n, <n_A n_B> = c_A c_B <n(n-1)> and
<n_A> = c_A <n>, <n_B> = c_B <n> with c the per-arm retention
probabilities, so every instrumental constant CANCELS in the ratio.

COROLLARY (thinning invariance): loss cannot manufacture or destroy
antibunching. g2 is a property of the SOURCE's number statistics, and a
lossy, unbalanced, inefficient apparatus measures it faithfully. This
is precisely the efficiency-independence that makes the real
Grangier-Roger anticoincidence parameter meaningful, here derived
rather than assumed.

## T2 — the pin, resolved rather than contradicted

The QB campaign's bound g2 >= 1 is a theorem ABOUT CONTINUOUS INTENSITY
FIELDS: for classical stochastic intensities I_A proportional to I_B,
Cauchy-Schwarz forces <I_A I_B> >= <I_A><I_B> at zero delay. Grant 3
changes the OBJECT the detector samples: not a divisible intensity but
an integer number of indivisible quanta. For n = 1, <n(n-1)> = 0 and
g2 = 0 -- the bound's premise (divisibility) is removed, not violated.
The pin therefore stands exactly as registered (it is the reason a
grant was NEEDED), and the grant is exactly what steps past it. The
corpus's earlier cornering survives untouched: any MECHANISM for the
grant must still be nonlocal-in-delivery at the two arms, which is what
QB-009's constraint-propagation toy demonstrated sufficient -- that toy
is hereby the STANDING MECHANISM CANDIDATE for the funneling dynamics
(F4's bounty has one named contender).

## T3 — the measured 0.18, located

A real heralded source is a mixture: p0 vacuum, p1 one quantum, p2 two
(higher terms negligible). By T1:

    g2 = 2 p2 / (p1 + 2 p2)^2

The measured g2 ~ 0.18 is therefore a statement about SOURCE PURITY
(two-quantum contamination), not about detector physics: p2/p1^2 ~ 0.09
reproduces it. The framework's prediction for a perfect single-quantum
source is g2 = 0 exactly; for any real source, g2 = the contamination
formula -- both falsifiable (F2 of the grant), and the second one
CONFRONTABLE against any published heralded-source characterization
that reports p1, p2 alongside g2.

## T4 — the discrimination table (what each source class must show)

| Source (number statistics) | g2(0) under Grant 3 | classical field bound |
|---|---|---|
| Single quantum (n = 1) | 0 | >= 1 |
| Heralded with contamination | 2p2/(p1+2p2)^2 | >= 1 |
| Fock n | 1 - 1/n | >= 1 |
| Coherent (Poisson) | 1 | 1 (attained) |
| Thermal (geometric) | 2 | 2 (attained) |

The grant and the classical field theory AGREE everywhere the classical
theory is attainable and DISAGREE exactly where experiment disagrees
with classical fields. Sub-Poissonian rows are the framework's
commitment; the super-Poissonian rows are its consistency check.

## Status and scope

Derived, conditional on Grant 3 (carried on the face). The theorem is
counting arithmetic; the benchmark executes T1's invariance (sweeping
tau and efficiencies), T3's contamination formula, and T4's table
against Monte Carlo. Which-path, delayed choice, HOM, and CHSH remain
exactly where the roadmap and QB-003 put them. Absolute scale untouched
(FND-MATTER-003).
