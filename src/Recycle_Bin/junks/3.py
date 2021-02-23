#xpath全名Xml Path Language(xml路径语言)，说实话，我没用过xpath，现学现卖。
#https://blog.csdn.net/CatchLight/article/details/113623014

#在原生爬虫中，lxml封装的xpath，相对于bs4封装的css性能要好，所以很多人选择使用xpath。在爬虫框架scrapy中，其底层使用的是parsel封装的选择器，css规则最终也会转换成xpath去选择元素，所以css会比xpath慢，因为转换是需要耗时的，但是微乎其微，在实际爬虫程序中基本上感知不到。

import requests
from lxml.html import etree

url = 'https://v.qq.com/detail/m/m441e3rjq9kwpsc.html'
response = requests.get(url)
response_demo = etree.HTML(response.text)
print(response_demo)
# 选择_stat属性为info:title的a元素，/text()表示输出选中的a元素的文本内容
# <a _stat="info:title>斗罗大陆</a>，结果是输出 斗罗大陆
name = response_demo.xpath('//a[@_stat="info:title"]/text()')
# *表示所有节点，所有class="type_txt"的节点的文本
type_txt = response_demo.xpath('//*[@class="type_txt"]/text()')
tag = response_demo.xpath('//*[@class="tag"]/text()')
describe = response_demo.xpath('//*[@class="txt _desc_txt_lineHight"]/text()')
print(name, type_txt, tag, describe, sep='\n')