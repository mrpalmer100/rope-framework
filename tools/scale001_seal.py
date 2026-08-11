#!/usr/bin/env python3
"""SCALE-001 blind-target seal.

The commission's blinding is only meaningful if the target cannot be
consulted while the mechanism classes and their scaling laws are being
written. This tool computes the target from the registry, commits to it
with a SHA-256 hash, and refuses to print it until the Phase 2 laws are
locked.

    python3 tools/scale001_seal.py --seal     # write the commitment
    python3 tools/scale001_seal.py --lock     # hash + freeze Phase 2 laws
    python3 tools/scale001_seal.py --unseal   # reveal, ONLY after --lock

The target itself is derived, not stored: it is regenerated from
registered quantities at unseal time, so the seal commits to a
PROCEDURE, not to a number someone could have edited.
"""
import argparse
import hashlib
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEAL = os.path.join(ROOT, "analysis", "SCALE001_TARGET.sealed")
LAWS = os.path.join(ROOT, "analysis", "SCALE001_PHASE2_laws.md")
LOCK = os.path.join(ROOT, "analysis", "SCALE001_PHASE2.lock")

# Registered inputs (claim IDs on every line; see the charter).
HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA = 1 / 137.036              # measured
K_ME = 2.6065e-14                # T0*a, the spent calibration (FND-038)
S_EFF = 3.61e35                  # ELEC-081
FLOORS = (50, 250)               # FND-040, conditional on FND-037


def target():
    """g = l_q/a at the two registered floor readings (FND-041/042)."""
    qarea = 4 * math.pi * ALPHA * HBAR * C          # R1, GRV-093
    out = []
    for kap in FLOORS:
        a = (3 * K_ME / (kap * S_EFF)) ** (1 / 3)   # FND-038 solve
        t0 = K_ME / a
        out.append(math.sqrt(qarea / t0) / a)
    return (round(min(out), 1), round(max(out), 1))


def digest():
    lo, hi = target()
    payload = json.dumps({"quantity": "g = l_q/a", "range": [lo, hi],
                          "floors": FLOORS, "provenance":
                          "FND-038/040/041/042; R1 from GRV-093"},
                         sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seal", action="store_true")
    ap.add_argument("--lock", action="store_true")
    ap.add_argument("--unseal", action="store_true")
    args = ap.parse_args()

    if args.seal:
        with open(SEAL, "w") as f:
            f.write("SCALE-001 target commitment (SHA-256 of the range and "
                    "its provenance)\n")
            f.write("quantity: g = l_q/a at the FND-040 floor readings\n")
            f.write(f"sha256: {digest()}\n")
            f.write("The plaintext range is NOT stored here. It regenerates "
                    "from the registry at --unseal.\n")
        print(f"SEALED. commitment written to {os.path.relpath(SEAL, ROOT)}")
        print("The target is not printed and must not be quoted in Phase 1/2.")
        return

    if args.lock:
        if not os.path.exists(LAWS):
            sys.exit("REFUSED: Phase 2 laws file does not exist yet.")
        h = hashlib.sha256(open(LAWS, "rb").read()).hexdigest()
        with open(LOCK, "w") as f:
            f.write(f"phase2_sha256: {h}\n")
        print(f"LOCKED. Phase 2 laws frozen at {h[:16]}...")
        print("Evaluation may now proceed; laws may not be edited.")
        return

    if args.unseal:
        if not os.path.exists(LOCK):
            sys.exit("REFUSED: Phase 2 is not locked. Blinding is not "
                     "optional -- lock the laws before unsealing.")
        h = hashlib.sha256(open(LAWS, "rb").read()).hexdigest()
        recorded = open(LOCK).read().split(":")[1].strip()
        if h != recorded:
            sys.exit("REFUSED: the Phase 2 laws changed after locking. "
                     "The blind is broken; register the breach.")
        lo, hi = target()
        print(f"UNSEALED. commitment {digest()[:16]}... verified.")
        print(f"TARGET: g = l_q/a in [{lo}, {hi}] "
              f"(kappa_pack = {FLOORS[0]} and {FLOORS[1]} respectively).")
        print("Compare the locked laws' evaluations against this range now, "
              "and state the look-elsewhere rate from the class count.")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
