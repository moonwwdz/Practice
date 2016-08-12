#! /usr/bin/python
# -*- coding:utf-8 -*-
import zipfile
import threading
from optparse import OptionParser

class Unzip:
    def __init__(self):
        pass

    def zipExtrace(self,zipObj,passwd):
        try:
            zipObj.extractall(pwd=passwd)
            print u'解压密码为'+passwd
            return passwd
        except Exception,e:
            #print passwd print e
            pass

    def unZipWithFile(self,zipFile,pwFile):
        try:
            pws = file(pwFile,'r')
            zipobj = zipfile.ZipFile(zipFile)
        except:
            print u'压缩文件和密码字典不存在'
            return False
        for pw in pws.readlines():
            pw = pw.strip('\n')
            t = threading.Thread(target=self.zipExtrace,args=(zipobj,pw))
            t.start()

    def start(self):
        parse = OptionParser()
        parse.add_option('-p',dest='pwdfile',help='one password file disc')
        parse.add_option('-z',dest='zipfile',help='the file to unzip')
        (options,args) = parse.parse_args()
        if options.pwdfile and options.zipfile:
            self.unZipWithFile(options.zipfile,options.pwdfile)
        print options
        print args



if __name__ == '__main__':
    unzip = Unzip()
    unzip.start()
