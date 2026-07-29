#!/usr/bin/env python3
"""QGATE-002: the corpus-wide quantum-input ledger (Part-1 audit).

Classifies every claim that touches a quantum marker (hbar, electron mass, zero-point,
tunneling, quantum phase, Born, 13.6 eV) into seven categories:

  IMPORT   direct import: a quantum quantity is an explicit input
  CALIB    calibration proxy: a measured value (13.6 eV) indirectly fixes a quantum combination
  FORM     form-only: the marker appears but cancels from / does not carry the structural result
           (includes the QB boundary-characterization rungs: quantum-SHAPED bounds derived
           classically)
  NUMER    numerical dependence: the absolute prediction changes with hbar
  FENCE    fence marker: the claim stops precisely because the missing term is quantum
  CLASS    previously quantum, now classicalized: an hbar-dependent reading was eliminated and a
           geometric version survived (the lambda-saga category)
  MENTION  incidental mention: no dependence at all

Method: rule-based defaults + a curated override table with justifications, ALL printed --
the classification is auditable line by line. QGATE-001 sharpening: IMPORT/CALIB/NUMER entries
are additionally tagged smooth-sector (subject to the no-go) or reconnection-attachable.
"""
import yaml, re, json
from collections import Counter, defaultdict

MARKERS = {
    'hbar': r'\bhbar\b|ħ|planck', 'e_mass': r'electron mass|lepton mass|1836|m_e\b',
    'zp': r'zero-point|zero point', 'tunnel': r'tunnel',
    'qphase': r'quantum phase|wavefunction|schrodinger|schrödinger',
    'born': r'born rule|probability amplitud', 'ryd': r'13\.6|rydberg',
    'q': r'\bquantum\b',
}

# Curated overrides: id -> (category, justification quoted from/grounded in the claim text)
OVERRIDE = {
    # THE CLASSICALIZED FAMILY (the lambda saga and the matter sector's "zero-point" vocabulary,
    # which FND-MATTER-034 resolved into classical jitter under reading C)
    'FND-MATTER-033': ('CLASS', "the kill itself: quantum reading of lambda forces a~200fm vs 0.1fm bound; eliminated"),
    'FND-MATTER-034': ('CLASS', "the surviving classical-amplitude reading; hbar exits the ledger"),
    'FND-MATTER-029': ('CLASS', "lambda gate anatomy; superseded by 033/034 classicalization"),
    'FND-MATTER-038': ('CLASS', "Lambda computed by percolation; no quantum input remains"),
    'FND-MATTER-008': ('CLASS', "'zero-point mass term' = classical ground-state geometric cost (via 034)"),
    'FND-MATTER-009': ('CLASS', "two-term model's zero-point = classical ledger constant"),
    'FND-MATTER-010': ('CLASS', "crossing spectroscopy of the classical ledger"),
    'FND-MATTER-011': ('CLASS', "bend spectroscopy, classical"), 'FND-MATTER-013': ('CLASS', "bend law closed classically"),
    'FND-MATTER-014': ('CLASS', "zero-point cost derived classically"), 'FND-MATTER-016': ('CLASS', "kc dissolved; constraint not spring"),
    'FND-MATTER-018': ('CLASS', "calibrated mapping, classical"), 'FND-MATTER-019': ('CLASS', "certified spectrum under classical ledger"),
    'FND-MATTER-007': ('CLASS', "first spectrum; zero-point vocabulary later classicalized"),
    # DIRECT IMPORTS
    'PM-005': ('IMPORT', "electron mass registered as INPUT; scope statement says so explicitly"),
    'CHEM-STRUCT-001': ('IMPORT', "2n^2 = n^2 modes x TWO SPIN STATES: spin degeneracy imported alongside the 13.6 calibration"),
    # CALIBRATION PROXIES (the 13.6 eV -> xi chain; hides an hbar-bearing combination)
    'EM-RECON-010': ('CALIB', "coupling calibrated on hydrogen 13.6 eV; H2 vibration then predicted to 16%"),
    'EM-RECON-006': ('CALIB', "13.6 eV enters the EM-reconstruction calibration"),
    'CHEM-HB-005': ('CALIB', "chemistry inherits the 13.6-calibrated coupling"),
    'CHEM-HB-006': ('CALIB', "same inherited calibration"),
    'NUC-005': ('CALIB', "one calibrated nuclear constant; quantum kinetic residue acknowledged"),
    # NUMERICAL DEPENDENCE (absolute normalizations that move with hbar)
    'GRV-007': ('NUMER', "Sakharov-type induced G: absolute strength needs the action normalization"),
    'GRV-021': ('NUMER', "finite zero-point from measured band (self-regulated UV) but absolute coefficient tracks the action scale"),
    'GRV-005': ('NUMER', "mass-knot zero-point premise; absolute value action-normalized"),
    'GRV-004': ('NUMER', "zero-point theorem's absolute scale"),
    # FENCES (stop precisely at the quantum term)
    'FND-MATTER-001': ('FENCE', "atomic size blocked pending wavelength/scale inputs"),
    'FND-MATTER-003': ('FENCE', "atomic-scale derivation BLOCKED: two inputs missing"),
    'FND-MATTER-005': ('FENCE', "mesh scale a IRREDUCIBLE: the named fundamental input"),
    'PM-004': ('FENCE', "lepton spectrum does NOT fall out without the quantum layer; Failed and kept"),
    'PM-002': ('FENCE', "lepton ratios attempt; Failed"), 'PM-001': ('FENCE', "lepton conjecture awaiting quantum layer"),
    'PM-003': ('FENCE', "mass-structure scope; absolute spectrum fenced"),
    'QB-003': ('FENCE', "counting form cannot reproduce entanglement; Failed and kept"),
    'QB-005': ('FENCE', "Born |c|^2 partial (symmetric case); timing-universality open"),
    'QB-006': ('FENCE', "QB reframing; the boundary named"), 'QB-007': ('FENCE', "measurement decomposition; conditional"),
    'CHEM-MET-001': ('FENCE', "metallic bonding absent pending delocalized/quantum layer"),
    'EM-RECON-015': ('FENCE', "vacuum tension open, flagged"), 'EM-RECON-016': ('FENCE', "birefringence discriminator confronts quantum prediction"),
    'FND-BOUND-001': ('FENCE', "the one fence: registry-consistency boundary statement"),
    'GRV-012': ('FENCE', "standing adverse verdict; quantum-completion among named outs"),
    'GRV-014': ('FENCE', "quantum-completion hypothesis, audited and admitted as conjecture"),
    'EM-RECON-009': ('FENCE', "extensibility coefficient identified; quantum-scale residue"),
}
# rule defaults by family for the rest
def default_cat(cid, status, text):
    if cid.startswith(('QB-01', 'QB-02')):
        return ('FORM', "boundary characterization: quantum-shaped bound derived classically")
    if cid.startswith('GRV-03') or cid.startswith('GRV-04'):
        return ('FORM', "Hawking/horizon chain: shape derived classically; hbar only converts units")
    if status in ('Failed', 'Open'):
        return ('FENCE', "stops at a quantum-flavored boundary (default rule)")
    return ('MENTION', "incidental vocabulary; no dependence (default rule)")

# QGATE-001 sharpening: which genuine dependencies are reconnection-attachable?
RECON_ATTACH = {'GRV-007', 'GRV-021', 'GRV-005', 'GRV-004', 'NUC-005'}  # action-normalization residues
SMOOTH = {'PM-005', 'CHEM-STRUCT-001', 'EM-RECON-010', 'EM-RECON-006', 'CHEM-HB-005', 'CHEM-HB-006'}

def run(verbose=True):
    d = yaml.safe_load(open('claims.yaml'))
    claims = d['claims'] if isinstance(d, dict) and 'claims' in d else d
    ledger = {}
    for c in claims:
        t = (c['title'] + ' ' + str(c.get('note', ''))).lower()
        ms = [k for k, p in MARKERS.items() if re.search(p, t)]
        if not ms or c['id'] in ('QGATE-001', 'QGATE-002', 'THM-006'):
            continue
        cat, why = OVERRIDE.get(c['id']) or default_cat(c['id'], c['status'], t)
        branch = ""
        if cat in ('IMPORT', 'CALIB', 'NUMER'):
            branch = "reconnection-attachable" if c['id'] in RECON_ATTACH else "smooth-sector"
        ledger[c['id']] = dict(status=c['status'], markers=ms, cat=cat, why=why, branch=branch)
    counts = Counter(v['cat'] for v in ledger.values())
    if verbose:
        print(f"=== QUANTUM-INPUT LEDGER: {len(ledger)} marker-touching claims classified ===\n")
        for cat in ('IMPORT', 'CALIB', 'NUMER', 'FENCE', 'CLASS', 'FORM', 'MENTION'):
            members = [(k, v) for k, v in sorted(ledger.items()) if v['cat'] == cat]
            print(f"--- {cat} ({len(members)}) ---")
            for k, v in members:
                b = f"  [{v['branch']}]" if v['branch'] else ""
                print(f"  {k:18s} {v['status']:14s}{b}  {v['why'][:78]}")
            print()
        genuine = [k for k, v in ledger.items() if v['cat'] in ('IMPORT', 'CALIB', 'NUMER')]
        print(f"=== THE DEPENDENCY SURFACE ===")
        print(f"claims with GENUINE quantum dependence (import+calib+numerical): {len(genuine)}")
        print(f"distinct underlying INPUTS they trace to: electron mass (PM-005), spin degeneracy")
        print(f"(CHEM-STRUCT-001), the 13.6 eV coupling calibration (EM-RECON chain), and the")
        print(f"action normalization of induced gravity (GRV Sakharov chain) -- FOUR.")
        print(f"\nfences: {counts['FENCE']}  classicalized: {counts['CLASS']}  form-only: {counts['FORM']}  incidental: {counts['MENTION']}")
    json.dump(ledger, open('docs/quantum_ledger.json', 'w'), indent=1)
    return ledger, counts

if __name__ == "__main__":
    run()
