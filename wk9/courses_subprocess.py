#!/usr/bin/env python3

import re,sys, subprocess, pprint

url = f"http://www.timetable.unsw.edu.au/2023/{sys.argv[1]}KENS.html"
course_code = []
course_name = []
courses = {}
p = subprocess.run(
        ["curl", "--silent", "--location", url], text=True, capture_output=True
    )
webpage = p.stdout
webpage = webpage.splitlines()
# print(webpage.splitlines())

for line in webpage:
    # print(line, end="")
    if m := re.search(f"{sys.argv[1]}", line):
        if l := re.search("<td class=\"data\"><a href=(.*)>([a-zA-z\s+]+.*)</a></td>$", line):
            # print(line.lstrip())
            code = l.group(1)[1:9]
            name = l.group(2)
            if (code, name) not in courses:
                courses[code] = name
            # if name not in course_name:
            #     course_name.append(name)
            # if code not in course_code:
            #     course_code.append(code)
for (code,name) in sorted(courses.items()):
    print(f"{code} {name}")
# pprint.pprint(courses)