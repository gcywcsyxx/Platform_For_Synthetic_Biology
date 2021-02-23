#在命令行操作时，需要使用命令：mysql -u dog -p  然后输入密码123456，来进入这个mysql数据库
"""mysql> create table doc_helper(
    -> id varchar(255),
    -> solution varchar(255)
    -> );
"""
import pymysql 
 
# 打开数据库连接
# Connect to the database
db = pymysql.connect(host='localhost',
                             user='dog',
                             password='123456',
                             database='information_schema',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("use test;")
# 使用 fetchone() 方法获取单条数据.

import xlrd
#xlrd只能读取xls文件（03年），尽量不要搞出xlsx文件！！！
data = xlrd.open_workbook("./bio_ex.xls")
table=data.sheet_by_index(0)
#i[2]和i[3]对应起来最好了

for i in table:
    t=str(i[0])
    t=t[0:240]
    s=str(i[1])
    s=s[0:240]
    print(t)
    sql = "INSERT INTO doc_helper VALUES (%s, %s);"
    val = (t, s)
    cursor.execute(sql, val)

db.commit()  
# 关闭数据库连接



db.close()