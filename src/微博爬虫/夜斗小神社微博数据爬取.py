import requests
import json
from tqdm import tqdm
import datetime
import time
import random
import csv
import threading


# 一条主微博链接部分评论, 需要构造参数max_id获取全部ajax
up_main_url = 'https://m.weibo.cn/comments/hotflow?id=4596226979532970&mid=4596226979532970&max_id_type=0'
up_second_url = 'https://m.weibo.cn/comments/hotFlowChild?cid=4596227151498853&max_id=0&max_id_type=0'
headers = {
        # ua代理
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        # 登录信息
        'cookie': 'SINAGLOBAL=5702871423690.898.1595515471453; SCF=Ah2tNvhR8eWX01S-DmF8uwYWORUbgfA0U3GnciJplYvqE1sn2zJtPdkJ9ork9dAVV8G7m-9kbF-PwIHsf3jHsUw.; SUB=_2A25NDifYDeRhGeBK7lYS9ifFwjSIHXVu8UmQrDV8PUJbkNANLRmlkW1NR7rne18NXZNqVxsfD3DngazoVlT-Fvpf; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhhI1TcfcjnxZJInnV-kd405NHD95QcSh-Xe0q41K.RWs4DqcjQi--ciK.RiKLsi--Ni-24i-iWi--Xi-z4iKyFi--fi-2XiKLhSKeEeBtt; wvr=6; _s_tentry=www.sogou.com; UOR=,,www.sogou.com; Apache=9073188868783.379.1611369496580; ULV=1611369496594:3:3:3:9073188868783.379.1611369496580:1611281802597; webim_unReadCount=%7B%22time%22%3A1611369649613%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A63%2C%22msgbox%22%3A0%7D'
    }

max_id_list = []  # 保存构造主评论ajax参数得max_id
max_id_url_list = []  # 保存主评论ajax链接
cid_list = []  # 保存cid参数
second_max_id_list = []  # 子评论max_id参数
second_max_id_url_list = []  # 子评论ajax链接


# 基本请求访问获取json数据
def requests_json(url):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        text = response.text.encode("gbk", "ignore").decode("gbk", "ignore")  # 解决报错双重严格限制
        content = json.loads(text)  # 将文本转为json格式

        return content


# 获取构造ajax主评论url全部max_id参数
def main_max_id():
    # 以没有内容报错作为终止条件break跳出
    while len(max_id_url_list) < 200:
        print("正在休眠中")
        time.sleep(random.randint(1, 3))  # 休眠
        print("休眠完毕啦")
        if (len(max_id_list) == 0):
            main_url = 'https://m.weibo.cn/comments/hotflow?id=4596226979532970&mid=4596226979532970&max_id_type=0'
            max_id_url_list.append(main_url)
        else:
            main_url = f'https://m.weibo.cn/comments/hotflow?id=4596226979532970&mid=4596226979532970&max_id={max_id_list[-1]}&max_id_type=0'
            max_id_url_list.append(main_url)
        try:
            content = requests_json(main_url)
            max_id = content['data']["max_id"]  # 获得主评论需要得参数max_id来构造url链接
            max_id_list.append(max_id)
            # TODO: 写一个终止条件, 什么时候不在获取max_id
            data = content['data']['data']  # 获取评论列表
            for comment in data:  # 循环遍历
                cid = comment["id"]  # 二级评论url构造所需id
                cid_list.append(cid)  # 添加
        except:
            print("最后一条max_id打底啦！该跳出走人咯！")
            break


# 获取子评论所需的max_id
def second_max_id():
    try:
        # TODO: 以每一个cid参数为基准一路往下延续获取max_id
        for cid in cid_list:
            # 10这个数字可以自己调整, 这里只获取十条
            while len(second_max_id_url_list) < 10:
                time.sleep(3)  # 休眠防止被反爬
                print('休眠->>>>>>>>>>>>>>>')
                time.sleep(random.random())  # 休眠

                if (len(second_max_id_list) == 0):
                    up_second_url = 'https://m.weibo.cn/comments/hotFlowChild?cid=4596227151498853&max_id=0&max_id_type=0'
                    second_max_id_url_list.append(up_second_url)
                else:
                    up_second_url = f'https://m.weibo.cn/comments/hotFlowChild?cid={cid}&max_id={second_max_id_list[-1]}&max_id_type=0'
                    second_max_id_url_list.append(up_second_url)
                try:
                    content = requests_json(up_second_url)
                    max_id = content["max_id"]  # 获得主评论需要得参数max_id来构造url链接
                    second_max_id_list.append(max_id)
                except:
                    print("子评论跳出去呗!")
                    break

    except:
        pass


# 专门获取主评论信息得接口, 获取同时保存信息
def main_info(url, flag=0):
    try:
        time.sleep(5) # 休眠
        content = requests_json(url)
        data = content['data']['data']  # 获取评论列表
        for comment in tqdm(data, desc='花花评论爬取加载进度--->!'):

            text = str(comment['text'])  # 获取文本信息
            # 卧槽，我房子又塌了<span class="url-icon">
            # 处理文本信息,find函数找到<span开始的索引
            if text.find('<span') != -1:
                text = text[:text.find('<span')]
            create_time = comment['created_at']  # 发布时间
            # 格林威治时间格式字符串 Wed Jul 10 20:00:09 +0800 2019 转换为好理解的标准时间格式 2019-07-10 20:00:09
            # Fri Jan 22 17:56:48 +0800 2021 转换为标准时间格式 2021/1/22 17:56:48
            std_transfer = '%a %b %d %H:%M:%S %z %Y'  # 转换的一个格式
            std_create_time = datetime.datetime.strptime(create_time, std_transfer)
            user_name = comment['user']["screen_name"]  # 用户姓名
            user_id = comment['user']['id']  # 用户id
            user_followers_count = comment['user']['followers_count']  # 该用户粉丝数
            user_follow_count = comment['user']['follow_count']  # 该用户关注数
            user_gender = comment['user']['gender']  # 用户性别
            total_number = comment["total_number"]  # 总回复数
            like_count = comment["like_count"]  # 点赞数
            flag_id = comment["id"]  # 二级评论url构造所需id
            # 将主评论保存为csv形式
            with open('花花微博主评论.csv', 'a', newline="", encoding="gbk") as fp:
                csv_writer = csv.writer(fp, delimiter=',')
                if flag == 0:
                    csv_writer.writerow(['内容', '评论时间', '用户名', 'id', '关注人数', '粉丝', '性别', '回复数量', '点赞数', 'cid'])
                    csv_writer.writerow(
                        [text, std_create_time, user_name, user_id, user_followers_count, user_follow_count,
                         user_gender,
                         total_number, like_count, flag_id])
                    flag = 1  # 标志设置为1
                else:
                    csv_writer.writerow(
                        [text, std_create_time, user_name, user_id, user_followers_count, user_follow_count,
                         user_gender,
                         total_number, like_count, flag_id])
            print('成功保存信息!')
    except:
        print("啊这，今晚是上分局!被反爬了")
        pass


# 专门获取子评论信息得接口，获取同时保存信息
def second_info(url, flag=0):
    try:
        time.sleep(5)
        content = requests_json(url)
        data = content['data']  # 获取评论列表
        for comment in data:
            text = comment['text']  # 获取文本信息(这里文本没有经过处理, 原生数据如需处理请参照主评论处理代码)
            user_name = comment['user']["screen_name"]  # 用户姓名
            user_id = comment['user']['id']  # 用户id
            user_followers_count = comment['user']['followers_count']  # 该用户粉丝数
            user_follow_count = comment['user']['follow_count']  # 该用户关注数
            user_gender = comment['user']['gender']  # 用户性别
            like_count = comment["like_count"]  # 点赞数
            flag_id = comment["id"]  # 二级评论url构造所需id
            # with open('花花微博子评论.txt', 'a', newline="", encoding="gbk") as fp:
            #     print("进来保存为txt文件")
            #     if flag == 0:
            #         fp.writelines(['内容', '用户名', 'id', '关注人数', '粉丝', '性别', '点赞数', 'cid'])
            #         fp.writelines([text, user_name, user_id, user_followers_count, user_follow_count, like_count, flag_id])
            #         flag = 1
            #     else:
            #         fp.writelines(
            #             [text, user_name, user_id, user_followers_count, user_follow_count, like_count, flag_id])

            # 将子评论保存为csv形式
            with open('花花微博子评论.csv', 'a', newline="", encoding="gbk") as fp:
                print("正在保存子评论信息")
                csv_writer = csv.writer(fp, delimiter=',')
                if flag == 0:
                    csv_writer.writerow(['内容', '用户名', 'id', '关注人数', '粉丝', '性别', '点赞数', 'cid'])
                    csv_writer.writerow([text, user_name, user_id, user_followers_count, user_follow_count, like_count, flag_id])
                    flag = 1  # 标志设置为1
                else:
                    csv_writer.writerow([text, user_name, user_id, user_followers_count, user_follow_count, user_gender, like_count, flag_id])
                print("子评论信息保存完毕")
    except:
        print("啊这，今晚是上分局!")
        pass

# 开始执行抓取主评论信息

def start_main_info():
    # 测试主评论链接获取获取没有问题

    print(max_id_list)  # 打印主评论max_id参数列表
    print(max_id_url_list)  # 打印主评论ajax参数列表d
    # 批量爬取主评论信息

    # 主评论爬取一点问题没有
    i = 1
    try:
        for url in tqdm(max_id_url_list, desc=f'正在爬取花花第{i}条主评论'):
            i = i + 1  # 计数加一
            main_info(url)  # 开始爬取主评论
            time.sleep(3)  # 休眠3s, 防止被反爬
    except:
        print(f'第{i}没获取到没关系,继续下一条')
        pass


# 开始执行抓取子评论信息
def start_second_info():
    # 开始爬取子评论信息
    print("开始爬取子评论信息")

    # print(second_max_id_list)
    # print(second_max_id_url_list)
    j = 0
    try:
        for url in tqdm(second_max_id_url_list, desc=f'正在爬取花花第{j}子评论'):
            j = j + 1  # 计数加一
            second_info(url)
            time.sleep(3)  # 休眠3s, 防止被反爬
    except:
        print(f'第{j}没获取到没关系,继续下一条')
        pass


if __name__ == '__main__':
    # 准备工作函数
    main_max_id()
    second_max_id()
    # 创建主评论抓取任务线程对象
    main_task = threading.Thread(target=start_main_info)
    # 开启主评论抓取
    main_task.start()
    # 创建子评论榨取任务线程对象
    second_task = threading.Thread(target=start_second_info)
    second_task.start()
    start_second_info()





