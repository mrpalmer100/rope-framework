"""
FND-068 -- STRAND-AREA CONVENTION PROVENANCE.

Bars: analysis/FND068_area_convention_bars_LOCKED.md
PROHIBITION (preregistered): the convention is derived from strand/cell
geometry ONLY. QGATE-004's and NUCQ-003's formulae are not consulted
until the substitution step, and no target count is used anywhere.
"""
import sympy as sp

a, w, R = sp.symbols('a w R', positive=True)
f_c_val = 0.309                      # FND-MATTER-038

print("="*72); print("B2  WHAT KIND OF FRACTION IS f_c?  (read from FND-MATTER-038)")
print("="*72)
print("FND-MATTER-038 constructs f_c as a Poisson field of width-w DISKS")
print("IN THE BUNDLE CROSS-SECTION, a transverse test rope passing iff its")
print("centre finds a channel, with a stated '2D-parallel reduction'.")
print("=> f_c is an AREAL fraction in a cross-sectional plane. NOT a")
print("   volume fraction of the 3D weave. Established, not assumed.")

print()
print("="*72); print("B1  THE DERIVATION, from primitive geometry alone")
print("="*72)
print("Registered geometry: the weave's point group is O_h (ELEC-096),")
print("i.e. a cubic weave with THREE orthogonal strand families, spacing")
print("a, strands of diameter w.")
print()
# line density: each family contributes one line per a^2 of transverse area
Lambda = 3/a**2                       # total strand length per unit volume
phi_vol = sp.simplify(Lambda*sp.pi*w**2/4)
# a plane perpendicular to z is pierced ONLY by the z-family
phi_areal = sp.simplify((1/a**2)*sp.pi*w**2/4)
print("total strand length per unit volume   Lambda = 3/a^2   (3 families)")
print("VOLUME fraction   phi_vol   = Lambda * pi w^2/4 =", phi_vol)
print("AREAL fraction in a plane perp to z: only the z-family pierces it,")
print("   one strand per a^2 cell, disk area pi w^2/4")
print("phi_areal = ", phi_areal)
print()
print("THE COEFFICIENT, derived without opening either route:")
print("   areal  ->  pi w^2/(4 a^2)      coefficient  pi")
print("   volume ->  3 pi w^2/(4 a^2)    coefficient  3 pi")
print("Since f_c is AREAL (B2), the correct relation is pi, NOT 3 pi.")
w_corr = sp.solve(sp.Eq(phi_areal, sp.Symbol('f_c', positive=True)), w)[0]
print("   => w/a = sqrt(4 f_c/pi) = %.4f" % float(sp.sqrt(4*f_c_val/sp.pi)))
print("   EM-RECON-018 registered w/a = 0.3621 from 3 pi w^2/(4a^2) = f_c")
print("   ratio = sqrt(3) = %.4f   -- a VOLUME fraction equated to an" %
      float(sp.sqrt(3)))
print("   AREAL threshold. OUTCOME O2: a different coefficient emerges.")

print()
print("="*72); print("SUBSTITUTION -- each route separately, now that pi is fixed")
print("="*72)
fc = sp.Symbol('f_c', positive=True)
w_of_a = sp.sqrt(4*fc/sp.pi)*a
n_Q = sp.simplify(fc*(2*R/w_of_a)**2)
print("ROUTE Q (QGATE-004, cross-section disk count, f_c areal -- self-consistent):")
print("   n_t = f_c (2R/w)^2 =", n_Q)
print("ROUTE N (NUCQ-003): its 3 pi comes from rho = 3 T_tube/(n c^2 a^2),")
print("   a LENGTH-DENSITY bookkeeping. Independent geometric check:")
print("   total strand length per unit tube length = Lambda * pi R^2 =",
      sp.simplify(Lambda*sp.pi*R**2))
print("   -> NUCQ-003's n is a LENGTH DENSITY over all three families.")
print()
print("THE TWO ROUTES COUNT DIFFERENT OBJECTS:")
print("   Q : strands THREADING the cross-section   = pi R^2/a^2")
print("   N : total strand length per unit length   = 3 pi R^2/a^2")
print("   ratio N/Q = 3 exactly.")
print()
print("=> FND-067's IDENTITY DISSOLVES. It was manufactured by exactly the")
print("   error this audit was chartered to look for: EM-RECON-018's")
print("   factor-3 conflation inflated route Q by 3, making it")
print("   accidentally equal route N. Correct the convention and the")
print("   agreement disappears.")
