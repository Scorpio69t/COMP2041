#!/bin/dash

#First test script tests if pigs-add is working

pigs-init

2041 pigs-init >/dev/null

if [ "#?" -eq 1 ]
then
    echo "Pigs-init working as intended!"
else
    echo "Test failed"
fi