# -*- codeing = utf-8 -*-
# @Time: 2/24/22 9:41 PM
# @Author: YinCY
# @File: testSqlite.py
# @Software: PyCharm

import sqlite3

conn = sqlite3.connect(database="test.db") # 打开或创建数据库

print("Opened database successfully")
c = conn.cursor() # 获取游标
sql = '''
    create table company
        (id int not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''

sql1 = '''
    insert into company (id, name, age, address, salary)
    values (1, "张三", 30, "成都", 8000) 
'''

sql2 = '''
    insert into company (id, name, age, address, salary)
    values (2, "李四", 32, "重庆", 15000)
'''

# c.execute(sql)    # 执行 SQL
c.execute(sql1)
c.execute(sql2)
conn.commit()     # 提交数据库操作

cursor = c.execute(sql)
for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3], end = "\n")

conn.close()      # 关闭数据库

print("add sheet successfully")

