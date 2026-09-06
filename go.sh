#!/usr/bin/env bash
export PY=$HOME/rope-venv/bin/python
nohup ./run_local.sh "$1" > /dev/null 2>&1 &
echo "launched $1 -> logs/$(basename "$1" .py).log"
