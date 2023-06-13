#!/bin/dash

if [ $# -ne 2 ] 
then
    echo "Usage: $0 <number of lines> <string>" 2>&1
    exit 1
fi


if [ "$1" -eq "$1" ] 2>/dev/null
then
    if [ "$1" -lt 0 ]
    then
        echo "$0: argument 1 must be a non-negative integer" 2>&1
        exit 1
    fi
    i=0
while [ "$i" -lt "$1" ]   
do
    echo "$2"
    i=$((i + 1))
done
else
    echo "$0: argument 1 must be a non-negative integer" 2>&1
    exit 1
fi
