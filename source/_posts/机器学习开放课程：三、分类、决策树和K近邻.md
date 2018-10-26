---
title: 机器学习开放课程：三、分类、决策树和K近邻
date: 2018-10-22 14:07:13
updated: 2018-10-26
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

##### [熵 (信息论)](https://zh.wikipedia.org/wiki/%E7%86%B5_(%E4%BF%A1%E6%81%AF%E8%AE%BA))

**熵最好理解为不确定性的量度而不是确定性的量度，因为越随机的信源的熵越大。**

**在信息论里面，熵是对不确定性的测量。但是在信息世界，熵越高，则能传输越多的信息，熵越低，则意味着传输的信息越少。熵的下降称为信息增益。**

假如我在不知情的情况下问某一届世界杯冠军是谁，而知道的人不愿意直接告诉我，而是让我猜，猜一次一块钱。为了省钱可以为所有的参赛队伍编号1~32，然后提问：“冠军队伍在1~16号之间吗？“假如他告诉我猜对了，我就会接着问：”冠军队伍在1~8号之间吗？“假如他告诉我猜错了，我自然知道冠军队伍在9~16号之间。这样只需要5次，就知道哪支球队是冠军了。

$$-\log({1 \over 32})=5$$

当然，有可能也用不了5次，因为总有些热门球队的夺冠概率会比较高，所以只需要把夺冠概率高的分在一组，正常情况下就会用更少的次数猜出结果。

$$H=-(P_{1}\log(P_{1})+P_{2}\log(P_{2})+ \cdots +P_{32}\log(P_{32}))$$

其中$$P{1},P{2},\cdots,P{32}$$分别是这32支球队的夺冠概率。

对于任意一个随机变量$$X$$，它的熵定义如下：

$$H_{s}=-\sum_{i=1}^{n}P_{i}\log\left (P_{i} \right )$$

英语文本数据流的熵比较低，因为英语很容易读懂，也就是说很容易被预测。即便我们不知道下一段英语文字是什么内容，但是我们能很容易地预测，比如，字母e总是比字母z多，或者qu字母组合的可能性总是超过q与任何其它字母的组合。如果未经压缩，一段英文文本的每个字母需要8个比特来编码，但是实际上英文文本的熵大概只有4.7比特。

如英语有26个字母，假如每个字母在文章中出现次数平均的话，每个字母的讯息量为：

$$I_{e}=-\log\left (1\over26 \right )=4.7$$

Excel公式：=$$-LOG(1/26,2)$$

##### [C4.5算法](https://zh.wikipedia.org/wiki/C4.5%E7%AE%97%E6%B3%95)

C4.5算法是由Ross Quinlan开发的用于产生决策树的算法。该算法是对Ross Quinlan之前开发的ID3算法的一个扩展。C4.5算法产生的决策树可以被用作分类目的，因此该算法也可以用于统计分类。

是贪婪最大化信息增益：在每一步，算法选择能在分割后给出最大信息增益的变量。接着递归重复这一流程，直到熵为零（或者，为了避免过拟合，直到熵为某个较小的值）。

##### [基尼不纯度](https://zh.wikipedia.org/wiki/%E5%86%B3%E7%AD%96%E6%A0%91%E5%AD%A6%E4%B9%A0#%E5%9F%BA%E5%B0%BC%E4%B8%8D%E7%BA%AF%E5%BA%A6%E6%8C%87%E6%A0%87)

基尼不纯度表示一个随机选中的样本在子集中被分错的可能性。基尼不纯度为这个样本被选中的概率乘以它被分错的概率。当一个节点中所有样本都是一个类时，基尼不纯度为零。


基尼不纯度的大概意思是**一个随机事件变成它的对立事件的概率**。

**基尼不确定性和信息增益的效果差不多。**

##### 决策树示例

下面使用决策树分析患者的检查结果来分析心血管疾病(CVD)的存在是否有关系。

数据来源：[mlbootcamp5_train.csv](mlbootcamp5_train.csv)

相关类及方法：

* [sklearn.tree.DecisionTreeClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn-tree-decisiontreeclassifier) 决策树分类器
* [sklearn.tree.DecisionTreeClassifier.fit](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit) 使用数据填充决策树分类器
* [sklearn.tree.DecisionTreeClassifier.predict](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.predict) 回归测试准确率
* [sklearn.metrics.accuracy_score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) 计算分类得分
* [sklearn.tree.export_graphviz](http://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html)

| 特征                                          |                    | 特征类型 | 列名        | 列数据类型                                       |
| --------------------------------------------- | ------------------ | -------- | ----------- | ------------------------------------------------ |
| Age                                           | 年龄               | 客观特征 | age         | int (days)                                       |
| Height                                        | 身高               | 客观特征 | height      | int (cm)                                         |
| Weight                                        | 体重               | 客观特征 | weight      | float (kg)                                       |
| Gender                                        | 性别               | 客观特征 | gender      | categorical code （1 – woman, 2 – man）          |
| Systolic blood pressure                       | 收缩压             | 检查特征 | ap_hi       | int                                              |
| Diastolic blood pressure                      | 舒张压             | 检查特征 | ap_lo       | int                                              |
| Cholesterol                                   | 胆固醇             | 检查特征 | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose                                       | 葡萄糖             | 检查特征 | gluc        | 1: normal, 2: above normal, 3: well above normal |
| Smoking                                       | 是否吸烟           | 主观特征 | smoke       | binary                                           |
| Alcohol intake                                | 是否喝酒           | 主观特征 | alco        | binary                                           |
| Physical activity                             | 体力劳动           | 主观特征 | active      | binary                                           |
| Presence or absence of cardiovascular disease | 是否存在心血管疾病 | 目标特征 | cardio      | binary                                           |

> 以下代码需要：
>
> - pandas
> - sklearn
> - [graphviz](https://www.graphviz.org/) *对于windows环境来说，需要将安装目录中的bin目录添加至环境变量中。*
> - pydotplus *先安装 graphviz*

```python
from io import BytesIO
from io import StringIO
import pandas as pd
import pydotplus
from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


def S(X, Y, criterion='gini'):
    """显示决策树的决策过程的方法

    :param X: 训练集。
    :param Y: 结果集。
    :param criterion: 衡量指标。与 `sklearn.tree.DecisionTreeClassifier` 一致。默认为 `gini`。 也可以使用 `entropy`。
    :return:
    """
    # 以深度为3层来创建决策树分类器
    tree_model = DecisionTreeClassifier(criterion=criterion, max_depth=3)
    # 从训练集（X，y）构建决策树分类器。
    tree_model.fit(X, Y)
    return tree_model


def showImg(tree, feature_names=None):
    """显示决策树"""
    dot_data = StringIO()
    # 导出决策树为 DOT 格式
    export_graphviz(tree, feature_names=feature_names, out_file=dot_data, filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    image = Image.open(BytesIO(graph.create_png()))
    image.show()

if __name__ == '__main__':
    df = pd.read_csv('mlbootcamp5_train.csv', index_col='id', sep=';')

    # # 使用sklearn.model_selection.train_test_split将数据拆分成训练集和测试集
    # # 使用3/7比率
    X_train, X_valid, Y_train, Y_valid = train_test_split(df.drop(columns=['cardio']), df['cardio'], test_size=0.3)

    # 按照 基尼不纯度 分割的决策树
    tree_gini = S(X_train, Y_train);
    # 按照 信息熵 分割的决策树
    tree_entropy = S(X_train, Y_train, 'entropy')

    showImg(tree_gini, X_train.columns)
    showImg(tree_entropy, X_train.columns)
```

* 按照基尼不纯度分割：

![NZXca6g](NZXca6g.png)

* 按照信息熵分割：

![3VT+hGyI](3VT+hGyI.png)

无论按照哪种方式分割，都可以看到，随着叶子节点的不断展开，基尼不纯度或者信息熵都会不断下降。

计算分类回归准确率：

```python
def V(tree, X, Y):
    """验证结果准确度"""
    y_pred = tree.predict(X)
    return accuracy_score(y_pred=y_pred, y_true=Y)
    
    
if __name__ == '__main__':
    print(V(tree_gini, X_valid, Y_valid))
    print(V(tree_entropy, X_valid, Y_valid))
```

```
0.7282857142857143
0.7269047619047619
```





