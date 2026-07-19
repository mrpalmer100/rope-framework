#!/usr/bin/env python3
"""
verify_corpus.py — one-command verification of the Rope Programme corpus.

Reads claims.yaml, runs every benchmark referenced by a claim, and reports,
claim by claim, whether its backing computation passes. Also checks that every
referenced paper and benchmark file actually exists in the package.

Usage:
    python tools/verify_corpus.py            # verify everything
    python tools/verify_corpus.py --quick    # existence checks only, no runs

Exit code 0 iff every referenced file exists and every referenced benchmark
passes. This is the executable backbone of the claim registry: it makes the
corpus's "reproducible" claim itself reproducible.
"""

# --- UTF-8 console shim (cross-platform; fixes Windows cp1252 crashes) ---
import sys as _sys
for _s in ("stdout", "stderr"):
    _stream = getattr(_sys, _s, None)
    _rc = getattr(_stream, "reconfigure", None)
    if callable(_rc):
        try:
            _rc(encoding="utf-8", errors="replace")
        except Exception:
            pass
# --- end shim ---
import os, sys, subprocess, argparse

# Strict YAML guard: catch structural corruption (e.g. jammed '..."  - id:' entries)
# that a regex scan would silently miss.
def _strict_yaml_guard(path="claims.yaml"):
    import yaml, sys
    try:
        yaml.safe_load(open(path))
    except Exception as e:
        print(f"STRICT YAML PARSE FAILED for {path}: {e}")
        sys.exit(1)



ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_claims():
    """Minimal YAML read (no PyYAML dependency): parse the claims list we need."""
    path = os.path.join(ROOT, "claims.yaml")
    claims, cur = [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("  - id:"):
            if cur: claims.append(cur)
            cur = {"id": line.split("id:",1)[1].strip()}
        elif cur is not None and line.startswith("    ") and ":" in line:
            k = line.strip().split(":",1)[0].strip()
            v = line.strip().split(":",1)[1].strip()
            if k in ("title","status","paper","benchmark","note"):
                cur[k] = None if v=="null" else v.strip('"')
    if cur: claims.append(cur)
    return claims

def run_benchmark(rel):
    """Run a benchmark script; return (ok, tail)."""
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return False, "MISSING FILE"
    env = dict(os.environ, PYTHONPATH=ROOT)
    try:
        r = subprocess.run([sys.executable, path], cwd=ROOT, env=env,
                           capture_output=True, text=True, timeout=300,
                           encoding="utf-8", errors="replace")
        tail = ((r.stdout or "").strip().splitlines() or ["(no output)"])[-1]
        return r.returncode==0, tail
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    except Exception as e:
        return False, f"ERROR {e}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="existence checks only")
    args = ap.parse_args()

    claims = load_claims()
    print(f"Rope Programme corpus verification — {len(claims)} claims\n"+"="*64)

    # 1. existence checks
    missing = []
    for c in claims:
        paper = c.get("paper")
        if paper:
            # papers may live in papers/, papers/_sources/, or docs/ (search all)
            cand = [os.path.join(ROOT,d,paper+".docx") for d in ("papers","papers/_sources","docs")]
            if not any(os.path.exists(p) for p in cand):
                missing.append(f"{c['id']}: missing paper {paper}.docx (searched papers/, papers/_sources/, docs/)")
        bm = c.get("benchmark")
        if bm and not os.path.exists(os.path.join(ROOT,bm)):
            missing.append(f"{c['id']}: missing benchmark {bm}")
    if missing:
        print("EXISTENCE FAILURES:")
        for m in missing: print("  ✗ "+m)
    else:
        print("All referenced papers and benchmarks exist. ✓")
    print("-"*64)

    if args.quick:
        return 1 if missing else 0

    # 2. run each distinct benchmark once, cache result
    cache = {}
    coded = [c for c in claims if c.get("benchmark")]
    uncoded = [c for c in claims if not c.get("benchmark")]
    print(f"Running benchmarks for {len(coded)} code-backed claims "
          f"({len(set(c['benchmark'] for c in coded))} distinct scripts)...\n")
    fails = 0
    for c in coded:
        bm = c["benchmark"]
        if bm not in cache:
            cache[bm] = run_benchmark(bm)
        ok, tail = cache[bm]
        mark = "✓" if ok else "✗"
        if not ok: fails += 1
        print(f"  {mark} [{c['id']}] {c.get('status','?'):13} {c['title'][:52]}")
        if not ok:
            print(f"       backing {bm} FAILED: {tail}")

    print("-"*64)
    print(f"Code-backed claims: {len(coded)}   passing: {len(coded)-fails}   failing: {fails}")
    print(f"Claims backed by paper only (no benchmark): {len(uncoded)} "
          "(status-labelled; not machine-verified here)")
    # status distribution
    from collections import Counter
    dist = Counter(c.get("status","?") for c in claims)
    print("Status distribution: "+", ".join(f"{k}={v}" for k,v in sorted(dist.items())))
    print("="*64)
    ok_all = (fails==0 and not missing)
    print("RESULT: "+("ALL CHECKS PASS ✓" if ok_all else "FAILURES PRESENT ✗"))
    return 0 if ok_all else 1

if __name__=="__main__":
    _strict_yaml_guard()
    sys.exit(main())
