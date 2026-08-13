# COMMISSION BET4 -- RESULTS

**Bars:** `analysis/BET4_stability_identity_bars_LOCKED.md` (locked first,
with the operator error stated before any work).
**Benchmark:** `benchmarks/foundations/bet4_stability_identity.py`

## VERDICT: V-IDENTICAL

---

## 0. The operator error repaired

FND-063 (BET3) built its B2 verdict and its acquisition target on
EM-RECON-013's statement that K_c is "O(k), argued not derived."
**That is the superseded face value.** EM-RECON-013's own annotation
records EM-RECON-017 deriving K_c in form (`K_c = C(standoff) x Ac/a`,
routing through the contact amplitude and NOT the stretch modulus), and
EM-RECON-018 then narrowing the survival band 41-fold to [0.40, 0.46].

STALE-VALUE CLASS, exactly as HANDOFF section 6 names it, with the
prescribed tripwire firing one commission late. **FND-063's acquisition
target is withdrawn: K_c does not need acquiring.**

Second repair: FND-063's guard disclosure 1 (the exact zero at K_c = k,
k = 2T0) was presented as newly noticed. It is EM-RECON-017's
registered MARGINALITY DISCOVERY, found at its chartering. Refusing it
was right; claiming it was not.

## 1. B1 -- IDENTITY (PASS, exact)

    BET3 localised branch :  c4_loc = (K_c k - K_c T0 - T0 k) / (8(K_c + k))
    EM-RECON-013 survival :  (k_eff - T0)/8, k_eff = k K_c/(k + K_c)
    symbolic difference   :  0

The denominator 8(K_c + k) is manifestly positive, so both inequalities
reduce to the same numerator condition:

    K_c (k - T0) > T0 k        i.e.   K_c > T0 k/(k - T0)
    at k = 2T0:                       K_c > 2T0 = k

Not nested. Not merely co-directional. **The same inequality.**

**What this means:** the quartic's positivity IS the existence of the
repulsive core. EM-RECON-009 opened this loop at its own registration
("a repulsive core exists iff k > T0"); under relaxation the condition
becomes k_eff > T0, and BET3's functional shows that is simultaneously
the sign of the quartic. Two questions, one inequality.

**Consequence for the charter:** C6's sign question is not an
independent open question. It collapses into the matter-stability
question the corpus has prosecuted across EM-RECON-013 -> 017 -> 018,
and inherits that chain's narrowed band and its designated settler
(EM-RECON-017's nuclear import, a zero-freedom decision).

## 2. B2 -- THE FND-040 MAPPING

    c4 = -T0/8  =>  k_eff = 0  =>  K_c -> 0

FND-040's registered coefficient is the no-contact-stiffness corner. In
a localised setting it is the statement that the relaxed core stiffness
vanishes: **no repulsive core, hence no stable matter.**

Its arithmetic remains exact within its stated condition (constant
tension, cost-free flow) and BET3 reproduces it exactly. What is now
visible is that the condition describes a medium that cannot hold
matter together -- which is not the medium the rest of the registry is
about.

## 3. B3 -- LIMIT HYGIENE (held)

The uniform branch is c4_uni = (k - T0)/8 with **K_c absent** (verified
by differentiation: dc4_uni/dK_c = 0). It carries no core and no
contact channel. Its positivity at k = 2T0 follows from k > T0 alone.

**The stability argument governs the LOCALISED branch only and is not
extended to the uniform branch.** EM-RECON-016's PVLAS confrontation
(f = 1) is therefore untouched by this commission as well as by BET3.

## 4. B4 -- WHAT IS NOT CLAIMED

**Matter stability is NOT settled here.** EM-RECON-018 is Modeled,
rests on leading-order (non-overlapping-disk) coverage counting, and
displays its plausible-contact-geometry prior *without adopting it*.
Its position is carried unchanged:

| geometry | m_b | verdict vs ~63-73 |
|---|---|---|
| single pair | ~1 | survives |
| surface line | ~22 | survives |
| contact patch | ~63 | survives (marginal) |
| full cross-section | ~498 | FAILS |

Survival looks good under every plausible touching geometry and fails
only under an implausible one. That was EM-RECON-018's honest summary
and it remains the honest summary. This commission moves the sign
question ONTO that track; it does not finish it.

## 5. B7 -- ANTI-RESCUE FLAG, CARRIED AT FULL VOLUME

This is the SECOND consecutive commission to move a coefficient toward
positive while FND-047's SU(6) k-string data favours a positive
deviation that FND-040's sign misses. No magnitude is supplied here
either. **Nothing in this commission may be cited as landing on that
data.**

The defensible statement, and it should be quoted in this form and no
stronger: *the corpus's own stability requirement -- registered many
commissions before the k-string confrontation existed -- excludes the
negative sign in localised settings, conditional on EM-RECON-018, which
is Modeled.*

## 6. B5 -- GRADE ACTION REFUSED

FND-040 is not retracted; its grade remains the author's. The question
attached to it is now sharper than BET3 could pose: not "is the
coefficient conditional on an undetermined K_c" but **"is the
coefficient the corner in which the framework has no stable matter."**

## 7. Named next-orders

1. **The nuclear import** (EM-RECON-017's settler 1) -- now decides the
   sign as well as survival. Zero-freedom, still undischarged, and by
   this commission's arithmetic it is worth more than it was.
2. **The FND-040 grade decision** -- author's, unchanged, better posed.
3. The Rank-1 g question remains untouched by both BET3 and BET4.
