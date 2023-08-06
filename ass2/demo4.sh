#!/bin/dash
#Grabs the first and last line in every file in current dir
for file in *
do
    head -1 $file
    tail -1 $file
done