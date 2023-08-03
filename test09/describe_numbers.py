#!/usr/bin/env python3

import sys, statistics, numpy

nubmers = sys.argv[1:]
nubmers = [eval(i) for i in nubmers]
print(f"count={len(nubmers)}")
uniq = len(set(nubmers))
minimum = min(nubmers)
maxaimum = max(nubmers)

mean = statistics.mean(nubmers)
median = statistics.median(nubmers)
mode = statistics.mode(nubmers)
total = sum(nubmers)
product = numpy.prod(nubmers)
print(f"unique={uniq}")
print(f"minimum={minimum}")
print(f"maximum={maxaimum}")
print(f"mean={mean}")
print(f"median={median}")
print(f"mode={mode}")
print(f"sum={total}")
print(f"product={product}")

