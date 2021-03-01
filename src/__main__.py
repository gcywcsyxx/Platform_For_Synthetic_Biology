from spider import cnki
from spider import weibo
from helper import build

def main(url=None, headers=None, method=None, keywords=None) -> None:
    # example_2 = cnki.CNKI(url, headers)
    # example_2.AsyncRun(method, keywords)
    example_3 = weibo.WeiBo()
    example_3 = example_3.RunComments(headers, "4609879806839971", "storage/test.csv")

if __name__ == '__main__':
    # main(build.BuildCNKIURL(), build.BuildCNKIHeaders(), "POST", build.BuildCNKIKeyWords())
    main(headers=build.BuildWeiBoHeaders())  
    
