---
title: 机器学习开放课程：三、分类、决策树和K近邻
date: 2018-10-22 14:07:13
updated: 2018-10-24
tags:
 - 编程
 - Python
 - 机器学习
 - 决策树
 - K近邻
 - 熵
categories:
 - 编程
 - Python
 - 机器学习
typora-root-url: 机器学习开放课程：三、分类、决策树和K近邻
mathjax: true
description: <!—more—->
---

### 三、分类、决策树和K近邻

[机器学习开放课程：三、分类、决策树和K近邻](https://www.jqr.com/article/000139)

#### 决策树

##### 熵

{% blockquote 熵 (信息论)  https://zh.wikipedia.org/wiki/%E7%86%B5_(%E4%BF%A1%E6%81%AF%E8%AE%BA) %}
**熵最好理解为不确定性的量度而不是确定性的量度，因为越随机的信源的熵越大。**

**在信息论里面，熵是对不确定性的测量。但是在信息世界，熵越高，则能传输越多的信息，熵越低，则意味着传输的信息越少。熵的下降称为信息增益。**

> 假如我在不知情的情况下问某一届世界杯冠军是谁，而知道的人不愿意直接告诉我，而是让我猜，猜一次一块钱。为了省钱可以为所有的参赛队伍编号1~32，然后提问：“冠军队伍在1~16号之间吗？“假如他告诉我猜对了，我就会接着问：”冠军队伍在1~8号之间吗？“假如他告诉我猜错了，我自然知道冠军队伍在9~16号之间。这样只需要5次，就知道哪支球队是冠军了。
>
> $$-\log _{2}({1 \over 32})=5$$
>
> 当然，有可能也用不了5次，因为总有些热门球队的夺冠概率会比较高，所以只需要把夺冠概率高的分在一组，正常情况下就会用更少的次数猜出结果。
>
> $$H=-(P_{1}\log(P_{1})+P_{2}\log(P_{2})+ \cdots +P_{32}\log(P_{32}))$$
>
> 其中$$P{1},P{2},\cdots,P{32}$$分别是这32支球队的夺冠概率。

对于任意一个随机变量$$X$$，它的熵定义如下：

$$H_{s}=-\sum_{i=1}^{n}p_{i}\log\left (p_{i} \right )$$

英语文本数据流的熵比较低，因为英语很容易读懂，也就是说很容易被预测。即便我们不知道下一段英语文字是什么内容，但是我们能很容易地预测，比如，字母e总是比字母z多，或者qu字母组合的可能性总是超过q与任何其它字母的组合。如果未经压缩，一段英文文本的每个字母需要8个比特来编码，但是实际上英文文本的熵大概只有4.7比特。

> 如英语有26个字母，假如每个字母在文章中出现次数平均的话，每个字母的讯息量为：
>
> $$I_{e}=-\log\left (1\over26 \right )=4.7$$
>
> Excel公式：=$$-LOG(1/26,2)$$

{% endblockquote %}

{% blockquote C4.5算法 %}

C4.5算法是由Ross Quinlan开发的用于产生决策树的算法。该算法是对Ross Quinlan之前开发的ID3算法的一个扩展。C4.5算法产生的决策树可以被用作分类目的，因此该算法也可以用于统计分类。

是贪婪最大化信息增益：在每一步，算法选择能在分割后给出最大信息增益的变量。接着递归重复这一流程，直到熵为零（或者，为了避免过拟合，直到熵为某个较小的值）。

{% endblockquote %}

##### 基尼不纯度

{% blockquote 基尼不纯度 https://zh.wikipedia.org/wiki/C4.5%E7%AE%97%E6%B3%95 %}

基尼不纯度表示一个随机选中的样本在子集中被分错的可能性。基尼不纯度为这个样本被选中的概率乘以它被分错的概率。当一个节点中所有样本都是一个类时，基尼不纯度为零。

{% endblockquote %}

基尼不纯度的大概意思是**一个随机事件变成它的对立事件的概率**。

**基尼不确定性和信息增益的效果差不多。**

按照年龄来区分放贷情况：

> 以下代码需要：
>
> - pandas
> - sklearn
> - [graphviz](https://www.graphviz.org/) *对于windows环境来说，需要将安装目录中的bin目录添加至环境变量中。*
> - pydotplus *先安装 graphviz*

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import io
from io import StringIO
import pydotplus
from PIL import Image

data = pd.DataFrame({'Age': [17, 64, 18, 20, 38, 49, 55, 25, 29, 31, 33],
                     'Loan Default': [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]})
# 根据年龄进行升序排列
print(data.sort_values('Age'))

age_tree = DecisionTreeClassifier(random_state=17)
age_tree.fit(data['Age'].values.reshape(-1, 1), data['Loan Default'].values)
dot_data = StringIO()
export_graphviz(age_tree, feature_names=['Age'],
                out_file=dot_data, filled=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
image = Image.open(io.BytesIO(graph.create_png()))
image.show()
```

```
    Age  Loan Default
0    17             1
2    18             1
3    20             0
7    25             1
8    29             1
9    31             0
10   33             1
4    38             1
5    49             0
6    55             0
1    64             0
```

从树上可以看出，*基尼不确定性* 在不断的下降。

阈值切割示例：

- 43.5 -> 49岁及以上都是0，这是使用 (38+49)/2=43.5
- 19 -> 18岁及以下都是1，这时使用 (18+20)/2=19

![基尼不确定性的下降](tmp_w3pmy_5.png)



