# COMMISSION GIMEL-2 -- RESULTS: FORM-FORCED; THE LAST IDENTIFICATION FALLS

*Adjudicated 2026-08-11 after bar lock
(analysis/GIMEL2_inertial_term_bars_LOCKED.md). Benchmark:
benchmarks/em/gimel2_inertial_term.py. EM-016's grade is UNCHANGED.*

## The obstacle the bar insisted be faced first

The easy move -- "strands have mass, so kinetic energy is Newtonian" --
was ruled out in advance: FND-REL-002 (Derived) says there is NO material
velocity here, and EM-RECON-012 uses precisely that to FORBID a mass
term. Writing (mu/2)|dX/dt|^2 for material points would contradict two
Derived claims. The bar required an explanation of why a term with two
time derivatives survives when a term with none does not.

## C1 -- the symmetry ledger (computed)

The variable is a gauge label, defined up to a constant shift
a -> a + c_0. Under that shift:

| term | shift-invariant? |
|---|---|
| m^2 a^2 / 2 (mass) | **NO** -- changes by c_0(c_0 + 2a)/2 |
| mu (da/dt)^2 / 2 (inertial) | YES |
| K (grad a)^2 / 2 (stiffness) | YES |
| lam a (da/dt) (mixed) | **NO** -- changes by c_0 da/dt |

**The apparent paradox dissolves, and cleanly:** a itself is a label, but
its RATE OF CHANGE is observable. The very symmetry that forbids the mass
term PERMITS the inertial term. Nothing is smuggled past the
no-material-points theorems -- the term survives them for a stated
reason, and the mixed term, which one might have expected, is killed by
the same test.

## C2 -- uniqueness at leading order

Among shift-invariant, local, isotropic, quadratic terms ordered by
derivative count, the two-derivative level contains exactly two scalars:
(grad a)^2 -- already registered as EM-007's stiffness -- and (da/dt)^2.
Time-reversal forbids a single-time-derivative scalar; isotropy forbids
a preferred-direction kernel.

Alternatives named and excluded, per the locked bar:
- **higher time derivatives** -- suppressed by the derivative expansion,
  entering at the same order as lattice corrections the corpus already
  truncates;
- **anisotropic kernel mu_ij** -- excluded by the registered isotropy of
  the wave sector (FND-REL-002 forces Lorentz-invariant form);
- **nonlocal kernel mu(k)** -- excluded at leading order by LOCALITY,
  which is what the derivative expansion assumes. **Stated as an
  assumption rather than smuggled**: the derivation is of the leading
  local term, and a genuinely nonlocal kernel would evade it.

**(mu/2)(da/dt)^2 is the unique leading-order term. The FORM is forced.**

## C3 -- the coefficient (form and value kept separate)

The form fixes the dispersion, c = sqrt(K/mu), but not the scale.
Matching to the already-registered transverse branch
omega^2 = (T0/mu) q^2 (EM-RECON-025), whose mu is the rope mass density,
identifies the two -- so mu is not a new constant.

**Honest limit, registered as partial:** this is a CONSISTENCY
IDENTIFICATION with an already-registered sector, not an independent
derivation of the numerical value. The value rides on the same
calibration the transverse sector rides on.

## VERDICT: FORM-FORCED -- blocker (ii) discharges as to form

EM-016's ledger, over one day:

| blocker | status |
|---|---|
| (iv) uniqueness of the dictionary | discharged, EM-017 |
| (iii) phi's channel identification | discharged, EM-018 |
| (ii) the inertial term | **discharged as to form here**; coefficient fixed by consistency, not independently derived |
| (i) SIGMA's absolute value | **stands** -- a declared input |

## THE STATEMENT THAT MATTERS, and its careful limit

**Every identification in the dictionary is now forced.** Nothing in the
mapping from mechanical state to field tensor is a choice: the
assignment is unique (EM-017), phi's channel is the only survivor
(EM-018), and the inertial term is the unique leading-order term the
gauge symmetry permits (here).

**EM-016 is NOT upgraded by this commission**, and the reason is worth
stating precisely so nobody mistakes it: what remains is (i) SIGMA,
which the BET-2 audit found meets the corpus's own definition of a
calibration input, and whose relabelling is **a DECISION on the author's
desk, not a computation anyone can run.** A reader must be able to see
that the ledger emptied by derivation down to one item, and that the
last item awaits a judgement about labelling rather than a result. Those
are different things and the corpus does not blur them.

Two smaller honesties, both above: the coefficient is matched rather
than derived, and the locality assumption behind the derivative
expansion is stated rather than hidden.
