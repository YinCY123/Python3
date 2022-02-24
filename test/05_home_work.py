# -*- codeing = utf-8 -*-
# @Time: 2/20/22 3:46 PM
# @Author: YinCY
# @File: 05_home_work.py
# @Software: PyCharm
'''
import os
f = open("gushi.txt", mode = "r+")
f.write("日出而作，日如而息。\n凿井而饮，耕田而食。\n帝力于我何有哉。")
content = f.readlines()
print(content)
f.close()
'''

def r(path):
    f = open(path, mode = "r")
    content = f.readlines()
    f.close()
    return str(content)

def w(string, path):
    f = open(path, mode = "w")
    f.write(string)
    f.close()

def fread(path, mode):
    content = r(path)
    f = open("copy.txt", mode = "w")
    f.write(content)
    f.close()
    print("复制完毕")

fread(path="gushi.txt", mode="r+")
