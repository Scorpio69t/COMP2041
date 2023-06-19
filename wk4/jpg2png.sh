#!/bin/dash

for file_name in * 
do
    newfile="$(echo "$file_name")"
    echo "$newfile"
done