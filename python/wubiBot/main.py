#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import json

from flask import Flask
from flask import jsonify
from requests_html import HTMLSession
session = HTMLSession()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           'Origin':'http://www.chaiwubi.com'}

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/wubi/<word>')
def wubi(word):
    ret = {}
    data = {'select_value':'查单字','wz':word}
    res = session.post('http://www.chaiwubi.com/bmcx/',data=data,headers=headers)
    select = 'table.dw-bmcx > tr'
    if len(res.html.find(select)):
        code86 = res.html.find(select)[0].find('td')
        ret['one'] = code86[2].text.upper()
        ret['two'] = code86[3].text.upper()
        ret['three'] = code86[4].text.upper()
        ret['four'] = code86[5].text.upper()
        ret['imgs'] = []
        for m in code86[6].find('img'):
            ret['imgs'].append(m.attrs['src'])
        code98 = res.html.find(select)[1].find('td')
        #print(code98[6].find('div.dw-bmcx-86 > img'))
        ret['pic'] = code98[6].find('div.dw-bmcx-86 > img')[0].attrs['src']
        return jsonify(ret)
    else:
        return "API已经变更，无法查询"

    return word



if __name__ == '__main__':
        app.run(host='0.0.0.0')
