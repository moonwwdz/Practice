#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re

page = 1

url = 'http://www.qiushibaike.com/hot/page/'+ str(page)+ '?s=4903073'

header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
try:
    request = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(request)
#    print response.read()
    content = response.read().decode('utf-8')
#    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?"'+
#            'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'
#            ,re.S)
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
    m = re.findall(pattern,content)
    if m:
        for item in m:
            print item[0]
            print item[1]
            print item[2]
            print item[3]
    else :
        print "not match"
except urllib2.URLError, e:
    print e.code
