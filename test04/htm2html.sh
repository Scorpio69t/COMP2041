#!/bin/dash
# set -x 

IFS='
'


for file in *.htm*
do
    prefix="$(echo $file | cut -d'.' -f2)"
    if [ $prefix = "html" ]
    then
        continue
    fi
    FileName="$(echo $file | cut -d'.' -f1)"
    if [ ! -f "$FileName.html" ]
    then
        mv "$file" "$FileName.html"
    else
        echo "$FileName.html exists"
        exit 1
    fi
done