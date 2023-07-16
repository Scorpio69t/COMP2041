#!/usr/bin/env python3

import sys

f = open(sys.argv[2])
lines = f.readlines()

try:
    print(lines[int(sys.argv[1]) - 1], end="")
except IndexError:
    print("", end ="")