import requests
import sys

class Spider:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers 

    def __NewHttpRequest(self, method, data={}):
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

    def run(self, method, data={}):
        res = self.__NewHttpRequest(method, data)
        if not res == None:
            print(res)
        else:
            print("faild!\n")              