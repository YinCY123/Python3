# -*- codeing = utf-8 -*-
# @Time: 2/19/22 3:05 PM
# @Author: YinCY
# @File: 02_home_work.py
# @Software: PyCharm

'''
# 1 - 100 求和
s = 0
i = 1
while i < 101:
    s += i
    i += 1

print(s)


s = 0
for i in range(101):
    s += i

print(s)
'''

count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")