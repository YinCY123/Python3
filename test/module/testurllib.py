# -*- codeing = utf-8 -*-
# @Time: 2/20/22 9:26 PM
# @Author: YinCY
# @File: testurllib.py
# @Software: PyCharm

import urllib.request

# get
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response)
# print(response.read().decode("utf-8"))

# post
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = "utf-8")
# resposne = urllib.request.urlopen("http://httpbin.org/post", data = data)
# print(resposne.read().decode("utf-8"))

# get
# 超时处理
# try:
#     resposne = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(resposne.read().decode("utf-8"))
# except urllib.error.URLError as error:
#     print("time out")

# resposne = urllib.request.urlopen("http://httpbin.org/get")
# # print(resposne.status)
# print(resposne.getheaders())

# url = "https://httpbin.org/post"
url = "https://movie.douban.com/top250?start=0"
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
# data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding = "utf-8")
req = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

