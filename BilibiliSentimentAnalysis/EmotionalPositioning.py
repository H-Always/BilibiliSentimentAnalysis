from collections import defaultdict
import os
import re
import jieba
import codecs

# @Name : EmotionalPositioning
# @Description : 情感定位
# @Author : 余霜
# @Date  2021/01/30 16:40
# @Version : V1.0

"""
2. 情感定位
    将句子中各类词分别存储并标注位置。
"""


def classify_words(wordDict,wordIndex):
    # (1) 情感词
    senList = []
    f = open('Resources/BosonNLP_sentiment_score.txt', 'r', encoding='UTF-8')
    for line in f.readlines():
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行
            continue
        senList.append(line)

    # defaultdict()这本身是一个字典
    # 对于普通的dict，key&value不存在就报错。
    # 但是对于defaultdict，key不存在就会返回默认值。defaultdict(None, {})
    # 下面这三行，先用空格分隔每一个单词，然后把index[0]作为key，index[1]作为value
    senDict = defaultdict()
    for s in senList:
        senDict[s.split(' ')[0]] = s.split(' ')[1]

    # (2) 否定词
    notList = []
    f = open('Resources/new_notDict.txt', 'r', encoding='UTF-8')
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        notList.append(line)

    # (3) 程度副词
    degreeList = []
    f = open('Resources/degreeDict.txt', 'r', encoding='UTF-8')
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        degreeList.append(line)

    degreeDict = defaultdict()
    for d in degreeList:
        degreeDict[d.split(',')[0]] = d.split(',')[1]

    senWordScore = defaultdict()
    notWordScore = defaultdict()
    degreeWordScore = defaultdict()

    # 以上代码是把所有的情感极性词汇分类和标注
    # 下面是把处理好停用词的文本进行极性定位
    # 再简单点来说，下面这几行的作用就是标注每一个词多少分
    for word in wordDict:
        # 正面的情感词，按照分数来给
        if word in senDict.keys() and word not in notList and word not in degreeDict.keys():
            senWordScore[word] = senDict[word]
        # 所有的否定词，都给-1
        elif word in notList and word not in degreeDict.keys():
            notWordScore[word] = -1
        # 程度副词按照相关的分数给
        elif word in degreeDict.keys():
            degreeWordScore[word] = degreeDict[word]

    senWordIndex = defaultdict()
    notWordIndex = defaultdict()
    degreeWordIndex = defaultdict()

    for i in wordIndex.keys():
        # 正面的情感词，按照分数来给
        if wordIndex[i] in senDict.keys() and wordIndex[i] not in notList and wordIndex[i] not in degreeDict.keys():
            senWordIndex[i] = senDict[wordIndex[i]]
        # 所有的否定词，都给-1
        elif wordIndex[i] in notList and wordIndex[i] not in degreeDict.keys():
            notWordIndex[i] = -1
        # 程度副词按照相关的分数给
        elif wordIndex[i] in degreeDict.keys():
            degreeWordIndex[i] = degreeDict[wordIndex[i]]

    return senWordScore, notWordScore, degreeWordScore, senWordIndex, notWordIndex, degreeWordIndex






