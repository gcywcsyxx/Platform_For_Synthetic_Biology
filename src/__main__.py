from spider import spider
from helper import build

def main(url:str, headers:dict, method:str, keywords:list) -> None:
    example_2 = spider.Spider(url, headers)
    example_2.AsyncRun(method, keywords)

if __name__ == '__main__':
    main(build.BuildCNKIURL(), build.BuildCNKIHeaders(), "POST", build.BuildCNKIKeyWords())  
