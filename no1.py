import urllib
from urllib import request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)

def getHTML(url):
    headers = { 'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url, headers=headers)
    return request.urlopen(req)

try:
    response = getHTML(url)

    content=response.read().decode('utf-8')
    pattern=re.compile('''<div class="article.*?<h2>(.*?)</h2>'''
							 + '''.*?<a href="(.*?)"'''
							 + '''.*?<span>(.*?)</span>'''
							 + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
							 + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
    items=re.findall(pattern,content)
    with open('output.txt', 'w') as f:
     for item in items:
        #haveImg=re.search('img',item(3))
        #if not haveImg:
           print(item[2])
           f.write(item[2])



except urllib.request.URLError as e:
    if hasattr(e, 'code'):
        print(e.code())
    if hasattr(e, 'reason'):
        print(e, reason())
