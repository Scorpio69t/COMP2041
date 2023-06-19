#!/bin/dash
# set -x
for file_name in *
do
    test -f "$file_name" ||
    continue
    if echo "$file_name" | grep -E ".jpg$" >/dev/null
    then
    old_name="$(
        echo $file_name |
        cut -d\. -f1
    )"
    jpg_name=${old_name}.jpg
    png_name=${old_name}.png
    convert "$jpg_name" "$png_name"
    rm "$jpg_name"
    fi
done
