"""
validation/run_physics_validation.py  --  Physics + EM regression heartbeat.

Runs the physics-endpoint regression suite AND the electromagnetism regression
+ cross-sector consistency suite. Exits non-zero if any test fails.
"""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
suites = [os.path.join(root, "tests", "test_physics.py"),
          os.path.join(root, "tests", "test_electromagnetism.py")]
total_pass = total = 0
fail = False
for s in suites:
    r = subprocess.run([sys.executable, s], capture_output=True, text=True)
    print(r.stdout, end="")
    if r.returncode != 0:
        fail = True
    # parse "RESULT: x/y"
    for line in r.stdout.splitlines():
        if line.startswith("RESULT:"):
            frac = line.split(":")[1].strip().split()[0]  # "12/12"
            x, y = frac.split("/")
            total_pass += int(x); total += int(y)
print("="*64)
print(f"COMBINED PHYSICS+EM: {total_pass}/{total} tests passed")
print("="*64)
sys.exit(1 if fail else 0)
