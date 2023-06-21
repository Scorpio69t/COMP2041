#!/bin/dash
base=$(pwd)

# set -x

for dir in "$@"
do
    Album="$(echo "$dir" |
            cut -d'/' -f2)"
    Year="$(echo "$dir" |
            cut -d'/' -f2 |
            cut -d',' -f2 |
            sed "s/\s//g")"
    cd ./"$dir"
    for file in *
    do
        Properties=$(echo "$file" |
                    tr '-' '\n' |
                    sed 's/ *$//' |
                    sed 's/^ *//'> tmp.txt)
        Track="$(head -1 tmp.txt)"
        Title="$(head -2 tmp.txt | tail -1)"
        Artist="$(tail -1 tmp.txt| cut -d\. -f1)"
        id3 -t "$Title" -T "$Track" -a "$Artist" -A "$Album" -y "$Year" "$file" >/dev/null
    done
    rm tmp.txt
    cd "$base"
done