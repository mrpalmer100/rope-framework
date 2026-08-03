# GRV-090 bars — LOCKED before computing (2026-08-03)

Commission (GRV-088 suspect (iii), the one pushing UP): the pile-up correction
to premise P-e. The coefficient chain identified the cell energy density in
the pressing formula with the ambient vacuum density Sigma; the accretion
shell visibly piles deposited energy above ambient in the engine. Does the
pile-up matter? Tonight it is DERIVED, not estimated: the chain's own
identities give the pile-up ratio in closed form, and the engine's measured
numbers (f*, beta_phys, r_d*) evaluate it.

The derivation route, recorded before computing:
- Deposited-energy channel: broken-crossing density in the fired shell is
  f* n_x = f* chi/a^3; each carries e_bit = beta_phys W with the lift-over
  barrier W = Sigma a^3 h/(chi sigma). Multiply: the deposited density is
  e_dep = f* beta_phys Sigma h/sigma, so the RATIO is
      P_dep = e_dep/Sigma = f* beta_phys (h/sigma).
  Every a and chi cancels; the ratio is the shell's occupancy times the bit
  price times THICKNESS OVER DEPTH. Machine-verify the cancellation.
- Live-wave channel: the firing region operates at r_d* ~ 1 (GRV-089), i.e.
  wave energy density ~ the threshold density W/(a^3/chi) = Sigma h/sigma --
  the SAME h/sigma suppression, bounded by r_d* (h/sigma).
- Matter channel (the physical accretor): infalling matter's rest+kinetic
  density is bounded by the densest astrophysical matter; compare rho c^2 to
  Sigma on BOTH forks.

Bars:
- B1: the closed-form ratio P_dep = f* beta_phys h/sigma derived by machine
  (sympy; all lattice factors must cancel exactly).
- B2: evaluation with MEASURED inputs (f* = 0.036-0.119 from GRV-084's shells;
  beta_phys = 35.4 from GRV-089; h = 1.87e-19 m from HBAR-005) across the
  physically generous depth range sigma in [1e-3 m, 1e4 m]: report the
  maximum of the deposited and live-wave ratios.
- B3: the matter channel: max astrophysical density (neutron-star core,
  ~1e36 kg/m^3 x c^2 is over-generous; use 1e21 J/m^3) against Sigma on F-Lor
  (3.6e35 J/m^3 lower edge) and F-Sak (2.3e71): report the ratios.
- B4: the verdict grammar, fixed in advance:
  - If every channel's pile-up ratio is below 1e-6, premise P-e is VINDICATED,
    suspect (iii) is ELIMINATED, and -- the campaign consequence stated in
    advance so the adjudication cannot drift -- THE UPWARD DIRECTION CLOSES:
    the remaining resolution space is (ii) the h-convention rescaling the
    mechanism side, and (iv) the lineage's 0.23 coming down. The tension's
    prior shifts accordingly and is said plainly.
  - If any channel reaches 1e-2 or above, the pile-up is live and its proper
    treatment becomes the next construction.
