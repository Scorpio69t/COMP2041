#!/usr/bin/env python3

import re, sys
pod = {}
count = {}
for filename in sys.argv[1:]:
    stream = open(filename)
    for line in stream:
        Whale_name = line.split()[2:]
        Whale_name = " ".join(Whale_name)
        Whale_name = Whale_name.lower()
        Whale_name = Whale_name.rstrip('sS')
        Whale_name = Whale_name.strip()
        if Whale_name not in pod:
            count[Whale_name] = int(line.split()[1])
            pod[Whale_name] = 1
        else:
            count[Whale_name] += int(line.split()[1])
            pod[Whale_name] += 1
# print(count)
# print(pod)
sortedCount = sorted(count.items())
sortedPod = sorted(pod.items())


for whale,pod in zip(sortedCount,sortedPod):
    print(f"{whale[0]} observations: {pod[1]} pods, {whale[1]} individuals")
