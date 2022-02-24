# -*- codeing = utf-8 -*-
# @Time: 2/19/22 9:48 PM
# @Author: YinCY
# @File: dict.py
# @Software: PyCharm

'''
无序对象集合，使用键值对存储（key-value）
key 必须使用不可变类型
在同一个字典中，key 必须是唯一的


info = {"name":"吴彦祖", "age":18}
print(info["name"])
print(info["age"])
print(info.get("gender", "NA"))
print(info.get("name"))


#增加
info = {"name":"吴彦祖", "age":18}
newid = input("请输入ID:")
info["id"] = newid
print(info.get("id"))


# del
info = {"name":"吴彦祖", "age":18}
print(info.get("name"))
del info["name"]
print(info.get("name"))

info = {"name":"吴彦祖", "age":18}
del info
print(info)

# clear
info = {"name":"吴彦祖", "age":18}
print(info)
info.clear()
print(info)


# 修改
info = {"name":"吴彦祖", "age":18, "id":1102}
info["age"] = 20
print(info["age"])

print(info.keys())
print(info.values())
print(info.items())


info = {"name":"吴彦祖", "age":18, "id":1102}
for key in info.keys():
    print(key)

for value in info.values():
    print(value)

for key, value in info.items():
    print("key = %s, value = %s"%(key, value))
'''

mylist = ["a", "b", "c", "d"]
print(enumerate(mylist))

for i, x in enumerate(mylist):
    print(i, x)





