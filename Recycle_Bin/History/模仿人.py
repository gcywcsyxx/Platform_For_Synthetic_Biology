import urllib.request
 
 
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHtml(file_name, file_content):
    with open(file_name + ".html", "wb") as f:
        f.write(file_content)
 
aurl = "https://www.londonstockexchange.com/news-article/RCP/annual-financial-report/13989778"
html = getHtml(aurl)
saveHtml("wangye", html)

print("success")