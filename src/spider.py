import requests
import sys
import threading

class Spider:

    def __init__(self, url:str, headers:dict):
        self.url = url
        self.headers = headers 

    def _NewHttpRequest(self, method:str, data={}) -> str:
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
        res = self._NewHttpRequest(method, data)
        if not res == None:
            print(res)
        else:
            print("faild!\n")    

    def AsyncRun(self, method:str, keywords:list):
        threads = []
        for index, data in enumerate(keywords):
            threads.append(threading.Thread(target=self.Run, args=(method, data)))
            threads[index].start()
        for index in range(len(threads)):
            threads[index].join()
