#!/usr/bin/env python3

import sys

vowels = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']
word_to_print = []
for arg in sys.argv[1:]:
    count = 0
    for letter in arg:
        if letter in vowels:
            count += 1
        else :
            count = 0
        if count >= 3:
            word_to_print.append(arg)
            break
print(" ".join(word_to_print))