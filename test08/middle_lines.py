#!/usr/bin/env python3

import sys

line_count = 0
with open(sys.argv[1]) as f:
    for line in f:
        line_count +=1
if line_count == 0:
    sys.exit(0)

line_to_print = int(line_count/2)

if line_count % 2 == 1:
    line_to_print += 1

with open(sys.argv[1]) as f:
    lines = f.readlines()
    if line_count % 2 == 1:
        print(lines[line_to_print - 1], end ="")
    else:
        print(lines[line_to_print - 1], end ="")
        print(lines[line_to_print], end ="")