# -*- codeing = utf-8 -*-
# @Time: 2/22/22 9:10 PM
# @Author: YinCY
# @File: testBs4.py
# @Software: PyCharm

'''
BeautifulSoup4 将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是 python 对象，所有对象可以归纳为4种。
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup
file = open("./book.xml", mode="rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# print(type(bs.book))
# print(bs.title.string)
# print(type(bs.title.string))
# print(bs.book.attrs)

# print(type(bs)) # 整个文档的类型
# print(bs.name)
# print(bs)

# 文档的遍历
# print(bs.chapter.contents[0])

import re
# 文档的搜索
# t_list = bs.find_all(re.compile("section"))
# print(t_list)

# def name_is_exist(tag):
#     return tag.has_attr("title")
#
# t_list = bs.find_all(name_is_exist)

t_list = bs.find_all(id = "head")

print(t_list)
