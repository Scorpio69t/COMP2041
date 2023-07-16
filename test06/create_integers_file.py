#!/usr/bin/env python3

import sys

f = open(sys.argv[3], "w")

i = int(sys.argv[1])

while i <= int(sys.argv[2]):
    f.write(f"{str(i)}\n")
    i += 1