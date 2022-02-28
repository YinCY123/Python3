# -*- codeing = utf-8 -*-
# @Time: 2/19/22 9:14 PM
# @Author: YinCY
# @File: 04_home_work.py
# @Software: PyCharm
products = [["iphone", 6888],
           ["MacPro", 14800],
           ["小米", 2499],
           ["Coffee", 31],
           ["Book", 61],
           ["Nike", 699]]

n = 0
print("-" * 6, "商品列表", "-" * 6)
for product in products:
    print(n, product[0], product[1])
    n += 1

