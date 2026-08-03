# PRED-003-DICT bars — LOCKED before computation (2026-08-02)

Commission (PRED-003-CHAIN's specification): evaluate the Maxwell-sector dictionary —
map the unit linking number to a source strength q_s and verify
q_s^2 = 8 pi eps0 lambda J a.

Strategy declared up front: the full Chern-Weil two-form evaluation is not a
one-session computation, but a REDUCTION of it is, using only registered structure:
OPT-006 (Derived): the medium's wave impedance is Z_med = sqrt(T mu) = T/c, intrinsic;
EM-002 (Derived): Z0 = sqrt(mu0/eps0), c^2 = 1/(mu0 eps0), hence eps0 = 1/(Z0 c);
EM-002b: the corpus already relates alpha to the impedance (as consistency).
The exact Maxwell identity alpha = q^2 Z/(4 pi hbar) then transfers to the medium with
Z -> Z_med, reducing the dictionary question to a single geometric unknown: the LENGTH
the unit winding presents as a source.

Rules fixed in advance:
- R1: Only registered structure plus exact algebra. No coefficient may be chosen to
  hit the CONST target; if the reduction leaves the target undetermined, the residual
  unknown is named and the candidates are TABLED, not selected.
- R2: If the reduction produces a candidate that CONTRADICTS PRED-003-CONST's triple
  (2, 1, -1), the contradiction is registered at full volume — including any
  consequence for the -2 ratio itself.
- R3: Candidate lengths must be corpus-native (built from registered primitives
  T, kappa, a); no length invented for fit. The internal decision question (which
  registered modulus curves the on-site locking potential) is NAMED, not answered,
  unless the answer is derivable from registered claims alone.
- R4: No tier motion this session. PRED-003's provisional list is updated to whatever
  the reduction shows, favourable or not.

Bars:
- B1 (the permittivity of the medium): from Z_med = T/c and eps = 1/(Z c), derive
  eps_med = 1/T — the medium's permittivity is the inverse tension — and verify the
  Maxwell identity alpha = q^2 Z/(4 pi hbar) symbolically against the definition
  alpha = q^2/(4 pi eps hbar c).
- B2 (the reduction theorem): alpha = l_q^2 T/(4 pi hbar c), where l_q is the source
  length of the unit winding (q_s carries length units in medium normalization —
  exactly the dimensional structure PRED-003-CHAIN's B1 found). The CHAIN target
  q_s^2 = 8 pi eps0 lambda J a reduces to l_q^2 = 8 pi lambda * l_lock * a, with
  l_lock = T/kappa the LOCKING LENGTH (a genuine registered-primitive length,
  dimensionally verified). The field-theory specification collapses to one geometry
  question: what length does a unit winding present?
- B3 (the candidate table, per R3): the three corpus-native candidates and their
  full consequences, each verified symbolically end-to-end:
    l_q ~ a                => alpha ~ T a^2,        triple (1, 2, 0),  ratio -1
    l_q ~ sqrt(l_lock a)   => alpha ~ T^2 a/kappa,  triple (2, 1, -1), ratio -2
    l_q ~ l_lock           => alpha ~ T^3/kappa^2,  triple (3, 0, -2), ratio -3
  (ratios under PRED-003's own G ~ 1/(Ta), hbar external, tension channel).
- B4 (the consequence for the sole T1, per R2): the -2 is the MIDDLE CANDIDATE, not
  the framework's unique value. What survives unconditionally: all three candidates
  give a FIXED, scale-free ratio — the paper's own stated "framework-forced content"
  — and a measured nonzero drift ratio in {-1, -2, -3} would SELECT the source
  length, converting the geometric unknown into an observable.
- B5 (the internal decision, per R3): state the bounded question that picks the
  candidate — the curvature of the on-site locking potential (J-based curvature gives
  the healing length ~ a; kappa-based gives ~ l_lock; the geometric-mean case is the
  mixed normalization) — on the microscopic-mechanics paper's machinery. Named, and
  answered only if registered claims force it.
- B6 (propagation): PRED-003, CONST, and CHAIN annotated with the reduction; the
  paper's P6 correction queue gains the ratio's candidate-dependence.
