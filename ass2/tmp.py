#!/usr/bin/python3 -u

import glob


print(f"hello world") # This is also a comment

print(f"{' '.join(sorted(glob.glob('*')))}")


C_files=' '.join(sorted(glob.glob('*.[ch]')))

print(f"{C_files}")


print(f"all of the single letter Python files are: {' '.join(sorted(glob.glob('?.py')))}")
