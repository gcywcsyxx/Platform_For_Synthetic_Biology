from spider import cnki
from helper import build

def main(url:str, headers:dict, method:str, keywords:list) -> None:
    example_2 = cnki.CNKI(url, headers)
    example_2.AsyncRun(method, keywords)
    # example_3 = WeiBo(url, headers)
    # example_3 = example_3.Run(method)

if __name__ == '__main__':
    main(build.BuildCNKIURL(), build.BuildCNKIHeaders(), "POST", build.BuildCNKIKeyWords())  
    
