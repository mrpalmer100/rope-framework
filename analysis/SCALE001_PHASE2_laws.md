# SCALE-001 PHASE 2 -- THE SCALING LAWS (LOCKED BEFORE EVALUATION)

*Written 2026-08-11 under the sealed target (analysis/SCALE001_TARGET.sealed).
NO law is evaluated in this file. Each of the eight frozen classes (charter,
docs/commissions/COMMISSION_SCALE-001_emergent_length.md) is either written as
g_class = f(registered inputs) with every input's claim ID, or registered
UNDERSPECIFIED with its reason on the record. Evaluation happens once, after
--lock, in benchmarks/foundations/scale001_evaluate.py.*

## Blind-integrity disclosure, stated before anything else

The charter itself concedes the blind is a discipline, not cryptography: the
target regenerates from the registry, and this session's orientation documents
(HANDOFF.md, docs/ROPE_PARAMETERS.md) display the FND-041 ratio values in
plaintext. The laws below were therefore written under DISCLOSED-TARGET
conditions. The discipline honoured instead is the one that can be honoured:
every functional form and every exponent below is forced by its mechanism and
its registered inputs, none contains a free number or a choosable exponent,
and the UNDERSPECIFIED registrations refuse exactly the classes where a number
COULD have been steered. The look-elsewhere computation at Phase 3 must state
this condition.

## Notation and registered symbol table (inputs only, no evaluation)

- a       : mesh spacing, from the m_e-pinned solve a = (3 K_me / Sigma_vac)^(1/3),
            K_me = T0 a (spent calibration), per FND-038 as corrected by FND-040;
            per-floor like the sealed target itself (FND-040 floors).
- T0      : strand tension, T0 = Sigma_vac a^2 / 3 (FND-017; ELEC-053 invariance).
- k       : stretch modulus; registered adjudicated value k = 2 T0
            (EM-RECON-013 edge resolution; EM-RECON-017; GRV-073 unconditional
            reading; stability requires k > T0 per EM-RECON-009).
- kappa_lock : locking (crossing) modulus, kappa_lock = 2 T0 / a, EXACT
            (PRED-003-ETA one-metric enslavement); units J/m^2, matching the
            crossing term s/a in EM-RECON-025's registered stiffness matrix,
            so s = kappa_lock is the registered identification of the
            crossing strength (no other J/m^2 crossing stiffness exists in
            the registry).
- R_eq    : chromoelectric flux-tube equilibrium radius, a MEASURED registered
            length (ELEC-052; ELEC-081 independent-estimator confirmation).
- f_c     : interpenetrability coverage threshold, pure geometric number
            (FND-MATTER-004).

## The eight classes

### C1 -- collective mode localization: UNDERSPECIFIED

Localization of the transverse Goldstone pair (EM-RECON-025) requires a
registered DISORDER: a variance of the crossing strength across the weave.
The registry contains none. The crossing modulus is registered as the exact
enslavement kappa_lock = 2 T0 / a (PRED-003-ETA) with zero registered spread;
no claim anywhere registers a disorder distribution, correlation, or variance
for crossings (registry sweep, this session: no carrier). A localization
length xi_loc = a * (kappa_lock / delta_kappa)^2 (weak-disorder 1D form, the
exponent mechanism-given) cannot be written without inventing delta_kappa.
Per the charter's admissibility rule 2, the class retires UNDERSPECIFIED:
the ontology registers a perfectly ordered weave and therefore cannot pose
its own localization question.

### C2 -- instability-proximity correlation length: EVALUABLE

Mechanism: the registered transverse energy functional expands as
(T0/2) g'^2 + c4 g'^4 with c4 = (k - T0)/8 (EM-RECON-009, exact expansion);
stability requires k > T0, so k/T0 - 1 measures proximity to the registered
mechanical stability boundary (EM-RECON-009's bound, the charter's C2
pointer). Gaussian fluctuations about the registered functional give the
mean-field correlation length, exponent -1/2 forced by the mechanism (the
quadratic coefficient of the fluctuation operator vanishes linearly at the
boundary):

    g_C2 = ( k/T0 - 1 )^(-1/2)

Inputs: k (EM-RECON-013 / EM-RECON-017 / GRV-073, adjudicated k = 2 T0),
T0 (FND-017). No free parameter; the exponent is mean-field, not chosen.
Drift filters (ELEC-082 / PRED-003-CONST): k and T0 co-drift as strand
moduli, so g_C2 is drift-invariant; passes trivially.

### C3 -- recruitment coherence length: EVALUABLE

Mechanism: FND-037 derives shape factorization -- the mesh's linear response
to a source has a CHARGE-INDEPENDENT profile shape and penetration length
(u_D(r) = C_D u_1(r), same penetration length across representations, the
9/4 density ratio constant across the profile). Read as the charter directs
(a coherence scale rather than a packing factor), the recruitment structure's
one registered length is that universal penetration scale, and its registered
measured carrier is the flux-tube equilibrium radius R_eq (ELEC-052, with
ELEC-081's independent estimator agreeing to 1.3 percent). The coherence
length of the ambient weave's linear response, in cells:

    g_C3 = R_eq / a

Inputs: R_eq (ELEC-052 / ELEC-081, measured), a (FND-038 solve as corrected
by FND-040, per floor). No free parameter; no exponent to choose.
Circularity check, on the face: R_eq is a lattice MEASUREMENT, not derived
through l_q or the alpha relation; a comes through the m_e-pinned solve.
Neither input routes through GRV-093's quantum area, so the law does not
smuggle the target. Drift filters: R_eq/a is a ratio of medium lengths;
under the registered E2 branch both scale with the mesh; passes.

### C4 -- reconnection mean-free path: UNDERSPECIFIED

A mean-free path requires a registered reconnection RATE or cross-section
(events per strand length, or per crossing per time). The reconnection
sector registers conservation laws (FND-010, FND-012), the action carrier
and its magnitude gap (QGATE-001, QGATE-003), and transport constraints
(FND-KIN-001) -- but NO rate, frequency, cross-section, or number density
of reconnection events anywhere (registry sweep, this session: no carrier).
lambda_mfp = 1/(n_x sigma_x) cannot be written in registered inputs. The
class retires UNDERSPECIFIED per admissibility rule 2.

### C5 -- topological / BKT screening length: UNDERSPECIFIED

Pre-flagged by the charter itself and by FND-045's locked clause: the BKT
correlation length requires a temperature (THM-004: T_BKT = pi K / 2;
THM-005: the universal jump), and the vacuum sector registers NO temperature.
The charter forbids importing one. No registered effective temperature was
found (registry sweep: the temperature claims are all gravity-sector horizon
temperatures, not vacuum weave temperatures, and none is registered as such).
The class retires UNDERSPECIFIED exactly as the charter anticipated it must.

### C6 -- nonlinear strain localization: UNDERSPECIFIED

Two registered readings of the quartic coefficient conflict in sign at the
adjudicated k = 2 T0: the extensible expansion gives c4 = (k - T0)/8 = +T0/8
(EM-RECON-009, stabilizing, no self-focusing), while the constant-tension
arc-length reading gives -T0/8 (FND-040, softening). A soliton width
w = a * sqrt( beta / ( |c4/T0| x^2 ) ) (beta = 1/12 - B/(T0 a^2),
FND-REL-004) additionally requires the strain amplitude x -- and amplitude
selection is REGISTERED AS SLAVED TO g ITSELF (FND-044: A = 2.6348 l_q via
ELEC-054). Using the registered amplitude is circular on the face; using any
other is a free parameter. The class retires UNDERSPECIFIED on two
independent grounds (contested sign at the registered k; the only registered
amplitude is the target's own slaved unknown).

### C7 -- percolation / coverage length: UNDERSPECIFIED

The percolation correlation length xi = a * |f/f_c - 1|^(-nu) has its
exponent from universality (mechanism-given) but requires the ambient weave's
coverage fraction f RELATIVE to the threshold. FND-MATTER-004 registers f_c
and places ATOMS at threshold; no claim registers the vacuum weave's own
coverage fraction or its distance from f_c (registry sweep: no carrier).
Without |f - f_c| the law has a free parameter. UNDERSPECIFIED per
admissibility rule 2.

### C8 -- spectrum of the full lattice dynamical operator: EVALUABLE

Mechanism: EM-RECON-025 registers the full two-strand dynamical matrix
[[T0 q^2 + s/a, -s/a], [-s/a, T0 q^2 + s/a]] with acoustic branch
omega^2 = (T0/mu) q^2 and optical gap 2 s / (mu a). The spectrum of this
registered operator contains exactly one non-trivial length: the crossover
wavenumber q* at which the acoustic branch energy reaches the optical gap,
T0 q*^2 = 2 s / a, below which the two branches are spectrally separated and
above which they mix. With the registered identification s = kappa_lock
(the only J/m^2 crossing stiffness in the registry, PRED-003-ETA exact):

    g_C8 = xi / a = (1/a) * sqrt( T0 a / (2 kappa_lock) )
         = sqrt( T0 / (2 kappa_lock a) )

Inputs: T0 (FND-017), kappa_lock = 2 T0 / a (PRED-003-ETA), a (FND-038/040).
No free parameter; the crossover condition is the mechanism, the exponent
1/2 is forced by the quadratic dispersion. Honesty note, written before
evaluation: the registered operator is translation-invariant and
short-ranged, and FND-045's exclusion pointed at this class as the direction
of escape; whatever this law returns, it is the licensed operator's own
answer, and if the operator's spectrum contains no mesoscopic scale then
registering that IS the finding. Drift filters: a ratio of registered moduli
and lengths, drift-invariant under the E2 branch; passes.

## Ledger before lock

- Evaluable: C2, C3, C8 (three laws, zero free parameters, all exponents
  mechanism-forced).
- UNDERSPECIFIED: C1, C4, C5, C6, C7 (five classes; each with its missing
  registered carrier named).
- Five of eight is a majority: the UNDERSPECIFIED-DOMINANT branch of the
  pre-committed verdict grammar is live regardless of how the three
  evaluable laws land, and the verdict must confront both facts.
- Look-elsewhere convention, committed now: the rate is computed for the
  three LOCKED evaluable laws against the log-width of the sealed range,
  under a log-uniform prior over the four-decade window 10^0 to 10^4 cells
  (the widest range any registered discussion has entertained for a
  mesoscopic cell count); the DISCLOSED-TARGET condition above is restated
  next to the number.
