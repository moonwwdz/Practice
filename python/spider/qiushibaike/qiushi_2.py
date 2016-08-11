#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re

class CSBK:
    def __init__(self):
        #模拟浏览器信息
        self.header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        #当前的页数
        self.page = 1


    def getPageConent(self,page_num):

        url = 'http://www.qiushibaike.com/hot/page/'+ str(page_num)

        try:
            request = urllib2.Request(url,headers=self.header)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content

            if m:
                for item in m:
                    print item[0]
                    print item[1]
                    print item[2]
                    print item[3]
            else :
                print "not match"
        except urllib2.URLError, e:
            if hasattr(e,'reason'):
                print u'页面走丢了，你先歇歇！！！'
                return None




    def getPageItem(self):
        items = []
        content = self.getPageConent()
        if not content:
            pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
            m = re.findall(pattern,content)
            if m:
                replace_pattern = re.compile(r'<br>')
                for item in m:
                    item[1] = re.sub(replace_pattern,'\n',item[1])
                    items.append(item[0],item[1],item[2],item[3])

        return items
