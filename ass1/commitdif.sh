#!/bin/dash

#This script, given a file as an arguement, will go through all comits
#and see if the file hhas been changed.
ArgCutName="$(echo $1 | cut -d'/' -f3)"
#Loop through all commits
for dir in .pig/commits/*
do
    CommitNum="$(echo $dir | cut -d'/' -f3)"
    for file in .pig/commits/$CommitNum/*       #loop through files in each commit
    do
        fileCutName="$(echo $file | cut -d'/' -f4)"
        if [ "$fileCutName" = "$ArgCutName" ]
        then                 #If a commit contains a file with same name as arguement, will call diff on both
            diff -q "$file" "$1" >/dev/null
            if [ $? -eq 0 ]
            then
                exit 1      #Exit with code 1 if there is no change
            fi
        fi
    done
done
exit 0