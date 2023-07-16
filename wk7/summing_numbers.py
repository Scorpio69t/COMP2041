#!/usr/bin/env python3

import re,sys
sum = 0
stream = open(sys.argv[1])
for line in stream:
    x = re.findall("[0-9]+", line, re.DOTALL)
    if x:
        for i in x:
            sum += int(i)

print(sum)
stream.close()