# COMMISSION BET3 -- BARS LOCKED BEFORE COMPUTING

**Charter:** SCALE-001 (FND-051) class C6, the amplitude-plus-sign
adjudication between EM-RECON-009's quartic coefficient c4 = (k-T0)/8
(which at the adjudicated k = 2T0 reads +T0/8) and FND-040's derived
c4 = -T0/8 for an inextensible constant-tension mesh.

**Locked:** 2026-08-11, before any symbolic or numerical work.
**Operator:** Claude, for Mark Palmer.
**Lineage:** BET (FND-040) derived the negative sign; BET2 audited the
phi channel; BET3 adjudicates BET against EM-RECON-009.

---

## 0. The observation that motivated the charter (stated before computing)

Framing C6 as "+T0/8 versus -T0/8, which sign wins" may be the wrong
question. Under EM-RECON-009's formula c4 = (k-T0)/8, the inextensible
limit is k -> infinity, giving c4 -> +infinity. FND-040 derives
c4 = -T0/8 for an inextensible strand, which is EM-RECON-009's k = 0
row. The two claims therefore attach the SAME WORD ("inextensible") to
OPPOSITE ENDS of the same axis.

**Working hypothesis (H-MISMATCH), recorded as a hypothesis and not a
result:** the two functionals are evaluated under different
material/boundary conditions -- FND-040 with an arc-length reservoir at
fixed T0 (FND-017's global Lagrange multiplier), EM-RECON-009 at fixed
material with local stretch -- and both are correct in their own domain.
This is the same 1/L relaxation escape EM-RECON-009 flagged on its own
face and EM-RECON-013 closed with P-VOL.

H-MISMATCH is what the bars below are built to REFUSE if it is wrong.

## 1. Pre-committed verdict classes (exhaustive; exactly one is returned)

- **V-MISMATCH** -- the claims compute different quantities under
  different conditions; a single functional reduces to both, and the
  control parameter is identified.
- **V-KILL-009** -- EM-RECON-009's quartic is wrong on registered
  kinematics; its c4 is retracted.
- **V-KILL-040** -- FND-040's quartic is wrong; its c4 is retracted,
  and every FND-040 downstream number (the kappa_pack floor, the
  OMEGA pair, FND-046's pin) re-opens.
- **V-BOTH-WRONG** -- neither functional survives.
- **V-UNDERSPECIFIED** -- the control parameter cannot be written in
  registered inputs; C6 returns the SCALE-001 verdict class rather
  than an adjudication.

## 2. Quantitative bars

**B1 (REDUCTION, decisive for V-MISMATCH).** A single energy functional
must reproduce BOTH quartics EXACTLY, by symbolic expansion, with no
fitted coefficient: -T0/8 in one stated limit and (k-T0)/8 in the other.
Exactness is required; agreement to O(1) does not pass. If no single
functional reduces to both, V-MISMATCH is REFUSED and the commission
returns a kill class.

**B2 (POSABILITY).** The control parameter separating the two limits
must be expressible in REGISTERED inputs. If it cannot be, the verdict
is V-UNDERSPECIFIED and the carrier that would fix it is named as an
acquisition target, per SCALE-001's protocol. Naming a plausible
parameter that the registry does not carry does NOT pass this bar.

**B3 (MONOTONICITY).** The interpolation between limits must be
monotonic in the control parameter. Non-monotonic interpolation refutes
H-MISMATCH and forces a kill class.

**B4 (ASSIGNMENT BEFORE INSPECTION).** The registered downstream users
of a quartic coefficient must be enumerated, and each assigned to a
limit BY ITS OWN GEOMETRY, in writing, BEFORE checking which sign that
user's registered result requires. Assignment made after seeing the
required sign is bar-shopping and is refused by rule.

**B5 (NO PARAMETER RESCUE).** k/T0 is held at the adjudicated value 2
(EM-RECON-009 / GRV-009) throughout. Adjusting k/T0 to make any
downstream number land is forbidden. The eight-order k dispute
(FND-021: QB-008 demands k/T0 >= 1.9e8) is NOT adjudicated here and
must not be silently resolved by this commission.

**B6 (GUARD DISCLOSURE).** Any O(1) factor or near-coincidence noticed
against any registered target during the work is displayed in the
results document and explicitly refused, whether or not it is used.

**B7 (SCOPE FENCE).** This commission adjudicates the QUARTIC
COEFFICIENT ONLY. It does not touch: the k/T0 magnitude dispute
(FND-021), the kappa_pack floors, FND-037's nonlinearity form, or
EM-016's grade. If the work appears to bear on those, the bearing is
REPORTED and left for the author, not acted on.

**B8 (GRANT DISCIPLINE).** If the adjudication requires adopting a
premise, the premise is NAMED and PRICED and left on the author's desk.
Claude does not adopt grants.

## 3. What would make this commission a failure

- No single functional reduces to both quartics (B1 fails) AND no
  clean kill is establishable -> V-BOTH-WRONG or V-UNDERSPECIFIED.
- The control parameter turns out to be unregistered -> V-UNDERSPECIFIED,
  which is a legitimate and reportable outcome, not a defeat to be
  avoided by inventing a parameter.

## 4. Registered inputs permitted

FND-017 (T0 as global Lagrange multiplier), FND-KIN-001
(inextensibility), EM-RECON-009 (the extensibility functional),
EM-RECON-013 (P-VOL and k_eff), FND-040 (the arc-length expansion),
FND-MATTER-004 (coverage threshold), EM-RECON-025 (the registered
dispersion). No unregistered input may enter without a B8 grant note.
