# How 1/alpha Was Derived

*A plain provenance record: every factor of the fine-structure constant in the
electron-dressing chain, and the theorem that produced it. See the diagram at
docs/alpha_derivation_map.png. Full per-brick record in docs/commissions/
SYNC_STATE.md and the COMMISSION_{T..Z} and Gate files. Registered as claim
ALPHA-DE-CHAIN.*

## The result

    1/alpha = 4 pi^3 D_E = 137.060504     (measured: 137.035999,  +178.8 ppm (0.018%))

Every factor is derived. The +178.8 ppm (0.018%) residual is the single unexplained
number. This is a **reduction** of 1/alpha to one blind number times a derived
prefactor -- it is **not a derivation of alpha's value**.

## Factor by factor, with provenance

**D_E = 1.1051029  --  the electron dressing.**
Commission W. An Euler-Lagrange boundary-value solver on the rotating winding
terminus computes the dressing BLIND -- before any comparison to alpha -- across
5 configurations, agreeing to 7 digits with a passing convergence gate. This is
the one number the chain takes from direct computation.

**x 4  --  the rectified two-component sampling.**
Gate 2 (LINEAR) together with Gate 1's rectification theorem. The electron's
charge couples through a force-type (linear) observable: the directed tether
load I_Q[f] = P(g^2) f', degree 1 in the profile, computed on the committed
solution (the energy competitor is degree 2 and is already spent as D_E, so
there is no double counting). A first-power quantity rotating with the source
has identically zero smooth cycle mean, so by Gate 1's theorem its laboratory
recording must be rectified, and the two-component rectified mean <|cos|+|sin|>
is 4/pi exactly. This factor was discharged OUT OF SAMPLE by the magnetic moment
(see below).

**x pi  --  the J0 anchor conversion.**
Gate 1 (CLOSED). The occupancy freeze I_mode = E/omega = m J0 (Commission O)
forces the recording convention: kappa = <cos^2>/<|cos|> = pi/4. The forcing is
not a fit -- a first-power linear recording of a pure harmonic has identically
zero smooth mean, so rectified is the only recording that produces a number at
all. Confirmed by one formula, J0 = m_e c A / pi, reproducing TWO registered
targets (hbar/(pi alpha) at the anchor scale and hbar at the confinement scale);
the smooth-quadratic competitor misses both by pi/4.

**x pi  --  the target scale pi lambda_C.**
Commission E. The conversion of the confinement scale through the tension T0 --
a single conversion with no free factor, audited clean.

**x pi  --  the U-closure geometry.**
Commissions U and T. The two-constraint closure R* = J/(pi^2 mu q^2 c), with
ln x* = pi^2 exact (T's confinement anchor, x* = e^(pi^2) = 19333.7). The pi^2
is clean rotation-closure geometry; one of its two pi factors is the third pi in
the prefactor.

*(Prefactor bookkeeping: the naive geometric form is pi^4 = pi^2 [U closure] x
pi [target] x pi [J0 anchor]. Gate 2's rectified 4/pi enters at the J0-anchor
conversion, turning pi^4 into 4 pi^3. This was the correction of a premature
pi^4 lock caught on external review.)*

## The residual

**+178.8 +/- 0.4 ppm (0.018%)  --  the single open number.**
Not derived. Z Brick 5 proved a scale-invariance theorem (d ln D_E / d ln x* = 0
exactly): the chain's value depends on no continuous dial, only the discrete
branch choice k/T0 = 2 (adjudicated by the electron against FND-021). The
residual ladder is exhausted -- the branch, the r_min continuum limit, and the
q^2 winding slot are all excluded by computation. So the +178.8 ppm (0.018%) is either
physics the chain does not yet contain or the anchor-metrology
reading's own limit. It is pinned against a construction with no adjustable
continuous parameters.

RESIDUAL STATUS (final, 2026-08-09): every named candidate has now been run.
The V-A boundary term missed cleanly; the functional-completeness audit
(D-E-COMPLETE) came back clean; and the last surviving class, the radiative
back-reaction (Commission LEAD-RAD), was run blind and closed at OUTCOME 4,
THE QUANTUM FENCE: the moment-side back-reaction weight is cutoff-defined at
power 1/3 in the angular cutoff, with no alpha-independent registered core
scale to regulate it, so the required two-target confrontation was never
licensed. The residual is fenced as quantum-radiative: not derived, not
refuted, the classical arc's constructively-audited endpoint.

## Three independent observables, one convention structure

The same convention structure that fixes the prefactor was tested on three
observables that did not all fix it:

- **Anchor J0** (Gate 1): one formula hits two registered J0 targets (hbar/pi
  alpha and hbar).
- **Magnetic moment g = 2** (Gate 2b): with every input frozen before the moment
  was mentioned, the mechanical moment pi mu_B converts under the Gate-1
  recording (x 1/pi) to exactly 1 mu_B -- the Dirac value, g = 2, zero freedom.
  It misses the measured moment by -1160 ppm, which is the radiative Schwinger
  anomaly alpha/2pi (+1161 ppm) to 0.15% -- the same class of not-yet-contained
  physics as the chain's own residual. The smooth-quadratic competitor gives
  pi/4 mu_B (-21.5%, the wall class). This is a genuine out-of-sample check: the
  moment was never used to build the chain.
- **Atomic binding 13.6 eV** (Gate 3): the derived-alpha chain reproduces the
  Rydberg at exactly the residual squared (-357.6 ppm = 2 x the chain residual,
  since E ~ alpha^2). The consistency core is algebra once the chain is
  consistent (correctly not oversold); the independent content is the 1/2
  derived from the EM-015 Coulomb virial and the convention-count confirming the
  single 4/pi lives in e^2 (a competitor with an extra 4/pi misses by +27%).

## The honest headline

Every factor of 1/alpha = 4 pi^3 D_E has a derivation. One +178.8 ppm (0.018%) residual
is unexplained. Three independent observables are consistent with the one
convention structure, and g = 2 falls out as a free byproduct with its residual
localized on the Schwinger term (named, not derived). This is a reduction of the
fine-structure constant to a single blind number times a fully-derived
prefactor, pinned against a dial-free construction -- **not a derivation of
alpha's value**. The last residual question is now ANSWERED at the classical
level: LEAD-RAD (2026-08-09) closed at the quantum fence, so the residual is
the quantum/radiative wall, reached constructively (cutoff-defined weight,
power 1/3) rather than by elimination. The classical arc is complete; the
fence re-opens only if an alpha-independent core scale is ever registered.

## Self-corrections in the permanent record

Three flattering results were retired during this arc, and the retractions
stand: the premature pi^4 prefactor lock (corrected to 4 pi^3 on external
review); the -15 ppm Delta correction (retired by Z's consistency audit as a
reading-mixing artifact); and the Omega x D_E numerical coincidence (its rate
channel nulled in-package when the derived coefficient came out -0.19, not the
required value). The discipline that caught these is why the surviving result is
trustworthy.
