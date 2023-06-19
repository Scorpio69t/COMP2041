#!/bin/dash

for image in "$@"
do
    display "$image"
    echo -n "Address to e-mail this image to? "
    read email
    if [ "$email" = "" ] 
    then
        echo No email sent
        continue
    fi
    echo -n "Message to accompany image? "
    read message
    echo "$message" | mutt -s 'SUBJECT?' -e 'set copy=no' -a "$image" -- "$email"
    echo "$image sent to $email"
done