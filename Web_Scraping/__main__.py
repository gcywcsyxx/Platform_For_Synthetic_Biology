def func():
    import spider
    import utils
    import pandas as pd
    url = "https://search.cnki.com.cn/Charts/GetTrendJson"

    headers = {
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

    data = {
        "Content": "基因合成"
    }

    with open("./Data/terminology.csv","r",encoding="utf-8") as f:
        terminology=pd.read_csv(f)

    m=[i for i in terminology["中文名"]]

    keywords=[]
    for i in m:
        dic={}
        dic["Content"]=i
        keywords.append(dic)
    print(keywords)
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
        example_2 = spider.Spider(url, headers)
        example_2.AsyncRun(method, keywords)


    main(url, headers, "POST", keywords)  
