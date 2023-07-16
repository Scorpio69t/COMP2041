#!/usr/bin/env python3

import re,sys
sum = 0
for line in sys.stdin:
    m = re.split('[^a-zA-Z]', line)
    m = list(filter(None, m))
    sum += len(m)

print(f"{sum} words")