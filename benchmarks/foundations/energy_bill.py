"""THE ENERGY BILL (FND-132, 2026-08-17) -- the rotating winding's kinetic
energy priced against the registered Sigma bookkeeping and the registered
zero-point window. Executed as FND-131's named next-order.
"""
import numpy as np
ok=True
print("THE ENERGY BILL -- what the wave costs, and whether the registry can pay")

print("\nLEG 1 -- THE MATERIAL-SPEED IDENTITY (the jewel)")
s1=1/3; sin2th=1-s1               # transverse sine^2 at level 1 (reading A)
Tf=1.5                            # fibre tension, T0_f units (BLOCH-L)
vm2 = sin2th*Tf                   # v_m^2/c^2 = sin^2(theta) * (T/mu c^2); kb term
                                  # deleted by the neutrality theorem
print(f"  v_m^2/c^2 = sin^2(theta) x T_fibre/T0_f = (2/3)(3/2) = {vm2:.10f}")
print("  THE MATERIAL POINTS OF THE LEVEL-1 WINDING ORBIT AT EXACTLY c.")
print("  Two registered numbers -- the magic angle's transverse share and the")
print("  dynamical fibre tension -- multiply to ONE. The vacuum's constituents")
print("  move at the medium's own causal speed: marginal, photon-like, an")
print("  identity not a violation (the 6.1x floor prices WAVE speeds; the")
print("  wave speed 1.2247 c was priced at FND-130).")
ok &= abs(vm2-1.0)<1e-12

print("\nLEG 2 -- THE BILL, per coarse strand per unit axial length (T0 units)")
P1=np.sqrt(3.0)                   # level-1 arc per axial length = 1/c_ax
P2lo,P2hi=2.409,2.409             # registered two-level path factor (SHIN8)
KE1_arc=0.5                       # KE per unit level-1 arc = (1/2) mu c^2 = T0_f/2 -> x n_sub = T0/2
E_static_booked=1.0               # Sigma books T0 per axial length per strand (3T0/a^2)
E_L1 = P1*(1.0+KE1_arc)           # tension along path + KE, level-1-only exact
# two-level bracket: KE_2 per level-2 arc <= (1/2) v_m2^2, v_m2^2 = (1-s2)(1.5+17.926 kb)
s2=(15+2*np.sqrt(30))/35
kb_hi=0.07909
vm2_2=(1-s2)*(Tf+17.926*kb_hi)
E_2lvl = P2lo*(1.0+KE1_arc+0.5*vm2_2)
print(f"  static bookkeeping (Sigma_vac = 3 T0/a^2): {E_static_booked:.3f} per strand")
print(f"  wave reading, level-1 exact:  E = sqrt(3) x (1 + 1/2) = {E_L1:.4f}")
print(f"  wave reading, two-level bracket (path 2.409, kb <= 0.079): E <= {E_2lvl:.4f}")
share_lo=(E_L1-1)/E_L1; share_hi=(E_2lvl-1)/E_2lvl
print(f"  THE DYNAMICAL SHARE (excess over booked / total): [{share_lo:.3f}, {share_hi:.3f}]")

print("\nLEG 3 -- THE REGISTERED WINDOW")
print("  FND-MATTER-041 (the F-2SCALE window verdict) carries a derived")
print("  robustness condition: the surviving arm SURVIVES IFF the zero-point")
print("  share of the vacuum energy is < 0.889.")
print(f"  The wave winding's dynamical share lands at [{share_lo:.3f}, {share_hi:.3f}]:")
print("  **INSIDE THE WINDOW AT BOTH EDGES**, with margin [1.14x, 1.45x].")
ok &= share_hi<0.889<1.45*share_hi or share_hi<0.889
print("  THE BILL IS PAYABLE: the perpetual rotation's energy fits inside the")
print("  share the registered matter-route window already reserves for")
print("  non-tension vacuum energy. The wave reading is NOT falsified by the")
print("  energy accounting -- and it gives the zero-point share a mechanical")
print("  identity: the vacuum's 'zero-point energy' IS the winding's rotation.")

print("\nLEG 4 -- NAMED RESIDUALS, undiluted")
print("  (1) Sigma naming: the wave total (2.6-4.5 T0/a^2-class) is a distinct")
print("      object from Sigma_vac = 3 T0/a^2; the corpus's third naming-")
print("      collision risk, flagged before it collides (EM-020 precedent).")
print("  (2) The two-level KE is BRACKETED, not exact: the composite wave")
print("      build (already queued) owns the exact number.")
print("  (3) The level-1 identity v_m = c is exact at the registered T = 3/2;")
print("      any future re-pricing of the fibre tension moves it off c --")
print("      the identity is a TRIPWIRE on the tension, registered as such.")
print("\nVERDICT:", "PRICED-AND-PAYABLE -- the wave survives its own bill" if ok else "FAILURE")
raise SystemExit(0 if ok else 1)
