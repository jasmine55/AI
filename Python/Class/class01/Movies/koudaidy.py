#coding:utf-8
import urllib2
import urllib
import re

class Spider:
    def __init__(self):
        self.baseURL = 'http://www.kuyiyuan.cn'

    def get_page(self, page_url):
        try:
            url = self.baseURL + page_url
            # print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('UTF-8')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print("连接koudaidy失败", e.reason)
                return None
        except urllib2.HTTPError, e:
            if hasattr(e, "code"):
                print e.code
                return None

    def get_content(self, page):
        # print page
        pattern = re.compile('<li data-widget-type="item".*?<a class="flex_video_link" href="(.*?)".*?<img alt="(.*?)" src="(.*?)"', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            new_item = []
            new_item.append(self.baseURL + item[0].encode('UTF-8'))
            new_item.append(item[1].encode('UTF-8'))
            new_item.append(self.baseURL + item[2].encode('UTF-8'))
            contents.append(new_item)
        return contents

def get_data():
    spider = Spider()
    page = spider.get_page('')
    contents = spider.get_content(page)
    return contents
