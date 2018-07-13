#/bin/bash

#笔记记录路径
NOTE_PATH=""

if [[ $# -lt 1 ]]
then
    NOTE_PATH=~/project/Practice/notes/
fi

cd ${NOTE_PATH}
if [[ $? -ne 0 ]]
then
    echo "ERROR::$NOTE_PATH No such file or directory"
    exit 1
fi

git pull

git_status=`git status`

if [[ `echo $git_status | grep "nothing to commit"` ]]
then
    exit 0
fi


git add . && git commit -m "note auto commit `date`"

/usr/bin/expect >/dev/null 2>&1 <<EOF

set timeout 180
spawn git push origin master
expect "Username for*"
send "moonwwdz\n"

expect "Password for*"
send "lklklklk\n"

interact

expect eof
EOF
