#!/usr/bin/env python3

import sys

seen = set()

for arg in sys.argv[1:]:
    if arg not in seen:
        print(arg, end=" ")
        seen.add(arg)

print("")