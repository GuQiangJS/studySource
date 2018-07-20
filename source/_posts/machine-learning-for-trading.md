---
title: Machine Learning for Trading
date: 2018-07-11 17:07:13
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
description: <!—more—->
typora-root-url: machine-learning-for-trading
---

教程Youtube链接:[https://www.youtube.com/playlist?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx)

#### The Data (介绍CSV文件)

#### Our Stock Data (介绍股票每日成交汇总数据格式)

* Date
* Open
* High
* Low
* Close
* Volume -> 成交量
* Adj Close -> 调整收盘价（除权除息价）

#### Pandas Dataframe

#### Actual CSV

#### Interesting Stuff

切片：取 `Dataframe` 中的部分数据

[pandas.DataFrame.loc](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html#pandas.DataFrame.loc)

#### Compute max closing price

[pandas.Series.max](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.max.html#pandas-series-max)

#### Plotting stock price data (绘图)

#### Plot two columns (绘制多个数据)

```python
import matplotlib.pyplot as plt
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader

df1 = EastMoneyDailyReader('601398').read()
df2 = EastMoneyDailyReader('601398', type='ba').read()
df = pd.DataFrame()
df['Close'] = pd.to_numeric(df1['Close'])
df['Adj Close'] = pd.to_numeric(df2['Close'])
print(df.tail())
df.plot()
plt.show()
```

![1531304006175](1531304006175.png)

#### Pandas dataframe recap

#### Problems to Solve

##### Data ranges(使用日期索引取值)

```
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader
df = EastMoneyDailyReader('601398').read()
df.tail()
Out[4]: 
            Open Close  High   Low   交易量(手)   成交金额     振幅   换手率
日期                                                             
2018-07-05  5.17  5.23  5.29  5.16  1865183  9.72亿  2.52%  0.07
2018-07-06  5.23  5.29  5.34  5.18  1925444  10.1亿  3.06%  0.07
2018-07-09  5.31  5.53  5.54  5.31  2155458  11.7亿  4.35%  0.08
2018-07-10  5.56  5.52  5.57  5.46  1289900  7.10亿  1.99%  0.05
2018-07-11  5.41  5.48  5.52  5.39  1520449  8.31亿  2.36%  0.06

df['2017-01-01':'2017-12-31'].tail()
Out[6]: 
            Open Close  High   Low   交易量(手)   成交金额     振幅   换手率
日期                                                             
2017-12-25  5.93  6.00  6.03  5.93  2396364  14.4亿  1.69%  0.09
2017-12-26  6.00  6.08  6.10  5.98  2165329  13.1亿     2%  0.08
2017-12-27  6.09  6.05  6.15  6.02  2151401  13.1亿  2.14%  0.08
2017-12-28  6.03  6.14  6.14  6.02  2100886  12.8亿  1.98%  0.08
2017-12-29  6.13  6.20  6.22  6.12  2168998  13.4亿  1.63%  0.08
```

取沪深300指数（399300）+单个股票数据。

取沪深300指数的意义在于，只要开市，那么指数就肯定有数据，而不像其他单一股票可能会出现不定期停牌的情况。

看下面的数据：

1. 2005年，300027还没有上市，所以数值为 `NaN`。
2. 2018-07-07、2018-07-08两天是休息日，不开市。这时不会有数据。

```
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader
df1 = EastMoneyDailyReader('399300').read()
df2 = EastMoneyDailyReader('300027').read()
df = pd.DataFrame()
df['399300'] = df1['Close']
df['300027'] = df2['Close']

df.head()
Out[4]: 
            399300 300027
日期                       
2005-01-04  982.79    NaN
2005-01-05  992.56    NaN
2005-01-06  983.17    NaN
2005-01-07  983.96    NaN
2005-01-10  993.88    NaN

df.tail()
Out[3]: 
             399300 300027
日期                        
2018-07-05  3342.44   6.08
2018-07-06  3365.12   6.09
2018-07-09  3459.18   6.12
2018-07-10  3467.52   6.03
2018-07-11  3407.53   5.96
```

#### Create an exmpty data frame

#### Join SPY data (使用Join关联数据，使用dropna丢弃空数据)

```
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader
df1 = EastMoneyDailyReader('399300').read()
dates = pd.date_range('2010-01-01', '2010-01-05')
# 创建空白DataFrame
df = pd.DataFrame(index=dates)
df = df.join(df1)

df['Close'].head()
Out[3]: 
2010-01-01        NaN
2010-01-02        NaN
2010-01-03        NaN
2010-01-04    3535.23
2010-01-05    3564.04
Freq: D, Name: Close, dtype: object

df['Close'].head().dropna()
Out[4]: 
2010-01-04    3535.23
2010-01-05    3564.04
Freq: D, Name: Close, dtype: object
```

#### Read in more stocks(重命名，一个dataframe中不能出现同名的列)

#### Slicing (数据切片)

```python
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader

symbols = ['399300', '300027', '601398']

dates = pd.date_range('2010-01-01', '2010-01-05')
# 创建空白DataFrame
df = pd.DataFrame(index=dates)
for symbol in symbols:
    df_temp = EastMoneyDailyReader(symbol).read()
    df_temp = df_temp.rename(columns={'Close': symbol})
    df = df.join(df_temp[symbol])

print(df)
print('------------------------')
print(df.dropna())
print('------------------------')
print(df.loc['2010-01-04':'2010-01-04',['000002', '601398']])
```

```
             399300 300027 601398
2010-01-01      NaN    NaN    NaN
2010-01-02      NaN    NaN    NaN
2010-01-03      NaN    NaN    NaN
2010-01-04  3535.23  55.53   5.35
2010-01-05  3564.04  55.09   5.40
------------------------
             399300 300027 601398
2010-01-04  3535.23  55.53   5.35
2010-01-05  3564.04  55.09   5.40
------------------------
             399300 300027
2010-01-04  3535.23  55.53

```

#### Problems with Plotting (判断时股价起点不同，很难在同一层面观察)

```python
import matplotlib.pyplot as plt
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader

symbols = ['600519', '000002', '601398']

# 创建空白DataFrame
df = pd.DataFrame()
for symbol in symbols:
    df_temp = EastMoneyDailyReader(symbol).read()
    df[symbol] = df_temp['Close']

df = df.dropna()
df.loc['2017-01-01':'2017-12-31'].plot()
plt.show()
```

![1531383436936](1531383436936.png)

#### Normalizing (数据归一化)

```
def normalize_data(df):
    return df / df.iloc[0]

normalize_data(df.loc['2017-01-01':'2017-12-31']).plot()
```

让Dataframe的每一行数据除以第一行的值，从而使所有数据从1开始。

![1531384011994](1531384011994.png)

#### What is NumPy

#### Relationship to Pandas (numpy与Pandas的关系)

#### Compute global statistics

[标准差](https://zh.wikipedia.org/wiki/%E6%A8%99%E6%BA%96%E5%B7%AE)

> 例如，两组数的集合{0, 5, 9, 14}和{5, 6, 8, 9}其平均值都是7，但第二个集合具有较小的标准差。 

#### Rolling statistics

#### Bollinger Bands

[布林带](https://zh.wikipedia.org/wiki/%E5%B8%83%E6%9E%97%E5%B8%A6)

```python
df = pd.DataFrame()
df['Close'] = EastMoneyDailyReader('601398').read()['Close']
df['rol_30'] = pd.rolling_mean(df['Close'], window=30)
df.head(100).plot()
plt.show()
```

![1531465284221](1531465284221.png)

#### Daily returns (日收益)

日收益基本上是围绕0上下浮动。

`daily_ret[t]=(price[t]/price[t-1])-1`

`(110/100)-1=1.1-1=0.1=10%`

#### Cumulative returns (累计收益)

累积收益和数据归一化在计算中的意思基本一致。

#### A closer look at daily returns

使用直方图展示日收益率的分布情况

[峰度](https://zh.wikipedia.org/wiki/%E5%B3%B0%E5%BA%A6)

> 峰度高就意味着方差增大是由低频度的大于或小于平均值的极端差值引起的。 

[肥尾分布](https://zh.wikipedia.org/wiki/%E8%82%A5%E5%B0%BE%E5%88%86%E5%B8%83)

#### Computing rolling statistics

20日移动平均线

```python
df = EastMoneyDailyReader('601398').read().tail(200)
ax = df['Close'].plot(title='601398 rolling mean')
rm = pd.rolling_mean(df['Close'], window=20)
rm.plot(label='Rolling mean', ax=ax)

ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(loc='upper left')
plt.show()
```

![1531632440578](1531632440578.png)

#### Using fillna() (数据市场是不完整的，需要补齐)

#### Histogram of daily returns (使用直方图来查看每日收益)

#### How to plot a histogram (如何绘制直方图)

```python
def compute_daily_returns(df):
    return df[:-1].values / df[1:] - 1


df = EastMoneyDailyReader('601398').read()
daily_returns = compute_daily_returns(df['Close'])
daily_returns.hist(bins=50)
print(daily_returns.tail(100))
plt.show()
```

![1531634310060](1531634310060.png)

[关于证券收益分布原因的讨论](https://www.ricequant.com/community/topic/126/)

#### 绘制平均值和标准差

```python

mean = daily_returns.mean()
print("mean=", mean)
std = daily_returns.std()
print('std=', std)
plt.axvline(mean, color='g')
plt.axvline(std, color='r', linestyle='dashed')
plt.axvline(-std, color='r', linestyle='dashed')
plt.show()
```

![1531635134977](1531635134977.png)

#### 计算峰度

```python
print(daily_returns.kurtosis())
```

```
7.34265127165
```

> 在机率论中，**肥尾分布**（英语：Fat-tailed distribution）是一种[机率分布](https://zh.wikipedia.org/wiki/%E6%A9%9F%E7%8E%87%E5%88%86%E5%B8%83)模型。它是一种[重尾分布](https://zh.wikipedia.org/wiki/%E9%87%8D%E5%B0%BE%E5%88%86%E5%B8%83)，但是它的[偏度](https://zh.wikipedia.org/wiki/%E5%81%8F%E5%BA%A6)或[峰度](https://zh.wikipedia.org/wiki/%E5%B3%B0%E5%BA%A6)极端的大。与无所不在的[正态分布](https://zh.wikipedia.org/wiki/%E5%B8%B8%E6%85%8B%E5%88%86%E5%B8%83)作比较，[正态分布](https://zh.wikipedia.org/wiki/%E5%B8%B8%E6%85%8B%E5%88%86%E5%B8%83)属于一种细尾分布，或[指数分布](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B0%E5%88%86%E5%B8%83)。 



