#!/usr/bin/python
# __encoding:utf8__

import pexpect

sucd = ['# ', '>>> ', '> ', '\$ ',pexpect.TIMEOUT,'root@']
ssh_str = 'Are you sure you want to continue connecting'
def connectSSH(h,u,p,c):
    try:
        child = pexpect.spawn('ssh',[ '-p 14987',u+'@'+h])
        ret = child.expect([pexpect.TIMEOUT,ssh_str,'[P|p]assword:'])
        if ret == 0:
            print u'Timeout Try Again'
            return

        if ret == 1:
            child.sendline('yes')
            ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])

        if ret == 0:
            print u'Timeout Try Again....'
            return

        #输入密码
        child.sendline(p)
        child.expect(sucd)
        #登陆成功，执行命令
        child.sendline(c)
        child.expect(sucd)
        #打印执行命令的结果
        print child.before

    except Exception as e:
        print e
        return


if __name__ == '__main__':
     connectSSH('192.168.212.26','root','123456','cat /etc/passwd | grep root')
