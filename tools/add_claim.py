#!/usr/bin/env python3
"""Safely append/insert a claim block into claims.yaml with GUARANTEED separation.

Motivation: manual regex insertions repeatedly produced jammed entries like
'...note."  - id: NEXT' (no newline), silently corrupting the YAML sequence
(caught only by a strict parse). This helper normalizes separation and strict-
parses before writing, so the corruption cannot be saved.

Usage (programmatic):
    from tools.add_claim import insert_after
    insert_after("PRIOR-ID", block_text)   # block_text is the full '  - id: ...' entry
"""
import re, sys, yaml

PATH = "claims.yaml"


def _normalize_separation(text):
    # ensure every '- id:' entry starts on its own line with a blank line before it
    text = re.sub(r'"[ \t]*-[ \t]+id:', '"\n\n  - id:', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def insert_after(prior_id, block, path=PATH):
    s = open(path).read()
    m = re.search(rf'(  - id: {re.escape(prior_id)}\n(?:.*\n)*?    note: "[^"]*"\n)', s)
    if not m:
        raise SystemExit(f"prior id {prior_id} not found")
    blk = block if block.startswith("\n") else "\n" + block
    if not blk.endswith("\n"):
        blk += "\n"
    new = s[:m.end()] + blk + s[m.end():]
    new = _normalize_separation(new)
    yaml.safe_load(new)  # strict parse BEFORE writing; raises on corruption
    open(path, "w").write(new)
    print(f"inserted after {prior_id}; strict YAML OK")


if __name__ == "__main__":
    print(__doc__)
