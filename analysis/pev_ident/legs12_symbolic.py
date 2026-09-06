"""PEV-IDENT Legs 1-2 (symbolic; charter D1-D5). Symbols: a_f, m, p, E_anchor.
Registered relations entered as relations. No prediction numbers consulted."""
import sympy as sp
a_f, m, p, E_anch, hbar, c, S, c_eff = sp.symbols('a_f m p E_anchor hbar c S c_eff', positive=True)
h = 2*sp.pi*hbar
# --- registered constructions ---
s1 = sp.Rational(1,3)                        # sin^2 psi_1, FND-088 (convention A: axial cosine = sin psi)
tan_psi1 = sp.sqrt(s1/(1-s1))                # axial/transverse
R1 = p/(2*sp.pi*tan_psi1)                    # FND-125 (corrected reading), worst-case pitch p = a_f
R1 = R1.subs(p, a_f)
E_rot = hbar*c/R1                            # Prediction 33's construction: material orbit at c (FND-132)
# homogenization (lambda/4) ceiling, FND-083/086/087: a_f = lambda/4 at E_max = m*E_anchor
E_max = m*E_anch
a_f_ceil = h*c/(4*E_max)                     # the ceiling on a_f
E_ceiling_of_af = h*c/(4*a_f)                # the photon energy whose lambda/4 equals a_f
# --- Leg 1 / Q1: the ratio, reduced ---
ratio = sp.simplify(E_rot/E_ceiling_of_af)
print("Q1  E_rot/E_ceiling (both at the same a_f) =", ratio, " free symbols:", ratio.free_symbols)
ratio_at_ceiling = sp.simplify((E_rot.subs(a_f, a_f_ceil))/E_max)
print("    E_rot(a_f=a_f,ceil)/E_max =", ratio_at_ceiling, " free symbols:", ratio_at_ceiling.free_symbols)
# --- Leg 2 / Q2: the fine frequency ladder, units c/a_f ---
w_rot = c/R1                                                       # material orbit angular frequency
cos_psi1 = sp.sqrt(1-s1)                                           # transverse component
L_turn = 2*sp.pi*R1/cos_psi1                                       # fibre length per turn
v_wave = sp.sqrt(sp.Rational(3,2))*c                               # FND-130 rotating-helix wave speed
w_wave = v_wave*2*sp.pi/L_turn                                     # temporal frequency of the winding wave
w_homog = 2*sp.pi*c/(4*a_f)                                        # lambda/4 rule as a frequency
w_band_S = S*c/a_f                                                 # charter D4 literal: S c/a_f
w_band_ceff = S*c_eff/a_f                                          # instrument normalization: S c_eff/a_f
u = c/a_f
for name, w in (("omega_rot", w_rot), ("omega_wave (rotating helix)", w_wave), ("omega_homog (lambda/4)", w_homog)):
    print(f"Q2  {name:30s} = {sp.simplify(w/u)} c/a_f")
print("Q2  omega_band = S c/a_f (D4 literal) | S c_eff/a_f (instrument units, c_eff from the FND-089/C1 run)")
print("Q2  omega_rot / omega_wave =", sp.simplify(w_rot/w_wave))
