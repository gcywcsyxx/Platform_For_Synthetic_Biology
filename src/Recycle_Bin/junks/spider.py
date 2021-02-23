import xlrd
#xlrd只能读取xls文件（03年），尽量不要搞出xlsx文件！！！
data = xlrd.open_workbook("./bio_ex.xls")
table=data.sheet_by_index(0)
#i[2]和i[3]对应起来最好了
print(table)
print(table[0])

"""m=input("请输入关键词")
for i in table:
    if m in str(i[0]):
        print(i[1])
    else:
        pass"""

https://ilearning.zbgedu.com/#/video?courseId=70ac9476e0ab8b6480f57041a2baf21a&taskId=563d4eb41940b90991b9aff5c81340f3&isSlider=true

task-563d4eb41940b90991b9aff5c81340f3

1、网页解析得到各个taskID 然后嵌入各个网址中 实现300个网页手机
2、使用循环遍历网页 然后在html处提取到blob网址 
3、通过工具集中输入这些网址进行下载