#coding:utf-8

# 1.抓取淘宝MM的姓名，头像，年龄
# 2. 抓取每一个MM的资料简介以及写真图片
# 3. 把每一个MM的写真图片按照文件夹保存到本地
# 4. 熟悉文件保存的过程
import urllib2
import urllib
import re
import tools
import os
class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tools.Tools()

    def get_page(self, page_index):
        try:
            url = self.siteURL + "?page=" + str(page_index)
            # print url
            requst = urllib2.Request(url)
            response = urllib2.urlopen(requst)
            return response.read().decode('gbk')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print("连接百度贴吧失败:", e.reason)
                return None

    def get_contents(self, page):
        print page
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        # print items
        contents = []
        for item in items:
            contents.append(item)
        return contents

    # def get_detail_page(self, detail_url):
    #     response = urllib2.urlopen(detail_url)
    #     return response.read().decode('gbk')
    #
    # def get_person_brief(self, page_content):
    #     pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
    #     result = re.search(pattern, page_content)
    #     return self.tool.replace(result.group(1))
    #
    # def save_img(self, image_url, file_name):
    #     response = urllib2.urlopen(image_url)
    #     data = response.read()
    #     f = open(file_name, "wb")
    #     f.write(data)
    #     f.close()
    # def save_txt(self, content, name):
    #     fileName = name + "/" + name + ".txt"
    #     f = open(fileName,"w+")
    #     print u"个人信息为:",fileName
    #     f.write(content.encode('utf-8'))
    #
    # def mkdir(self, path):
    #     path = path.strip()
    #     is_exists = os.path.exists(path)
    #     if not is_exists:
    #         os.makedirs(path)
    #         return True
    #     else:
    #         return False

spider = Spider()
page = spider.get_page(1)
contents = spider.get_contents(page)
# print contents


# for item in contents:
#     print "\n" ,item
# print contents
# briefs = spider.get_person_brief(page_content)


# print briefs
