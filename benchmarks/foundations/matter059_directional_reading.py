# FND-MATTER-059: THE FND-017 DIRECTIONAL READING, SETTLED BY FORCED GEOMETRY
#
# CONTAMINATION DISCLOSED ON THE FACE: this session read the MATTER058 record
# (target, gap, and which reading lands) before running. It is therefore NOT
# target-blind, and per 058's own bar it may not CHOOSE the reading. What it
# may do is prove the reading is not a choice: if the displacement count is
# forced by a theorem, the answer is computed, not selected, and the
# adjudication rests on checkable geometry rather than this session's
# judgment. The decision rule applied at the end (which outcome means what)
# was pre-committed by the blind 058 session, not by this one.
#
# THE QUESTION (from FND-MATTER-058): a displacing strand inclusion of radius
# r sits in the cubic weave (3 strand families, spacing a). Does it displace
# ambient mode content per the full cell face (a^2: one family's channel
# only) or per one direction's share (a^2/3: all three families equally)?
#
# THE THEOREM (Cauchy/Crofton, stated and then verified numerically):
# for a family of parallel straight lines with length density rho = 1/a^2
# (length per unit volume), the total line length excluded by a convex body
# of volume V is exactly rho * V, INDEPENDENT of the family's direction --
# because the excluded length is the integral of chord lengths over the
# family's transverse positions, and the chord integral over a transverse
# plane IS the volume, whichever plane you project onto.
#
# Consequence: a cylindrical inclusion (radius r, length L, axis along z)
# excludes, from EACH of the three families:
#   parallel family (z):   chords are full length L over the disk pi r^2
#                          -> excluded length = pi r^2 L / a^2
#   transverse family (x): chords 2 sqrt(r^2 - y^2) integrated over (y,z)
#                          -> excluded length = pi r^2 L / a^2
#   transverse family (y): same by symmetry -> pi r^2 L / a^2
# All three are EQUAL. The displacement is direction-blind by theorem, so
# the mode content displaced counts all three families: the a^2/3 reading
# is DERIVED. There is no convention left to choose.
#
# The verification below computes all three excluded lengths numerically
# (analytic chord integrals + Monte Carlo) and requires agreement.

import numpy as np

rng = np.random.default_rng(59)
A = 1.0          # mesh spacing (units)
R = 1.3e-3 * A   # inclusion radius, r << a (registered thinness regime)
L = 1.0          # inclusion length

print("== FND-MATTER-059: the directional reading, forced by geometry ==\n")
print(f"   cylinder: radius r = {R:.3e} a, length L = {L} (axis z)")
print(f"   line density per family: rho = 1/a^2\n")

V = np.pi * R**2 * L
theorem = V / A**2
print(f"   theorem (Cauchy): excluded length per family = rho V = {theorem:.6e}\n")

# --- family parallel to the axis (z): channel occupation -------------------
# lines at transverse positions (x,y); excluded length = L where x^2+y^2<r^2
# integral over positions * density = L * pi r^2 / a^2
par = L * np.pi * R**2 / A**2
print(f"   parallel family (analytic):    {par:.6e}   ratio to theorem {par/theorem:.6f}")

# --- transverse family (x): chord integral ---------------------------------
# line at (y,z): chord through the disk = 2 sqrt(r^2-y^2) for |y|<r, any z in [0,L]
# excluded length = (1/a^2) * L * int_{-r}^{r} 2 sqrt(r^2-y^2) dy = L pi r^2/a^2
from scipy.integrate import quad
chord_int, _ = quad(lambda y: 2.0 * np.sqrt(max(R**2 - y**2, 0.0)), -R, R)
trans = L * chord_int / A**2
print(f"   transverse family (analytic):  {trans:.6e}   ratio to theorem {trans/theorem:.6f}")

# --- Monte Carlo cross-check, both families --------------------------------
N = 2_000_000
# parallel: sample (x,y) uniform in a box of side 4r; excluded length = L * P(inside)*box_area*rho
xy = rng.uniform(-2 * R, 2 * R, size=(N, 2))
inside = (xy[:, 0]**2 + xy[:, 1]**2) < R**2
mc_par = L * inside.mean() * (4 * R)**2 / A**2
# transverse: sample (y,z) in [-2r,2r]x[0,L]; chord length per line
yz = np.column_stack([rng.uniform(-2 * R, 2 * R, N), rng.uniform(0, L, N)])
ch = 2.0 * np.sqrt(np.clip(R**2 - yz[:, 0]**2, 0.0, None))
mc_trans = ch.mean() * (4 * R) * L / A**2
print(f"   parallel family (MC):          {mc_par:.6e}   ratio {mc_par/theorem:.6f}")
print(f"   transverse family (MC):        {mc_trans:.6e}   ratio {mc_trans/theorem:.6f}")

ok = (abs(par/theorem - 1) < 1e-12 and abs(trans/theorem - 1) < 1e-5
      and abs(mc_par/theorem - 1) < 5e-3 and abs(mc_trans/theorem - 1) < 5e-3)
print(f"\n   EQUALITY OF ALL THREE FAMILIES: {'VERIFIED' if ok else 'FAILED'}")
print("   The displacement is direction-blind. The inclusion excludes the SAME")
print("   strand length from each family; the displaced mode content therefore")
print("   counts all three directions. THE READING IS FORCED: a^2/3.\n")

# --- the confrontation (pre-committed by the blind 058 session) ------------
# 058 locked the consequence of each outcome before this session existed:
#   a^2   -> mechanism misses at 2.08x, likely wrong in detail
#   a^2/3 -> lambda = 2 x 3 x pi (r/a)^2, lands 1.44x, first derived lever
print("-- confrontation under 058's pre-committed rule --")
r_over_a_sq = 2.776e-6 / np.pi          # registered base pi(r/a)^2 = 2.776e-6
lam_base = np.pi * r_over_a_sq
lam = 2.0 * 3.0 * lam_base              # polarizations (forced, 058) x directions (derived here)
target = 1.156e-5                        # MATTER055 target, loaded ONLY here
print(f"   lambda = 2 (pol) x 3 (directions, derived) x pi(r/a)^2 = {lam:.4e}")
print(f"   target (MATTER055): {target:.4e}")
gap = max(target/lam, lam/target)
print(f"   gap: {gap:.3f}x (derived {'over' if lam>target else 'under'} target; bar: 2.00x, inherited)")
print(f"   VERDICT: {'INSIDE the bar' if gap < 2.0 else 'OUTSIDE the bar'}")
