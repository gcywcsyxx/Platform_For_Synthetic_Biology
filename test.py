"""import pandas as pd
with open("./Data/terminology.csv","r",encoding="utf-8") as f:
    terminology=pd.read_csv(f)

m=[i for i in terminology["中文名"]]

keywords=[]
for i in m:
    dic={}
    dic["Content"]=i
    keywords.append(dic)
print(keywords)"""
import streamlit as st
import pandas as pd
#import CNKI
#CNKI.func()
res={'ResultCode': 200, 'title': '发文', 'xAxisData': ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'], 'series': [{'name': '发文', 'type': 'line', 'data': ['54', '64', '54', '47', '63', '41', '27', '41', '89', '9']}]}
res2={'ResultCode': 200, 'title': '发文', 'xAxisData': ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'], 'series': [{'name': '发文', 'type': 'line', 'data': ['54', '64', '54', '47', '63', '41', '27', '41', '89', '9']}]}
rest=[res]
rest.append(res2)
print(rest)
print(
    list(res.values())[2],
    (list(int(i) for i in list(list(res.values())[3][0].values())[2]))#超级嵌套
    )
chart_data = pd.DataFrame(
    (list(int(i) for i in list(list(res.values())[3][0].values())[2])),
     list(res.values())[2]
)
st.line_chart(chart_data)

with open("Data/terminology_data.csv","r") as f:
    data=pd.read_csv(f)
print(eval(data["数据"][2])[0:-1])