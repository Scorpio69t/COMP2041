#!/bin/dash

#given an arguement, check if file exists in index

for file in .pig/index/*
do
    fileName="$(echo "$file" | cut -d'/' -f3)"
    if [ "$fileName" = "$1" ]
    then
        exit 1
    fi
done
#ERROR NOT PICKING UP TMPINDEX
for file in .pig/tmpIndex/*
do
    fileName="$(echo "$file" | cut -d'/' -f3)"
    if [ "$fileName" = "$1" ]
    then
        exit 1
    fi
done

exit 0