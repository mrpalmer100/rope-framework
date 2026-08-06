# Rope Parameters — the canonical card

*Every quantity that describes a strand in this framework, with its status,
provenance, and value on both registered scale branches. Compiled 1 August 2026.*

**Read this before any session that uses a rope constant.** Values are verified
by `benchmarks/foundations/rope_parameter_card.py`, which recomputes every
derived relation and fails if the card drifts from the registry.

---

## The short version

A strand is a **thin, framed, very stiff but EXTENSIBLE rod** under tension, with
**no material points**. It has:

- **two independent lengths** — the spacing between strands, and the strand's own
  thickness — and the ratio between them is ~1000, which matters more than it
  looks;
- **one independent stiffness scale**, the vacuum stiffness Σ, from which the
  tension follows;
- **a frame**, giving it twist and torsional rigidity — it is a rod, not a string;
- **two postulates rather than numbers**: near-inextensibility (a *limit*, not an
  exact property — see below), and no material points.

**On "inextensible" — the word is a trap and the card used to fall in it.** The
strand *does* stretch. It must: a perfectly rigid strand carries no longitudinal
wave, and the framework's entire superluminal channel **is** a longitudinal wave,
with c_L/c = √(k/T₀). Inextensibility is the k → ∞ idealisation, useful for
deriving the tension's role and wrong if taken literally.

Everything else is derived.

---

## 1. The independent quantities

| Quantity | Symbol | Lattice-anchored | Σ-route | Status | Source |
|---|---|---|---|---|---|
| Vacuum stiffness | Σ | 3.61e35 J/m³ | 5.10e35 J/m³ | **the one open number** | ELEC-052, ELEC-081 |
| Strand thickness | d_c | 1.87e-19 m | 1.87e-19 m | measured (calibration) | HBAR-005 |

**Σ is the corpus's single remaining free scale** (FND-017). The two candidates
differ by 28%; the lattice-anchored value derives from published QCD flux-tube
data and survived an independent recomputation to 1.3% (ELEC-081), so the corpus
**leans** to it without claiming it. No vacuum experiment in reach separates them
(QGATE-018).

---

## 2. Derived lengths

| Quantity | Symbol | Lattice-anchored | Σ-route | Relation |
|---|---|---|---|---|
| Strand spacing | a | 9.999e-17 m | 1.000e-16 m | a = √(3T₀/Σ) |
| Coherence spacing | w | 5.773e-17 m | 5.774e-17 m | **w = a/√3, exactly** |

The invariance theorem T₀/Σ = a²/3 holds **for any tube radius** (ELEC-053), so
w never depended on the quantities a long campaign spent adjudicating. Both
branches land on the Lorentz bound a ≲ 1e-16 m to better than 0.1%.

**The thinness ratio r/a ≈ 9.4e-4** — the strand is roughly a thousand times
thinner than the distance to its neighbour. This is not decorative; see §5.

---

## 3. Mechanical constants

| Quantity | Symbol | Lattice-anchored | Σ-route | Status | Source |
|---|---|---|---|---|---|
| Tension | T₀ | 1203 J/m | 1700 J/m | **not independent**: T₀ = Σa²/3 | ELEC-053, FND-017 |
| Line density | μ | 1.339e-14 kg/m | 1.892e-14 kg/m | derived: μ = T₀/c² | FND-MATTER-033 |
| Stretch modulus | k | **DISPUTED — see below** | | k > T₀ required for nonlinear stability | EM-RECON-009, QB-008 |
| Torsional rigidity | C | 4.21e-36 J·m | 5.95e-36 J·m | per strand, C = G·πr⁴/2 | GRV-009, GRV-073 |
| Couple-stress modulus | γ | 4.21e-4 J/m | 5.95e-4 J/m | medium: γ = C/a² | GRV-073 |
| Young's modulus | E | 8.76e40 Pa | 1.24e41 Pa | E = k/(πr²) | GRV-073 |
| Shear modulus | G | 3.50e40 Pa | 4.95e40 Pa | G ≈ E/2.5 (**Poisson ratio unregistered**) | GRV-073 |

**On the tension — corrected 1 Aug 2026 (FND-021).** T₀ behaves as a **Lagrange
multiplier** *in the inextensible limit*, and in that limit stores no energy, from
which follows the useful no-go that **no local derivation of T₀ can succeed**
(FND-017).

But **the medium is not exactly inextensible, and must not be** — a perfectly
inextensible strand has no longitudinal wave at all, and the framework's
superluminal channel exists precisely *because* k is finite. The longitudinal
speed is

    c_L / c = √(k/T₀)

so "inextensible" is the k → ∞ idealisation. At finite k there **is** stored
elastic energy, of order T₀²/2k per unit length.

**On the wave speed.** c = √(T₀/μ) is satisfied identically on both branches, by
construction of μ. It is a consistency check, not an independent input.

---

## 4. Postulates, not numbers

- **P-VOL / near-inextensibility** — FND-STRAND-001 works with "literal
  inextensible elastic curves", and that is an **idealisation adopted for
  tractability**, not a claim that k is infinite. It is what makes T₀ behave as a
  multiplier *in the limit*. Taken literally it would forbid the fast channel
  (FND-021).
- **No material points** — FND-REL-002 (Derived). Longitudinal displacement is
  *gauge*; only its gradient (the strand density perturbation) is physical. This
  forbids the Galilean convective term, forces the wave sector into
  Lorentz-invariant form, and selects the lab parametrization over arclength.
- **Framed** — every strand carries a material frame with an explicit twist field
  and a conserved Calugareanu ledger, Lk = Tw + Wr (FND-STRAND-002/003). This is
  what makes the medium a **Cosserat continuum**.
- **The medium is a reservoir** — infinite and pre-tensioned. Without it a closed
  medium absorbs transverse displacement at *zero* energy cost and carries no
  waves at all (ELEC-080), so **the optics sector depends on this premise**.

---

## 5. Two facts worth carrying into every session

**The strand is a ROD, not a string.** It has a stretch modulus and an r⁴ torsion
law (GRV-009's primitives, `torsion~r^4`). A tensioned string with no shear
modulus would have *no torsional stiffness whatever*, and the framework's twist
sector would not exist. This was registered inside a claim marked **Failed** —
GRV-009 failed for the wrong sign of spatial curvature, and its *primitives* were
never in dispute.

**The thinness ratio does real work.** Axial stiffness carries r² (a
cross-sectional area); torsional rigidity carries r⁴ (a polar moment). Their
ratio therefore leaves one factor of (r/a)² ≈ 8.7e-7 — which is why γ/T₀ ≈ 3.5e-7
rather than order unity. **A dimensional estimate using only T₀ and a cannot find
this**, because the whole suppression lives in the second length that estimate
discards. It was found only by locating the registered elastic constants.

---

## 5a. ⚠ TWO DIFFERENT "FAST CHANNELS" (FND-022)

The corpus uses one name for two objects that want **opposite limits of k**:

| | What it is | Needs | Used by |
|---|---|---|---|
| **(a) Longitudinal elastic wave** | a real propagating mode at c_L = c√(k/T₀) ≈ 1.4e4·c | k **finite** — an infinitely stiff strand has no wave at all | EM-RECON-011/012, ELEC-067 |
| **(b) Instantaneous constraint** | not a wave; no speed; the rigidity of the k → ∞ limit | k → **infinity** — Bancal's theorem excludes *all finite speeds* | QB-007, QB-008, QB-012, QB-023, ELEC-079 |

**The finite-speed wave cannot supply Bell correlations**, however large √(k/T₀)
is — that is precisely why QB-008 forced the conjecture onto the
instantaneous-constraint limb.

**Resolved (FND-023).** They are *not* the same modulus. **P-VOL is volume
conservation of the MEDIUM**; **k is the STRAND's stretch modulus** — independent
constraints on different objects. A strand can stretch while the medium conserves
volume.

And **incompressible elasticity is the standard precedent**: an elliptic,
instantaneous pressure multiplier coexisting with hyperbolic, finite-speed shear
waves in one action. Textbook, and not paradoxical.

Bancal's theorem doesn't apply either: its argument runs through relativity of
simultaneity as *fundamental*, while FND-REL-001 makes Lorentz invariance
**emergent** and FND-REL-002 forces only the **wave sector** into Lorentz form. A
constraint is not a wave.

*Still open:* nobody has written the constrained action with the volume
multiplier explicit — and whether that multiplier is the right **carrier** for
the nonlocal conditional is unestablished, since QB-007 needs spacelike
*depletion of a wave amplitude*.

## 5b. ⚠ THE k/T₀ DISPUTE — eight orders, unresolved

Two registered claims give the stretch modulus incompatible values, and neither
cites the other:

| Source | k/T₀ | Basis |
|---|---|---|
| EM-RECON-009, GRV-009 | **2** | fitted to nuclear and chemical spacings; k > T₀ for nonlinear stability |
| QB-008 | **≥ 1.9e8** | forced by Bell timing, v_dep > 1.38e4 c; and √(1.9e8) = 1.38e4 confirms c_L/c = √(k/T₀) |

**Everything downstream of k inherits this.** The couple-stress modulus is
γ = 4.21e-4 J/m at k/T₀ = 2, and **3.996e+04 J/m** at the Bell-timing value —
eight orders apart, and the sign of the comparison with T₀ *inverts* (γ/T₀ =
3.5e-7 versus 33).

This is reported, not adjudicated. Choosing by preference is the failure mode
this corpus spent 1 August correcting.

## 6. What is *not* registered

- **The strand's Poisson ratio.** G ≈ E/2.5 is imported from isotropic elasticity.
  This is the one unpinned quantity in the mechanical chain and can move γ by a
  factor of a few — not by orders.
- **A matter-to-rotation coupling.** GRV-005's source is a static force density
  with no torque, spin or angular-momentum term. See GRV-071.
- **A metric map with a shift slot.** GRV-029's dictionary is an exact
  *four-to-four* bijection for a static diagonal metric; g_0i has nowhere to live.
- **Fundamental masses.** The lepton spectrum is an irreducible input (PM-004).

---

*Branch note: use ONE branch throughout a calculation. The two differ by 28% in Σ
and ~41% in T₀, and mixing them has produced errors before. The ratio γ/T₀ =
3.50e-7 is branch-independent, as is w/a = 1/√3.*

---

## Card sync note — 2026-08-04 (FND-MATTER-044)

**The M-point.** Solving the m_e-pinned combination T₀a = m_e c²/L (the scale
campaign's single spent calibration, FND-MATTER-040/041) jointly with the
invariance theorem T₀ = Σa²/3 at the lattice-anchored Σ gives the
m_e-consistent mesh point:

- **a = 6.0e-17 m** (Lorentz bound satisfied with 40% margin, no longer
  saturated — the §2 values held a at the bound by adoption)
- **T₀ = 434 J/m**

All pairwise EM comparisons land inside the zero-point band (factor ≤ 3);
see analysis/MATTER044_whisper_pricing_results.md. The §1–§3 tables above
retain the historical adoption values pending full card regeneration
(rope_parameter_card.py update flagged); treat the M-point as the working
mesh point for scale-sensitive work. n_q is invariant under this move
(proven), so the snap-band shortfall is a genuine residual interrogating the
core thickness h.
