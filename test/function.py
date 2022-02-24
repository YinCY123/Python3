# -*- codeing = utf-8 -*-
# @Time: 2/19/22 10:28 PM
# @Author: YinCY
# @File: function.py
# @Software: PyCharm

'''
def add2Num(a, b):
    c = a + b
    print(c)

add2Num(11, 22)


def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu

sh, yu = divid(5, 2)
print(sh, yu)
'''

def hl():
    print("-"*20)


def mhl(a = 1):
    for i in range(a):
        hl()

mhl(a = 3)

def add3(a, b, c):
    sum = a + b + c
    return sum

s = add3(1, 2, 3)
print(s)

def avg(a, b, c):
    return add3(a, b, c) / 3

a = avg(1, 2, 3)
print(a)



