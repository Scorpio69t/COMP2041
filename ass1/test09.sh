#!/bin/dash

#Testing pigs-log with no commits

pigs-init >/dev/null

expected=""
outcome=$(./pigs-log)

if [ "$expected" = "$outcome" ]
then
    echo "Test Passed"
else
    echo "Test Failed"
fi