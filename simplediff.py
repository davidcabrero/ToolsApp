#!/usr/bin/env python3

from difflib import Differ
from pprint import pprint

text1 = input("Introduce texto 1: ").splitlines(keepends=True)

text2 = input("Introduce texto 2: ").splitlines(keepends=True)

diff = Differ()
differences = diff.compare(text1, text2)
pprint(list(differences))
