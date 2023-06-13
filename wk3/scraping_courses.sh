#!/bin/dash



URL1="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${1}%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubject.educationalArea:${2}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:ugrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"
URL2="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${1}%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubject.educationalArea:${2}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:pgrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"

if [ "$#" -ne 2 ]
then
    echo "Usage: $0 <year> <course-prefix>" 2>&1
    exit 1
fi

if ! [ "$1" -eq "$1" ] 2> /dev/null
then
    echo "$0: argument 1 must be an integer between 2019 and 2023" 
    exit 1
fi

if [ "$1" -ge 2019 ] && [ "$1" -le 2023 ] && [ "$1" -eq "$1" ]
then
    ( curl -sL "$URL1" | jq -j '.contentlets[] | .code, " ", .title, "\n"' ;
    curl -sL "$URL2" | jq -j '.contentlets[] | .code, " ", .title, "\n"' ) |
    sort -t' ' -k1 -n | uniq
    
else
    echo "$0: argument 1 must be an integer between 2019 and 2023" 
    exit 1
fi



#grep -Ei ""code: $2"" | cut -d\: -f2 | sed "s/\",//g" | sed "s/\"//g"
#. | {code: .contentlets[].code, title: .contentlets[].title}

# | sed -E ":a;N;$!ba;s/${2}([0-9]{4})\n/${2}\1 /g" 