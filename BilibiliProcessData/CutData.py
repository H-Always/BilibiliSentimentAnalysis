from collections import defaultdict
import os
import re
import jieba
import codecs

# @Name    : CutData
# @Description: 文本切割
# @Author  : 余霜
# @Date    : 2021/01/27 15:20
# @Version: V1.0

"""
1. 文本切割
"""


def sent_word(sentence):
    # 先利用结巴分词，(我觉得这个挺好用的)，把原始句子分成一个列表，
    # 这里不可以使用元组，因为后续要变
    segList = jieba.lcut(sentence)

    # 结巴分词返回的数据类型是generator类型的，要把他们放到一个列表里
    segResult = []
    for w in segList:
        segResult.append(w)
    # print(segResult)

    # 把所有停用词表也放到一个列表里，这里后续可以改成元组，使它不可变
    f = open('Resources/new_stopwords.txt', 'r', encoding='UTF-8')  # 以只读方式打开文件
    stopwords = []
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        # print(line)
        if not len(line) or line.startswith('#'):  # 判断是否是空行
            continue
        stopwords.append(line)  # 保存到列表

    # print(stopwords)
    newSent = []
    newSent_index = defaultdict()
    index = 0
    for word in segResult:
        if word in stopwords or word == '\n' or word == ' ':
            # print "stopword: %s" % word
            continue
        else:
            newSent.append(word)
            newSent_index[index] = word
            index = index + 1

    return newSent, newSent_index


