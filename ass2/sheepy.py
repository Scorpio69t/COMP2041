#!/usr/bin/env python3

import re, sys

# This function below changes all variables in shell script to python variables

def variable_replace(line):
    if string := re.sub(r"\$(\w+)", r"{\1}", line):
        return string
    
#function splits line if it has a comment. 
def comment_split(line):
    return line.split('#')

#Functions converts echo statement to printf statements
def echo_expand(line):
    #if line is an echo, print it
    if m := re.search("^echo\s+(.*)$", line):
        line = line.replace(line, f"print(f\"{' '.join(m.group(1).split())}\")")
    return line

def variable_assignment(line):
    #If line is a variable
    if m:= re.sub(r"(\w+)=(.*)", r'\1 = "\2"', line):
        return m
#function replaces glob adds {} around it if it starts with echo
def echo_glob(line):
    if m:= re.sub("^(echo.*)(' '.join.*)", r"\1{\2}", line):
        return m

def sys_exit(line):
    if m:= re.sub(r"exit ?(\d)?", r"sys.exit(\1)", line):
        return m

# Expands glob.
########################################## ########################################## 
#       REGEX PATTERN IS WRONG. NEED TO ACCOUNT FOR DEALING WITH SINGLE GLOB CAHRACTER
#       EG: echo *
########################################## ##########################################
def glob_expand(line):
    if m:= re.sub(r"([\*\?\[\]].*[\*\?\.\[\]]?)", r"' '.join(sorted(glob.glob('\1')))", line):
        return m

def dict_key_from_value(d, v):
    for (key,value) in d.items():
        if value == v:
            return key

def main():
    shell = []
    imports = {'glob' : ['?', '*', '[', ']'], 'sys' : ['exit']} 
    to_import = set()
    with open(sys.argv[1]) as f:
        for line in f:
            line = comment_split(line)[0]
            shell.append(line)

    for line in shell:
        for import_chars in imports.values():
             if any(ele in line for ele in import_chars):
                to_import.add(dict_key_from_value(imports, import_chars))
    #########
    #   if keywords realting to modules are in shell list, print import line.
    #########

    print("#!/usr/bin/python3 -u\n")
    print(f"import {', '.join(to_import)}")
    with open(sys.argv[1]) as f:
        next(f)
        for line in f:
            comment = None                              #Set comment to none for each line, so that comment does not carry on to next line.
            if re.search("#", line):
                if re.search("^\s?#", line):
                    print(line)
                    continue
                comment = comment_split(line)[1]        #If comment exists, comment becomes the comment string.

            line = comment_split(line)[0]               #At this point, line does not include the comment

            line = sys_exit(line)

            line = glob_expand(line)                    #All glob characters are expanded

            if not re.search("glob", line):
                line = variable_assignment(line)            # variables are assigned, only if line does not contain a glob. Eg a=5 is now a = '5'

            line = variable_replace(line)               # all variables are replaced. eg: $a is now {a}
        
            line = echo_glob(line)                      #echo statements that have glob, adds {} around glob so it can be printed.
        
            line = echo_expand(line)                    #Echo lines are replaced with print stateemnts w fstrings
            print(line, end="")                 #Print the final line 
            if (line == ""):
                continue 
            if comment:
                print(f" #{comment}")
            else:
                print("")
if __name__ == "__main__":
    main()

