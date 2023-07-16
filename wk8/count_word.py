#!/usr/bin/env python3

import re,sys
sum = 0
for line in sys.stdin:
    m = re.split('[^a-zA-Z]', line)
    m = list(filter(None, m))
    m = [x.lower() for x in m]
    sum += m.count(sys.argv[1])

print(sum)