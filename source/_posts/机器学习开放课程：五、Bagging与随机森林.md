---
title: 机器学习开放课程：五、Bagging与随机森林
date: 2018-11-08 09:41:51
updated: 2018-11-08
tags:
 - 编程
 - Python
 - 机器学习
 - 随机森林
 - scipy.special.comb
 - 评审团定理
 - Bootstraping（自助抽样法）
 - Bagging（装袋算法）
 - 袋外误差
 - .632自助法
 - 分类
 - sklearn.model_selection.cross_val_score
 - sklearn.ensemble.RandomForestClassifier
 - sklearn.ensemble.BaggingClassifier
 - sklearn.tree.DecisionTreeClassifier
categories:
 - 编程
 - Python
 - 机器学习
typora-root-url: 机器学习开放课程：五、Bagging与随机森林
mathjax: true
description: <!—more—->
---

### 集成

#### [孔塞多陪审团定理](https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem)

如果评审团的每个成员做出独立判断，并且每个陪审员做出正确决策的概率高于0.5，那么整个评审团做出正确的总体决策的概率随着陪审员数量的增加而增加，并趋向于一。另一方面，如果每个陪审员判断正确的概率小于0.5，那么整个陪审团做出正确的总体决策的概率随着陪审员数量的增加而减少，并趋向于零。

$\mu = \sum_{i=m}^{M}\binom{N}{i} p^{i}(1-p)^{(N-i)}$

- **N**为陪审员总数；
- **m**是构成多数的最小值，即**m** = (N+1)/2；
- **p**为评审员做出正确决策的概率；
- **μ**是整个评审团做出正确决策的概率。

```python
from scipy.special import comb

p = 0.8
N = 7
m = int((1 + N) / 2)
score = 0
for i in range(m, N + 1, 1):
    score += ((p ** i) * ((1 - p) ** (N - i)) * comb(N, i))
# 96.67%
print("{:.2%}".format(score))
```

*机器学习领域采用类似的思路以降低误差。*

> Condorcet陪审团定理也用于[机器学习](https://en.wikipedia.org/wiki/Machine_learning)领域的[集成](https://en.wikipedia.org/wiki/Ensemble_learning)[学习](https://en.wikipedia.org/wiki/Machine_learning)。集合方法通过多数表决来组合许多单独分类器的预测。假设每个单独的分类器预测准确度略高于50％，那么他们的预测集合将远远大于他们的个人预测分数。

### Bootstraping（自助抽样法）/Bagging（装袋算法）

{% blockquote https://zh.wikipedia.org/wiki/Bagging%E7%AE%97%E6%B3%95 Bagging算法 %}

给定一个大小为 $n$ 的训练集$D$，Bagging算法从中均匀、有放回地（即使用[自助抽样法](https://zh.wikipedia.org/wiki/%E8%87%AA%E5%8A%A9%E6%B3%95)）选出 $m$ 个大小为  ${n}'$ 的子集 $D_{i}$，作为新的训练集。在这 $m$ 个训练集上使用分类、回归等算法，则可得到 $m$ 个模型，再通过取平均值、取多数票等方法，即可得到Bagging的结果。

Bagging算法可与其他[分类](https://zh.wikipedia.org/wiki/%E7%BB%9F%E8%AE%A1%E5%88%86%E7%B1%BB)、[回归](https://zh.wikipedia.org/wiki/%E5%9B%9E%E5%BD%92%E5%88%86%E6%9E%90)算法结合，提高其准确率、稳定性的同时，通过降低结果的[方差](https://zh.wikipedia.org/wiki/%E6%96%B9%E5%B7%AE)，避免[过拟合](https://zh.wikipedia.org/wiki/%E8%BF%87%E6%8B%9F%E5%90%88)的发生。

{% endblockquote %}

### 袋外误差

{% blockquote https://zh.wikipedia.org/wiki/%E8%87%AA%E5%8A%A9%E6%B3%95 .632自助法 %}

最常用的一种是.632自助法，假设给定的数据集包含d个样本。该数据集有放回地抽样d次，产生d个样本的训练集。这样原数据样本中的某些样本很可能在该样本集中出现多次。没有进入该训练集的样本最终形成检验集（测试集）。 显然每个样本被选中的概率是1/d，因此未被选中的概率就是(1-1/d)，这样一个样本在训练集中没出现的概率就是d次都未被选中的概率，即(1-1/d)d。当d趋于无穷大时，这一概率就将趋近于e-1=0.368，所以留在训练集中的样本大概就占原来数据集的63.2%。

{% endblockquote %}

### 随机森林

随机森林扩展了Bagging。随机森林在以决策树为基学习器构建Bagging集成的基础上，进一步在决策树的训练过程中引入了随机属性选择。

> 传统决策树在选择划分属性时是在当前节点的属性集合（假定有 $d$ 个参数）中选择一个最优属性；
>
> 而在随即森林中，对基决策树的每个节点，先从该节点的属性几何中随机选择一个包含 $k$ 的属性的子集，然后再从这个自己种选择一个最优属性用于划分。
>
> 参数 $k$ 控制了随机性的引入程度：
>
> 若令 $k=d$ ，则基决策树的构建与传统决策树相同；
>
> 若令 $k=1$，则是随机选择一个属性用于划分；
>
> 一般情况下，推荐值 $k=\log_{2}{d}$

**随机森林和bagging的主要差别在于，在随机森林中，分割的最佳特征是从一个随机特征子空间中选取的，而在bagging中，分割时将考虑所有特征。**

### 分类器

* [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
* [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier)
* [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)

以下使用三种分类器，分别对数据进行分类预测。

[credit_scoring_sample.csv](credit_scoring_sample.csv)

**数据看起来像这样：**

##### 目标变量

* SeriousDlqin2yrs - 该人在2年内长期拖延付款;二进制变量

##### 特征

| 列名                                 | 说明                                                         | 数据类型 |
| ------------------------------------ | ------------------------------------------------------------ | -------- |
| age                                  | 借款人的年龄（全年数）                                       | integer  |
| NumberOfTime30-59DaysPastDueNotWorse | 在过去两年中，一个人延迟偿还其他贷款超过30-59天（但不是更多）的次数 | integer  |
| DebtRatio                            | 每月付款（贷款，赡养费等）除以每月总收入，百分比             | float    |
| MonthlyIncome                        | 以美元计算的月收入                                           | float    |
| NumberOfTimes90DaysLate              | 一个人延迟偿还其他贷款超过90天的次数                         | integer  |
| NumberOfTime60-89DaysPastDueNotWorse | 在过去两年中，一个人延迟偿还其他贷款超过60-89天（但不是更多）的次数 | integer  |
| NumberOfDependents                   | 借款人家庭中的人数                                           | integer  |

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('credit_scoring_sample.csv', sep=";")
# 不包含目标值的列名集合
independent_columns_names = [x for x in data if x != 'SeriousDlqin2yrs']
```

```python
def impute_nan_with_median(table):
    """用表中每列的中位数替换NaN值"""
    for col in table.columns:
        table[col] = table[col].fillna(table[col].median())
    return table

table = impute_nan_with_median(data)

X = table[independent_columns_names]  # 数据（替换过NaN值）
y = table['SeriousDlqin2yrs']  # 目标值

n_estimators = 200  # 森林中树的数量
random_state = 17
scoring = 'roc_auc'
class_weight = 'balanced'

dtc = DecisionTreeClassifier(class_weight=class_weight, random_state=random_state)
results = cross_val_score(dtc, X, y, scoring=scoring)
print("决策树交叉验证精确度评分： {:.2f}%".format(results.mean() * 100))

bc = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=n_estimators, random_state=random_state)
results = cross_val_score(bc, X, y, scoring=scoring)
print("Bagging交叉验证精确度评分： {:.2f}%".format(results.mean() * 100))

rfc = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state, class_weight=class_weight)
results = cross_val_score(rfc, X, y, scoring=scoring)
print("随机森林交叉验证精确度评分： {:.2f}%".format(results.mean() * 100))
```

```
决策树交叉验证精确度评分： 65.21%
Bagging交叉验证精确度评分： 80.41%
随机森林交叉验证精确度评分： 80.60%
```

