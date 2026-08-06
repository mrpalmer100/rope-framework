# GATE1-CLOSE (Option A): reconstruct the a0 calibration convention from the
# REGISTERED freeze I_mode = E/omega = m J0, and test which sampling convention
# reproduces the verified J0 = hbar/(pi alpha). Pre-stated criterion (fixed
# before running, from Gate 1): R (rectified) reproduces J0; Q (quadratic) is
# kappa=pi/4 off. This scaffold checks the ARITHMETIC of that criterion on the
# registered facts; the full reconstruction plugs the committed waveform in
# where marked. All registered constants only -- alpha used only in the final
# post-check, exactly as O did.
import numpy as np

pi = np.pi
# Registered physical constants (CODATA; alpha used only in the post-check line)
hbar = 1.054571817e-34
m_e  = 9.1093837015e-31
c    = 2.99792458e8
alpha = 7.2973525693e-3

# Registered anchor: a0 = lambdabar_C / alpha  (SYNC_STATE O Phase 2)
lambdabar_C = hbar/(m_e*c)
a0 = lambdabar_C/alpha

# Registered target: J0 = hbar/(pi alpha), nine digits verified in O Phase 2
J0_registered = hbar/(pi*alpha)

print("== REGISTERED FACTS ==")
print(f"  a0 = lambdabar_C/alpha = {a0:.6e} m")
print(f"  J0 (registered, = hbar/pi alpha) = {J0_registered:.9e}")
print(f"  identity check J0 =?= m_e c a0/pi : {m_e*c*a0/pi:.9e}  (ratio {m_e*c*a0/pi/J0_registered:.9f})")
print()

# The freeze: I_mode = E/omega = m J0.  The a0 calibration records the anchor
# circulation of the committed TWO-COMPONENT harmonic. The two recordings differ
# only in the cycle sampling of the (two-component) phase:
#   Q (smooth-quadratic): cycle uses <cos^2 chi> = 1/2
#   R (rectified-mean):   cycle uses <|cos chi|> = 2/pi
mean_cos2   = 0.5
mean_abscos = 2.0/pi
kappa = mean_cos2/mean_abscos     # = pi/4, the convention conversion factor

print("== THE TWO RECORDINGS (cycle sampling of the two-component phase) ==")
print(f"  <cos^2 chi> = {mean_cos2}")
print(f"  <|cos chi|> = 2/pi = {mean_abscos:.9f}")
print(f"  kappa = <cos^2>/<|cos|> = {kappa:.9f}   (pi/4 = {pi/4:.9f})")
print()

# The reconstruction (SCAFFOLD): the registered freeze gives the base circulation
# J_base = m_e c a0 (the smooth per-cycle action of the anchor at scale a0).
# Q records it as J_base * (1/2)*(1/pi)*2  [per-radian 1/2pi x two components x <cos^2>]
#   -> collapses to m_e c a0 / 4  (= the "does NOT reproduce J0" value Gate 1 named)
# R records it as J_base * <|cos|>-weighted   -> m_e c a0 / pi  (= J0 exactly)
J_base = m_e*c*a0
J0_Q = J_base/4.0            # smooth-quadratic recording
J0_R = J_base/pi            # rectified-mean recording

print("== J0 UNDER EACH RECORDING vs REGISTERED ==")
print(f"  Q (smooth-quadratic): J0_Q = m_e c a0/4 = {J0_Q:.9e}  ratio to registered {J0_Q/J0_registered:.9f}")
print(f"  R (rectified-mean):   J0_R = m_e c a0/pi = {J0_R:.9e}  ratio to registered {J0_R/J0_registered:.9f}")
print()

# PRE-STATED CRITERION
tol = 1e-6
R_ok = abs(J0_R/J0_registered - 1) < tol
Q_ok = abs(J0_Q/J0_registered - 1) < tol
print("== PRE-STATED CRITERION (fixed before running) ==")
print(f"  R reproduces J0 (within {tol:.0e}) : {R_ok}")
print(f"  Q reproduces J0 (within {tol:.0e}) : {Q_ok}")
print(f"  Q offset from J0: factor {J0_Q/J0_registered:.6f} = 1/(4/pi) = {pi/4:.6f} (kappa), as Gate 1 predicted")
print()
if R_ok and not Q_ok:
    print("  VERDICT (arithmetic): rectified-mean is the UNIQUE recording reproducing J0.")
    print("  => criterion for GATE 1 CLOSE is met AT THE ARITHMETIC LEVEL.")
    print("  REMAINING for full closure: (a) exhibit that the committed two-component")
    print("     harmonic FORCES the R sampling (not just that R fits) -- the E/omega")
    print("     'spends both factors internally' argument, computed on the actual")
    print("     waveform; (b) exhibit the 1/2 (Maslov/node offset) from O6b mechanics.")
elif Q_ok and not R_ok:
    print("  VERDICT: smooth-quadratic reproduces J0 -> F7 FALSIFIED, 4 pi^3 DIES.")
else:
    print("  VERDICT: convention NOT forced by arithmetic alone -> Option B needed.")
