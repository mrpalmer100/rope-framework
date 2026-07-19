# `rope_solver.electromagnetism.photon`

Light: photon and birefringence

> rope_solver.electromagnetism.photon  --  Light in the rope framework.

## `birefringence_velocity_split(chi, wavelength)`

Fractional speed split between circular polarizations: dv/c = chi lambda/2pi.

Topological (frequency-independent in the rotation it produces); at visible
wavelengths this is ~1e-38, unobservable locally but cumulative over
cosmological distance.

## `chirality_chi(sin2thetaW, n_rope, r_H)`

Rope chirality coupling chi = sin(2 theta_W) n_rope r_H^2 / c  [1/m].

Emerges mechanically from the two-strand helix geometry, not postulated.

## `chirality_product_from_beta(beta_deg=0.342, D_gly=13.8)`

Invert the measured rotation to the rope geometric constraint.

sin(2 theta_W) n_rope r_H^2 = 2 beta / D   [1/m].
With the Eskilt-Komatsu value this is ~9.18e-29 /m.

## `cosmic_birefringence_deg(chi, D_gly=13.8)`

Polarization rotation angle beta = chi c D / 2, in degrees.

Integrated over the distance D to last scattering.

## `cross_sector_massless()`

Check the photon (Lk=0) is massless under the particle mass mechanism.

The particle sector gives mass from soliton self-energy that scales with
linking; at Lk=0 there is no charged soliton and no mass.  Returns
(photon_Lk, consistent) where consistent means Lk=0 -> massless holds.

## `dispersion_omega(k)`

Vacuum dispersion omega = c k (exactly linear -- non-dispersive).

The rope vacuum has a single wave speed, so there is no frequency-dependent
term.  Falsifiable: any measured vacuum dispersion would break this.

## `eb_ee_ratio(beta_deg=0.342)`

Predicted CMB EB/EE cross-correlation = sin(4 beta)/2, flat in multipole.

The specific rope prediction LiteBIRD (2030s) will test (~0.0119 at the
measured beta).

## `group_minus_phase_velocity(k)`

v_group - v_phase in vacuum: exactly 0 (non-dispersive).

Returned explicitly so a regression test can assert masslessness/no
dispersion rather than trust the linear form by eye.

## `photon_energy(nu)`

Kink energy E = h nu (nu = flick oscillation frequency).

## `photon_linking_number()`

The photon carries Lk = 0: no net linking -> massless, chargeless.

This is the structural reason the photon is massless in the same language
that makes charged solitons (Lk != 0) massive.  See cross_sector_massless.

## `photon_momentum(nu)`

Kink momentum p = h nu / c = h / lambda.
