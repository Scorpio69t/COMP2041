#!/bin/dash

#Testing if pigs-log works as intended
pigs-init >/dev/null

echo "hellow" > a

pigs-add a 2>/dev/null
pigs-commit -m 'first' >/dev/null


expected="0 first"
output=$(pigs-log)
if [ "$expected" = "$output" ]
then
    echo "Test Passed"
else
    echo "Test Failed"
fi