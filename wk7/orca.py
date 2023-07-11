#!/usr/bin/env python3

import re 
import sys 
sum = 0
for filename in sys.argv[1:]:
    stream = open(filename)
    for line in stream:
        result = re.search("Orca", line, re.IGNORECASE)
        if result is not None:
            sum += int(line.split()[1])
            # print(line.split()[1])
    stream.close()

print(f"{sum} Orcas reported")
