# TOPOLOGY COMMISSION -- analytic spectator test (FIRST BRICK)
# Computed 2026-08-23 under the locked charter
# (analysis/TOPOLOGY_COMMISSION_charter_LOCKED.md). Shared
# parameters throughout: rope tension T0, linear density mu, source
# strength q_s, identical boundary conditions. NO parameter is
# introduced after seeing results; every FAIL below is stated with
# the rescue that would cure it and why the no-rescue rule bars it.

## THE SETUP (as chartered)

Atoms A and B held at separation r in identical configurations.
M distant neutral spectators added at distance R >> r,
M = 0, 8, 64, 512, ... The question per test: do A's LOCAL
properties change, other than through an identifiable field
arriving from the spectators?

=====================================================================
## MODEL 1: DIRECT-ROPE (every atom roped to every other atom)
=====================================================================

The primitive is a physical rope: tension T0, density mu, one rope
per pair. Its mechanics are fixed by classical string theory and are
not negotiable once T0 and mu are shared.

T4 STATIC FORCE. A taut rope pulls each endpoint with force T0
    DIRECTED ALONG THE ROPE, INDEPENDENT OF ITS LENGTH. That is the
    defining property of constant-tension string. So the A-B force
    is F = T0 at every separation: F(r) = const, not 1/r^2.
    THE ONLY CURE is a per-rope tension law T(r) = K/r^2 inserted by
    hand; uniform rope mechanics cannot produce it (a rope does not
    know its length at its endpoint). BARRED RESCUE. ** FAIL **

T1 ENERGY SCALING. The energy of a taut rope grows at least as
    T0 * length. A carries one rope to every atom:
    E_A = T0 * sum_i r_i. The universe carries
    E = T0 * sum_pairs r_ij ~ N^2 * T0 * <r>: SUPER-EXTENSIVE.
    Cure: renormalize T0 -> T0/N (population-dependent). BARRED.
    ** FAIL **

T2 SPECTATOR INDEPENDENCE. Two separate reprices, both local and
    measurable:
    (a) Energy: adding M spectators at distance R adds
        Delta E_A = M * T0 * R to the energy bound in A's ropes --
        unbounded in both M and R.
    (b) Inertia/drag: transverse motion of A launches waves into
        every attached rope; a long rope presents input impedance
        Z = sqrt(T0 * mu) at its endpoint, so A feels reaction
        force F = -(N-1+M) * Z * v. A's effective dynamical
        response DEPENDS ON THE POPULATION OF THE UNIVERSE.
    Cure for both: the same barred 1/N normalization. ** FAIL **

T3 GAUSS LAW. The natural flux object is the count/strength of
    ropes crossing a sphere S of radius s around A. Every rope from
    A to an atom OUTSIDE S crosses it, so the flux is
    N_outside(s) * T0: it depends on the EXTERIOR population, not
    the enclosed source. ** FAIL **

T5 PROPAGATION. Signals travel along each rope at
    c = sqrt(T0/mu); arrival at separation r occurs at r/c (rope
    length >= r). No superluminal response. ** PASS **

T6 FLUX SPREADING. A rope is a 1D waveguide: amplitude does NOT
    decay along it. A disturbance at A arrives at B with amplitude
    independent of r; energy delivered to a shell scales with the
    number of ropes threading it, not with any conserved spherical
    flux. There is no 1/r law and no flux conservation across
    spheres. ** FAIL **

T7 ISOTROPY. The vector sum over many discrete ropes becomes
    direction-independent for isotropic atom distributions at large
    N. ** PASS (asymptotically) **

T8 POLARIZATION. Each rope carries exactly two transverse modes
    with a separate longitudinal channel. ** PASS (per rope) **

T9 CLUSTER SEPARABILITY. Two laboratories of N1 and N2 atoms at
    separation R: every cross pair is a rope pulling with T0, so
    the inter-lab force is N1 * N2 * T0, INDEPENDENT OF R and
    growing with lab size. Two distant laboratories are never
    independent. Cure: the same barred rescues. ** FAIL **

DIRECT-ROPE SCORE: 3 PASS (T5, T7, T8), 6 FAIL
(T1, T2, T3, T4, T6, T9). Every failure is curable ONLY by a
population-dependent normalization (T0/N) or a hand-inserted
per-rope force law (T(r) ~ 1/r^2), both barred by the locked
no-rescue rule unless derived from rope mechanics -- and constant
tension string mechanics cannot derive either.

=====================================================================
## MODEL 2: LOCAL-WEAVE (each atom couples to its neighborhood;
## disturbances travel through the connected medium)
=====================================================================

The primitive is a 3D elastic medium of the SAME tension and
density; the coarse-grained disturbance field phi obeys the local
operators the corpus already computes with:
    static:   nabla^2 phi = -rho / kappa        (kappa from T0, mu)
    dynamic:  (1/c^2) d^2 phi/dt^2 - nabla^2 phi = source,
              c = sqrt(T0/mu)

T4 STATIC FORCE. The 3D Green function of the Laplacian is
    phi(r) = q_s / (4 pi kappa r), so F(r) ~ 1/r^2. DERIVED, not
    inserted: 1/r^2 is the geometry of three dimensions expressed
    through a local operator. ** PASS **

T1 ENERGY SCALING. Energy is a density integral,
    E = integral (kappa/2)|grad phi|^2 + ... ; for well-separated
    sources E ~ N * (self energy) + O(pair/R): EXTENSIVE up to
    interaction terms that vanish with distance. ** PASS **

T2 SPECTATOR INDEPENDENCE. M spectators at distance R contribute
    at A a potential ~ M q_s / (4 pi kappa R) whose GRADIENT at A
    is ~ M q_s / R^2 -> 0 as R grows (or is the identifiable
    arriving field when finite). A constant potential offset
    repriceses nothing local: forces, energies stored near A, wave
    speed, and coupling depend on LOCAL gradients and LOCAL medium
    properties (T0, mu), none of which know M. ** PASS **

T3 GAUSS LAW. By the divergence theorem applied to
    nabla^2 phi = -rho/kappa:
    closed-surface flux of grad phi = -(enclosed charge)/kappa,
    EXACTLY, identically, for any exterior configuration. ** PASS **

T5 PROPAGATION. The wave operator is hyperbolic; its retarded
    Green function is supported on (3D: exactly on) the cone
    |x| = c t. Nothing arrives before r/c. ** PASS **

T6 FLUX SPREADING. Outgoing 3D wave amplitude ~ 1/r; energy flux
    through spheres ~ (1/r)^2 * 4 pi r^2 = const: conserved
    spherical flux with 1/r amplitude, by the same geometry that
    gave 1/r^2 statics. ** PASS **

T7 ISOTROPY. A discrete weave has lattice anisotropy at scale a
    that enters observables at O((k a)^2) and vanishes in the
    long-wavelength limit; the corpus's own 4th-order stencils are
    built exactly to accelerate this convergence, and the
    registered continuum-limit studies measure it. ** PASS **

T8 POLARIZATION. A tensioned 3D medium carries two transverse
    modes; longitudinal contamination is a controllable channel --
    the corpus's wsNyq bar IS the standing instrument that polices
    it, and every registered member satisfies it. ** PASS **

T9 CLUSTER SEPARABILITY. Inter-cluster interaction energy
    ~ N1 N2 / R -> 0 as R grows; distant laboratories decouple as
    1/R. ** PASS **

LOCAL-WEAVE SCORE: 9 PASS, 0 FAIL. No parameter was introduced
beyond the shared (T0, mu, q_s); every 1/r^2, 1/r, and r/c above is
a THEOREM of the local 3D operator, not an input.

=====================================================================
## VERDICT (by the registered forms; the four forms are exhaustive)
=====================================================================

** V2: LOCAL TOPOLOGY SUPPORTED. **
The weave passes all nine locked tests by derivation from shared
parameters. Direct ropes fail six of nine, and every failure is
curable only by the barred rescues (population-dependent
normalization, or a per-rope 1/r^2 tension law that constant-tension
rope mechanics cannot produce). This is not V3 (empirical
equivalence): the two models differ OBSERVABLY at T1, T2, T4, T6,
and T9 -- constant vs 1/r^2 pair force alone separates them in any
laboratory.

The author's declared prior (local weave) is CONFIRMED by the
analytic brick. Scored for the record.

## WHAT THE ANSWER MEANS FOR THE CORPUS (per the registered
## consequences)

The weave is real and the all-to-all ropes are metaphor. Every
registered equation was already weave-native (the psi Poisson
solver, the torus stencils, the EM wave operators), so NO REGISTERED
PHYSICS CHANGES. What the corpus owes is prose harmonization: the
Gaede-style point-to-point language ("A Taut Rope Between Every Two
Things", "stretching between every pair of atoms") should be
recast as what it correctly gestures at -- the EFFECTIVE pairwise
1/r^2 interaction that the weave MEDIATES, the way "field lines"
are spoken of in electromagnetism without anyone building them out
of string. The direct-rope picture survives as a visualization of
the weave's Green function, not as ontology.

Numerical follow-ups (M-ladder simulations of T2, discrete-weave
isotropy scaling) remain available to the commission but are NOT
required for the verdict: every decisive line above is closed-form.

## STANDING NOTE

The spectator test was decided analytically, as the author's
first-brick scheduling anticipated. If any future result appears to
give the direct model a derivation of per-rope 1/r^2 tension from
rope mechanics alone, this verdict reopens at that specific point;
nothing else in it is contingent.
