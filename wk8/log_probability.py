#!/usr/bin/env python3
import re, sys, glob, math
for file in sorted(glob.glob("lyrics/*.txt")):
    log_prob = 0
    word_count = {}  
    fileName = file.split("/")[1]
    fileName = fileName.split(".")[0]
    fileName = fileName.replace("_", " ")
    with open(file) as lyricFile:
        totalSum = 0
        for line in lyricFile:
                m = re.split('[^a-zA-Z]', line)
                m = list(filter(None, m))
                m = [x.lower() for x in m]
                totalSum += len(m)
                loop = list(set(sys.argv[1:]))
                # print(loop)
                for argv in loop:
                    if argv in m:   
                        if argv not in word_count:
                            word_count[argv] =  m.count(argv)
                        else:              
                            word_count[argv] += m.count(argv)
    for argv in sys.argv[1:]:
         if argv not in word_count:
              word_count[argv] = 0
    # print(f"{file}:{word_count} {totalSum}")
    for word in sys.argv[1:]:
        # print((word_prob+1)/totalSum)
        log_prob += math.log((word_count[word]+1)/totalSum)
        # print(f"{word}: {word_prob/totalSum}")
    
    print(f"{log_prob:10.5f} {fileName}")