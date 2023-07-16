#!/bin/dash

max="$(wc -l $1 | cut -d" " -f1)"
filename="$1"

for file in "$@"
do
    cur="$(wc -l $file | cut -d" " -f1)"
    if [ "$max" -lt "$cur" ]
    then
        max=$cur
        filename=$file
    fi
done

echo $filename