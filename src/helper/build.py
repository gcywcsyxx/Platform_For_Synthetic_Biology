"""
This file to build struct for test
"""

from spider import utils
import pandas as pd

def BuildCNKIURL() -> str:
    return "https://search.cnki.com.cn/Charts/GetTrendJson"

def BuildCNKIKeyWords() -> list:
    with open("./storage/terminology.csv","r",encoding="utf-8") as f:
        terminology=pd.read_csv(f)
        m=[i for i in terminology["KeyWord"]]
        keywords=[]
        for i in m:
            dic={}
            dic["Content"]=i
            keywords.append(dic)
        return keywords

def BuildCNKIHeaders() -> dict:
    return {
        "User-Agent": utils.GetUserAgent(),
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
