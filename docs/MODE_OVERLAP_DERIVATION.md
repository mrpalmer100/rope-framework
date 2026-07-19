# Mode-Overlap Coupling from Network Primitives

**Target:** open problem EM-RECON-005 (`docs/OPEN_PROBLEM_mode_overlap.md`) — derive
E_overlap[psi1, psi2] from the rope-network primitives {T, mu, lambda} such that the
long-range limit reproduces the swirl-field anchor, the ~0.1 eV scale at 2–3 Å falls
out rather than being inserted, and the ferro/antiferro sign is computed, not chosen.

**Companion program:** `mode_overlap_harness.py` — ONE frozen functional, all checks,
no per-case retuning. Run output is the record; this document is the reasoning.

---

## 1. Starting point: the quadratic network energy

The corpus (micromech benchmarks) gives the coarse-grained elastic energy of the
rope network as quadratic in the displacement/phase field:

    E[psi] = T ∫ |∇psi|² dV  +  (swirl sector)  T ∫ |b|² dV

with mu = T/c² and torsional stiffness lambda entering only through the healing
length xi = sqrt(lambda/T), which sets the transverse size of a mode.

For a **superposition** psi = psi1 + e^{i·d}·psi2 of two modes (d = relative internal
phase, a genuine mechanical coordinate of the pair — the relative winding origin),
the energy splits as self + self + **cross**:

    E_cross(d) = T ∫ Re( e^{i d} ∇psi1* · ∇psi2 ) dV  +  T ∫ b1 · b2 dV

Nothing here is chosen: the cross term is what the quadratic form produces. Both
terms carry the single stiffness T; the only other constant is xi inside the mode
profile. This is the entire functional:

    E_overlap = min_d  T ∫ Re( e^{i d} ∇psi1* · ∇psi2 ) dV   [core / overlap term]
              +        T ∫ b1 · b2 dV                        [swirl / far term]

Writing A = T ∫ ∇psi1* · ∇psi2 dV (a single complex number per pair), the core
term is |A|·cos(d + arg A). Relaxing d gives the **bonding branch −|A|**; the
orthogonal (constrained) state is the **antibonding branch +|A|**. The 2|A|
splitting and its sign come from the integral, never from a coefficient choice.

## 2. The mode field

The corpus commits (explorations/atom_scale_plausibility.py) to "atom = mode" with
transverse extent set by xi. The minimal mode carrying one unit of winding s about
axis m is

    psi(r) = w(rho_perp/xi) · e^{−rho/xi} · e^{i·s·phi}

where phi is the azimuth about m, and w(u) = u/sqrt(1+u²) is the standard vortex
core regularization (psi must vanish on the winding axis; w is the unique
lowest-order profile with w~u at 0 and w→1 outside the core — the same profile
class the corpus swirl benchmarks use). The exponential envelope e^{−rho/xi} is
the generic bound-mode decay at healing length xi; this is an **ansatz choice**
(declared in Sec. 7), though any monotone envelope of range xi gives the same
qualitative results and the same anchors.

The swirl field of the mode is b = ∇ × (winding phase), which at distances ≫ xi
is exactly the corpus's line-vortex / dipole field with moment m·s.

## 3. Long-range limit = the anchor (Checks 1a, 1b)

At separation d ≫ xi the overlap term dies exponentially and only the swirl term
survives. Computed on the harness grid:

- **2D:** slope of E vs ln(d) = −6.204 vs −2π = −6.283 (1.3% grid error). With the
  corpus's units T = 1/(4π²) this is exactly the anchor (1/2π)·s1·s2·ln(L/d),
  including the sign convention (same-sense costs energy, corpus V2).
- **3D:** the swirl term tracks the dipole tensor [m1·m2 − 3(m1·n)(m2·n)]/r³ over
  all six orientation cases with correlation +0.997.

So the far field is not merely consistent with the anchor — it **is** the anchor,
because the swirl cross term is the same object the corpus computed directly.

## 4. The scale falls out (Check 2)

T is frozen ONCE: the one-atom self energy T ∫ |∇psi|² dV must be the one-atom
binding scale, 13.6 eV. With xi tied to the corpus atom size (rms rule → 0.443 Å),
the dimensionless self integral is J_self = 2.850, giving T·xi = 4.772 eV. That is
the only energy calibration in the atomic sector, and it is not a harness target.

The same frozen functional then yields E_overlap(2.5 Å, head-on, phase-relaxed)
= **−0.27 eV**: squarely in the exchange/chemical-bond decade and an order of
magnitude above kT_room = 0.025 eV. This is the number the dipole-only picture
missed by five orders of magnitude (benchmarks/em/ferromagnetic_alignment.py).
The 0.1 eV scale is a *ratio* — (13.6 eV) × (overlap integral at 2.5 Å / self
integral) — and both integrals are computed from the same profile. Nothing at
0.1 eV was inserted.

## 5. Sign structure

### 5.1 Chemistry: sigma > pi (Check 3a)
Head-on (axes collinear, along the bond) vs side-on (axes parallel, perpendicular
to the bond) overlap of the same two modes: |A_sigma| > |A_pi| at **every**
separation in 1.5–3.5 Å (ratio ≈ 4 at 2.4 Å). The ordering is geometric — the
gradient fields of collinear windings interleave constructively over a larger
volume — and is independent of the core question. Bonding/antibonding split
= 2|A|, sign from the integral (Sec. 1).

### 5.2 Magnetism: ferromagnetism from phase frustration (Check 3c)
This is the result the corpus explicitly could not compute. In a lattice the
relative phase d is **per site**, not per bond: each mode has one internal phase,
shared by all its bonds. On bcc Fe (a = 2.87 Å, nn 2.48 Å):

- **Aligned senses:** the cross amplitude A of a nn bond is azimuth-invariant
  (the factor e^{i(phi2−phi1)} cancels), so all 8 nn bonds of a site demand the
  SAME phase difference. Computed bond coherence = 1.000 — every bond sits at its
  own minimum simultaneously. Energy per site: −0.353 eV.
- **Anti-sense (antiferro):** A picks up e^{−i·2β} where β is the bond azimuth;
  the 8 body-diagonal azimuths of bcc distribute the optima uniformly around the
  circle. Computed coherence = 0.000 — **exact frustration**. The per-site phase
  cannot satisfy any bond; the overlap energy gain cancels to +0.000.

Ferro wins by the full bond energy, >10⁴ × the dipole term. The sign is a
computed interference/frustration result of the frozen functional plus lattice
geometry — no exchange constant was chosen. (The corpus's 2D out-of-plane
antiferro result, lattice_swirl_strain.py, remains the correct dipole-sector
answer where overlap vanishes; here overlap dominates and reverses it, as in
real Fe.)

## 6. The located derivation boundary: the repulsive core

At superposition order the quadratic energy has **no repulsive core**: −|A| grows
monotonically as r → 0, so nothing sets an equilibrium spacing. A core requires
the medium's response to leave the quadratic regime — a saturation penalty
E_sat = (steepness) · T ∫ f(|psi|²) dV. We attempted to derive the steepness from
{T, mu, lambda} and failed honestly: those primitives fix the scale T/xi² of the
penalty but **not the threshold/steepness of f**, which is a property of the
microscopic rope (how hard the network resists over-compression), i.e. a fourth
primitive the corpus has not yet supplied. This is the residual open problem,
stated rather than papered over.

**Consequence for the harness:** all atomic-sector checks (1a, 1b, 2, 3a, 3c) are
CORE-INDEPENDENT — they compare energies at fixed or scanned separations and
never need the core. The nuclear check needs an equilibrium spacing, so it is
CORE-CONDITIONAL: the core length is stood in by the ONE declared empirical
input r_core = 1.9 fm (the observed internucleon spacing), with sensitivity shown
at 1.6 and 2.2 fm and **no tuning to the peak**.

### Nuclear result (Check 3b)
Same functional shape with xi_nuc = 0.87 fm (nucleon rms radius) and the pair
depth D fixed once from the deuteron (2.2245 MeV at core contact). Nucleons pack
at core contact (FCC sites), overlap term binds nearest neighbours, the SAME
functional's swirl/Coulomb term (K = 1.44 MeV·fm, corpus-derived EM) repels the
proton windings, Z(A) from the stability valley. Output across A = 2…258:

- B/A **rises** (2.7 MeV at A=4) → **peaks 7.7 MeV at A = 78** → **declines** to
  7.0 MeV at A=258 (9% decline; observed Fe→U is 16%).
- B(A≈56) ≈ 393 MeV (observed 492 MeV).
- Peak location is stable at A = 78 under the core-length sensitivity scan.

The rise–peak–decline shape and its mechanism (surface-to-volume overlap loss vs
long-range winding repulsion — both terms of the one functional) are genuine
outputs. The peak lands at A = 78, above Fe-56 but inside the iron-region window;
with one declared stand-in input and no shape freedom, we report this as-is.

## 7. Honesty statement

**Fell out of the derivation (not inserted):**
- The functional itself — cross term of the quadratic network energy; both terms
  share the single stiffness T.
- The long-range anchor, exactly (2D log form incl. sign convention; 3D dipole
  tensor, corr 0.997).
- The ~0.1 eV scale at 2.5 Å, as a ratio of computed integrals once T is fixed by
  the 13.6 eV one-atom energy.
- Bonding/antibonding split and sign; sigma > pi at all r.
- Ferromagnetic order of bcc Fe, from computed per-site phase frustration
  (coherence 1.000 vs 0.000).
- Nuclear rise–peak–decline shape and its two-mechanism explanation.

**Assumed / calibrated (each once, declared, never retuned):**
1. Mode envelope form w(rho/xi)·e^{−rho/xi} (profile ansatz; class-generic).
2. xi_atom from the corpus atom size (rms rule, 0.443 Å); T·xi from the 13.6 eV
   one-atom self energy.
3. xi_nuc = nucleon rms radius 0.87 fm; D from deuteron binding.
4. **r_core = 1.9 fm** — the one empirical stand-in for the underived saturation
   steepness (Sec. 6). Sensitivity shown; nuclear check labeled conditional.
5. Per-SITE (not per-bond) phase relaxation in lattices — a physical statement
   about the mode's internal coordinate, argued in Sec. 5.2, not proven from the
   network Lagrangian.
6. Z(A) stability-valley formula as input to the Coulomb term (empirical
   nuclear-chart fact, not a rope prediction).

**Residual open problem:** the saturation steepness (hence the repulsive core and
all equilibrium spacings) is not determined by {T, mu, lambda} at superposition
order. It requires one additional micro-property of the rope network. Locating
this boundary precisely — rather than fitting past it — is a deliverable of this
work.
