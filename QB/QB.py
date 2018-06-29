_author_='lcs'
import urllib
from urllib import request
import re


class QB:
    #初始化方法，定义变量
    def __init__(self):
         self.index = 1
         self.url = 'http://www.qiushibaike.com/hot/page/'
         self.stories=[]
    def getHTML(self,url):
         self.headers = { 'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
         req = request.Request(url, headers=self.headers)
         return request.urlopen(req)
    #获得一页代码
    def getPage(self,index=1):
         #print(self.url)
         try:
             url1 = self.url+str(index)
             response = self.getHTML(url1)
             pageCode=response.read().decode('utf-8')
             return pageCode
         except urllib.request.URLError as e:
             if hasattr(e, 'code'):
                 print(e.code)
             if hasattr(e, 'reason'):
                 print(e, reason)
             return None
    #提取一页的不带图片的段子
    def getPageItems(self, index):
        content=self.getPage(index=index)
        #对每一组阱行分类：1.发布人，2.段子信息地址，3.发布内容，4.发布图片，5.点赞数
        pattern=re.compile('''<div class="article.*?<h2>(.*?)</h2>'''#将正则表达式编译为pattern实例
							 + '''.*?<a href="(.*?)"'''
							 + '''.*?<span>(.*?)</span>'''
							 + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
							 + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
        items=re.findall(pattern,content)
        #print(items)
        pageItems=[]
        #一个item代表一个段子
        for item in items:
          #段子中没有图片
          #if not re.search("img",item[4]):
           #print(item.group())
               result=re.sub("<br/>","\n",item[2])
               pageItems.append([item[0].strip(),result.strip()])
          #print(item[0])
        #print(pageItems)
        return pageItems
    #加载页面
    def loadPage(self):
        #print(self.index)
        if self.enable:
            if len(self.stories)<2:
                pageStories=self.getPageItems(self.index)
                if pageStories:
                    self.stories.append(pageStories)
                    self.index+=1
        #print(2)
    #从一页内容中获取段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            receive = input()
            self.loadPage()
            if receive == "Q" or receive == "q":
                self.enable = False
                return

            print("当前第:%s页\t发布人:%s\t内容:\n%s\n" % (page, story[0], story[1]))


        # 开始
    def start(self):
            print("正在读取求糗事百科，按回车查看新段子，q推出")
            self.enable = True
            self.loadPage()
            #print(1)
            nowPage = 0
            while self.enable:
                if len(self.stories) > 0:
                    #从全局的list中获取一页
                    pageStories = self.stories[0]
                    nowPage += 1
                    # 从全局的list中删除一页
                    del self.stories[0]
                    #输出
                    self.getOneStory(pageStories, nowPage)
            #print(1)

spider = QB()
spider.start()