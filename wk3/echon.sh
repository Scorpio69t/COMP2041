#!/bin/dash

if [ $# -ne 2 ] 
then
    echo "Usage: $0 <number of lines> <string>" 1>&2
    exit 1
fi

if [ $1 -lt 0 ]
then
    echo "$0: argument 1 must be a non-negative integer"
fi

i=0
while [ $i -lt "$1" ]   
do
    echo "$2"
    i=$((i + 1))
done