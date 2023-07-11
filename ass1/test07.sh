#!/bin/dash

#Test if pigs-add gives error with no .pig dir

echo hi > a 
pigs-add a 2>/dev/null

if [ "$?" = 1 ]
then
    echo Test Passed
else
    echo Test Failed
fi