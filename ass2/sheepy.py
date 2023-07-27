#!/usr/bin/env python3

import re, sys

################################################################################################################################################################
#        
#
#                       INDENTING MAY BE AN ISSUE: TUT RECOMMENED HAVING A VARIABLE TO KEEP TRACK OF INDENT.
#                       HOWEVER, IT ALSO WORKS IF I ONLY REPLACE KEYWORDS, AND HENCE KEEP THE INDENT FROM THE SHELL SCRIPT.
#
#
################################################################################################################################################################
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
    if m := re.search("echo\s+(.*)$", line):
        line = re.sub("echo\s+(.*)$", f"print(f\"{' '.join(m.group(1).split())}\")", line)
        # line = line.replace(line, f"print(f\"{' '.join(m.group(1).split())}\")")
    return line

def variable_assignment(line):
    #If line is a variable
    if m:= re.sub(r"(\w+)=(.*)", r'\1 = "\2"', line):
        return m
#function replaces glob adds {} around it if it starts with echo
def echo_glob(line):
    if m:= re.sub("(echo.*)(' '.join.*)", r"\1{\2}", line):
        return m

def sys_exit(line):
    if m:= re.sub(r"exit ?(\d)?", r"sys.exit(\1)", line):
        return m

# Expands glob.
def glob_expand(line):
    if m:= re.sub(r"([\*\?\[\]].*[\*\?\.\[\]]?)", r"' '.join(sorted(glob.glob('\1')))", line):
        return m

def for_expand(line):
    if m := re.search("^for (.*) in (.*)$", line):
        if re.search("glob.glob", m.group(2)):                               # If for loop contains glob, change glob so it is loopable.
            line = re.sub("' '.join\((.*)\)", r"\1:", line)
        else:
            line = re.sub("in (.*)$", f"in {m.group(2).split()}:", line)
    return line

def indent_counter(line, indent):
    if re.search("^do$", line):
        indent += 1
    if re.search("^done$", line):
        indent = indent - 1
    return indent

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

    #Based on the shell list, if any keywords relating to an import exists, add that import to the to_import set
    for line in shell:
        for import_chars in imports.values():
             if any(ele in line for ele in import_chars):
                to_import.add(dict_key_from_value(imports, import_chars))


    print("#!/usr/bin/python3 -u\n")
    #If there are imports, print the imports out
    if len(to_import) != 0:
        print(f"import {', '.join(to_import)}")
    
    indent = 0

    with open(sys.argv[1]) as f:
        next(f)                                         #Skips first line to avoid #!/bin/dash
        for line in f:
            
            comment = None                              #Set comment to none for each line, so that comment does not carry on to next line.
            if re.search("#", line):
                if re.search("^\s?#", line):
                    print(line)
                    continue
                comment = comment_split(line)[1]        #If comment exists, comment becomes the comment string.
            line = comment_split(line)[0]               #At this point, line does not include the comment
            indent = indent_counter(line, indent)       # Get the number of indentends needed.
            if re.search("^do$", line):
                continue
            if re.search("^done$", line):               # if the line is a keywords ('do','done'), skip the line since we won't need to print it
                continue
            # print(f"The indent in this line is {indent}")
            # i = 0
            # while (i < indent):
            #     print("\t", end="")                     #print the indents
            #     i += 1
            line = sys_exit(line)                         # converts exit into sys.exit

            line = glob_expand(line)                    #All glob characters are expanded

            if not re.search("glob", line):
                line = variable_assignment(line)            # variables are assigned, only if line does not contain a glob. Eg a=5 is now a = '5'

            line = for_expand(line)

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

