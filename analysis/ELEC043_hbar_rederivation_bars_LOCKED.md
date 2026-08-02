# ELEC-043 — The hbar relation re-derived: locked bars (registered before computation)

## Commission
ELEC-040/041/042 named W = 1.80 T D^2/c (QGATE-005's reconnection separatrix,
QGATE-006's n_t ~ 111 transfer) as the sector's load-bearing outlier at 2.7e6.
This audit re-derives W from scratch and decomposes the outlier into the
derivation's assumptions. It does NOT tune anything to close the gap; every
lever tested must be a quantity already registered elsewhere in the corpus.

## The derivation's assumption ledger (enumerated before testing)
A1. Barrier form: cosine, V(q) = Eb(1+cos(pi q/D))/2.
A2. Barrier height: Eb = T * D (tension times one length).
A3. Barrier width: 2D, with D identified as the rope CORE DIAMETER d_c.
A4. Effective inertia: mu_eff = T/c^2 (which is what yields the T D^2/c form).
A5. Participation: a SINGLE strand pair reconnects (n_t = 1); collectivity
    enters only as a multiplier n_t on W.

## Locked bars
B1 (regression). The from-scratch WKB separatrix integral at E -> Eb+ for the
    declared cosine barrier reproduces kappa in [1.70, 1.90]. FAIL => the
    published 1.80 is not reproducible and everything downstream is void.

B2 (prefactor boundedness). Across four alternative barrier families at the
    SAME height and width (square, triangular, parabolic-cap, Gaussian
    truncated at the same base), the prefactor kappa stays within a factor of
    4 of 1.80. PASS establishes that barrier FORM cannot supply the 2.7e6 and
    the outlier lives in A2-A5. FAIL (spread > 4x) reopens barrier form as a
    live lever and the bar's verdict must say so.

B3 (dimensional necessity). Verify symbolically/numerically that A2 + A4
    jointly force the T D^2/c form; i.e. W scales as sqrt(mu_eff * Eb) * D and
    only the stated choices give T D^2/c. Records WHICH assumption carries
    each power of D.

B4 (the length-choice decomposition). Registered lengths at the electron
    scale: core diameter d_c = 1.877e-19 m (ELEC-041) and vacuum strand
    spacing w = 2.87e-16 m (ELEC-040, nuclear-density medium). Compute
    W(D = d_c) and W(D = w) with the registered single-strand tension
    T = 1.70e3 J/m and report each as a fraction of hbar. No verdict bar;
    a measurement whose numbers are quoted whatever they are.

B5 (the closure test, the decider). With NO new parameters: does any
    combination of ONE registered length choice (d_c or w) and ONE registered
    collectivity value (n_t = 1, n_t = 111 from QGATE-006, n_t = 2.95e8 from
    ELEC-042, n_t = 8.7e8 from ELEC-037) bring n_t * W within a factor of 3
    of hbar? Every combination is tabulated; cherry-picking is prevented by
    exhaustive enumeration (8 cells). If a cell closes, the finding is a
    RECONCILIATION CANDIDATE, held to Modeled and explicitly conditional on
    justifying that cell's length identification physically. If no cell
    closes, the hbar relation survives as a genuine no-go and the sector must
    say so.

B6 (honesty guard). The audit must state, whichever way B5 falls, that the
    separatrix model itself (a 1D WKB tunnel through a static barrier) is a
    MODEL of reconnection, not a derivation from rope dynamics; upgrading it
    is named as the next order regardless of outcome.

## Kill condition
If B1 fails, the claim registers as Failed-and-kept with no downstream
numbers quoted.
