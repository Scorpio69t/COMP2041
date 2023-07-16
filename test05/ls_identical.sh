#!/bin/dash

for file in "$1"/*
do
    for file2 in "$2"/*
    do
        file1name="$(echo "$file" | cut -d"/" -f2)"
        file2name="$(echo "$file2" | cut -d"/" -f2)"
        if [ "$file1name" = "$file2name" ]
        then
            cmp -s -- "$file" "$file2" > /dev/null
            if [ "$?" -eq 0 ]
            then
                echo "$file1name"
            fi
        fi
    done
done