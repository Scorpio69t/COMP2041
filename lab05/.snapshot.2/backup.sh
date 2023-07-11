#!/bin/dash
count=0
for file in .*
do
    FileName="$(echo $file | cut -d\. -f2,3)"
    if [ "$FileName" = "$1" ]
    then
        count=$((count + 1))
    fi
done

FileName=".${1}.${count}"
cp "$1" "$FileName"
echo "Backup of '$1' saved as '$FileName'"