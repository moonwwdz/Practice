爬虫，爬糗事百科上的段子
=========================

这是学习python后的第一个爬虫，参考[崔庆才](http://weibo.com/cuiqingcai/profile?s=6cm7D0)的[静觅](http://cuiqingcai.com/)上的[Python爬虫实战一之爬取糗事百科段子](http://cuiqingcai.com/990.html)的教程一点点来实现的。

主要的核心步骤有三点

    - [x] 抓取网页内容

    - [x] 正则匹配到数据

    - [x] 完整的展示过程


## 核心正则
```python
pattern = re.compile(<div class="author clearfix">.*?<h2>(.*?)</h2>.*?'+
        '<div class="content">(.*?)</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?'+
        '<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S')
```
虽然看着很长其实就是把整个数据的html表示了一次而已，当然后面深入学习正则后会简化这个
    
