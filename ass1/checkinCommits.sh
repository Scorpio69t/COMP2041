#!/bin/dash
#Given a file as an arguement, checks if the file has ever been commited
for dir in .pig/commits/*
do
    CommitNum="$(echo $dir | cut -d'/' -f3)"
    for file in .pig/commits/$CommitNum/*       #loop through files in each commit
    do
        fileName="$(echo $file | cut -d'/' -f4)"
        if [ $fileName = "$1" ]
        then 
            exit 0
        fi
    done
done
exit 1