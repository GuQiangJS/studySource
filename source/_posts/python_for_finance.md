---
title: Python 金融大数据分析
date: 2018-06-29 09:12:26
tags:
 - 编程
 - Python
 - 金融
 - 股票
categories:
 - 编程
 - Python
 - 金融
 - 股票
出版社: 人民邮电出版社
ISBN: 9787115404459
出版时间: 2015-12-01
typora-root-url: python_for_finance
description: <!—more—->
---

## 第一章 为什么将Python用于金融

## 第二章 基础架构和工具

### 2.1 Python部署

#### 2.1.1 [Anaconda](https://anaconda.org/)

[初学python者自学anaconda的正确姿势是什么？？](https://www.zhihu.com/question/58033789)

#### 2.1.2 Python Quant Platform

## 第三章 入门示例

* 隐含波动率 [隐含波动率- MBA智库百科](http://wiki.mbalib.com/wiki/%E9%9A%90%E5%90%AB%E6%B3%A2%E5%8A%A8%E7%8E%87)

  以某些到期H 的期权1&价倒惟出这些期权的隐含波动率，并绘出阁表一一这是期权交易者和风险管理者每天都要面对的任务。

* 蒙特卡洛模拟 [蒙特卡罗方法- MBA智库百科](http://wiki.mbalib.com/wiki/%E8%92%99%E7%89%B9%E5%8D%A1%E7%BD%97%E6%96%B9%E6%B3%95)

  通过蒙特卡洛技术，模拟股票指数在一段时间中的变化，对选中的结果进行可视化.并计算欧式期权价值。蒙特卡洛模拟是期权数字化定价的基石，也是涉及风险价值计算或者信用值调整的风险管理℃作的基础。

* 技术分析 [技术分析-维基百科](https://zh.wikipedia.org/wiki/%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90)

  实施历史时间序列数据的分析，对根据趋势信号的投资策略进行事后验证;专业投资者和有抱负的业余投资者常常进行这类投资分析。

### 第四章 数据类型和结构

* [https://www.python.org/doc/](https://www.python.org/doc/)
* [https://www.scipy.org/docs.html](https://www.scipy.org/docs.html)

###第五章 数据可视化

* [https://matplotlib.org/contents.html](https://matplotlib.org/contents.html)

### 第六章 金融时间序列

#### 6.2 金融数据

https://github.com/GuQiangJS/finance-datareader-py

```python
import matplotlib.pyplot as plt
import numpy as np
from finance_datareader_py.netease.daily import NetEaseDailyReader

df = NetEaseDailyReader('000002').read()
df = df.tail(n=100)
df = df.replace(0, np.nan)
df = df.fillna(method='ffill')
df.plot(y='Close')
plt.show()
```

![1533087934260](1533087934260.png)

根据每日收盘价返回对数收益率。

```python
from finance_datareader_py.netease.daily import NetEaseDailyReader

df = NetEaseDailyReader('000002').read()
df = df.replace(0, np.NaN)
df['Return'] = df['Close'] / df['Close'].shift(1)
print(df[['Close', 'Return']].tail())
```

```
            Close    Return
                           
2018-07-04  23.00  0.982067
2018-07-05  23.05  1.002174
2018-07-06  23.21  1.006941
2018-07-09  24.01  1.034468
2018-07-10  24.15  1.005831
```

> **波动率聚集**：波动率不是长期恒定的；既有高波动率时期（正负收益都很高），也有低波动率时期
>
> **杠杆效应**：一般来说，波动性的股票市场收益是负相关的；当市场下跌的时候波动性升高，反之亦然。

```python
# 收盘价与回报率的对应图表
df[['Close', 'Return']].plot(subplots=True, figsize=(8, 5))
plt.show()
```

![1533088423103](1533088423103.png)

[移动平均](https://zh.wikipedia.org/wiki/%E7%A7%BB%E5%8B%95%E5%B9%B3%E5%9D%87)

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from finance_datareader_py.netease.daily import NetEaseDailyReader

df = NetEaseDailyReader('601398').read()
df['Return'] = np.log(df['Close'] / df['Close'].shift(1))
print(df[['Close', 'Return']].tail())
df['42d'] = pd.rolling_mean(df['Close'], window=42)
df['252d'] = pd.rolling_mean(df['Close'], window=252)
print(df[['Close', '42d', '252d']].tail())
df[['Close', '42d', '252d']].tail(n=1000).plot(figsize=(8, 5))
plt.show()
```

![1533088473653](1533088473653.png)

#### 6.3 回归分析

[最小二乘法](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95)

### 第七章 输入输出操作

#### 7.3 PyTables的快速I/O

[PyTables ](https://www.pytables.org/index.html)是 Python 与 HDF5 数据库/文件标准的结合(https://www.hdfgroup.org/)

> PyTables可以把大数据直接写入本地硬盘而并不使用任何数据库管理软件和SQL 

##### 7.3.4 内存外计算

[numexpr](https://github.com/pydata/numexpr)

#### 延伸阅读

* 用 pickle 进行的 Pytbon 对象序列化参见如下文梢: http://docs.python.orgl2/library/pickle.html 。

* SciPy 网站上提供 NumPy 1/0 能力的概述: http://docs.scipy.orgldoc/numpy/referencc/rolltines.io.htm1 。
* pandas 的I/0 参见在线文档的相应章节: http://pandas.pydata.orglpandas-docs/stab1e/io.html 。
* PyTables 首页提供教程和详细文梢: http://www.pytables.org

### 第八章 高性能Python

#### 延伸阅读

* numexpr 的细节参见http://github.com/pydata/nwnexpr
* IPytbon.parallel 在这里介绍: http://ipython.org!ipython-doc/stable/parallel
* multiprocessing 模块的文稍: https://docs.python.org/2/library/multiprocessing.html

* Numba 的信息、可以在http://github.com/numbalnumba 找到
* http://cython.org是Cython 编译器项目的首页
* NumbaPro 的文树可以参见http://docs.continuum.io/nwnbapro

### 第九章 数学工具

#### 9.1 逼近法

[逼近理论](https://zh.wikipedia.org/wiki/%E9%80%BC%E8%BF%91%E7%90%86%E8%AE%BA) 

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x) + 0.5 * x

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
plt.plot(x, f(x), 'b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
```

![1531297702083](1533088496598.png)

