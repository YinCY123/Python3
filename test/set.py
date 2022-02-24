# -*- codeing = utf-8 -*-
# @Time: 2/19/22 10:22 PM
# @Author: YinCY
# @File: set.py
# @Software: PyCharm

'''
set 类似与 dict, 是 key 的集合， 但不储存 value, key 不能重复
set 是无序的， 重复的元素自动被过滤掉
'''

s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 4])
print(s)

