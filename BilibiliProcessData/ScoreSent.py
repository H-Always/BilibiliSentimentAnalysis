# @Name : ScoreSent.
# @Description : 
# @Author : 余霜
# @Date : 2021/02/18 13:52
# @Version : V1.0


def score_sent(senWord, notWord, degreeWord, segResult):
    W = 1
    score = 0
    # 存所有情感词的位置的列表
    sen = senWord.items()
    senLoc = []
    for k, v in sen:
        senLoc.append(k)

    notLoc = notWord.keys()
    degreeLoc = degreeWord.keys()
    senloc = -1
    # notloc = -1
    # degreeloc = -1

    # 遍历句中所有单词segResult，i为单词绝对位置
    for i in range(0, len(segResult)):
        # 如果该词为情感词
        if i in senLoc:
            # loc为情感词位置列表的序号
            senloc += 1
            # 判断热评添加该情感词分数
            score += W * float(senWord[i])
            # print "score = %f" % score
            if senloc < len(senLoc) - 1:
                # 判断该情感词与下一情感词之间是否有否定词或程度副词
                # j为绝对位置
                for j in range(senLoc[senloc], senLoc[senloc + 1]):
                    # 如果有否定词
                    if j in notLoc:
                        W *= -1
                    # 如果有程度副词
                    elif j in degreeLoc:
                        W *= float(degreeWord[j])

        # i定位至下一个情感词
        if senloc < len(senLoc) - 1:
            i = senLoc[senloc + 1]

    return score
