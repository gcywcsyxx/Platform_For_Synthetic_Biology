
import pandas as pd
import re
import jieba
import collections
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import schedule
import time
import mysql.connector
import pymysql 
import streamlit.components.v1 as components
from tqdm import tqdm
#刷新按钮，自动更新数据
st.button("更新数据源")
"""
调用tqdm，程序运行步骤在网站进行进度条展示，让爬虫进度可视化
"""
#热榜集合网站 很好！   https://tophub.today/
# 打开数据库连接
# Connect to the database
db = pymysql.connect(host='localhost',
                             user='dog',
                             password='123456',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("use test;")
box=st.text_input('搜索引擎')
ex=cursor.execute("select * from doc_helper where id like '%%%s%%';"%box)
myresult = cursor.fetchall()
st.subheader("搜索结果：")
if True:#打印前两个搜索结果
    st.write(myresult[0])
    st.write(myresult[1])


#百度内置定制榜单形式可变 网址： http://top.baidu.com/add

import baiwei_hot_search
baiwei_hot_search.baidu()
baiwei_hot_search.weibo()

#开始部署关键词云图
import Word_Cloud
Word_Cloud.func()


#开始部署LDA预览图（需要运行并接入本地接口），将本地接口接入streamlit主界面的小窗口中
import os
LDA_MODEL=st.checkbox("LDA Model")
if LDA_MODEL:
    os.system("python3 ./LDA.py")
    #选中才开始执行LDA模型文件 注意：windows环境应改成python！！
    box=st.text_input('端口号')
    components.iframe("http://127.0.0.1:%s/#topic=3&lambda=0.12&term="%box,width=1150,height=800,scrolling=True)


#开始部署名知网论文数量图
import CNKI









