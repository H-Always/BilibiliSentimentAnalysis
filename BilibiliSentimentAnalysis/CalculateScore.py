from collections import defaultdict
import os
import re
import jieba
import codecs

# @Name : CalculateScore
# @Description: 计算句子得分
# @Author : 余霜
# @Date : 2021/01/27 15:41
# @Version : V1.0

'''
计算句子得分之和
定义一个情感词语组：两情感词之间的所有否定词和程度副词与这两情感词中的后一情感词构成一个情感词组，即notWords + degreeWords + sentiWords
例如不是很交好，其中不是为否定词，很为程度副词，交好为情感词，那么这个情感词语组的分数为：
finalSentiScore = (-1) ^ 1 * 1.25 * 0.747127733968
'''


def calculate_score(senWord, notWord, degreeWord, count=10, nrows= 100):
    sentenceScore = 0
    senWordScore = 0
    notWordNum = 0
    degreeWordScore = 0

    for k, v in senWord.items():
        sentenceScore = sentenceScore + float(v)
        senWordScore = senWordScore + float(v)

    for k, v in notWord.items():
        sentenceScore = sentenceScore + float(v)
        notWordNum = notWordNum + 1

    for k, v in degreeWord.items():
        sentenceScore = sentenceScore + float(v)
        degreeWordScore = degreeWordScore + float(v)

    if senWordScore != 0 and degreeWordScore != 0:
        score = pow(-1, notWordNum) * degreeWordScore * senWordScore
    elif senWordScore != 0:
        score = pow(-1, notWordNum) * senWordScore
    else:
        score = 0

    if count < nrows * 0.02:
        score *= 1.4
        sentenceScore *= 1.4
    elif count < nrows * 0.05:
        score *= 1.2
        sentenceScore *= 1.2
    else:
        score *= 0.9
        sentenceScore *= 0.9

    return score, sentenceScore
