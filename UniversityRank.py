from urllib import request
from bs4 import BeautifulSoup
import bs4
import re


def getHTML(url):
    try:
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = request.Request(url,headers=headers)
        response = request.urlopen(req)
        return response
    except:
        return ""
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    print(ulist)
def printUnivList(ulist,num):
    print("{0:^10}\t{1:{3}^10}\t{2:^10}".format("排名","学校名称","总分",chr(12288)))
    with open("data.txt", "w") as f:
     for i in range(num):
        u=ulist[i]
        print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0],u[1],u[2],chr(12288)))
        f.write(u[0])
        f.write('\t')
        f.write(u[1])
        f.write('\t\t')
        f.write(u[2])
        f.write('\n')
    f.close()
def main():
    ulist=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html=getHTML(url)
    fillUnivList(ulist,html)
    printUnivList(ulist,600)
main()


