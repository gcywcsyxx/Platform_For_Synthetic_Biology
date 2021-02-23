
def func():
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
    import tqdm

    word_cloud=st.checkbox('词云图')
    if word_cloud:
        st.button("刷新")
        #读取数据
        path = r"./Data/Raw_Comment.txt"
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
        print("已统计完top100词汇...")
        words=[i[0] for i in word_counts_top100]
        #print(words)
        file = open('./Data/Words.txt', 'w')
        for i in range(len(words)):
            file.write(words[i]+"\n")  
        file.close()
        print("已经统计完词频...")
        
        #绘制词云
        my_wordcloud = WordCloud(
            background_color='white',  # 设置背景颜色
            # mask=img,  # 背景图片
            max_words=100,  # 设置最大显示的词数
            stopwords=STOPWORDS,  # 设置停用词
            # 设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载可能会出现问题。
            font_path='./Data/微软雅黑.ttf',
            max_font_size=400,  # 设置字体最大值
            random_state=50,  # 设置随机生成状态，即多少种配色方案
            ##提高清晰度
            width=1000,height=650,
            min_font_size=30,
        ).generate_from_frequencies(word_counts)

        # 显示生成的词云图片
        plt.imshow(my_wordcloud)
        plt.axis('off')
        cloud=plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(cloud)
        plt.savefig("header.png")
func()
        
            
        
        

def func2():
    print("fuck you")