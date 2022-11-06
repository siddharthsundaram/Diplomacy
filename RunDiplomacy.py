#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C)
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Diplomacy import diplomacy_solve

# ----
# main
# ----

if __name__ == "__main__":
    diplomacy_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
$ cat RunDiplomacy1.in
A Madrid Hold
B Barcelona Move Madrid
C London Move Barcelona
D Paris Support A
E Cairo Support A
F Austin Support B
G Amsterdam Move Oslo
H Oslo Move Amsterdam
I Moscow Support G
J Shanghai Support B
K Tokyo Move Shanghai
L Taipei Support J



$ python RunCollatz.py < RunCollatz.in > RunCollatz.out

$ cat RunDiplomacy1.out
A Madrid
B [dead]
C Barcelona
D Paris
E Cairo
F Austin
G Oslo
H Amsterdam
I Moscow
J Shanghai
K [dead]
L Taipei



$ python -m pydoc -w Collatz
# That creates the file Diplomacy.html
"""
