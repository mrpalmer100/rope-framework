# EM-RECON-017 — K_c derived in form: the O(k) argument routed through the wrong constant, and core survival reduces to one named material ratio

Date: 2026-08-09. Commission: EM-RECON-013's flagged edge.
Bars: `analysis/EMRECON017_Kc_bars_LOCKED.md` (locked first, with the
marginality discovery recorded at charter time).
Benchmark: `benchmarks/em/emrecon017_kc_derivation.py`.

## The marginality discovery (made at chartering, before computing)

EM-RECON-013's own note said K_c = k requires k > 2T0 for survival.
FND-027 adjudicated k = 2T0 EXACTLY. Therefore K_c = k gives k_eff = T0
and c4_eff = 0: no core. **Survival strictly requires K_c > k** — the old
O(k) argument was insufficient even if correct.

## What was derived

**B1 (exact):** P-VOL width-strain kinematics — w(ε) = w0/√(1+ε), so bulk
over-density thickens strands at rate w0/2 per unit strain and the
contact range runs as σ(ε) = σ0/√(1+ε).

**B2 (derived from placement, not chosen):** at the coverage threshold —
by the threshold's own definition, the configuration where free gaps have
just closed — further densification has exactly one load path: the
contact set. Below threshold K_c = 0 (the registered pre-protector
collapse); at threshold the contact-channel curvature IS K_c.

**B3 (computed):** K_c per unit strand length from the registered contact
form Ac/(1+(r/σ)⁴) for crossing strands at density 2/a under P-VOL
thickening: K_c = C(d0/σ0)·(Ac/a), with C ∈ [0.67, 5.06] across the
admissible standoff band, finite and positive at ε → 0 (no Hertz-type
vanishing — the registered form is smooth and long-ranged, so the channel
is linearly stiff at onset) and stiffening with over-density.

## The finding that supersedes the argument

**K_c is set by the contact amplitude Ac, not by the stretch modulus k.**
The "compressing contacting strands strains the same material that
resists stretch" argument — the sole basis for K_c ~ O(k) — routed
through the wrong constant: under P-VOL, contact compression is priced by
the registered contact energy directly, and k never enters the
contact-channel curvature. The O(k) claim is SUPERSEDED, not refined.

## The survival condition, made precise

    K_c > k = 2T0   ⟺   Ac/(T0·a) > 2/C(d0/σ0)  ∈  [0.40, 3.00]

**Ac/(T0·a) — the contact amplitude in tension units — is not registered
anywhere in the corpus** (FND-KIN-005 registers the form; the engine's
values are simulation units). Per bar 4 it is named, its survival
threshold computed, and left open. The core's status moves from "argued
O(k), presumed safe" to "conditional on one precise material ratio
exceeding a number of order unity."

## Named settlers (not run)

1. **The nuclear import** (the natural closer): the corpus's nuclear
   sector prices binding as rope-bundle contact — the nuclear binding
   scale IS a contact-amplitude measurement in disguise. A commission
   importing the NUC sector's calibrated contact scale into Ac/(T0·a),
   blind to this threshold, would decide survival with zero new freedom.
2. **The standoff refinement**: the band [1, 3]·σ0 was displayed, not
   derived; the exact threshold standoff follows from the coverage
   fraction f_c (registered via the Λ percolation determination) and
   would narrow C to a value rather than a band.

## Consequences

- EM-RECON-013's honest edge resolves into a precise open number; its
  k_eff formula and the protector structure stand unchanged.
- EM-RECON-009's core is now conditional on the named ratio — neither
  safer nor less safe than yesterday, but honestly priced for the first
  time.
- The FND-028 prediction package is unaffected (it rides k/T0 = 2 and the
  vertex, neither touched here).

## Not claimed

Ac/(T0·a)'s value; survival or failure; any new parameter; any change to
k/T0. Spend remains ONE.
