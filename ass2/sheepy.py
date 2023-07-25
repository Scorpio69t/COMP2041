#!/usr/bin/env python3

import re, sys
"""
This function below changes all variables in shell script to python variables
"""
def variable_replace(line):
    if string := re.sub(r"\$(\w+)", r"{\1}", line):
        return string
#functino splits line if comment. 
def comment_split(line):
    line.split('#')
#MAKE THIS A FUNCTION THAT CHANGES ECHO TO PRINT. NOTHING ELSE GIT
def shell_interpret(line):
    #If line is an echo including variables
    #if line is an echo
    if m := re.search("^echo\s+(.*)$", line):
        print(m.group(1))
        line = line.replace("echo ", f"print(f\"{' '.join(m.group(1).split())}\")")
        print(line)
        # print("print(f\"", end="")
        # print(" ".join(m.group(1).split()), end="")
        # print("\")")
    #If line is a variable
    if m:= re.search("(\w+)=(.*)", line):
        print(f"{m.group(1)} = \"{m.group(2)}\"")

def main():
    shell = []

    with open(sys.argv[1]) as f:
        for line in f:
            shell.append(line)

    # print(shell)

    #########
    #   if keywords realting to modules are in shell list, print import line.
    #########

    print("#!/usr/bin/python3 -u\n")

    with open(sys.argv[1]) as f:
        for line in f:
            line = variable_replace(line)
            shell_interpret(line)


if __name__ == "__main__":
    main()

'''
for x in "$list"
'''