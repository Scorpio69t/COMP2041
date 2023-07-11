#!/bin/dash

#test to see if pigs-show works as inteded

pigs-init >/dev/null

echo "hellow" > a

pigs-add a 2>/dev/null
pigs-commit -m 'first' >/dev/null

expected="hellow"
output=$(pigs-show 0:a)

if [ "$expected" = "$output" ]
then
    echo "Test Passed"
else
    echo "Test Failed"
fi