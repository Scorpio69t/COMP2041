#!/usr/bin/env python3
from operator import itemgetter
import sys

line_dict = {}
lines = 0
my_lines = []
with open(sys.argv[1]) as f:
    # my_lines = f.readlines()
    for line in f:
        my_lines.append(line)
        line_dict[lines] = len(line)
        lines += 1

line_dict = {val[0] : val[1] for val in sorted(line_dict.items(), key = lambda x: (x[1], x[0]))}

for line in line_dict.keys():
    print(my_lines[line], end="")