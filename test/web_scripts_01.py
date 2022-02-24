# -*- codeing = utf-8 -*-
# @Time: 2/20/22 6:39 PM
# @Author: YinCY
# @File: web_scripts_01.py
# @Software: PyCharm

# 豆瓣电影 top250
# https://movie.douban.com/top250

'''
def main():
    print("hello")

if __name__ == "__main__":
    main()
'''

from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式
import urllib.request, urllib.error # 制定 URL，获取网页数据
import sqlite3 # 进行 SQLite
import xlwt

def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    #1. 爬取网页
    datalist = getData(baseurl)
    savepath = "./豆瓣电影Top250.xlsx"
    saveData(datalist, savepath)

    askURL("https://movie.douban.com/top250?start=0")
    print("Done!")

findLink = re.compile(r'a href="(.*?)">') # 生成正则表达式对象，表示规则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJuge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findDb = re.compile(r'<p class="">(.*?)</p>', re.S)

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url=url)

        # 2. 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_ = "item"):  # 查找符合要求的字符串，形成列表
            data = [] # 保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgsrc = re.findall(findImgSrc, item)[0]
            data.append(imgsrc)

            title = re.findall(findTitle, item)
            if(len(title) == 2):
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            jugeNum = re.findall(findJuge, item)[0]
            data.append(jugeNum)

            inq = re.findall(findInq, item)
            if(len(inq) != 0):
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            db = re.findall(findDb, item)[0]
            db = re.sub('<br(\s+)?/>(\s+)?', " ", db)
            db = re.sub("/", " ", db)
            data.append(db.strip())

            datalist.append(data)
    # print(datalist)
    return datalist


# 得到指定一个 URL 的网页内容
def askURL(url):
    head = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as error:
        if hasattr(error, "code"):
            print(error.code)
        if hasattr(error, "reason"):
            print(error.reason)

    return html

def saveData(datalist, savepath):
    # 3. 保存数据
    print("save...")
    book = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0,8):
        sheet.write(0, i, col[i])

    for i in range(0, 250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)


main()



