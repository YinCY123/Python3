# -*- codeing = utf-8 -*-
# @Time: 2/19/22 7:20 PM
# @Author: YinCY
# @File: list.py
# @Software: PyCharm

'''
1. 列表的元素类型可以不同
2. mutable
'''

'''
namelist = ["小张", "小王", "小李"]
print(namelist[0])
print(namelist[1])
print(namelist[2])

# append
nametemp = input("请输入学生名字：")
namelist.append(nametemp)
for name in namelist:
    print(name)

a = [1, 2]
b = [3, 4]
a.append(b)
print(a)

# extend, 将b list 中的元素逐个加入到 a list
a.extend(b)
print(a)

# insert
a = [0, 1, 2]
a.insert(1, 3)
print(a)


# del
movie_name = ["加勒比海盗", "骇可帝国", "速度与激情", "指环王", "拳王"]
del movie_name[0]

for name in movie_name:
    print(name)


# pop, 弹出末尾元素
movie_name = ["加勒比海盗", "骇可帝国", "速度与激情", "指环王", "拳王"]
movie_name.pop()

for name in movie_name:
    print(name)

# remove, 删除指定元素
movie_name = ["加勒比海盗", "骇可帝国", "速度与激情", "指环王", "拳王", "指环王"]
movie_name.remove("指环王")

for name in movie_name:
    print(name)


# 修改
movie_name = ["加勒比海盗", "骇可帝国", "速度与激情", "指环王", "拳王"]
movie_name[1] = "战士"
for name in movie_name:
    print(name)


# 查， in, not in
movie_name = ["加勒比海盗", "骇可帝国", "速度与激情", "指环王", "拳王"]
findName = input("要查找的名字")
if findName in movie_name:
    print("找到")
else:
    print("没有找到")


a = ["a", "b", "c", "a", "b"]
print(a.index("a", 1, 4))


# count
a = ["a", "b", "c", "a", "b"]
print(a.count("a"))


# sort
a = [1, 3, 2, 4]
print(a)
a.sort(reverse=True)
print(a)

# reverse
a = [1, 3, 2, 4]
a.reverse()
print(a)


# 嵌套
schoolnames = [["a", "b", "c"], ["d", "e"], ["m", "o", "p"]] # 有三个空元素的空列表
#print(schoolnames[0][0])

for i in schoolnames:
    length = len(i)
    for j in range(length):
        print(i[j], end = "\t")
    print(end = "\n")
'''
import random
offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室 %d 的人数为：%d"%(i, len(office)))
    for name in office:
        print(name, end = "\t")
    print("\n")
    print("-"*20)

