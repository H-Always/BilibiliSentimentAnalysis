import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import xlrd

# @Name : Plot.
# @Description : 
# @Author : 余霜
# @Date : 2021/02/23 17:10
# @Version : V1.0

'''
可视化
'''


def plot_data(resScore, resCalculateScore, resCalculateScoreSum):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    colors1 = '#00CED1'  # 点的颜色
    colors2 = '#DC143C'
    colors3 = '#ff9201'
    area = np.pi * 2 ** 2

    ''' 折线图 '''
    # 综合取值分布
    x = resCalculateScoreSum
    plt.title('综合取值分布折线图')
    plt.xlabel('X')
    plt.ylabel('resCalculateScoreSum')
    plt.plot(x, c=colors1)
    plt.show()

    # 程度取值分布
    x = resCalculateScore
    plt.title('程度取值分布折线图')
    plt.xlabel('X')
    plt.ylabel('resCalculateScore')
    plt.plot(x, c=colors2)
    plt.show()

    # 情感聚合取值分布
    x = resScore
    plt.title('情感聚合取值分布折线图')
    plt.xlabel('X')
    plt.ylabel('resScore')
    plt.plot(x, c=colors3)
    plt.show()

    ''' 散点图 '''
    # 综合取值分布
    x = list(range(0, len(resCalculateScoreSum)))
    y = resCalculateScoreSum
    plt.title('综合取值分布散点图')
    plt.xlabel('X')
    plt.ylabel('resCalculateScoreSum')
    plt.scatter(x, y, s=area, c=colors1, alpha=0.4, label='类别A')
    plt.show()

    # 程度取值分布
    x = list(range(0, len(resCalculateScore)))
    y = resCalculateScore
    plt.title('程度取值分布散点图')
    plt.xlabel('X')
    plt.ylabel('resCalculateScore')
    plt.scatter(x, y, s=area, c=colors2, alpha=0.4, label='类别A')
    plt.show()

    # 情感聚合取值分布
    x = list(range(0, len(resScore)))
    y = resScore
    plt.title('情感聚合取值分布散点图')
    plt.xlabel('X')
    plt.ylabel('resScore')
    plt.scatter(x, y, s=area, c=colors3, alpha=0.4, label='类别A')
    plt.show()

    return
