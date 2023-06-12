#!/bin/dash

while read CMD 
do
    "$CMD" >> tmp.txt
done