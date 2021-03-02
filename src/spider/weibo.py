import json
import sys
import time
import re
import csv
import threading

from bs4 import BeautifulSoup
from .spider import Spider


class WeiBo(Spider):
    
    def __init__(self) -> None:
        pass

    def _NewHttpRequest(self, url:str, headers: str, method:str, data=None):
        res = super()._NewHttpRequest(url, headers, method, data=data)
        return res

    def Get(self, url:str, headers:dict, data=None):
        return self._NewHttpRequest(url, headers, "GET", data=data)

    def Post(self, url:str, headers:dict, data=None):
        return self._NewHttpRequest(url, headers, "POST", data=data)    

    def Parse(self, dom:str) -> list :
        soup = BeautifulSoup(dom, "html.parser")
        cards = soup.find_all("div", class_ = "card-main")
        for item in cards:
            yield {
                "content": item.find("div", class_ = "weibo-text").text
            }

    def ParseCommentsJson(self, data: str):
        return json.loads(data)

    def GetCommentByID(self, url:str, headers:dict) -> str:
        data = self.Get(url, headers, None)
        return data.json()

    def GenerateData(self, data:list) -> list:
        ret = []    
        for item in data:
            pattern = re.compile(r'<[^>]+>',re.S)
            each = {
                'nickname': item['user']['screen_name'],
                'comment': pattern.sub('',item['text'])
            }
            ret.append(each)
        return ret

    def StoreData(self, file):
        print("Start store data into csv......")
        while len(self.comments_data) == 0:
            time.sleep(1)

        while len(self.comments_data) > 0:
            with open(file, 'a+', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["nickname", "comment"])
                for item in self.comments_data:
                    for each in item:
                        writer.writerow([each["nickname"],each["comment"]])
                self.comments_data = []




    def RunComments(self, headers, id, file):
        self.comments_data = []
        # Request first page
        url = "https://m.weibo.cn/comments/hotflow?"+"id="+str(id)+"&"+"mid="+str(id)
        ret = self.GetCommentByID(url, headers)
        if ret["ok"] == 1:
            data = ret["data"]
            res = data["data"]
            max_id = data["max_id"]
            comments = self.GenerateData(res)
            self.comments_data.append(comments)
            # print(comments)
            print("Please wait......")
            time.sleep(1)
            while max_id != None:
                url = "https://m.weibo.cn/comments/hotflow?"+"id="+str(id)+"&"+"mid="+str(id)+"&"+"max_id="+str(max_id)
                ret = self.GetCommentByID(url, headers)
                if ret["ok"] == 1:
                    data = ret["data"]
                    res = data["data"]
                    max_id = data["max_id"]
                    comments = self.GenerateData(res)
                    self.comments_data.append(comments)
                    # print(comments)
                    print("Please wait......")
                    time.sleep(1)
                else:
                    # Store data into csv
                    self.StoreData(file)    

                    print("Fail to request comments")
                    sys.exit()

        else: 
            print("Fail to request comments")
            sys.exit()

    """
    Mutiple threads to run program to get data
    """
    def MutiRunComments(self, headers:str, id_list:list, file_list:list) -> None:
        thread_list = []
        length = len(id_list):
        for i in range(length):
            thread_list.append(threading.Thread(target=self.RunComments, args=(headers, id_list[i], file_list[i])))
            thread_list[i].start()

        for i in range(length):
            thread_list[i].join()    






    def Run(self, method: str, data=None) -> None:
       response = self._NewHttpRequest(method, data=data)
       res = self.parse(response.text)
       for item in res:
           print(item)
              


