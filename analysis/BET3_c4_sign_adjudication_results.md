# COMMISSION BET3 -- RESULTS

**Bars:** `analysis/BET3_c4_sign_adjudication_bars_LOCKED.md` (locked
before any symbolic work).
**Benchmark:** `benchmarks/foundations/bet3_c4_adjudication.py`
**Charter:** SCALE-001 (FND-051) class C6.

## VERDICT: V-MISMATCH on B1/B3; the SIGN SELECTION returns V-UNDERSPECIFIED on B2.

---

## 1. The functional (one, not two)

Strand with material coordinate s, lab coordinate z, transverse slope
g = Y'(z). Let rho(z) = ds/dz be material per unit lab length. An
element of lab length dz has arc length dz*sqrt(1+g^2) and carries
material rho*dz, so the stretch is lambda = sqrt(1+g^2)/rho and
e = lambda - 1. With EM-RECON-009's elastic strand and EM-RECON-013's
P-VOL contact cost of density deviation:

    E = int dz { rho [ T0 e + (k/2) e^2 ] + (K_c/2)(rho - 1)^2 }

Two-region model: core of lab length l = f*L carries slope g, the
remaining (1-f)*L is straight; total material conserved. FND-017's
statement that T0 IS the global Lagrange multiplier is what makes the
conservation constraint the right one.

## 2. B1 -- REDUCTION (PASS, exact, zero fitted coefficients)

Minimising over the material distribution gives the master result

    c4_eff = [ k (K_c + f k) / (K_c + k)  -  T0 ] / 8

with minimiser alpha_2 = k(1-f) / (2(K_c + k)).

| limit | c4_eff | matches |
|---|---|---|
| f -> 1 (uniform; nowhere to flow) | (k - T0)/8 | **EM-RECON-009, exactly** |
| f -> 0, K_c -> 0 (free flow) | -T0/8 | **FND-040, exactly** |
| f -> 0, finite K_c | (k K_c/(k+K_c) - T0)/8 | **EM-RECON-013's k_eff, identically** |
| f -> 0, k -> inf (strictly inextensible) | (K_c - T0)/8 | the FND-KIN-001 reading |

Both registered quartics are exact limits of one functional. B1 passes.

**The independent confirmation, and it is the strongest thing here.**
The f -> 0 row reproduces EM-RECON-013's k_eff = k K_c/(k + K_c)
IDENTICALLY. EM-RECON-013 derived that combination from a different
variational problem, for a different purpose (closing the core's 1/L
escape), several commissions earlier. It was not put in. This is a
DEPENDENCY PATH in the HANDOFF section-0 sense, not a resemblance.

**Mechanism, visible in the minimiser.** At f -> 0, K_c -> 0 the core
draws in material until alpha_2 = 1/2, i.e. rho_c = 1 + g^2/2, which
makes its stretch IDENTICALLY ZERO: the core then pays only
T0 x (arc length). That is FND-040's constant-tension picture, obtained
FROM EM-RECON-009's elastic functional rather than assumed alongside it.

## 3. B3 -- MONOTONICITY (PASS)

d(c4_eff)/df = k^2 / (8(K_c + k)) > 0, strictly, for all admissible
K_c, k. Monotonic in the control parameter. H-MISMATCH is not refuted.

## 4. The diagnosis: same word, opposite ends of one axis

The C6 conflict was framed as a sign dispute. It is not. Under
EM-RECON-009's formula the inextensible limit is k -> infinity, giving
c4 -> +infinity; FND-040 derives -T0/8 for an inextensible strand,
which is EM-RECON-009's k = 0 row. The two claims attached the same
word to opposite ends of the same axis because they hold DIFFERENT
QUANTITIES FIXED:

- EM-RECON-009 holds MATERIAL fixed and pays arc-length excess by
  local STRETCH.
- FND-040 holds TENSION fixed and pays arc-length excess by material
  FLOW at zero cost.

Neither is wrong within its own condition. This is the definitional
mismatch FND-021 warned about for the k/T0 dispute, in a second place.

## 5. B4 -- ASSIGNMENT BY GEOMETRY (recorded before any sign inspected)

| user | geometry | assigned limit |
|---|---|---|
| EM-RECON-014/016 (PVLAS birefringence) | static field uniform through the apparatus volume | f = 1 |
| EM-RECON-009 (matter core) | localised defect of size xi in a much larger mesh | f -> 0 |
| FND-040 (Casimir-scaling violation) | static source, field localised about the tube | f -> 0 |
| FND-046 (kappa_pack pin) | inherits FND-040 | f -> 0 |
| FND-052 / FND-055 (bundle sector) | parallel windings, localised | f -> 0 |

Checked only after the table above was written:

- **EM-RECON-016 CONSISTENT.** At f = 1 the coefficient is (k - T0)/8
  = +T0/8 at k = 2T0 -- exactly the value the claim used, and positive
  as its core-stability and negative-index-shift arguments require. The
  PVLAS confrontation and the 3:1 anisotropy discriminator are
  UNAFFECTED by this commission.
- **FND-040 NOT CONSISTENT WITH ITS OWN REGISTRY.** Its -T0/8 is the
  K_c = 0 corner: arc length supplied by flow at zero cost. P-VOL is
  ADOPTED (EM-RECON-013), and P-VOL prices exactly that supply at K_c.
  FND-040's derivation predates nothing -- it simply never carried the
  contact term.

## 6. B2 -- POSABILITY: the sign is NOT determined by the registry

Setting c4_eff = 0 in the localised limit:

    finite k:        c4 > 0  iff  K_c/k > T0/(k - T0)   [= 1 at k = 2T0]
    inextensible:    c4 > 0  iff  K_c > T0

EM-RECON-013 registers K_c only as **"K_c ~ O(k), argued not derived"**.
The sign flip sits INSIDE that O(1). The registry therefore cannot
currently say which sign the localised quartic carries.

**B2 FAILS for the sign selection.** Per the locked bar this returns
V-UNDERSPECIFIED for that half, and names the acquisition target:

> **ACQUISITION TARGET: a derived value (not an O(1) argument) for the
> P-VOL contact modulus K_c.** Registering K_c against T0 decides the
> localised quartic's sign outright, and with it FND-040's coefficient,
> FND-046's pin, and the bundle sector's direction.

This joins the SCALE-001 acquisition list. Note it is a DIFFERENT
carrier from the reconnection rate (missing in three contexts); K_c is
missing in one context but that context is Derived-grade.

## 7. B6 -- GUARD DISCLOSURE (mandatory, displayed and refused)

1. **The exact zero.** At K_c = k and k = 2T0 -- both registered
   central values -- the localised quartic is EXACTLY ZERO. Displayed
   because it is striking and because it is the kind of coincidence
   this corpus has been flattered by before (QGATE-007's Schwinger
   diagnosis). REFUSED as content: it is an artefact of two O(1)
   estimates meeting, carries no derivation, and nothing is built on it.
2. **The rescue shape, and it deserves maximum suspicion.** FND-047
   registered that SU(6) k-string data favours a POSITIVE deviation,
   opposite FND-040's derived softening; FND-055 disclosed that
   FND-040's sign pushes the bundle prediction FURTHER from that data.
   This commission has found a mechanism that moves the coefficient
   TOWARD positive. That is the shape of an after-the-fact rescue and
   is flagged as such at full volume. Three things are offered against
   that reading, for the author to check rather than accept: the f -> 0
   assignment was written before any sign was inspected (section 5);
   K_c > 0 comes from P-VOL, adopted for unrelated reasons in
   EM-RECON-013; and **the magnitude is not determined, so this
   commission does NOT claim to land on the k-string data and must not
   be cited as doing so.** It withdraws a derivation; it supplies no
   number.
3. No other numerical adjacency was noticed.

## 8. B5, B7, B8 compliance

- **B5:** k/T0 held at 2 throughout. The FND-021 eight-order k dispute
  (QB-008 demands k/T0 >= 1.9e8) is NOT adjudicated here and is not
  touched. Note in passing, reported not used: the master formula's
  f -> 0 limit is bounded by K_c regardless of k, which MAY be relevant
  to that dispute, since the two claims may again be holding different
  things fixed. Left for the author.
- **B7:** bearing on the kappa_pack floors is REPORTED (section 9), not
  acted on. FND-037's form, EM-016's grade, and the floors are untouched.
- **B8:** no grant adopted. One is named in section 9.

## 9. REPORTED BEARING (not acted on -- author's desk)

FND-040 is **Derived** grade and its coefficient holds the kappa_pack
floor (>= 50 / >= 250), Sigma_vac, the OMEGA (a, T0) pair, and
FND-046's inversion. This commission does not retract FND-040: within
its stated condition (constant tension, free flow) its arithmetic is
correct and is reproduced exactly. What it shows is that the condition
is **narrower than the claim's own use of it**, because P-VOL is
adopted elsewhere in the registry and prices the flow.

The author's decision, named and priced, NOT taken here:

> **Does FND-040's Derived grade survive the disclosure that its
> coefficient is the K_c = 0 corner of a functional whose K_c > 0 is
> registered by an adopted postulate?**
>
> Price of leaving it: a Derived-grade coefficient carries an
> unstated condition that a Modeled claim contradicts.
> Price of re-grading: the kappa_pack floor arithmetic, Sigma_vac, the
> OMEGA pair and FND-046's pin all become conditional on an
> undetermined K_c/T0, and a re-solve commission is owed.

Recommended, but the author's call: annotate FND-040 with the
condition, leave the grade, and charter the K_c derivation. The floors
should not move on an O(1).

## 10. What this commission did NOT establish

- It did not determine c4's sign in any localised setting.
- It did not supply K_c.
- It did not adjudicate the k/T0 magnitude dispute.
- It did not touch the PVLAS confrontation, which stands unchanged.
- It did not advance the g question, which remains Rank-1 and untouched.
