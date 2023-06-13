#!/bin/dash



URL1="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${1}%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubject.educationalArea:${2}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:ugrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"
URL2="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${1}%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubject.educationalArea:${2}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:pgrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"

if [ "$#" -ne 2 ]
then
    echo "Usage: $0 <year> <course-prefix>"
fi

if [ "$1" -ge 2019 ] && [ "$1" -le 2023 ]
then
    curl -sL "$URL1" | jq -rc '.contentlets[] | .code, .title' | sed -E ':a;N;$!ba;s/([0-9])\n/\1 /g'
    # for code in $arr[]
    # do
    #     echo "$code"
    # done
else
    echo "$0: argument 1 must be an integer between 2019 and 2023"
fi


#grep -Ei ""code: $2"" | cut -d\: -f2 | sed "s/\",//g" | sed "s/\"//g"
#. | {code: .contentlets[].code, title: .contentlets[].title}