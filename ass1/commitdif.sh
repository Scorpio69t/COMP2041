#!/bin/dash

#arguement will be a file
#loop through dir in .pig/commits
#if file in dir == arguement
#call diff. If diff returns w exit 1, we exit 1
#else exit 0
ArgCutName="$(echo $1 | cut -d'/' -f3)"
base=$(pwd)
for dir in .pig/commits/*
do
    cd $dir
    for file in *
    do
        echo "FILE is $file"
        echo "Arguement is $1"
        if [ "$file" = "$ArgCutName" ]
        then
            echo 'srthjio4r'
            echo $file
            diff -q "$file" "$1"
            if [ $? -eq 0 ]
            then
                exit 1
            fi
        fi
    done
    cd "$base"
done
exit 0