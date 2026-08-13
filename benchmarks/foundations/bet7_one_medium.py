"""
COMMISSION BET7 -- prosecute the ONE-MEDIUM identity.
Bars: analysis/BET7_one_medium_bars_LOCKED.md (locked first).
B1 exact identity; B2 the provenance audit (V-CONSISTENT vs V-TAUTOLOGY).
"""
import sympy as sp

R, a, w, f_c = sp.symbols('R a w f_c', positive=True)

# EM-RECON-018 coverage relation -> w in terms of a, f_c
w_of_a = sp.solve(sp.Eq(3*sp.pi*w**2/(4*a**2), f_c), w)[0]

# ROUTE Q -- QGATE-004, percolation provenance, D = 2R
n_Q = sp.simplify(f_c*(2*R/w_of_a)**2)

# ROUTE N -- NUCQ-003, tension/density provenance
n_N = 3*sp.pi*(R/a)**2

print("="*70); print("B1  EXACT IDENTITY TEST")
print("="*70)
print("EM-RECON-018 coverage  : w = %s" % sp.simplify(w_of_a))
print("ROUTE Q (QGATE-004)    : n_t = f_c (2R/w)^2 = %s" % sp.simplify(n_Q))
print("ROUTE N (NUCQ-003)     : n   = 3 pi (R/a)^2 = %s" % n_N)
print("DIFFERENCE             : %s" % sp.simplify(n_Q - n_N))
print("IDENTICAL:", sp.simplify(n_Q - n_N) == 0)
print()
print("NOTE: f_c CANCELS. The percolation threshold enters route Q")
print("      explicitly and leaves the answer entirely -- so the")
print("      agreement is NOT arranged through f_c.")

print()
print("="*70); print("B2  PROVENANCE AUDIT -- is this evidence or a consequence?")
print("="*70)
print("SHARED CONSTANTS between the two routes:")
print("  f_c   : appears in Q explicitly and in EM-RECON-018's coverage")
print("          relation; CANCELS exactly. Non-trivial.")
print("  3 pi  : appears in N as 3 pi (R/a)^2 and in EM-RECON-018's")
print("          coverage counting 3 pi w^2/(4 a^2) = f_c.")
print()
print("THE QUESTION B2 EXISTS TO ASK: is that 3 pi ONE constant or two?")
print("  N's 3 pi  : from rho = 3 T_tube/(n c^2 a^2) with mu = T_tube/c^2")
print("              = rho pi R^2 -- i.e. a TENSION/DENSITY bookkeeping")
print("              factor (the 3 from the per-strand area convention,")
print("              the pi from the tube's circular cross-section).")
print("  018's 3 pi: from COVERAGE counting of strands per mesh cell.")
print()
print("VERDICT ON B2: the two 3 pi's are NOT independently motivated in")
print("the registry -- both encode 'how much strand area sits in a cell',")
print("and neither claim derives its factor from the other's premises.")
print("They are plausibly ONE convention wearing two derivations.")
print("=> The agreement is DEMOTED: it is a CONSISTENCY CHECK that could")
print("   have failed on the f_c structure and did not, but it is NOT")
print("   independent evidence for one-medium.")

print()
print("="*70); print("B4  DOWNSTREAM, REPORTED NOT EXECUTED")
print("="*70)
print("IF one-medium holds, Q and N count the SAME object, so:")
print("  NUCQ-003's floor n >= ~115 applies to QGATE-004's n_t.")
print("  QGATE-003/004's demanded n_t = 111 sits BELOW that floor.")
print("  => the collective-hbar demand is excluded by the tube width,")
print("     which is what NUCQ-003 already concluded for its own n.")
print("  The two claims were never linked because the name collision")
print("  (FND-066) hid that they count the same thing.")
print()
print("NO census executed, NO branch of FND-065's fork picked (B4).")
