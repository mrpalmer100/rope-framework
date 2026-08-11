#!/usr/bin/env python3
"""COMMISSION PE -- the label-blindness audit's computable core.

Bars: analysis/PE_label_blindness_bars_LOCKED.md.
The question the sweep exists to answer: does GRANT-N2's label index
MULTIPLY any registered count? The naive "no derivation mentions labels"
argument is tested, not assumed.
"""
import math

N_LABELS = 3          # the SU(3)-anchored reading; the audit is N-general
print("GRANT-N2 adds an internal index of multiplicity N to every strand.")
print("A degree of freedom that can be EXCITED multiplies every count over")
print("strand states. The grant explicitly makes labels DYNAMICAL (exchange")
print("with an energy V -- that is a coupling, not a passive tag).\n")

print("MULTIPLICATION TEST -- registered counts that carry a strand index:")
rows = [
    ("photon polarizations (EM-RECON-022/023/025)", 2, "2N",
     "PDG: exactly 2. At N=%d the label-multiplied count is %d."
     % (N_LABELS, 2 * N_LABELS)),
    ("vacuum zero-point mode sum (GRV-004, FND-MATTER-014)", 1, "N",
     "Sigma_vac and the fence scale linearly with mode multiplicity."),
    ("horizon entropy microstate count (GRV-034..039)", 1, "N per strand",
     "S gains A/a^2 * ln N; the area law's COEFFICIENT shifts."),
    ("tube strand count n = 152-156 (ELEC-052/081, FND-030)", 1, "n or nN",
     "measured by lattice profile; the identification of 'strand' with"
     " 'labeled strand' decides whether Sigma_eff rescales by N."),
]
for name, base, mult, note in rows:
    print(f"  - {name}\n      registered count: {base} -> label-multiplied: {mult}\n      {note}")

print("\nTHE DECISIVE ONE, computed:")
print(f"  EM-RECON-022/023 killed the screw/torsion light candidate ON STATE")
print(f"  COUNT (one polarization vs the photon's two, kill class 4). The")
print(f"  same instrument turned on the SURVIVING carrier under GRANT-N2:")
print(f"  the collective transverse Goldstone pair carries a strand index,")
print(f"  so its state count is 2N = {2*N_LABELS} at N={N_LABELS}, against a measured 2.")
print(f"  BY THE CORPUS'S OWN KILL CRITERION, APPLIED SYMMETRICALLY, that is")
print(f"  a kill -- UNLESS label excitations are GAPPED out of the photon's")
print(f"  spectrum.")

print("\nTHE ESCAPE, and its price:")
gap_needed_eV = 1e6   # order: label modes must sit above accessible photon energies
print("  Labels must be a GAPPED internal sector: exchangeable between")
print("  tubes (the grant's purpose) but not excitable as propagating")
print("  modes at optical/gamma energies (the photon count's requirement).")
print("  That gap is a NEW SCALE. It is not registered. It is not derived.")
print("  Nothing in GRANT-N2 as adopted supplies it.")
print("\n  Consistency direction (stated, not derived): a confinement-like")
print("  gap on the label sector is exactly what gauge theory has (colour")
print("  is non-excitable in asymptotic states) -- so the escape is")
print("  physically standard and ontologically UNPAID here.")
