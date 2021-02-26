# BilibiliSentimentAnalysis
# 基于哔哩哔哩用户评论的文本情感分析

### 有两个主要文件夹，分别为 BiliBiliReptile 和 BilibiliSentimentAnalysis
### 对应b站爬虫 和 对爬下来的数据进行分析
# -----------------------------------------------------------------
## 怎么用?
## BiliBiliReptile：
#### 这个文件夹里有一个BilibiliReptileProcess.py
#### 里面包含着main函数，这其中有两个参数，分别是BV和oid
#### bv号就是对应作品的BV号，很容易找
#### oid需要pc端对应作品的网页找开发者模式寻找，这里以BV1Qi4y1F7Zh这部作品为例
#### 按F12打开开发者，寻找network选项的All分支往下滑会有wepb类型文件，多数都是图片
#### 往上找会发现有一个script类型的文件，名字叫reply?callback什么的，点进去会发现有一个请求链接
#### 这个链接就是对应网页评论的链接，如果把他复制到浏览器地址会发现打不开，因为默认不允许访问，
  https://api.bilibili.com/x/v2/reply?callback=jQuery17209026971645378477_1614314528543&jsonp=jsonp&pn=1&type=1&oid=543581885&sort=2&_=1614314549765
#### 把他截取成
  https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=801110238&sort=2
#### 再复制到网页地址中，就可以打开了，里面就是未处理的数据，
#### 这里我们只要oid
#### 把这两个参数复制到BilibiliReptileProcess.py 的main函数里面对应的变量中，运行即可，
#### 爬出来的格式是 用户ID点赞数/评论时间/评论内容

## BilibiliSentimentAnalysis：
### 这个文件夹里面有一个Main函数
#### 有一个filename，把这个变量换成你文本的名字，然后点击运行
# -----------------------------------------------------------------
## 作者的话
### 这里面的停用词和情感词我加了一些，但还是缺少很多，缺太多了...
### 语言这个东西高度复杂，主观性很强，加上现在网络上阴阳怪气的评论越来越多，使得情感词仅仅给出一个唯一的分数很不应该
### 一般采用简单的线性叠加显然会造成很大的精度损失。词语权重同样如此。
## 本算法仅供个人学习、研究使用，切勿用于商业用途
