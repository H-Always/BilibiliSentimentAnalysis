from PIL.Image import Image
import os
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# @Name : WordCloud.
# @Description : 
# @Author : 余霜
# @Date : 2021/02/24 11:56
# @Version : V1.0

'''生成词云'''


def word_cloud(words, fileName):
    if not os.path.exists("Resources/word_cloud_" + str(fileName) + ".txt"):
        with open("Resources/word_cloud_" + str(fileName) + ".txt", 'w', encoding='UTF-8') as file:
            for word in words:
                for i in word:
                    file.write(str(i) + ' ')

    with open("Resources/word_cloud_" + str(fileName) + ".txt", "r", encoding='UTF-8') as file:
        txt = file.read()

    mask = np.array(image.open("Resources/python_word_cloud_image.png"))
    # mask = np.array(image.open("Resources/cc.jpg"))
    word = WordCloud(background_color='black',
                     font_path='simhei.ttf',mask=mask, ).generate(txt)
    word.to_file('Visualization/word_cloud_' + str(fileName) + '.png')
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()

    # mask = np.array(image.open("Resources/python_word_cloud_image.png"))
    mask = np.array(image.open("Resources/cc.jpg"))
    word = WordCloud(background_color='black',
                     font_path='simhei.ttf', mask=mask, ).generate(txt)
    word.to_file('Visualization/word_cloud_' + str(fileName) + '1.png')
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()
