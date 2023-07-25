#!/usr/bin/env python3

import sys

seen = {}
    
try:
    for line in sys.stdin:
        if line not in seen:
            seen[line] = 1
        else:
            seen[line] += 1
        for word in seen:
            if seen[word] >= int(sys.argv[1]):
                print(f"Snap: {word}", end="")
                sys.exit(0)
except EOFError:
    print("")
    sys.exit(0)
        