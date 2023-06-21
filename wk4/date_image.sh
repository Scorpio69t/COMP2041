#!/bin/dash

if [ "$#" -ne 1 ]
then
    echo "Usage: $0 <image.jpg>"
    exit 2
fi

text="$(ls -l $1 | cut -d' ' -f6,7,8)"
convert -gravity south -pointsize 36 -draw "text 0,10 '$text'" "$1" temporary_file.jpg
display temporary_file.jpg