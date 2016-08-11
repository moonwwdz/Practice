#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

values = {"search":"王婷"}
data = urllib.urlencode(values)
url = "http://google.moonwwdz.me"
request = urllib2.Request(url,data)
print request.__str__
res = urllib2.urlopen(request)
print res.read()
