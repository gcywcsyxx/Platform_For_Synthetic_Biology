import spider
import utils

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
    "searchType": "MulityTermsSearch",
    "ParamIsNullOrEmpty": "false",
    "Islegal": "false",
    "Content": "基因合成"
}

def main(url, headers, method, data={}):
    example = spider.Spider(url, headers)
    example.run(method, data)

if __name__ == '__main__':
    main(url, headers, "POST", data=data)  
