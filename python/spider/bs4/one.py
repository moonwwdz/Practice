#!/usr/local/bin/python3.5
#__encoding:utf8__

import urllib.request
from bs4 import BeautifulSoup

def getContent(url):
    request = urllib.request.Request(url,headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    #print (content)
    return content

def bsHtml(h):
    soup = BeautifulSoup(h,"html.parser")
    #print(soup.prettify())
    print(soup.title)


if __name__ == '__main__':
    html = getContent('http://moonwwdz.me')

    bsHtml(html)
