#!/usr/bin/python3 -u

import glob, subprocess


for file in sorted(glob.glob('*')):

    subprocess.run([f"head", f"-1", f"{file}"])
    subprocess.run([f"tail", f"-1", f"{file}"])
