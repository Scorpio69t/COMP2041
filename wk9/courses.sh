#!/bin/dash

curl --location --silent "http://www.timetable.unsw.edu.au/2023/{$1}KENS.html" | grep -E "<td class=.*><a href=.*>.*</a></td>$" | grep -Ev "<td class=.*><a href=.*>[A-Z]{4}[0-9]{4}</a></td>$" |
cut -d"=" -f3 | cut -d"<" -f1 | sed -E "s/>/ /g" | sed -E "s/\"//g" | sed -E "s/.html//g" | tail -n +6 | sort -k1n