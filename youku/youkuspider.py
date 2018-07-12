from bs4 import BeautifulSoup
import requests
import os
import re

def getHTMLText(url):
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

def parsePage(ilt, html):
    soup = BeautifulSoup(html, 'html.parser')
    titlelist= soup.find_all('li',class_='title')
    for i in titlelist:
        ilt.append(i.a.string)
        print(i.a.string)
    print(len(titlelist))
    print("end parsePage")

def printGoodsList(ilt,year):
    if not os.path.exists(r'C:\Users\god\Desktop\电影'):
        os.mkdir(r'C:\Users\god\Desktop\电影')
    path=r'C:\Users\god\Desktop\电影\{0}.txt'.format(year)
    list = open(path,'w',encoding='utf-8')
    list.write(str(year)+'年全部剧集节目'+'\n')
    for i in range(len(ilt)):
        list.write(str(i+1)+". "+ilt[i]+'\n')
    list.close()
    print("this is printNameList")


def main():
    depth = 2
    start_url = 'https://list.youku.com/category/show/c_97_r_2018_s_1_d_1_p_'
    year=2018
    infolist = []
    for i in range(depth):
            url = start_url + str(i) + '.html?spm=a2h1n.8251845.0.0'
            print(url)
            html = getHTMLText(url)
            parsePage(infolist, html)
    printGoodsList(infolist,year)
main()
#http://list.youku.com/category/show/c_97_r_2018_s_1_d_1_p_1.html?spm=a2h1n.8251845.0.0