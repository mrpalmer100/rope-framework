# ELEC-047 — The bundle census at the coherence radius: locked bars (before computation)

## Commission
ELEC-046 named this the sector's decisive computation: does the medium supply
~498 strands of coherence? QGATE-004 attempted the census and returned
"underdetermined by one ratio" because the constituent width w was free. It is
free no longer: ELEC-040/038 fixed w = 2.87e-16 m (nuclear-density spacing) at
the tension-matched scale. The census is therefore now answerable, and it must
be answered in the medium's actual 3D geometry, not the 2D sheet scaling
(R_c = sqrt(n_t) w) that ELEC-046 quoted as a placeholder.

## Model (declared before running)
The medium: an isotropic network of strands at spacing w, represented as a
Poisson line process with length density rho_L = 1/w^2 (one strand per w^2 of
transverse cross-section). Strand count within a ball of radius R:
n(R) = pi (R/w)^2 (exact for Poisson lines; to be verified by Monte Carlo).
Causal availability: a reconnection event of duration tau can be in one-way
causal contact with strands out to R = c tau (ELEC-043's bound, transverse
speed exactly c).
Event duration: the derived barrier's own dynamics. A separatrix traversal at
threshold takes divergent time (logarithmic in the energy excess) -- so
near-threshold events are SLOW, and slowness recruits strands. tau(eps) is
computed on ELEC-045's derived profile V(s), mu(s), at E = E_b(1+eps).

## Locked bars
B1 (bookkeeping closure, tautology-adjacent and flagged as such). The line
   process at rho_L = 1/w^2 implies mass density (T_s/c^2)/w^2; this must
   reproduce nuclear density ~2.3e17 kg/m^3 within 20%, because w was DEFINED
   from nuclear density -- the bar validates the counting convention, not the
   physics, and the output must say so.

B2 (instrument). Monte Carlo Poisson-line count through a ball agrees with
   n(R) = pi (R/w)^2 to < 5% at R = 5w, 12w, 22w. FAIL voids the census.

B3 (THE CENSUS). Report n(R) at R = 22.3w (ELEC-046's quoted radius) and the
   radius R_req solving n(R) = 498. The geometric verdict: does the medium
   CONTAIN ~498 strands within a causally plausible radius (R_req < 22.3w)?

B4 (the mechanism). Compute tau(eps) on the derived barrier and find eps* such
   that c*tau(eps*) >= R_req (one-way) and >= 2 R_req (round-trip). PASS if
   eps* > 1e-12 for the one-way criterion (the slowing mechanism can supply
   the duration without absurd fine-tuning). The logarithmic form of the
   divergence must be verified (fit tau ~ -A ln eps + B).

B5 (verdict discipline). ELEC-046 set a trichotomy: census near 500 = chain
   closes; near 1 = dies; near 1e4 = dies. The honest possible fourth outcome
   -- geometry supplies the strands, dynamics supplies the duration only for
   near-threshold events, participation (pre-correlation) remains underived --
   must be reported as CONDITIONAL, not as closure. Causal contact is
   NECESSARY for participation, not sufficient; that sentence is load-bearing
   and appears in the output verbatim.

## Kill condition
B2 fail => Failed-and-kept, no downstream numbers.
