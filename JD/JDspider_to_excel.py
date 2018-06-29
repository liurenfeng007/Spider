#https://search.jd.com/Search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&wq=%E5%B7%A7%E5%85%8B%E5%8A%9B&pvid=343929dad1e74534aba44084e5d29931
#https://search.jd.com/Search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%B7%A7%E5%85%8B%E5%8A%9B&stock=1&page=3&s=57&click=0
#https://search.jd.com/Search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%B7%A7%E5%85%8B%E5%8A%9B&stock=1&page=5&s=110&click=0
#https://search.jd.com/Search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%B7%A7%E5%85%8B%E5%8A%9B&stock=1&page=7&s=163&click=0
from bs4 import BeautifulSoup
import requests
import re
import csv
import os

def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for news in soup.select('.gl-item'):
            title = news.find('div', class_='p-name').text.strip()
            #title = news.select('.p-name.p-name-type-2 a')[0].text.strip()
            #print(title)
            price = news.select('.p-price')[0].text.strip()
            commit = news.select('.p-commit')[0].text.strip()
            urls = r'http://' + news.select('.p-img')[0].contents[1]['href']
            ilt.append([title, price, commit,urls])


            #print(ilt)


    except:
        print("")

def printGoodsList(ilt):
    #tplt = "{:^8}\t{:^16}\t{:^8}"
    #print(tplt.format("序号", "名称", "价格"), chr(12288))
    count = 0
    for g in ilt:
        count = count + 1
        #print(tplt.format(count, g[0], g[1], g[2]), chr(12288))
        print("%d、 \n 名称：%s \n 价格：%s\n 评论：%s\n 网址：%s" % (count,g[0], g[1], g[2],g[3]))

def printComnent():
    url1 = 'https://sclub.jd.com/comment/productPageComments.action?' \
           'callback=fetchJSON_comment98vv76668&productId='
    url2=       '&score=0&sortType=5&page='
    url3 = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    ID=input("请输入产品编号")
    depth =input("请输入你要爬取的评论页码数：")
    for i in range(int(depth)):
        url = url1+str(ID)+url2 + str(i) + url3
        #print(url)
        r = requests.get(url=url)
        html = r.content
        # print("当前抓取页面：",url,"状态:",r)
        html = str(html, encoding="GBK")
        content = re.findall(r'"guid".*?,"content":(.*?),', html)
        for j in range(len(content)):
            print(str(i * 10 + j + 1) + content[j])

def save(ilt):
    path = 'F:/数据/'
    if not os.path.exists(path):
        os.mkdir(path)
    with open( '京东商品数据.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['商品', '价格',  '评论数', '链接'])
        writer.writerows(ilt)
    f.close()



def main():
    print('请输入爬取商品：')
    goods = input()
    print('请输入爬取页数：')
    depth = int(input())
    print("正在抓取...........................................")
    start_url = 'https://search.jd.com/Search?keyword=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&enc=utf-8&page=' + str(2 * i + 1)
            #print(url)
            html = getHTMLText(url)
            #print(html)
            parsePage(infolist, html)
        except:
            continue
    #print(infolist)
    printGoodsList(infolist)
    printComnent()
    save(infolist)

main()