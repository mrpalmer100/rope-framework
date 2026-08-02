# ELEC-057 — Is there ANY strand scale where both sectors live? Locked bars

## Commission
The Lorentz constraint a <= 1e-16 m is a BOUND, never a measurement, and the
corpus has sat at the ceiling throughout. The electron sector's 2e4 (ELEC-036/
040) is a LENGTH RATIO and therefore points at a smaller a; the hbar sector's
patch grows as a shrinks (L ~ 1/a). Under the one-medium declaration
(ELEC-038) both sectors must share one a. Question: does a viable window exist?

## The scaling laws, fixed before evaluation
With T_tube (hadronic measurement) and R (lattice, ELEC-052) held fixed:
  n(a)  = 3 pi (R/a)^2                       [structural strand count]
  T0(a) = T_tube / n(a)      ~ a^2           [per-strand tension]
  w(a)  = a / sqrt(3)                        [ELEC-053 invariance theorem]
  L(a)  = sqrt(2 pi hbar c / T0)  ~ 1/a      [ELEC-054 subluminality floor]
  r_e(a) = 21.16 fm x (a / 1e-16)            [ELEC-036 calibrated radius;
           linear because ELEC-041's geometry is pure RATIOS]

## Locked gates (a scale is VIABLE only if all pass)
G1 LORENTZ:    a <= 1e-16 m.
G2 ELECTRON:   r_e(a) <= 1e-3 fm (ELEC-036's conservative structure bound).
G3 TENSION-MATCHING: an electron rope must be a whole number of vacuum
   strands (ELEC-040 under ELEC-038), so T0(a) <= 0.2376 J/m, the calibrated
   rope tension.
G4 HBAR/NUCLEAR: standard QM must hold in nuclei, requiring many sub-quantum
   patches in the lightest nucleus. Demand L(a) <= R_He4 = 1.905 fm for even
   ONE patch (the weakest defensible form; the >=100-patch version is also
   reported).

## Locked verdict rules
B1 Sweep a over 25 decades (1e-30 to 1e-10 m) and report each gate's allowed
   interval EXACTLY, by solving the inequality, not by grid resolution.
B2 THE VERDICT: report the intersection. If non-empty, the corpus has an
   unexamined viable window and that is a major positive. If empty, report
   the SIZE of the gap in decades, and state which gates are mutually
   exclusive.
B3 SEPARABILITY: for each gate, state whether it fails ALONE (i.e. has no
   solution inside G1) or only in combination. A gate with no solution under
   the Lorentz bound is excluded independently of every other sector, which is
   a stronger statement than a two-sector clash and must be reported as such.
B4 HONESTY: r_e(a) linearity assumes the electron geometry rescales rigidly
   (true for ratios, and the calibration itself carries ELEC-034's recalibration
   residue ~2.4%); G4's threshold choice is stated and the stricter variant
   reported alongside. No gate may be relaxed after the intersection is seen.
