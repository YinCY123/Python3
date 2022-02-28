# -*- codeing = utf-8 -*-
# @Time: 2/24/22 9:07 PM
# @Author: YinCY
# @File: testXwlt.py
# @Software: PyCharm

import xlwt
workbook = xlwt.Workbook(encoding = "utf-8") # 创建 workbook 对象
worksheet = workbook.add_sheet(sheetname="sheet1") # 创建工作表
# worksheet.write(0,0, "hello") # 写入数据
# workbook.save("student.xlsx")

for i in range(1, 10):
    for j in range(1, i+1):
        worksheet.write(i-1,j-1,"%d * %d = %d"%(i, j, i * j))

    workbook.save("student_2022.xlsx")

