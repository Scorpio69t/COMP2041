#!/usr/bin/env python3

import sys

outpute = open(sys.argv[2], "w")
for line in reversed(list(open(sys.argv[1]))):
    outpute.write(f"{line.rstrip()}\n")
