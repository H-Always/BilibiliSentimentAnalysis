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

    fileName = '动物狂想曲BEASTARS 第二季'

    xl = xlrd.open_workbook(r'Resources/' + str(fileName) + '.xls')
    table = xl.sheets()[0]
    nrows = table.nrows
    # 这个函数支持三个参数，(第几列，从第几行开始，第几行结束)
    sentences = table.col_values(3, 1,5)

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

    WordCloud.word_cloud(resSent,fileName)
    print(mean(resScore))
    print(mean(resCalculateScore))
    print(mean(resCalculateScoreSum))
    Plot.plot_data(resScore, resCalculateScore, resCalculateScoreSum)


