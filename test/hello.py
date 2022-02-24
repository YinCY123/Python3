# -*- codeing = utf-8 -*-
# @Time: 2/19/22 12:44 PM
# @Author: YinCY
# @File: hello.py
# @Software: PyCharm

'''
print("hello word!")

import keyword
print(keyword.kwlist)

# 格式化输出
a = 10
print("变量", a)

age = 18
print("我的年龄是： %d 岁"%age)
print("我的名字是%s, 我的国籍是%s"%("小张", "中国"))
print("www", "bing", "com", sep = ".", end = "\t")
print("python", end = "\n") # 换行
print("end")


password = input("请输入密码:")
print("你输入的密码是：", password)
'''

'''
运算符   描述         实例
=       赋值运算      c = a + b
+=      加法赋值运算   c += a 等于 c = c + a
-=      减法赋值运算   c -= a 等于 c = c - a
*=      乘法赋值运算   c *= a 等于 c = c * a
/=      除法赋值运算   c /= a 等于 c = c / a
%=      取模赋值运算   c %= a 等于 c = c % a
**=     幂赋值运算     c **= a 等于 c = c**a
//=     取整除赋值运算  c //= a 等于 c = c // a

Python 指定任何非 0 和非空值为 True, 0 或者 None 为 False
'''

'''
if 1:
    print("True")
else:
    print("False")


score = 77
if score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")


import random
x = random.randint(0, 2) #随机生成 0， 1, 2随机数。
print(x)
'''

