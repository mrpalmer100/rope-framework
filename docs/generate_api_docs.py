"""
docs/generate_api_docs.py  --  Generate browsable API docs from docstrings.

Run:  python docs/generate_api_docs.py
Writes one Markdown file per module under docs/api/, plus an index. Docs are
generated FROM the installed code's signatures and docstrings, so they cannot
drift from the implementation -- regenerating after any change keeps them honest.
"""
import inspect
import importlib
import os

MODULES = [
    ("rope_solver.psi.solver", "Poisson solver for the field psi"),
    ("rope_solver.topology.linking", "Linking number and link constructions"),
    ("rope_solver.geometry.curve", "Discrete-curve forces (rope tension)"),
    ("rope_solver.relaxation.relax", "Curve relaxation with topology tracking"),
    ("rope_solver.gravity", "Weak-field / PPN observables"),
    ("rope_solver.spectrum", "Fluctuation determinant"),
    ("rope_solver.particles", "Charge, coupling, mass machinery"),
    ("rope_solver.electromagnetism", "EM sector and cross-sector locks"),
    ("rope_solver.electromagnetism.photon", "Light: photon and birefringence"),
    ("rope_solver.open_problems", "Registry of what is NOT derived"),
    ("rope_solver.benchmark_catalogue", "Frozen benchmark numbering"),
]

HERE = os.path.dirname(os.path.abspath(__file__))
API = os.path.join(HERE, "api")


def public_functions(mod):
    return sorted(
        (n, o) for n, o in inspect.getmembers(mod, inspect.isfunction)
        if o.__module__ == mod.__name__ and not n.startswith("_")
    )


def render_module(modname, blurb):
    mod = importlib.import_module(modname)
    lines = [f"# `{modname}`", "", blurb, ""]
    moddoc = inspect.getdoc(mod)
    if moddoc:
        lines += ["> " + moddoc.split("\n")[0], ""]
    for name, fn in public_functions(mod):
        try:
            sig = str(inspect.signature(fn))
        except (ValueError, TypeError):
            sig = "(...)"
        doc = inspect.getdoc(fn) or "_(no docstring)_"
        lines += [f"## `{name}{sig}`", "", doc, ""]
    return "\n".join(lines)


def main():
    os.makedirs(API, exist_ok=True)
    index = ["# rope_solver API reference", "",
             "Auto-generated from docstrings. Regenerate with "
             "`python docs/generate_api_docs.py` after any change so the docs "
             "cannot drift from the code.", "",
             "| Module | Functions | Summary |", "|---|---|---|"]
    for modname, blurb in MODULES:
        mod = importlib.import_module(modname)
        fns = public_functions(mod)
        fname = modname.replace("rope_solver.", "").replace(".", "_") + ".md"
        with open(os.path.join(API, fname), "w") as f:
            f.write(render_module(modname, blurb))
        index.append(f"| [`{modname}`](api/{fname}) | {len(fns)} | {blurb} |")
    total = sum(len(public_functions(importlib.import_module(m))) for m, _ in MODULES)
    index += ["", f"**{total} public functions across {len(MODULES)} modules.**"]
    with open(os.path.join(HERE, "API.md"), "w") as f:
        f.write("\n".join(index))
    print(f"Generated docs for {total} functions across {len(MODULES)} modules.")
    print(f"  index: docs/API.md")
    print(f"  pages: docs/api/*.md")


if __name__ == "__main__":
    main()
