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
        #当前的数据
        self.stores = []
        #是否退出
        self.enable = True


    def getPageConent(self,page_num):

        url = 'http://www.qiushibaike.com/hot/page/'+ str(page_num)

        try:
            request = urllib2.Request(url,headers=self.header)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e,'reason'):
                print u'页面走丢了，你先歇歇！！！'
                print e.reason
                return None


    def getPageItem(self,page_num):
        items = []
        content = self.getPageConent(page_num)
        if content:
            pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
            m = re.findall(pattern,content)
            if m:
                replace_pattern = re.compile(r'<br>')
                for item in m:
                    #item[1] = re.sub(replace_pattern,r'\n',item[1])
                    item_br = item[1].replace('<br/>','\n')
                    #print item[1]
                    items.append([item[0],item_br,item[2],item[3]])

        return items


    def loadPage(self):
        if len(self.stores) < 1:
            page = self.getPageItem(self.page)
            self.page += 1
            if len(page)>0:
                self.stores.append(page)
                return True
            else:
                return False

    def getMessage(self,page):
        for c in page:
            print (u'[%s] 发表了\n---\n%s---\n有%s人点赞\t%s人评论\n' % (c[0],c[1],c[2],c[3]))
            print ('=+=+'*8+'第'+str(self.page-1)+'页'+'=+=+'*8+'\n')
            key = raw_input(u'Exit with "Q":')
            if key == 'q' or key == 'Q':
                self.enable = False
                return None


    def start(self):
        print u'正在从网站偷偷的下载。。。'
        if not self.loadPage():
            print u'网络连接出现问题'
            return None
        while self.enable:
            self.loadPage()
            self.getMessage(self.stores[0])
            del self.stores[0]

        print u'ByeBye!!!'


if __name__ == '__main__':
    q = CSBK()
    q.start()
