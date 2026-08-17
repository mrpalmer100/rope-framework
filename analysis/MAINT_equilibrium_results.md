# COMMISSION MAINT -- RESULTS (2026-08-17)

Executed under analysis/MAINT_equilibrium_bars_LOCKED.md (locked at
v3.26.74). Benchmark: benchmarks/foundations/maint_equilibrium.py.
Doubled clean-room held: the derive-point family and the kb values appear
in no build leg (kb enters build legs as a symbol only).

**VERDICT: CHANNEL-OPEN.** The static question is not closed -- two channels
blocked, neither refuted, both at the SAME missing registration (the twist
channel, GRV-072) -- so NO-STATIC-EQUILIBRIUM is NOT declared, FND-121
condition 1 does NOT fire, and the warrant stays HELD. The session's
positive findings are a theorem and an exhibited state.

## 1. THE BENDING-NEUTRALITY THEOREM (the session's jewel)

The exact normal force density of a uniform Kirchhoff helix carrying
tension T with bending energy (1/2) kb integral kappa^2 ds is
(sympy-derived from the helix-family variation, numeric control 0.005%):

    f_n (inward) = kappa [ T + kb (tau^2 - kappa^2/2) ]

and the bending coefficient at winding parameter s = sin^2 psi is

    tau^2 - kappa^2/2 = 2 pi^2 s (3s - 1) = 0   iff   s = 1/3.

**The bending force density of a uniform helix vanishes identically iff
sin^2 psi = 1/3 -- the magic angle.** FND-088 derived that angle from the
isotropy demand; it turns out to also be the unique bending-force-neutral
winding. The corpus's level-1 winding exerts no net bending force on
itself, exactly, at any kb.

## 2. THE PURE-BENDING REFUTATION (channels i and ii-pure, DERIVED)

Channel (i) (intrinsic curvature) is INADMISSIBLE under FND-118's granted
class, read verbatim (no stress-free wound reference is granted).
Channel (ii)-pure: static equilibrium demands T = -kb (tau^2 - kappa^2/2):
ZERO at level 1 (the theorem, kb-free) and NEGATIVE at level 2
(tau-dominated -- bending REINFORCES the inward imbalance and can never
balance a positive tension). The registered fibre tension is +3/2 T0_f.
**No static pure-bending equilibrium exists at either level.** The level-1
refutation is kb-free: the corpus's own derived angle deletes the only
static restoring channel the granted rod owns.

## 3. THE TWIST RESCUE, REDUCED AND BLOCKED (channels ii-twist and iv)

The only remaining static channel is a twist moment C omega t. The
frame-Kirchhoff route reduces the requirement to closed form,

    C omega = T/tau + kb (kappa^2/2 - tau^2)/tau,

which at level 1 is **kb-FREE by the theorem: C omega = T_fibre/tau_1 =
0.7162 T0_f a_f** -- one number [single-route; an energy-route cross-check
is owed if the branch ever opens]. Both factors (twist modulus C, imposed
twist omega) are unregistered: GRV-072 registers the twist constitutive
fact as never determined anywhere in the corpus. Channel (iv)
(topological rigidity) needs the same registration -- Lk conserves a
number; a BARRIER requires twist stiffness to price the Tw <-> Wr trade.
**Blocked, not refuted -- both at GRV-072.**

## 4. THE DYNAMICAL STATE, EXHIBITED (channel iii)

A rotating helix (circularly polarized wave) balances f_n by centripetal
acceleration: mu v^2 = T + kb (tau^2 - kappa^2/2) along the fibre. At
level 1 the theorem deletes kb: **v_1 = sqrt(T_fibre/mu_f) exactly,
bending-independent** -- and with mu_f = T0_f/c^2 forced and T_fibre =
3/2 T0_f, **v_1 = sqrt(3/2) c = 1.2247 c from registered inputs alone.**
Level 2: v_2 = sqrt(3/2 + kb (tau_2^2 - kappa_2^2/2)) c -- at kb = 0.079:
1.708 c; at kb = 0.126: 1.939 c; all inside the 6.1x Lorentz floor. The
nested two-level composite is the same construction on the level-1
backbone; the composite build on FND-089-class machinery is the channel's
named residual.

## 5. THE TWIST SHEET (pre-registered for any future determination)

    C omega = 0.7162 T0_f a_f  ->  STATIC branch: the pre-stress terms
        become computable from the twist-held equilibrium; KBSAT
        adjudicates on numbers.
    C omega != 0.7162          ->  DYNAMICAL branch forced, not adopted:
        condition 1 fires on that release with FND-128's reverting set
        executed verbatim.

No outcome is null. The bottleneck has MOVED and SHARPENED: from "no
contact rule" (resolved by FND-129) to "no twist registration" (GRV-072),
now carrying the entire KBSAT adjudication on a one-number sheet.

## REFUSALS
Clean-room held (both exclusion sets). The tripwire not fired (B4 honoured
-- CHANNEL-OPEN is the verdict the evidence supports; declaring
NO-STATIC-EQUILIBRIUM would have required refuting a channel the registry
merely fails to feed). No twist modulus invented. The single-route caveat
on the C omega closed form displayed, not hidden. Condition 4 unchanged.
