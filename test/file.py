# -*- codeing = utf-8 -*-
# @Time: 2/20/22 1:47 PM
# @Author: YinCY
# @File: file.py
# @Software: PyCharm

'''
# 打开文件
f = open("test.txt", mode="w") # w - write
# 写入内容
f.write("hello world, i'm here.")
# 关闭文件
f.close()

read 读取指定的字符，每执行一次指针向后移动指定的字符个数。
f = open("test.txt", mode = "r")
content = f.read(5)
print(content)

content = f.read(5)
print(content)
f.close()


f = open("test.txt", "r")
# content = f.readline()
content = f.readlines()
print(content)
f.close()


i = 1
for temp in content:
    print("%d: "%i, temp)
    i +=1


f = open("test.txt", "r")
content = f.readline()
print(content, end = "")

content = f.readline()
print(content)
f.close()

# os 模块可以对文件进行重命名，删除等一些操作。
import os
# os.rename("test.txt", "demo.txt")
# print(os.listdir("./"))
# print(os.environ)
# print(os.getcwd())
# print(os.fsencode("demo.txt"))
print(os.fsdecode("demo.txt"))
'''


'''
访问模式
r - 以读的方式打开
w - 打开文件只用于写入，如果该文件存在则被覆盖。如果不存在则创建新的文件。
a - 打开一个文件用于追加。如果文件存在，从文件末尾追加。如果文件不存在，则创建新的文件。
rb - 以二进制格式打开文件用于只读。文件指针默认放到文件的开头。
wb - 以二进制格式打开一个文件用于写入。如果文件已存在则被覆盖，如果不存在创建新的文件。
ab - 以二进制格式打开一个文件用于追加。如果文件存在，文件指针放在文件的结尾。如果文件不存在，创建新的文件写入。
r+ - 打开一个文件用于读写。文件指针放到文件的开头。
w+ - 打开一个文件用于读写。如果文件存在则被覆盖。如果文件不存在，创建新的文件。
a+ - 打开一个文件用于读写。如果文件以存在，文件指针会放在文件的末尾。文件打开时会是追加的模式。如果文件不存在，创建新的文件。
'''



