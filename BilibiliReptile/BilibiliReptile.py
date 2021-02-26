import requests
import time
from bs4 import BeautifulSoup
import json
import xlwt

# @Name    : BilibiliReptile
# @Description: 爬取数据原始版
# @Author  : 余霜
# @Date    : 2021/01/07 15:40
# @Version: V1.0

'''
爬取B站评论区内容

'''

wookbook = xlwt.Workbook(encoding='utf-8')
sheet = wookbook.add_sheet('sheet', cell_overwrite_ok=True)
sheet.write(0, 0, 'ID')
sheet.write(0, 1, '点赞数')
sheet.write(0, 2, '评论时间')
sheet.write(0, 3, '评论内容')


# 首先我们写好抓取网页的函数


def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息

    r = requests.get(url, timeout=30, headers=headers)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    # print(r.text)
    return r.text


def get_content(url):
    '''
    分析网页文件，整理信息，保存在列表变量中
    '''
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)
    try:
        s = json.loads(html)
    except:
        print("jsonload error")

    num = len(s['data']['replies'])  # 获取每页评论栏的数量
    # print(num)
    i = 0
    while i < num:
        comment = s['data']['replies'][i]  # 获取每栏评论

        InfoDict = {}  # 存储每组信息字典

        InfoDict['Uname'] = comment['member']['uname']  # 用户名
        InfoDict['Like'] = comment['like']  # 点赞数
        InfoDict['Content'] = comment['content']['message']  # 评论内容
        InfoDict['Time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))  # ctime格式的特殊处理？不太清楚具体原理

        comments.append(InfoDict)
        i = i + 1
    # print(comments)
    return comments


def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 BiliBiliComments.txt文件中。
    '''
    with open('CommentsResult/BiliBiliComments.txt', 'a+', encoding='utf-8') as f:
        i = 0
        for comment in dict:
            i = i + 1
            try:
                f.write('姓名：{}\t  点赞数：{}\t \n 评论内容：{}\t  评论时间：{}\t \n '.format(
                    comment['Uname'], comment['Like'], comment['Content'], comment['Time']))
                f.write("-----------------\n")
            except:
                print("out2File error")
        print('当前页面保存完成')


if __name__ == '__main__':
    e = 0
    page = 1
    while e == 0:
        url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + "&type=1&oid=969664445&sort=2"
        try:
            print()

            print(url)
            content = get_content(url)
            print("page:", page)
            Out2File(content)
            page = page + 1
            # 为了降低被封ip的风险，每爬20页便歇5秒。
            if page % 5 == 0:
                time.sleep(5)
        except:
            e = 1
