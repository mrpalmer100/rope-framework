# ============================================================================
# The Rope Programme — corpus verification Makefile
# ----------------------------------------------------------------------------
# One-command evaluation of the whole reproducible corpus.
#
#   make verify     run the full claim-registry verification (papers + benchmarks)
#   make test       run the test suite (pytest) + validation runners
#   make reproduce  reproduce every published benchmark number
#   make graph      regenerate the claim dependency graph (DOT + ASCII)
#   make heartbeat  the three core validation runs (fast green check)
#   make all        graph + verify + test + reproduce
# ============================================================================

PY := python3
export PYTHONPATH := $(CURDIR)

.PHONY: all verify test reproduce graph roadmap overview heartbeat clean

all: graph roadmap overview verify test reproduce

verify:
	@echo "== Corpus claim verification =="
	@$(PY) tools/verify_corpus.py

graph:
	@echo "== Dependency graph =="
	@$(PY) tools/build_depgraph.py

roadmap:
	@echo "== Computed sector roadmap =="
	@$(PY) tools/build_roadmap.py

overview:
	@echo "== Programme overview =="
	@$(PY) tools/build_overview.py

heartbeat:
	@echo "== Heartbeat (core validation) =="
	@$(PY) validation/run_physics_validation.py
	@$(PY) validation/run_validation.py
	@$(PY) benchmarks/reproduce_results.py

reproduce:
	@echo "== Reproduce published benchmark numbers =="
	@$(PY) benchmarks/reproduce_results.py
	@$(PY) benchmarks/micromech/gamma_convergence.py
	@$(PY) benchmarks/micromech/coarse_graining_stiffness.py
	@$(PY) benchmarks/micromech/parameter_count.py

test:
	@echo "== Test suite =="
	@$(PY) -m pytest -q tests/ || $(PY) tests/test_physics.py
	@$(PY) validation/run_physics_validation.py

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@echo "cleaned."
