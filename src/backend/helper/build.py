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

def BuildWeiBoURL() -> str:
    return "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%8D%8E%E6%99%A8%E5%AE%87"

def BuildWeiBoHeaders() -> dict:
    return {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": utils.GetUserAgent(),
        "Referer": "https://m.weibo.cn/search?containerid=100103type=1&q=花花".encode("utf-8").decode("latin1"),
        # "Host": "s.weibo.com",
        "Cookie": "_T_WM=49164022889; XSRF-TOKEN=b33953; WEIBOCN_FROM=1110003030; SCF=AkerXndfs-Dk6QlWwOTYTsTq1MTG6cX1N-wik_uYXPUb9JCD2r003vgb8iQhMSiUwrm61E9-UPUJVRpgmgn7lZg.; SUB=_2A25NOJM4DeRhGeBO71IW8SfKyTyIHXVuwj1wrDV6PUJbktANLWffkW1NShKJKG8bLVNVGLSSs-EL9nHD3jaCBH59; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFbSZb88EHpc_7FWnm7OmZ95NHD95QcehB7S024Soz7Ws4DqcjKi--NiKyFiKnEi--Xi-zRiK.Xg5tt; SSOLoginState=1614603112; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D10000011%26fid%3D100103",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "b33953"
    }