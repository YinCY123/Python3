# -*- codeing = utf-8 -*-
# @Time: 2/19/22 9:32 PM
# @Author: YinCY
# @File: tuple.py
# @Software: PyCharm

'''
类似与 list
imutable, 但是可以包含可变对象


tuple1 = ()
# tuple2 = (50) 是 int
tuple2 = (50,)
print(type(tuple1))
print(type(tuple2))


tup1 = ("abc", "def", 2000, 2020)
print(tup1[0])
print(tup1[-1])
print(tup1[1:5])


# 增加
tup1 = (12, 34, 56)
tup2 = ("abc", "xyz")
tup = tup1 + tup2
print(tup)
'''

# 删除， 删除整个变量
tup1 = (12, 34, 56)
print(tup1)
del tup1
print(tup1)

