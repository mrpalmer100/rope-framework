# ELEC-069 — Is the existence window reachable with the corpus's own numbers? Locked bars

## Commission
ELEC-068 found a stable dynamical branch inside the window A^2 > 12 B C and named
this as the first point at which the line could meet a registered number and
fail. It can, because QB-008 already bounds the stiffness ratio from Bell timing.

## The mapping, fixed before computing
For a profile psi = Amp f(x/L) with f = sech, the three coefficients are
  A = (T0/2) Amp^2 I1,  B = ((k-T0)^2/(8k)) Amp^4 I2,  C = (mu omega^2/2) Amp^2 I3
with I1 = int f'^2, I2 = int f'^4, I3 = int f^2 over the line. The window
A^2 > 12 B C then reduces, in the large-k limit where (k-T0)^2/k -> k, to
  (Amp omega)^2 < c^2 (T0/k) I1^2/(3 I2 I3),
and with ELEC-068's stabilized scale omega = c/L this is a pure constraint on
the configuration's STEEPNESS Amp/L.

## The registered number that decides it
QB-008 (EFT-constrained) bounds the stretch-to-transverse stiffness ratio from
Bell timing: K_L/K_T >= 1.9e8. Larger k makes ELEC-067's coupling stronger and
this window NARROWER. The two effects pull opposite ways and the bars require
that tension be stated whichever way the number falls.

## Locked bars
B1 Compute the profile integrals and the geometric factor.
B2 Evaluate the steepness bound at the registered k/T0 >= 1.9e8, and at larger
   values, since the bound is one-sided.
B3 THE TENSION, stated explicitly: ELEC-067 found the coupling grows as
   (Amp/L)^2 and strengthens with k; this window shrinks as 1/sqrt(k). Report
   the coupling strength AT the maximum allowed steepness. If it is negligible,
   say so plainly -- a soliton that exists only where the mechanism that binds
   it is vanishing is a hollow result.
B4 THE VERDICT: window reachable or not, and what it costs.
B5 HONESTY: the profile family is assumed (sech), the model is 1+1, and omega is
   still undetermined. Nothing here constructs a solution.
