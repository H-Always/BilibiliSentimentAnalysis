from numpy import *
import xlrd
import CutData
import EmotionalPositioning
import CalculateScore
import ScoreSent
import WordCloud
import Plot

# @Name    : Main
# @Description: 主文件，运行这个文件即可
# @Author  : 余霜
# @Date    : 2021/02/07 15:40
# @Version: V1.0


if __name__ == '__main__':

    sentence1 = '这个镜头的第一层暗示很明显。就如为了给观众下马威一般给了一个鹿角特写，' \
                '在美丽而强力的鹿角下连两旁的狮子都成了陪衬，独特的威严感甚至让我心生恐惧...' \
                '就像路易独特的高傲一般。划分世界的并非种族，而是赢家与输家。' \
                '路易已经于这层意义上摆脱了肉食与草食的桎梏，成为了配得上这美丽鹿角（力量）的赢家'

    # str = '对于这部外传，虽然不知其幕后的各类起源，但单从作品而言，不失为作者的新尝试'

    '''
    newSent = CutData.sent_word(sentence1)
    loc = EmotionalPositioning.classify_words(newSent[0], newSent[1])
    calculateScore = CalculateScore.calculate_score(loc[0], loc[1], loc[2])
    score = ScoreSent.score_sent(loc[3], loc[4], loc[5], newSent)
    WordCloud.word_cloud(newSent[0])
    print(newSent[0])
    print(calculateScore[0])
    print(calculateScore[1])
    print(score)
    '''

    xl = xlrd.open_workbook(r'Resources/教你如何装一台超级工作站：无敌是多么寂寞.xls')
    table = xl.sheets()[0]
    nrows = table.nrows
    sentences = table.col_values(3, 1)

    print(nrows)

    resSent = []
    resScore = []
    resCalculateScore = []
    resCalculateScoreSum = []
    count = 0

    for sentence in sentences:
        print(count)
        newSent = CutData.sent_word(sentence)
        resSent.append(newSent[0])
        loc = EmotionalPositioning.classify_words(newSent[0], newSent[1])
        calculateScore = CalculateScore.calculate_score(loc[0], loc[1], loc[2], count, nrows)
        score = ScoreSent.score_sent(loc[3], loc[4], loc[5], newSent)

        if count < nrows * 0.02:
            score *= 1.4
        elif count < nrows * 0.05:
            score *= 1.2
        else:
            score *= 0.9

        resScore.append(score)
        resCalculateScore.append(calculateScore[0])
        resCalculateScoreSum.append(calculateScore[1])
        count += 1

    WordCloud.word_cloud(resSent)
    print(mean(resScore))
    print(mean(resCalculateScore))
    print(mean(resCalculateScoreSum))
    Plot.plot_data(resScore, resCalculateScore, resCalculateScoreSum)


