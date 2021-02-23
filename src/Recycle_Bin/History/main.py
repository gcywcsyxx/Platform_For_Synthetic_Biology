
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


st.subheader("The map")
import pandas as pd
import numpy as np 
map_data = pd.DataFrame(
    (np.random.randn(1000, 2)*200) / [5, 5] + [-39.76, 102.4],
    
    columns=['lat', 'lon'])
st.write(np.random.randn(10, 2))
#随机数1000个 2个维度
# 50和50是横向和纵向的分布范围50 50代表大约是圆形  50代表点的大小 越小则点越小   
# 后面左边是纬度中心 右边是经度中心
st.map(map_data)

#设置三列按钮 也可以两列按钮 在同一行上！
left_column, middle_column,right_column = st.beta_columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')
middle_column.button("fuck this")
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)























#热榜集合网站 很好！   https://tophub.today/
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

box=st.text_input('Enter some text')
ex=cursor.execute("select * from doc_helper where id like '%%%s%%';"%box)

myresult = cursor.fetchall()
#print(myresult)
st.write(myresult)
