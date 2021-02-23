
import streamlit as st
import pandas as pd
import re
import jieba
import collections
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import schedule
import time
import mysql.connector
import pymysql 
import streamlit.components.v1 as components
def baidu():
    if st.checkbox("百度热搜"):
        components.iframe("http://top.baidu.com/clip?b=1")
        components.iframe("http://top.baidu.com/clip?b=42")

def weibo():
    weibo=st.checkbox("百度、微博热搜和热闻榜")
    if  weibo:
        st.write("百度热搜Top20")
        components.html(
            """
        <iframe vspace="0" hspace="0" scrolling="yes" frameborder="0" id="clip" name="clip" width="700" height="800" src="http://top.baidu.com/clip?b=1&hd_h_info=1&col=2&line=20"  ></iframe> """,
            height=200,
        )

        st.write("微博热搜榜")
        components.html(
            """
        <div style="width:630px;height:350px;overflow:hidden;border:0px">
        <div style="width:600px;height:600px;margin:-240px 0px 0px -200px;">
        <iframe src="https://s.weibo.com/top/summary" width="800" height="1400" scrolling="yes"></iframe>
        </div>
        </div>    """,
            height=200,
        )

        st.write("微博热闻榜")
        components.html(
            """
        <div style="width:630px;height:350px;overflow:hidden;border:0px">
        <div style="width:600px;height:600px;margin:-240px 0px 0px -200px;">
        <iframe src="https://s.weibo.com/top/summary?cate=socialevent" width="800" height="1400" scrolling="yes"></iframe>
        </div>
        </div>    """,
            height=200,
        )

        


        
