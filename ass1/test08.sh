#!/bin/dash

#Test if pigs-show error on wrong commit num works

pigs-init >/dev/null

echo "hellow" > a

pigs-add a 2>/dev/null
pigs-commit -m 'first' >/dev/null

pigs-show 2:a 2>/dev/null

if [ "$?" = 1 ]
then
    echo Test Passed
else
    echo Test Failed
fi