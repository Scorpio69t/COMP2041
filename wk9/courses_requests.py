#!/usr/bin/env python3

import requests, pprint
import re, sys
import bs4 as BeautifulSoup

url = f"http://www.timetable.unsw.edu.au/2023/{sys.argv[1]}KENS.html"
courses = {}
res = requests.get(url).text
soup = BeautifulSoup.BeautifulSoup(res, 'html5lib')

# for tag in soup.find_all('td', class_='data'):
#     print(tag)
for tag in soup.find_all('a')[11:]:

    href = tag.get('href')
    text = tag.text
    # print(href)
    if re.search("\w{4}\d{4}.html", str(href)):
        if re.search("\w{4}\d{4}", str(tag.text)):
            continue
        course = href.replace(".html","")
        if (course, text) not in courses:
           courses[course] = text
        # print(f"href is {tag.get('href')}")
        # print(tag.getText())
        # print(f"tag text is {tag.text}")
        # # print(tag.get('href'))
        # print("#############")
# print(soup.find_all('a'))
for (code,name) in sorted(courses.items()):
    print(f"{code} {name}")
