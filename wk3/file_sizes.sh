#!/bin/dash

SMALL="Small files:"
MEDIUM="Medium-sized files:"
LARGE="Large files:"

for FILE in *
do 
    COUNT=$(wc -l < "$FILE")
    if [ "$COUNT" -lt 10 ] 
    then
        SMALL="$SMALL $FILE"
    elif [ "$COUNT" -lt 100 ] 
    then
        MEDIUM="$MEDIUM $FILE"
    else 
        LARGE="$LARGE $FILE"
    fi
done
echo "$SMALL"
echo "$MEDIUM"
echo "$LARGE"