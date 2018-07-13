#/bin/bash

echo "start-------"
/usr/bin/expect >/dev/null 2>&1 <<EOF

spawn git push origin master
expect {
       "Username for*" {send "moonwwdz\r";exp_continue}
       "Password for*" {send "159753@wy\r"}
}
interact

expect eof
EOF
echo "end-----------"
