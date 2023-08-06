#!/bin/dash
#prints out all shell files and then all c files

echo THE FOLLOWING ARE SHELL FILES
for file in *.sh
do
    cat $file
done

echo THE FOLLOWING ARE C FILES

for file in *.c
do
    cat $file
done