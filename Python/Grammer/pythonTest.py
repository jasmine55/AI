#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chapter 2
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://www.douban.com")
# assert "优达学城" in driver.title
element = driver.find_element_by_name("q")
# element.send_keys("python")

print(element)
# element.clear()
# element.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
# chapter 3

# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("file:///Users/mac/Desktop/test.html")
# elements = driver.find_element_by_tag_name("select")
# print(elements)
# all_options = elements.find_elements_by_tag_name('option')
# for options in all_options:
#     print('option is %s' % options.get_attribute("value"))
# driver.close()

# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.get("file:///Users/mac/Desktop/test.html")
# select = Select(driver.find_element_by_tag_name("select"))
# index = select.select_by_index(1)
# text = select.select_by_visible_text("2")
# select.select_by_value("efg")
# select.deselect_all()
# all_selected_options = select.all_selected_options
# print(all_selected_options)
# option = select.options

# print(option)
# print(text)
# print(select)
# driver.close()
