#!/usr/bin/env python3

import sys, re

regex = sys.argv[1]

with open(sys.argv[2]) as f:
    for line in f:
        if re.search(regex, line):
            print(line, end="")