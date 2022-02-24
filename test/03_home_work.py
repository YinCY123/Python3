# -*- codeing = utf-8 -*-
# @Time: 2/19/22 3:22 PM
# @Author: YinCY
# @File: 03_home_work.py
# @Software: PyCharm

# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d"%(i,j, i * j), end = "\t")
        if i == j:
            print(end = "\n")

print("-"* 80)

i = 1
j = 1
while i < 10:
    for j in range(1, i + 1):
        print("%d * %d = %d"%(i, j, i * j), end = "  ")
        j += 1
    print(end = "\n")
    i += 1