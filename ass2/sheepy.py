#!/usr/bin/env python3

import re, sys

def shell_interpret(line):
    if m := re.search("^echo\s+(.*)$", line):
        print("print(\"", end="")
        print(" ".join(m.group(1).split()), end="")
        print("\")")

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
            shell_interpret(line)


if __name__ == "__main__":
    main()