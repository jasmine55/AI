#coding:utf-8

import urllib2
import urllib
import re
class Tools:
    remove_img = re.compile('<img.*?>')
    replace_line = re.compile('<tr>|<div>|</div>|</p>')
    remove_br = re.compile('<br><br>|<br>')
    remove_href = re.compile('<a href=.*?>|</a>')
    replace_td = re.compile('<td>')
    replace_para = re.compile('<p.*?>')
    remove_extra_tag = re.compile('<.*?>')

    def replace(self, item):
        item = re.sub(self.remove_img,"",item)
        item = re.sub(self.remove_br,"\n",item)
        item = re.sub(self.replace_line,"\n",item)
        item = re.sub(self.remove_href,"",item)
        item = re.sub(self.replace_td,"\t", item)
        item = re.sub(self.replace_para,"\n  ", item)
        item = re.sub(self.remove_extra_tag,"", item)
        return item.strip()

class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+ str(seeLZ)
        self.tool = Tools()
        self.file = None

    def get_page(self, page_num):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败，错误原因", e.reason
                return None

    def get_page_title(self, page_num):
        page_content = self.get_page(page_num)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page_content)
        if result:
            #删除空白字符
            return result.group(1).strip()
        else:
            return None


    def get_page_num(self):
        page_content = self.get_page(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page_content)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

    #提取正文内容
    def get_floor_contents(self, page_content):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern, page_content)
        contents = []
        for item in items:
            item = self.tool.replace(item)
            contents.append(item)
        return contents

    def set_file_name(self, page_title):
        if page_title is not None:
            self.file = open(page_title + '.txt','w+')
        else:
            self.file = open('default' + '.txt', 'w+')

    def save_content_to_file(self, content):
        floor_tag = 1
        for floor_content in content:
            floor_msg = '\n' + str(floor_tag) + '楼' + "---------------------------------------------------------------------------------------------------------"
            self.file.write(floor_msg)
            self.file.write(floor_content)
            floor_tag += 1

base_url = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(base_url, 1)
page_content = bdtb.get_page(1)
page_title = bdtb.get_page_title(1)
bdtb.set_file_name(page_title)

floor_contents = bdtb.get_floor_contents(page_content)
bdtb.save_content_to_file(floor_contents)
