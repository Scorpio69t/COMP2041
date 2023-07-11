#!/bin/dash

#Testing if pigs-show produces correct errror 

pigs-init >/dev/null

echo "hellow" > a

pigs-add a 2>/dev/null
pigs-commit -m 'first' >/dev/null

pigs-show :b 2>/dev/null

if [ "$?" = 1 ]
then
    echo Test Passed
else 
    echo Test Failed
fi