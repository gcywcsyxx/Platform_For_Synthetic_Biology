import requests
import sys
import threading
from .spider import Spider

class CNKI(Spider):

    def __init__(self, url:str, headers:dict) -> None:
        self.url = url
        self.headers = headers 

    def _NewHttpRequest(self, url:str, headers:str, method:str, data=None):
        res = super()._NewHttpRequest(self.url, self.headers, method, data)
        return res.json()     

    def Run(self, method: str, data={}) -> None:
        res = self._NewHttpRequest(self.url, self.headers, method, data)
        if not res == None:
            print(res)
        else:
            print("faild!\n")    

    def AsyncRun(self, method:str, keywords:list) -> None:
        """
        get data by muti threads
        """
        threads = []
        for index, data in enumerate(keywords):
            threads.append(threading.Thread(target=self.Run, args=(method, data)))
            threads[index].start()
        for index in range(len(threads)):
            threads[index].join()
