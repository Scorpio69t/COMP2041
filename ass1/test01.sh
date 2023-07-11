#!/bin/dash

#Testing if pigs-innit creates the .pig dir

pigs-innit

if [ -d ".pig" ]
then
    echo "Test Passed"
else
    echo "Test failed"
fi