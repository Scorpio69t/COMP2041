#!/usr/bin/env python3
import re, sys, glob
for file in sorted(glob.glob("lyrics/*.txt")):
    fileName = file.split("/")[1]
    fileName = fileName.split(".")[0]
    fileName = fileName.replace("_", " ")
    with open(file) as lyricFile:
        wordSum = 0
        totalSum = 0
        for line in lyricFile:
                m = re.split('[^a-zA-Z]', line)
                m = list(filter(None, m))
                m = [x.lower() for x in m]
                wordSum += m.count(sys.argv[1])
                totalSum += len(m)
    print(f"{wordSum:4}/{totalSum:6} = {wordSum/totalSum:.9f} {fileName}")