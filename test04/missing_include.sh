#!/bin/dash

for file in "$@" 
do
    check="$(cat $file | grep '#include \"' | cut -d'"' -f2 | tr ' ' '\n')" >/dev/null
    for fileToCheck in $check
    do
        if [ ! -f "$fileToCheck" ]
        then
            echo "$fileToCheck included into $file does not exist"
        fi 
    done
done