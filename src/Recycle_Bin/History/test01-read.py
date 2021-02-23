
import pandas as pd

#读取数据
f = open("/home/gcy/下载/Python-for-Data-Mining/blog28-LDA&pyLDAvis/data.csv",encoding='utf-8')
df = pd.read_csv(f)
print(df.shape)         #查看数据维度
print(df.head())        #查看前几行数据
