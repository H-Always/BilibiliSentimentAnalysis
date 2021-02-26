from collections import defaultdict
import os
import re
import jieba
import codecs



senList = ['哀痛欲绝 希望 再次','11','22']
print(type(senList))
print(enumerate(senList))
print(senList.sort())
wordDict = defaultdict()
wordDict['22'] = "123123"
wordDict[1] = "3123123"


print(2.2>5)


s = [('yellow', 1), ('blue', 2), ('red', 1)]


d=defaultdict(list)
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
print(d)
print(a)