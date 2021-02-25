from abc import ABCMeta, abstractmethod
import requests

class Spider(metaclass=ABCMeta):

    @abstractmethod
    def _NewHttpRequest(self, method:str, data=None):
        try:
            if method == "GET":
                response = requests.get(url=self.url, headers=self.headers, data=data)
            elif method == "POST":
                response = requests.post(url=self.url, headers=self.headers, data=data)
            else:
                print("Invalid method: %s\n", method)
                sys.exit()

            if response.status_code == 200:
                return response
            else:
                return None

        except ConnectionError as err:
             print("error: %s", err)
             sys.exit()  

    @abstractmethod
    def Run(self, method:str, data=None) -> None:
        pass

   