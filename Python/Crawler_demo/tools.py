
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
