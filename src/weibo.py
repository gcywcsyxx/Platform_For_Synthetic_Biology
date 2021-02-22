import spider
import pyquery


class WeiBo(spider.Spider):
    
    def __init__(self, url:str, headers:dict):
        super(WeiBo, self).__init__(url, headers)
        self.username = username
        self.password = password
        self.login_url = ""

    """
    TODO: login
    """
    def __login():
        print("hello")

    def __request(self, data->str) -> str:
        data = self._NewHttpRequest("GET", data=data)
        return data    

    """
    TODO: parse html to extract information
    """
    def __parse(self, dom:str) -> list:
        return []


