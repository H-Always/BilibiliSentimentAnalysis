import requests
import time
from bs4 import BeautifulSoup
import json
import xlwt
import re

# @Name    : BilibiliReptileProcess
# @Description: 爬取数据
# @Author  : 余霜
# @Date    : 2021/01/09 08:40
# @Version: V1.0


'''
爬取B站评论区内容
这个程序其实挺简单的，
'''

# 创建内容，注明标题
wookbook = xlwt.Workbook(encoding='utf-8')
sheet = wookbook.add_sheet('sheet', cell_overwrite_ok=True)
sheet.write(0, 0, 'ID')
sheet.write(0, 1, '点赞数')
sheet.write(0, 2, '评论时间')
sheet.write(0, 3, '评论内容')


def get_headers():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    return headers


def get_title(titleUrl):

    response = requests.request("POST", titleUrl, headers=get_headers())
    pattern=re.compile(r'name": "(.*?)",')
    title = re.findall(pattern,response.text)
    # print(title)
    # print(type(title[0]))

    return title[0]


# 首先我们写好抓取网页的函数
def get_html(url):
     # 爬虫模拟访问信息

    r = requests.get(url, timeout=30, headers=get_headers())
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
    # 先用json进行解析
    html = get_html(url)
    #print(html)
    try:
        s = json.loads(html)
        #print(s)
    except:
        print("jsonload error")

    # 获取每页评论栏的数量
    num = len(s['data']['replies'])
    # print(num)
    i = 0
    while i < num:
        # 获取每栏评论
        comment = s['data']['replies'][i]

        # 创建字典存储每组信息
        InfoDict = {}

        # 写入内容
        InfoDict['Uname'] = comment['member']['uname']  # 用户名
        InfoDict['Like'] = comment['like']  # 点赞数
        InfoDict['Content'] = comment['content']['message']  # 评论内容
        InfoDict['Time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))  # ctime格式的特殊处理？不太清楚具体原理

        comments.append(InfoDict)
        i = i + 1
    # print(comments)
    return comments


def Out2File(dict,count,title):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 BiliBiliComments.xls文件中。
    '''

    # 爬取
    for comment in dict:
        count = count + 1
        try:
            # 写入excel
            sheet.write(count, 0, comment['Uname'])
            sheet.write(count, 1, comment['Like'])
            sheet.write(count, 2, comment['Time'])
            sheet.write(count, 3, comment['Content'])
            wookbook.save('CommentsResult/'+str(title)+'.xls')  # 保存一下子
        except:
            print("out2File error")
    print('当前页面保存完成')
    return count


def get_start(commentsUrl, titleUrl, tittle):
    page = 1 # 当前页面数

    e = 0  # 报错了可以主动退出
    count = 0  # 计数器


    while e == 0:
        url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + commentsUrl

        try:
            print()

            # print(url)
            content = get_content(url)
            # 当前读取的是第几页
            print("page:", page)
            # 返回当前页面的字典
            count = Out2File(content, count, tittle)
            # 这个参数是当前的行数，最后也可以写入一下
            page = page + 1
            print("当前共写入:", count, "条数据")
            # 为了降低被封ip的风险，每爬8页便歇5秒，其实这样有点点保守，也可以设置成15页左右
            if page % 8 == 0:
                time.sleep(5)
        except:
            e = 1


# 主函数
if __name__ == '__main__':
    # 获取爬取作品的bv号名称
    bv = 'BV1uT4y1K7yL'
    # 将网页上获取的url复制到这里，注意，从开发者那里获取到的参数不能直接使用，要删减一下，否则会触发反爬虫机制
    oid = '92186919718'
    commentsUrl = "&type=1&oid="+str(oid)+"&sort=2"
    titleUrl = 'https://www.bilibili.com/'+bv
    tittle = get_title(titleUrl)
    print('正在爬取'+ tittle)

    get_start(commentsUrl, titleUrl ,tittle)


