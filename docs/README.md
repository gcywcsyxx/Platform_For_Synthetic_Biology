# 如果不能安装 或者安装后不能运行，可能因为模块需要安装历史版本 新版本可能不可以！
pyLDAvis==2.1.2
streamlit==0.68.0
# 如果python中打不开文件（cannot find...），则需要将文件地址换成完全地址，例如/home/gcy/下载/python结巴分词+云图绘制/可视化工具/Raw_Comment.txt，而不是./或者relative path

# streamlit issues
1、streamlit需要开启wide mode才能显示全缩放的网页
2、开启run on save后 每每保存一次python代码 会自动运行，不用手动刷新了

# LDA模型：需要提前用os调用运行model文件夹中的模型 并在main中输入对应的端口才可在同一个窗口中展示！
注意：windows环境应改成python！！而不是python3
1、data目前只能是标注需要的csv文件，后期可以让其兼容txt 前提是读懂LDA模型文件代码

# 地图绘制 
尽量才从streamlit内置的地图模块！更加清晰 GIS赏心悦目
*streamlit内置知识图谱配置好 展示论文之间的链接关系*
*信息加载时的进度条可视化展示并计时，更像一个成熟的web后端应用!*




### 整体架构
整体分为四个页面，架构为左边sidebar，右边是主要展示区域，宽屏模式！
1、搜索引擎、可视化页面-多种图表、按钮、仪表盘
搜索引擎-合成生物学安全相关名词引擎-十万、百万级数据-mysql数据库
可交互结构化数据图：条形、折线、饼图等等------数据来自网络爬虫json格式和csv格式
云图------数据来自网络，利用jieba分词，处理网上爬的txt云图格式文本，如微博、百度新闻、微信公众号文章、豆瓣评论等
工业级别数学模型------LDA模型------深度数据挖掘
知识图谱----平台内置最好！----NLP社交网络、论文关系、共现图谱分析等
GIS地图----合成生物学区域风险评估--地理位置可视化（红点的密集程度，可表示论文作者的国家、城市）

2、第三方网站的web可视化引用（直接数据参考，而1是经过团队模型的处理）
百度、微博等热搜排行
知网、aminer等网站的实时数据web镜像（集成化）
3、表格页面-meta表格、链表数据还有简单的filter功能
4、团队信息和github地址展示，包括引用的论文来源等等资料-方便评审
###st交互功能###
selectbox
radio
warning
search
tqdm进度条功能


