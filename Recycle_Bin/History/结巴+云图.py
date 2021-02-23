
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
st.title('My title')
st.header('My header')
st.subheader('The Wordcloud')
st.button('Hit me')
st.checkbox('Check me out')
#读取数据
path = r"Raw_Comment.txt"
with open(path) as f:
    data = f.read()


# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
data = re.sub(pattern, '', data)


# 文本分词--精确模式分词
seg_list_exact  = jieba.cut(data,cut_all = False)


object_list = []
# 自定义常见去除词库
remove_words =[]
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我们',u'需要']

for word in seg_list_exact:
    if word not in remove_words:
        object_list.append(word)

#去除单个词
for i in range(len(object_list)-1,-1,-1):
    if(len(object_list[i])<3):
        object_list.pop(i)

# 对分词做词频统计
word_counts = collections.Counter(object_list)
# 获取前100最高频的词
word_counts_top100 = word_counts.most_common(100)
print(word_counts_top100)
st.button("dfvd")
ter=open('ter.txt',mode='w')
words=[]
for i in word_counts_top100:
    words.append(i[0])
print(words)
file = open('ter.txt', 'w')
for i in range(len(words)):
    file.write(words[i]+"\n")
    
file.close()


"""
#读取积极、消极词库
negPath = r"ntusd-negative.txt"#这里是负面词汇数据库 需要自己 里面全是负面词汇
posPath = r"ntusd-positive.txt"#这里面是正面词汇数据库 需要自己写 里面全是好的词语
pos = open(posPath, encoding='utf-8').readlines()
neg = open(negPath, encoding='utf-8').readlines()
#统计积极、消极词
for i in range(len(pos)):
    pos[i] = pos[i].replace('\n','').replace('\ufeff','')
for i in range(len(neg)):
    neg[i] = neg[i].replace('\n','').replace('\ufeff','')
posNum = negNum = 0
for i in range(len(object_list)):
    if(object_list[i] in pos):
        posNum = posNum + 1
    elif(object_list[i] in neg):
        negNum = negNum + 1
print('posNum:',posNum)
print('negNum:',negNum)
"""
#绘制词云
my_wordcloud = WordCloud(
    background_color='white',  # 设置背景颜色
    # mask=img,  # 背景图片
    max_words=200,  # 设置最大显示的词数
    stopwords=STOPWORDS,  # 设置停用词
    # 设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载可能会出现问题。
    font_path='./微软雅黑.ttf',
    max_font_size=400,  # 设置字体最大值
    random_state=50,  # 设置随机生成状态，即多少种配色方案
    ##提高清晰度
    width=2560,height=1080,
    min_font_size=40,
).generate_from_frequencies(word_counts)

# 显示生成的词云图片
plt.imshow(my_wordcloud)

plt.axis('off')
st.pyplot()

plt.savefig("header.png")
plt.show()
st.image('./header.png')
