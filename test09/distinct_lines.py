#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
total_lines = []
unique_lines = set()
for line in sys.stdin:
    line = " ".join(line.lower().split())
    total_lines.append(line)
    unique_lines.add(line)
    if len(unique_lines) >= n:
        print(f"{n} distinct lines seen after {len(total_lines)} lines read.")
        sys.exit(0)
print(f"End of input reached after {len(total_lines)} lines read - {n} different lines not seen.")