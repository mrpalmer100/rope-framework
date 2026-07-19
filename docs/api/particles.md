# `rope_solver.particles`

Charge, coupling, mass machinery

> rope_solver.particles  --  Canonical particle-sector quantities.

## `breaks_time_reversal(k)`

True iff SU(2)_k Chern-Simons breaks time reversal (chiral c != 0).

## `charge_is_linking_number(C1, C2)`

Return the topological charge q = Lk of a two-strand configuration.

## `chiral_central_charge(k)`

Chiral central charge c = 3k/(k+2) of SU(2)_k Chern-Simons theory.

RIGOROUS (textbook TQFT). c != 0 is exactly the statement that the theory
breaks time reversal: T maps level +k to -k. For k=3, c = 9/5.

This is the rigorous route to the T-oddness of the helical fiber mode in
the Koide-phase derivation: the chiral framing phase exp(2 pi i c/24) it
carries is T-odd because c != 0. It replaces the two FAILED prior arguments
(helicity and mutual linking number, both T-even). See open_problems
'koide-phase-t-parity': this upgrades the T-oddness from unproven to
resting on a theorem, but does NOT close the full derivation (the j=1/2
sector assignment and k=3 postulate remain).

## `dimensional_transmutation_b(mass_ratio)`

Beta-function coefficient b for m = M_Pl exp(-2 pi /(b alpha)).

Given mass_ratio = m / M_Pl (e.g. m_e/M_Pl), return the b that reproduces
it.  For the electron b ~ 17; for mu, tau b differs (~18.6, 19.9), so the
coefficient is NOT universal -- the absolute scale remains open.

## `dimensional_transmutation_works()`

Can the rope generate the mass hierarchy by running its own coupling? No.

The tension running is power-law (luscher_critical_scale_planck -> O(1)) and
the dimensionless sector is at a conformal fixed point (wzw_beta_function=0).
Neither runs logarithmically, so dimensional transmutation cannot produce
the exp(-51.5) electron suppression. The scale must come from EXPLICIT
conformal-symmetry breaking (the cosmological/IR scale), not internal running.

## `higher_link_energy_scaling(Lk_values, energies)`

Fit E ~ Lk^p and return p.

Prior result: p ~ 0.08 (strongly sub-linear) -- higher-charge solitons
reuse rope structure rather than stacking copies.

## `hubble_planck_mass_exponent(H0_km_s_Mpc=70.0, two_pi_convention=False)`

Required exponent p in m_e = M_Pl * (m_H / M_Pl)**p.

p = ln(M_Pl/m_e) / ln(M_Pl/m_H) with m_H = hbar*H0/c^2 (or /2pi if
two_pi_convention). Numerically p ~ 0.3674, but note the IR-mass
CONVENTION shifts p by ~1.3% -- far more than the H0 uncertainty
(~0.06%) -- so any claimed coincidence sharper than ~1% in p is
convention noise. Hypersensitivity: d(ln m)/dp ~ 140, so predicting
m_e to 15% requires p to <0.1%. See open_problems
'electron-absolute-mass' (Fable-5 pass, 2026).

## `kappa_from_alpha()`

Model coupling kappa = alpha/(2 pi).

Dimensional identification (rope_alpha_higher_links): the field self-energy
carries alpha; the 2 pi is loop geometry; T0 L_Pl^2 = hbar c closes it.
Honest caveat: at this coupling the soliton is compact (R < lambda_c),
outside the thin-ring regime -- no numerical R* is claimed there.

## `knot_euclidean_action_planck_units()`

The rope knot's natural Euclidean action, in Planck units.

S_E ~ M_Pl c L_Pl / hbar = 1 exactly (Planck units). RIGOROUS structural
result: a simple knot (Hopf link, crossing number 2) has O(1) action, so
it gives an M_Pl-scale mass. The electron's exp(-51.5) suppression therefore
CANNOT be internal to the knot -- it must come from coupling to the
cosmological background. See open_problems 'electron-absolute-mass'.

## `koide_phase_coefficient()`

The (3 + Phi) coefficient of phi = (3+Phi) theta_W.

D = 3 * d_0 + 1 * d_{1/2} at CS level k=3.  The d_{1/2}=Phi part is
rigorous; the 3+1 T-parity mode count is CONJECTURAL (the T-oddness of
the fiber mode is unproven -- see open_problems 'koide-phase-t-parity').

## `lepton_mass_ratios(sin2_thetaW=0.23122)`

Predicted (m_mu/m_e, m_tau/m_e, m_tau/m_mu) from Koide + phi=(3+Phi)theta_W.

CONTINGENT on the supplied Weinberg angle. With the MEASURED value
(default) the ratios match experiment to ~0.5%. With the rope's own
sin^2 theta_W = 1/(3 sqrt2) the hypersensitivity makes them wildly wrong
-- this is NOT yet a parameter-free prediction (see open_problems).
Returns a dict of ratios.

## `luscher_critical_scale_planck(D=4)`

Scale where the worldsheet effective tension vanishes, in Planck units.

T_eff(R) = T_0 - (D-2)*pi/(24 R^2) = 0  =>  R_crit = sqrt((D-2)pi/24).
POWER-LAW running (Luscher/Alvarez) gives an O(1) critical scale, NOT an
exponential hierarchy. For D=4: R_crit ~ 0.51 L_Pl. This is why worldsheet
tension running cannot produce the electron mass scale.

## `mass_suppression_is_internal()`

Can the electron mass suppression come from the knot itself? No.

Returns False: the knot action is O(1) and its topology O(1) complexity,
insufficient for exp(-51.5). The suppression is provably external (the
knot-cosmos coupling). This is a structural finding, not a fit.

## `quantum_dimension_su2k(j2, k)`

Quantum dimension d_j = sin((2j+1)pi/(k+2)) / sin(pi/(k+2)) for SU(2)_k.

j2 = 2j (so j2=1 means spin-1/2). RIGOROUS: standard Reshetikhin-Turaev
TQFT. At k=3, d_{1/2} = 2cos(pi/5) = golden ratio exactly.

## `su2k3_dressing_scan()`

Scan the SU(2)_3 CFT's natural pure numbers against the required p.

Tests whether IR dressing of the knot mass operator by the framework's
own conformal data (primary weights h_j = j(j+1)/5, dimensions 2h,
central-charge combos, simple rationals) can supply the exponent p.
Returns (min_gap_percent, best_name). Result: minimum gap ~2% vs the
<0.1% hypersensitivity bar -- anomalous-dimension dressing by the
framework's own CFT spectrum is CLOSED as the mass mechanism. (1/e at
0.14% is excluded separately: it holds under only one IR convention,
fails the 2pi convention by 1.4%, and has no mechanism.)

## `wzw_beta_function(k)`

Beta function of the rope's SU(2)_k WZW-type dimensionless sector.

Returns 0.0 exactly: WZW models are conformal fixed points (beta = 0). A
theory at a fixed point does NOT run logarithmically, so it CANNOT generate
an exponential mass hierarchy by dimensional transmutation. This closes the
dimensional-transmutation route for the absolute mass scale "by structure"
(not merely "b isn't universal"). See open_problems 'mass-tension-beta'.
