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
    if test -f "$png_name"
    then
        echo "$png_name already exists" 1>&2
        exit 1
    fi
    convert "$jpg_name" "$png_name"
    rm "$jpg_name"
    fi
done
