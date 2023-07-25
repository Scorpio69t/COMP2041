#!/usr/bin/env python3

import sys,re
largest = 0

maxLine = []
for line in sys.stdin:
    if m:= re.findall(r"(\d+)", line):
        if (int(max(m)) >= largest):
            if len(maxLine) != 0 and int(max(m)) > largest:
                del maxLine[0]
            largest = int(max(m))
            maxLine.append(line)

# print(maxLine)

for line in maxLine:
    print(line, end="")

