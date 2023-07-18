#!/usr/bin/env python3
import sys, glob, re, math
def log_prob(word, my_dict):
    for file in sorted(glob.glob("lyrics/*.txt")):
        log_prob = 0
        fileName = file.split("/")[1]
        fileName = fileName.split(".")[0]
        fileName = fileName.replace("_", " ")
        with open(file) as lyricFile:
            totalSum = 0
            wordSum = 0
            for line in lyricFile:
                    m = re.split('[^a-zA-Z]', line)
                    m = list(filter(None, m))
                    m = [x.lower() for x in m]
                    totalSum += len(m)
                    wordSum += m.count(word)

        log_prob += math.log((wordSum+1)/totalSum)
        my_dict[fileName] += log_prob
    return my_dict


def main(): 
    #make a dict of dict { 'Adele' : {truth: '23', word2:'32'}, 'darren' : {word1}}
    # loop through words in song?.txt
    # for everyword, calculate frequency. If truth appeared 3 times, frequency = 3/23
    # 
    d={}
    for file in sorted(glob.glob("lyrics/*.txt")):
        fileName = file.split("/")[1]
        fileName = fileName.split(".")[0]
        fileName = fileName.replace("_", " ")
        d[fileName] = {}
        with open(file) as lyricFile:
            wordSum = 0 
            for line in lyricFile:
                m = re.split('[^a-zA-Z]', line)
                m = list(filter(None, m))
                m = [x.lower() for x in m]
    # print(log_prob)

if __name__ == "__main__":
    main()

# for file in sys.argv[1:]:
#     with open(file) as f:
#         for word in f.read().split():
#             for knownFile in sorted(glob.glob("lyrics/*.txt")):
#                 log_prob = 0
#                 word_count = {}  
#                 fileName = file.split("/")[1]
#                 fileName = fileName.split(".")[0]
#                 fileName = fileName.replace("_", " ")
#                 with open(file) as lyricFile:
#                     totalSum = 0
#                     for line in lyricFile:
#                         m = re.split('[^a-zA-Z]', line)
#                         m = list(filter(None, m))
#                         m = [x.lower() for x in m]
#                         totalSum += len(m)
#                         if word in m: