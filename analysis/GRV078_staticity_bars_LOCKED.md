# GRV-078 bars — LOCKED before computation (2026-08-02)

Commission (GRV-077's named next-order): derive P1' -- staticity of the exterior.
GRV-034's frozen-star reading and the whole pressing -> area-law -> whisper chain
assume the medium outside a horizon SITS STILL. Tonight asks whether the medium's
own dynamics makes it sit still.

The claim to be established, scoped honestly in advance:
  "The static exterior is a STABLE ATTRACTOR of the linearized medium dynamics:
  perturbations carry positive energy, cannot grow, and radiate out of any
  compact exterior region through the two open boundaries (outward to infinity,
  inward through the horizon), leaving the static profile."
This is staticity-as-relaxation at linear order. Nonlinear relaxation and the
interior (where the exhaustion degenerates the coefficients) are OUT OF SCOPE and
named as the residue.

The derivation route, fixed in advance:
- B1 (consistency closure): the static profile is a SOLUTION -- GRV-029's derived
  dictionary maps the static metric to positive wave-operator coefficients
  (mu, T_a) on the exterior, and GRV-077's theorem says the static support it
  needs is exactly the transverse pressing the weave supplies. The two claims
  close on each other; recorded, not re-derived.
- B2 (the energy identity, by machine): for the derived wave operator
  mu(x) u_tt = d_a(T_a(x) d_a u), the energy E = Integral (mu u_t^2 +
  T (du)^2)/2 satisfies dE/dt = boundary flux EXACTLY (sympy, 1D radial form).
  Positive coefficients on the exterior => E is positive-definite => NO GROWING
  MODES: exponential instability would need negative stiffness, which the
  exterior does not have this side of exhaustion. Growth is confined to where
  the chain never claimed staticity anyway.
- B3 (relaxation, numeric): 1D radial evolution on a Schwarzschild-class
  background (alpha = sqrt(1 - rs/r), isotropic-map coefficients per GRV-029),
  domain r/rs in [1.5, 40], absorbing boundaries at BOTH ends (outgoing to
  infinity; infalling through the inner edge -- the horizon side also REMOVES
  energy from the exterior, which is the frozen-star picture's mechanism).
  Gaussian pulse; the energy in the compact shell r/rs in [2, 20] must decay
  monotonically after the transient, by at least a factor of 30 over the run.
- B4 (the control): the SAME evolution with reflecting boundaries must NOT decay
  (energy conserved to numerical tolerance) -- proving the decay in B3 is
  radiation through the boundaries, not numerical dissipation. Conservation bar:
  drift < 2% over the run.

Rules fixed in advance:
- R1: the numerical scheme is energy-conserving up to boundary terms (leapfrog);
  the B4 control adjudicates the scheme before B3's decay is believed.
- R2: no statement about the interior, the exhaustion surface itself, or
  nonlinear settling; the residue is named.
- R3: no tier motion. P1' moves to DISCHARGED-AT-LINEAR-ORDER; the chain's
  premise ledger updates to (P1'') nonlinear relaxation and (P2') the O(1)
  crossing geometry.
