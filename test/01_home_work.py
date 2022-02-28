# -*- codeing = utf-8 -*-
# @Time: 2/19/22 2:41 PM
# @Author: YinCY
# @File: 01_home_work.py
# @Software: PyCharm

import random
# 剪刀(0), 石头(1), 布(2)
l = [0, 1, 2]
a = input("你输入的是：")
if a in ["0", "1", "2"]:
    a = int(a)
else:
    print("你输入的内容有误，请输入0, 1 或者 2。")

x = random.randint(0, 2)

if a not in l:
    exit()
else:
    if a == 0:
        print("你输入的是：剪刀(0)")
    elif a == 1:
        print("你输入的是：石头(1)")
    elif a == 2:
        print("你输入的是：布(2)")

print("随机生成的数字为：", x)

if a > x or (a == 0 and x == 2):
    print("恭喜你赢了。")
elif x == a:
    print("打平了。")
else:
    print("哈哈， 你输了。")