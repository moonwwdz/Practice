#!/usr/local/bin/python3.5
#__encoding:utf8__

from pexpect import pxssh

def connectSSH(h,u,p,pt='22'):
    try:
        c = pxssh.pxssh()
        c.login(h,u,password=p,port=pt)
        return c
    except Exception as e:
        print('[-]Can\'t Connect the serve')
        print(e)

def command(s,c):
    try:
        ret = s.sendline(c)
        s.prompt()
        print (s.before.decode())

    except Exception as e:
        print (e)
        print (123)


if __name__ == '__main__':
    s = connectSSH('23.110.64.84','root','wangy@3483','22')
    #s = connectSSH('192.168.212.131','root','123456','14987')
    command(s,'cat /etc/passwd | grep root')

