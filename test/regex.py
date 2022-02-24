# -*- codeing = utf-8 -*-
# @Time: 2/23/22 8:23 PM
# @Author: YinCY
# @File: regex.py
# @Software: PyCharm

'''
操作符      说明
.          表示任何单个字符
[]         字符集，对单个字符给出取值范围
[^]        非字符集，对单个字符给出排除范围
*          前一个字符0次或无限次扩展
+          前一个字符1次或无限次扩展
?          前一个字符0次或一次扩展
|          左右表达式任意一个
{m}        扩展前一个字符m次
{m,n}      扩展前一个字符 m 到 n 次（包含）
^          匹配开头
$          结尾
()         分组标记，内部只能使用 | 操作符
\d         数字
\w         单词字符，等价于[A-Za-z0-9_]


函数                说明
re.search()         在一个字符串中搜索匹配正则表达式的第一个位置，返回 match 对象
re.match()          从一个字符串的开始位置起匹配正则表达式，返回 match 对象
re.findall()        搜索字符串，以列表类型返回全部能匹配的子串
re.split()          将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()       搜索字符串，返回一个匹配结果的迭代类型，每次迭代元素是 match 对象
re.sub()            在一个字符串中替换掉所有正则表达式的子串，返回替换后的字符串


修饰符      描述
re.l       使匹配对大小写敏感
re.L       做本地化识别 (local-aware) 匹配
re.M       多行匹配，影响 ^ 和 $
re.S       使 . 匹配包括换行在内的所有字符
re.U       根据 Unicode 字符解析字符。这个标志影响 \w, \W, \b, \B
re.X       该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
'''

import re
# pattern = re.compile("AA") # AA 是正则表达式
# # m = pattern.search("ABCAADDCCAAA")
# m = re.search("asd", "Aasd")
# print(m)

# print(re.findall("[A-Z]", "ASDadfGaA"))
# print(re.findall("[A-Z]+", "ASDadfGaA"))

# print(re.sub("a", "A", "abcDasghaA"))
a = r"\aabd-\'"
print(a)

