#!/bin/dash

#arguement will be a file
#loop through dir in .pig/commits
#if file in dir == arguement
#call diff. If diff returns w exit 1, we exit 1
#else exit 0
ArgCutName="$(echo $1 | cut -d'/' -f3)"
base=$(pwd)
for dir in .pig/commits/*
do
    CommitNum="$(echo $dir | cut -d'/' -f3)"
    for file in .pig/commits/$CommitNum/*
    do
        fileCutName="$(echo $file | cut -d'/' -f4)"
        if [ "$fileCutName" = "$ArgCutName" ]
        then
            diff -q "$file" "$1" >/dev/null
            if [ $? -eq 0 ]
            then
                exit 1
            fi
        fi
    done
    cd "$base"
done
exit 0