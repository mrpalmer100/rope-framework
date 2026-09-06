"""Q54 stage 1 -- the fourth cell (charter:
analysis/Q54_charter_LOCKED.md; v-bars A and B passed on record).
run_q(4, 5, 144, 36) VERBATIM: level-1 seed, sub-pin ladder,
waypoints, rates. Resumable; rerun until the rates print. Durable
export of the q5/4 block to analysis/q54_stage1_ckpt.pkl once
members exist."""
import sys, pathlib, pickle

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1     # noqa

ROOT = pathlib.Path(__file__).resolve().parents[2]
DUR = ROOT / 'analysis' / 'q54_stage1_ckpt.pkl'


def main():
    st = q1.load()
    q1.run_q(st, 4, 5, 144, 36, 'q5/4')
    q = st.get('q5/4', {})
    if q.get('members'):
        DUR.write_bytes(pickle.dumps(q))
        print(f"[q54] durable export: {len(q['members'])} member(s), "
              f"rates_lo {len(q.get('rates_lo', []))} rates_hi "
              f"{len(q.get('rates_hi', []))}", flush=True)


if __name__ == '__main__':
    main()
