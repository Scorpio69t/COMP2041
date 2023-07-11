#!/bin/dash

#test if pigs-add error wroks 

pigs-init 2>/dev/null

pigs-add a 2>/dev/null

if [ "$?" = 1 ]
then
    echo "Test passed"
else
    echo "Test failed"
fi