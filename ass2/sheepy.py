#!/usr/bin/env python3

import re, sys
"""
This function below changes all variables in shell script to python variables
"""
def variable_replace(line):
    if string := re.sub(r"\$(\w+)", r"{\1}", line):
        return string

#function splits line if it has a comment. 
def comment_split(line):
    return line.split('#')

#MAKE THIS A FUNCTION THAT CHANGES ECHO TO PRINT. NOTHING ELSE GIT
def echo_expand(line):
    #if line is an echo, print it
    if m := re.search("^echo\s+(.*)$", str(line)):
        line = line.replace(line, f"print(f\"{' '.join(m.group(1).split())}\")")
        print(line, end="")

def variable_assignment(line):
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

    print("#!/usr/bin/python3 -u")

    with open(sys.argv[1]) as f:
        next(f)
        for line in f:
            comment = None                              #Set comment to none for each line, so that comment does not carry on to next line.
            variable_assignment(line)   
            line = variable_replace(line)               # Basic functions that assign variables and replace

            if re.search("#", line):
                comment = comment_split(line)[1]        #If comment exists, comment becomes the comment string.

            line = comment_split(line)[0]               #At this point, line does not include the comment
            echo_expand(line)                       #Print the line. Print comment aswell if it exists, else a newline.

            if comment:
                print(f" #{comment}")
            else:
                print("")
if __name__ == "__main__":
    main()

