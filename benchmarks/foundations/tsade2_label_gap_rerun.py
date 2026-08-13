"""COMMISSION TSADE2 -- the label gap re-run on post-SHIN lengths.

Executed under analysis/TSADE2_label_gap_bars_LOCKED.md. Conventions:
E(L) = hbar c / L exactly; lambda(E) = 2 pi hbar c / E; bar 1.4e15 eV
at m = 1; AT-BAND = within a factor pi of the bar (FND-060's O(1)).
TSADE's G1-G5 values carried verbatim from its results table.
"""
HBARC = 1.97327e-7  # eV m
BAR = 1.4e15        # eV
PI = 3.141592653589793

lam = 2 * PI * HBARC / BAR
af_edge = lam / 4.0

def verdict(E):
    if E >= BAR: return "CLEARS"
    if E >= BAR / PI: return "AT-BAND"
    return "MISSES"

print("TSADE2 -- label gap on post-SHIN lengths (locked bars)")
print(f"lambda(1.4 PeV) = {lam:.4e} m; window edge a_f = lambda/4 = {af_edge:.4e} m\n")

print("L-STRAND (carried verbatim from TSADE, coarse lengths):")
carried = [
    ("G1 T0 a (locking energy)", 1.63e5),
    ("G2 hbar c / a (mesh spacing)", 2.07e10),   # kappa250 (larger of the two)
    ("G3 hbar c / d_c (strand thickness)", 1.06e12),
    ("G4 hbar c / a_disp (KILLED unregistered, FND-058)", 2.12e20),
    ("G5 sqrt(T0 hbar c) (confinement)", 5.80e7),
]
for name, E in carried:
    v = verdict(E)
    if "G4" in name: v += " but UNAVAILABLE"
    print(f"  {name}: {E:.3e} eV -> {v}")

print("\nL-SUB (fine lengths, FND-087 windows, m = 1):")
G6 = HBARC / af_edge
G7 = HBARC / af_edge  # p <= lambda/4: same edge, same lower bound
print(f"  G6 hbar c / a_f at edge (LOWER bound; true a_f <= edge): {G6:.3e} eV -> {verdict(G6)}")
print(f"     ratio to bar: {G6/BAR:.4f} = 4/(2 pi) exactly")
print(f"  G7 hbar c / p at edge (LOWER bound): {G7:.3e} eV -> {verdict(G7)}")
print(f"  G8 T0_f a_f = (T0/n_sub) a_f: WINDOW ONLY (n_sub underived) -- report:")
T0 = 1.63e5 / 6.0056e-17  # eV/m from T0 a = 1.63e5 eV at M-point a (illustrative only)
print(f"     at n_sub in [2, 1e4]: {T0*af_edge/2:.2e} .. {T0*af_edge/1e4:.2e} eV (all MISS; informative only)")
print(f"  G6' consistency reading: fine ceiling must carry m x 1.4 PeV (FND-087's purpose)")
print(f"     => hbar c/a_f >= m x {BAR:.1e} / O(1) => label gap at L-SUB >= {BAR:.1e} eV / O(1)")
print(f"     -> CONDITIONALLY CLEARS; condition: FND-060's ceiling theorem transfers to the fine mesh")
