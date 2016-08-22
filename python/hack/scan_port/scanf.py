#! /usr/bin/python
# -*- coding:utf-8 -*-

import socket
from optparse import OptionParser

class Scanf:
    def __init__(self):
        pass

    def setOpt(self):
        parse = OptionParser()
        parse.add_option('-H','--hostname',dest='HostName',help='Need a avilibe Hostname')
        parse.add_option('-p','--port', dest='PortList',type='int',help='Need ad avilibe Ports list')
        parse.add_option('-f','--file', dest='FileName',help='Force scanf every port')
        (option,argv) = parse.parse_args()

        self.host  = option.HostName
        self.ports = option.PortList
        self.file = option.FileName

        argv.append(self.ports)
        self.ports = argv

    def connScanf(self,name,ip,port):
        try:
            conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            conn.connect((ip,int(port)))
            conn.send('abc\r\n')
            res = conn.recv(100)
            print '\033[1;32;32m[+]\033[0m('+str(name)+'):['+str(port)+'] is opening!'
            print '\033[1;34;34m[*]'+res+'\033[0m'
        except Exception ,e:
            #print e
            print '\033[1;31;31m[-]\033[0m('+str(name)+'):['+str(port)+'] is closed!'

    def gethost(self,web):
        try:
            tagip = socket.gethostbyname(web)
            self.tagip = tagip
        except:
            print '\033[1;31;31m[-]\033[0m('+str(web)+') is not resovled!'
            exit()

        try:
            tagDomain = socket.gethostbyaddr(tagip)
            return tagDomain[0]
        except:
            print '\033[1;31;31m[-]\033[0m('+str(web)+') is not defined name!'
            return tagip

    def start(self):
        self.setOpt()
        print self.ports
        tagHost = self.gethost(self.host)
        if not self.file:
            for p in self.ports:
                self.connScanf(tagHost,self.tagip,p)
        else:
            with open(self.file,'r') as f:
                for p in f.readlines():
                    self.connScanf(tagHost,self.tagip,p.strip())




if __name__ == '__main__':
    s = Scanf()
    s.start()
