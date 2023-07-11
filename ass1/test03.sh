#!/bin/dash

pigs-init >/dev/null

echo "hellow" > a

pigs-add a 2>/dev/null

expected="Committed as commit 0"
output=$(pigs-commit -m 'first')

if [ "$expected" = "$output" ]
then
    echo "Test passed"
else
    echo "Test failed"
fi