# -*- codeing = utf-8 -*-
# @Time: 2/20/22 2:52 PM
# @Author: YinCY
# @File: debug.py
# @Software: PyCharm

'''
# 捕获异常
try:
    print("-----test --- 1----")
    f = open("123.txt", mode="r") # IOError
    print("------test ---- 2----")

    print(num) # NameError
except (IOError, NameError):
    print("产生错误了")



# 捕获错误信息
try:
    print("-----test --- 1----")
    f = open("demo.txt", mode="r") # IOError
    print("------test ---- 2----")

    print(num) # NameError
except (IOError, NameError) as error:
    print("产生错误了")
    print(error)


# 捕获所有的异常
try:
    print("-----test --- 1----")
    f = open("123.txt", mode="r") # IOError
    print("------test ---- 2----")

    print(num) # NameError
except Exception as error:
    print("产生错误了")
    print(error)
'''
import time

try:
    f = open("demo.txt", "r")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as error:
    print(error)

