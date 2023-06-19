#!/bin/dash
cut -d\| -f2 | sort | uniq -c | sort | grep "      2" | cut -d " " -f8