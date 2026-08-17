# COMMISSION BLOCH-L -- RESULTS (2026-08-17)

Executed under `analysis/COMMISSION_BLOCHL_charter_LOCKED.md` (charter and
bars locked 2026-08-16 at v3.26.69; chartered FND-124, inputs closed
FND-125). Benchmark: `benchmarks/foundations/blochl_longitudinal.py`.

**VERDICT: CONFLICT-REGISTERED (sheet region 2), with a NAMED CORRECTION to
the charter's radius input, an INSTRUMENT CATCH disclosed before the run it
governed, and a CONDITIONAL kb CONSTRAINT that is tripwire-shaped but NOT
declared fired.**

Clean-room held throughout. The sealed values (2.844 c; r_s = 0.2496 a_f;
8.091) appear nowhere in any build leg and nowhere in the benchmark file;
they enter only at section 6 below.

---

## 0. THE CONVENTION AUDIT (leg 0) -- a named correction to FND-125

The charter's section 3 locks R_1 = 0.11254 a_f, R_2 = 0.26959 a_f from
FND-125's joint kappa+tau reading under the "psi-from-axis" realization.
The build could not use them.

The registered angle symbol psi admits two readings:

| | axial direction cosine | R_1, R_2 (a_f) | kappa_1, kappa_2 (1/a_f) | tau_1, tau_2 (1/a_f) |
|---|---|---|---|---|
| A (FND-088) | sin psi | 0.22508, 0.09396 | 2.9619, 2.7506 | 2.0944, 4.6593 |
| B (FND-125) | cos psi | 0.11254, 0.26959 | 2.9619, 2.7506 | 4.1888, 1.6239 |

**kappa is convention-blind** (sin 2psi is invariant under psi -> 90-psi), so
it cannot adjudicate. **tau and R are not**, and the registered tau values
(NUN-GRV8; used again in SHIN8's bars) match reading B.

FND-088's isotropy theorem adjudicates, and it is the load-bearing claim:
its derivation of the angles IS the statement that the axial component of
the tangent is sin psi (sin^2 psi_1 = 1/3 is the second-moment condition
E[t_z^2] = 1/3; the fourth moment fixes psi_2). Run as a control on the
two-level nested winding:

    reading A:  E[t_z^2] = 0.333333333   E[t_z^4] = 0.200000000
                max |A4 - isotropic| = 8.9e-15     <- reproduces FND-088's
                                                      registered 2.9e-13
    reading B:  E[t_z^2] = 0.295888793   E[t_z^4] = 0.180365889
                max |A4 - isotropic| = 2.1e-02     <- not isotropic

**NAMED CORRECTION.** FND-125's R values, and NUN-GRV8's tau values from
which they were read, carry an angle-convention inversion: they are the
tangent/cotangent swap of the correct ones. Corrected:

    R_1 = 0.22508 a_f    R_2 = 0.09396 a_f
    tau_1 = 2.0944/a_f   tau_2 = 4.6593/a_f

Independent strike on reading B, noted not leaned on: it places the
level-2 sub-winding (0.26959 a_f) WIDER than its level-1 parent
(0.11254 a_f).

**WHAT SURVIVES UNTOUCHED:** kappa is unaffected, so FND-091/SHIN7's
curvature arithmetic and the kb ceiling 0.126 T0_f a_f^2 stand exactly as
registered; FND-088's angles stand; FND-125's method (solve the joint
system, do not guess a convention) stands and is vindicated -- only its
reading of which symbol is which was inverted. FND-124's rigidity demand
and the charter survive.

**WHAT THIS DOES NOT COST THE BUILD:** R never enters the instrument
independently. The medium is parameterized by (psi, p) through the tangent
field, and the bending channel enters through kappa, which is
convention-blind.

**THE SENSITIVITY LEG (run so the correction cannot be accused of having
been chosen to reach an answer).** The whole commission was also executed
end-to-end on the charter's LOCKED geometry, reading B:

    reading A (corrected): k_f/T0_f = 9.008   c_L,f = 3.001 c   r_s = 0.2365 a_f
                           directional spread of the read 0.000%
    reading B (as locked):  k_f/T0_f = 12.256  c_L,f = 3.501 c   r_s = 0.2028 a_f
                           directional spread of the read 17.06%

Two things follow. First, **the verdict is robust to the correction**: both
readings land in the FND-122 CONFLICT region, neither is near the
derive-point, and neither fires EM-RECON-032's falsifier. The correction
moves the number, not the branch. Second, **reading B is independently
excluded by the instrument's own inherited bar**: 17.06% directional spread
against FND-089's registered B2 bar of 0.05. The locked geometry does not
carry an isotropic medium, which is the property FND-088 derived the angles
to supply.

---

## 1. THE AFFINE HOMOGENIZATION (leg 1) -- exact at the derived angles

The fine medium is a filament network. Per unit fibre length, under a
displacement gradient A (A_ab = d_b u_a), the registered channels are

    stretch:  1/2 k_f (t.A.t)^2
    tension:  1/2 T  (|A t|^2 - (t.A.t)^2)
    bending:  1/2 kb |Dk|^2      (Kirchhoff, rigid rotation removed)

The affine energy depends on the orientation distribution ONLY through its
2nd and 4th moments. FND-088 derived the angles precisely to make the
fourth-order orientation tensor isotropic. **Therefore the affine response
of the wound medium is exactly that of an isotropic filament network**, and
the stretch/tension coefficients are the exact isotropic averages --
reproduced by the ensemble to machine precision as a control:

    longitudinal:  <mu^4>     = 0.20000000  (1/5)    <mu^2>-<mu^4> = 0.13333333 (2/15)
    transverse  :  <mu^2 nu^2>= 0.06666667  (1/15)   <mu^2>-<mu^2 nu^2> = 0.26666667 (4/15)
    bending     :  L 5.070636   T 5.908746   (units 1/a_f^2)

Imposing the two registered anchors -- c_T,hom = c (the SHIN transverse-c
invariant) and c_L,hom = sqrt(k/T0) c (FND-114's coarse channel floor) --
with mu_f = T0_f/c^2 FORCED, the stretch+tension system closes in exact
closed form:

    k_f/T0_f      = 6 (k/T0) - 3
    T_fibre/T0_f  = 9/2 - (3/2)(k/T0)

At the registered k/T0 = 2: **k_f/T0_f = 9 exactly, T_fibre = 1.5 T0_f.**
Positivity of the fibre tension independently caps k/T0 < 3.

**THE STRUCTURAL FINDING.** The dynamical coarse->fine mapping is
**ADDITIVE**, not a product of per-level lock coefficients; and it contains
**NO WINDING ANGLE**. The angles enter only by making the orientation
tensor isotropic, so ANY isotropic winding returns the same mapping. A
multiplicative, angle-dependent law and an additive, angle-free law cannot
agree except by coincidence.

---

## 2. THE INSTRUMENT (leg 2) -- controls, and a catch

Instrument: FND-089's supercell Bloch machinery (P = 5 sites per pitch, the
>= 5-phases-per-level sampling rule SHIN6 derived a priori; 18-neighbour
stencil; least-squares gradient, exact for linear fields).

**CONTROL (i), straight configuration.** Must reproduce the registered
straight-medium longitudinal behaviour. At k_f = 9, T = 1.5:

    c_L = 2.998629  (exact 3.000000)     c_T = 1.224185  (exact 1.224745)

0.05% -- the discretization floor. PASS.

**CONTROL (ii), instrument validity.** Bloch/supercell only; FND-084's
retirement of the time-domain instrument honoured, no packet code used.

**CONTROL (iii), polarization identification.** Both branches identified by
eigenvector overlap with the polarized plane wave, never by ordering or
continuity. Plane-wave weights 0.995 / 0.995 on the straight control.

**THE INSTRUMENT CATCH, disclosed before the run it governed.** The first
wound build assigned ONE fibre orientation per cell (SHIN6's transverse-
sector construction). It returned c_L = 0.2646 with 5.7% directional
spread and plane-wave weight 0.402 -- a collapse. Diagnosis: a filament
penalizes only gradients ALONG itself, so one orientation per cell leaves
the local energy rank-deficient and the lattice finds soft non-affine
patterns no weave has. SHIN6's KX = 0.08 isotropic background regularized
this in the transverse sector; the longitudinal build has no such crutch
and the defect became visible. **The registered medium is a BUNDLE of
n_sub fine fibres, which carries fibres at ALL phase pairs (phi_1, phi_2)**,
so the local set must sample the 2-torus, not one point on it. Repaired:

    m^2 fibres/cell:   c_L(001)    c_L(111)    c_T(001)
        1  (  1)       0.264565    0.175357    0.208308     <- rank-deficient
        2  (  4)       1.224616    1.178180    0.959272
        4  ( 16)       1.413486    1.413504    0.999519
        6  ( 36)       1.413567    1.413567    0.999543     <- converged

Converged values reproduce the affine limit (1.414214, 1.000000) to 0.05%,
isotropically. Taken, not tuned -- the correction was found by a control
(direction spread and plane-wave weight), in the FND-089 tradition.

**THE READING WINDOW.** Locked at lambda = 24p and 48p, convergence bar
0.5%:

    c_L(24p) = 1.413567     c_L(48p) = 1.414052     drift 0.0343%

**PASS.** The regime is reached; no REGIME-NOT-REACHED. Resonance
avoidance confirmed by construction (24-48x from FND-085's p ~ lambda).

---

## 3. THE READ (leg 3)

Solving (k_f, T_fibre) against the two anchors THROUGH the instrument
(not through the closed form):

    stretch + tension:   k_f/T0_f = 9.00823     T_fibre/T0_f = 1.50137
                         c_L,f/c  = 3.00137
                         r_s/a_f  = 0.23654     (KBSAT rider)

The 0.09% excess over the exact 9 is the instrument's own discretization
bias, identical in sign and size to the straight control's.

**THE READ, at the convergence bar's resolution: c_L,f = 3.00 c.**

---

## 4. THE RIGIDITY DEMAND (charter section 5) -- NOT FIRED, and why that is
    a gap rather than a strength

The demand: axial transmission must land at or above the static
stretch-projection value. It lands AT it, to 0.09%.

The honest reason: the affine value IS the answer, because nothing in the
registered structure makes the response non-affine. Non-affine relaxation
requires local orientation deficiency or a connectivity constraint, and
**the corpus has no registered contact rule** (FND-123 registered exactly
this: packing/clearance is grant-class, no contact rule exists). With the
bundle carrying the full phase ensemble at every material point, the medium
is homogeneous at the winding scale and relaxes affinely.

So FND-124's demand passes, but it did not do the discriminating work it
was designed for. **Its discriminating power is gated on the contact rule.**
Registered as a limitation, not spent as a pass.

---

## 5. THE BENDING CHANNEL AND KBSAT -- a conditional constraint,
    NOT a tripwire firing

With the bending channel on at the granted kb = 0.126 T0_f a_f^2 and the
registered curvatures, the same solve returns:

    k_f/T0_f = 7.40833     T_fibre/T0_f = -0.89054

**The input set is INFEASIBLE: it demands negative fibre tension.** The
bending channel alone contributes 0.126 x 5.9087 = 0.744 T0_f to a
transverse modulus whose registered total is 1.000 T0_f. FND-125's
caveated load-path display is confirmed and then some: bending is not a
correction to the stretch path, it is the larger part of the transverse
channel at KBSAT.

Feasibility (T_fibre > 0) requires

    kb <= 0.07909 T0_f a_f^2

which lies BELOW the SHIN7 ceiling the KBSAT grant saturated (0.126).
This is dynamical and measurement-shaped, i.e. exactly the class FND-121
condition 1 names for AUTO-SUPERSESSION.

**IT IS NOT DECLARED FIRED, and the reason is on the face.** The bending
term computed here is the first-order Kirchhoff bending strain, which is
exact as material response. The SECOND-ORDER geometric (pre-stress) terms
are omitted: a helically wound filament is not in equilibrium by itself,
and those terms depend on the constraint forces that hold the winding --
i.e. on the contact rule, which is unregistered (section 4). Their
magnitude is the same order as the effect (kb kappa_0^2), and their sign is
undetermined; a pre-stressed structure can soften. Declaring a grant
superseded on a computation whose declared gap is as large as its result is
not something the house does.

**Registered instead:** kb <= 0.079 T0_f a_f^2 CONDITIONAL on the
Kirchhoff-only bending treatment, with the pre-stress gap named, and with
the contact rule identified as the single input that would convert it into
a determination and fire (or clear) the tripwire.

**ALSO OMITTED, named:** the twist channel. GRANT-BASEFIBER (FND-118)
grants ONE material modulus; GJ needs a shear modulus, which GRV-072
registered as never determined anywhere in the corpus. Omitting it is
stiffness-reducing, i.e. it pushes the required k_f up, away from the
derive-point rather than toward it.

---

## 6. THE PRE-REGISTERED OUTCOME SHEET (targets unsealed here only)

Read: **c_L,f = 3.00 c** (stretch + tension; the static stretch-projection
value, which the dynamics reaches exactly).

Conversion, r_s/a_f = 0.7099 c / c_L,f: **r_s = 0.2365 a_f**.

Against the charter's three regions:

- c_L,f = 2.844 c -> **NOT TAKEN.** 3.00 c misses by 5.5%, far outside the
  0.5% convergence bar's resolution. k/T0 = 2 does NOT derive; FND-114
  remains ADOPTED-ADJUDICATED and is NOT upgraded; the alpha chain's
  inheritance rider is unchanged.
- above the rigidity threshold, off-point in (0, 0.3529 a_f] ->
  **TAKEN. CONFLICT REGISTERED.** r_s = 0.2365 a_f sits off the derive-point
  0.2496 a_f, inside the FND-122 conflict region. Per the sheet, this
  sends the angles or the mapping to adjudication.
- c_L,f < 2.390 c (r_s > 0.3529 a_f) -> not taken; EM-RECON-032's core
  falsifier does NOT fire. The read sits on the safe side of it.
- below the stretch-projection transmission -> not taken (section 4).

**WHICH GOES TO ADJUDICATION -- the angles or the mapping?** The read
answers this, and it is the commission's most useful product. The
dynamical mapping is angle-free: any isotropic winding returns
k_f/T0_f = 6(k/T0) - 3. **The angles cannot be the defendant**, because
moving them within the isotropy-preserving family does not move the
mapping. **FND-117's FACTORIZATION IS THE DEFENDANT**, and it is convicted
of a form error, not an arithmetic one: it is multiplicative and
angle-dependent where the dynamics is additive and angle-free. Its
numerical value 4.046 (= 1/(sin^2 psi_1 sin^2 psi_2)) versus the dynamical
9/2 = 4.5 is a 11.2% miss, but the 11.2% is the smaller finding.

**FND-118's price sheet, read literally:** the granted rod's dynamically
determined k_f/T0_f = 9.01 lies in [4.046, inf) and off 8.091, which is the
sheet's CONFLICT branch verbatim. Registered as such.

---

## 7. WHAT THIS COSTS AND WHAT IT BUYS

COSTS: the corpus's most load-bearing adopted constant does not become a
theorem tonight. FND-117's factorization -- registered as "structure" and
"form-constraining on any future base-fiber model" -- is superseded in
form. Every quantity whose provenance runs through the 4.046 double
compensation inherits a re-pricing question, SHIN7's kb ceiling among them
(it was computed at T_f = 4.046 T0_f; the dynamics returns 1.5 T0_f). That
re-pricing is NOT done here and is named as owed.

BUYS: a closed-form, parameter-free, angle-free dynamical mapping law
where the corpus had a product of lock coefficients; a positivity cap
k/T0 < 3 that the registered value comfortably satisfies; the first
dynamical statement about the fine longitudinal channel in the programme's
history; and two named corrections (the radius convention, the local
multiplicity) that were both found by controls.

## 8. NAMED NEXT-ORDERS

1. **THE CONTACT RULE** is now the sector's single highest-value missing
   registration. It gates three separate things at once: the non-affine
   correction, the bending pre-stress terms, and therefore whether the
   KBSAT tripwire fires. FND-123 named it grant-class; it should go to the
   author's desk with this commission's three customers on its face.
2. **THE COMPENSATION RE-PRICING.** SHIN7's kb ceiling, FND-091's eps
   headroom, and every 4.046-conditional quantity were priced through the
   factorization this commission supersedes in form. A re-pricing session
   is owed before kb's ceiling can be quoted again.
3. **THE FND-117 SUPERSESSION** should be recorded superseded-not-erased:
   its refusal (the gamma/stretch-ratio name-adjacency), its exclusion (the
   inextensible bottom), and its non-circularity argument all survive; only
   the multiplicative FORM of the mapping is superseded.
4. The k/T0 < 3 positivity cap is a new registered structural bound on the
   coarse constant, independent of the spacings fit that originated it.

## REFUSALS

Clean-room held; the derive-point never entered a build leg. The
convention correction was registered rather than silently substituted, and
the commission was ALSO run end-to-end on the charter's locked geometry
(section 0's sensitivity leg) so the correction cannot be accused of having
been chosen to reach an answer. No contact rule invented. No twist modulus
invented. The KBSAT constraint registered conditional rather than
declared fired. Condition 4 unchanged.
