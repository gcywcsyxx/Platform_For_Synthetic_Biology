import random

user_agent_pool = [
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/603.1.30',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]


def GetUserAgent() -> str:
    return random.choice(user_agent_pool)
import requests
import sys
import threading
import pandas as pd
import streamlit as st
year_data=[]
class Spider:
    
    
    def __init__(self, url:str, headers:dict):
        self.url = url
        self.headers = headers 

    def __NewHttpRequest(self, method:str, data={}) -> str:
        try:
            if method == "GET":
                response = requests.get(url=self.url, headers=self.headers, data=data)
            elif method == "POST":
                response = requests.post(url=self.url, headers=self.headers, data=data)
            else:
                print("Invalid method: %s\n", method)
                sys.exit()

            if response.status_code == 200:
                return response.json()
            else:
                return None

        except ConnectionError as err:
             print("error: %s", err)
             sys.exit()       

    def Run(self, method:str, data={}):
        res = self.__NewHttpRequest(method, data)
        
        t=-1
        if not res == None:
            """print(
                list(res.values())[2],
                (list(int(i) for i in list(list(res.values())[3][0].values())[2]))#超级嵌套
                )"""
            
            data=list(int(i) for i in list(list(res.values())[3][0].values())[2])
            year=list(res.values())[2]
            with open("/home/gcy/下载/Platform_For_Biology_Synthetic/Data/terminology.csv","r",encoding="utf-8") as f:
                terminology=pd.read_csv(f)

            m=[i for i in terminology["中文名"]]
            t+=1
            #print(m)
            year_data.append(year)
            data.append(data)
            import csv

            with open("Data/terminology_data.csv","a") as f:
                writer = csv.writer(f)
                writer.writerow([m[t],year ,data])
            
           
            
        
              
        else:
            print("faild!\n")    
        
    

    def AsyncRun(self, method:str, keywords:list):
        for _, data in enumerate(keywords):
            thread_s = threading.Thread(target=self.Run, args=(method, data))
            thread_s.start()
    


#print(year_data)

def func():
    
    import pandas as pd
    url = "https://search.cnki.com.cn/Charts/GetTrendJson"

    headers = {
        "User-Agent": GetUserAgent(),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "SID=110105; KEYWORD=%E5%9F%BA%E5%9B%A0%E5%90%88%E6%88%90",
        "Host": "search.cnki.com.cn",
        "Origin": "https://search.cnki.com.cn",
        "Referer": "https://search.cnki.com.cn/Search/Result",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = {
        "Content": "基因合成"
    }

    with open("/home/gcy/下载/Platform_For_Biology_Synthetic/Data/terminology.csv","r",encoding="utf-8") as f:
        terminology=pd.read_csv(f)

    m=[i for i in terminology["中文名"]]

    keywords=[]
    for i in m:
        dic={}
        dic["Content"]=i
        keywords.append(dic)
    #print(keywords)
    """keywords=[
            {"Content": "基因合成"},
            {"Content": "云计算"},
            {"Content": "数据挖掘"},
            {"Content": "深度学习"},
            {"Content": "嵌入式系统"}
    ]"""

    def main(url:str, headers:dict, method:str, keywords:list):
        # example = spider.Spider(url, headers)
        # example.Run(method, data)
        example_2 = Spider(url, headers)
        example_2.AsyncRun(method, keywords)


    main(url, headers, "POST", keywords)  
    
func()
url="/home/gcy/下载/Platform_For_Biology_Synthetic/"
with open("%sData/terminology.csv"%(url),"r",encoding="utf-8") as f:
        terminology=pd.read_csv(f)

m=[i for i in terminology["中文名"]]
#下面进行#数据去重
from more_itertools import unique_everseen
with open('%sData/terminology_data.csv'%(url),'r') as f, open('%sData/2.csv'%(url),'w') as out_file:
    out_file.writelines(unique_everseen(f))

with open("%sData/2.csv"%(url),"r") as f:
    data=pd.read_csv(f)
#print(eval(data["数据"][2])[0:-1])
chosen = st.radio(
    '名词选择',
    (m))
if chosen:
    st.write(m.index(f"{chosen}"))
    num=m.index(f"{chosen}")
    chart_data = pd.DataFrame(
        eval(data["数据"][num])[0:-1],
        eval(data["年份"][num])
    )
    st.write(f"{chosen}主题论文数量变化")
    st.line_chart(chart_data)
