python3 - <<'EOF'
notes = """# Release Notes — v3.16.0 (2026-08-10): The Sigma Arc

Eight commissions in one day, bars locked before every computation, and the
corpus's one open number closed.

## The result in one paragraph
Sigma, the vacuum stiffness — carried since ELEC-053 as "the one genuinely
open number, two candidates 28% apart" — is pinned: **3.61–3.70e35 J/m³**.
The 28% was never a tension between two physics routes; it was one formula,
Sigma = 3 T_tube/(n a²), evaluated at a strand count (n_t = 111) that had
died twice since its registration without the Sigma value ever being re-run.
The kill-inheritance rule, locked before computing, demoted the 5.10e35
registration to historical. Everything downstream was then re-evaluated
(zero flipped verdicts; the vacuum fence *eased* for the first time in its
history; the EM arc's one-number lock resolved to kappa_0 = 1.66–1.68e-4
m³/(s·C)); the pinning was checked at partial independence, then at full
collaboration independence with the conversion locked while the data was
still inaccessible; the intrinsic/total width distinction was closed by an
exact convolution identity; and the one-medium declaration made — and passed
— its first out-of-sample prediction: the string tension must rise 6–22%
from quenched to physical quark masses, and the lattice literature,
consulted after the demand was locked, delivers 8–20%.

## The self-correction
Commission TAU, chartered to discharge the arc's deepest caveat, found the
caveat was stale: ELEC-053 had already derived the strand-count
identification, and the arc's own drafts had been propagating ELEC-052's
superseded language for nine bricks. Correction pointers were applied to all
six drafts at this merge. The lesson is procedural and permanent: when
citing a caveat, cite its current face.

## Claims registered
FND-030 (MU, the provenance audit), FND-031 (NU, the downstream sweep),
ELEC-085 (XI, partial independence), ELEC-086 (OMICRON, full independence),
ELEC-087 (PI, the de-convolution), FND-032 (RHO, the mass-dependence
prediction), FND-033 (TAU, the fork audit and self-correction). Correction
annotations on EM-RECON-027 and EM-RECON-029. Parameter card collapsed to
the pinned band with verifier enforcement.

## What remains
Sigma is measured, not derived; FND-017's no-local-derivation no-go stands
and the question of *why* the vacuum stiffness takes this value is the
sector's open frontier. Named next-orders: the additivity stress-test
(FND-029's inter-strand E_x channel vs the 0.02% closure), the 160 MeV
width non-monotonicity, and the standing rule that any new physical-mass
lattice width determination be run through the XI machinery on arrival.
"""
open('docs/history/RELEASE_NOTES_v3.16.0.md','w').write(notes)
EOF
# bump version if versioned anywhere
grep -rn "3\.15\.0" pyproject.toml CITATION.cff 2>/dev/null | head -4