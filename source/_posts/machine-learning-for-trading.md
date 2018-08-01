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
typora-root-url: machine-learning-for-trading
description: <!—more—->
---

教程Youtube链接:[https://www.youtube.com/playlist?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnIRwl6rad_mYwEk4Gmj7Mx)

### 单一股票收益

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

> 在机率论中，*肥尾分布**（英语：Fat-tailed distribution）是一种[机率分布](https://zh.wikipedia.org/wiki/%E6%A9%9F%E7%8E%87%E5%88%86%E5%B8%83)模型。它是一种[重尾分布](https://zh.wikipedia.org/wiki/%E9%87%8D%E5%B0%BE%E5%88%86%E5%B8%83)，但是它的[偏度](https://zh.wikipedia.org/wiki/%E5%81%8F%E5%BA%A6)或[峰度](https://zh.wikipedia.org/wiki/%E5%B3%B0%E5%BA%A6)极端的大。与无所不在的[正态分布](https://zh.wikipedia.org/wiki/%E5%B8%B8%E6%85%8B%E5%88%86%E5%B8%83)作比较，[正态分布](https://zh.wikipedia.org/wiki/%E5%B8%B8%E6%85%8B%E5%88%86%E5%B8%83)属于一种细尾分布，或[指数分布](https://zh.wikipedia.org/wiki/%E6%8C%87%E6%95%B0%E5%88%86%E5%B8%83)。 

> 

##### Plot two histograms together (合并绘制两个直方图)

```python
import matplotlib.pyplot as plt
import pandas as pd
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader


def compute_daily_returns(df):
    return df[:-1].values / df[1:] - 1


df = pd.DataFrame()
df['601398'] = EastMoneyDailyReader('601398').read()['Close']
df['601939'] = EastMoneyDailyReader('601939').read()['Close']
# 计算日收益率
daily_returns = compute_daily_returns(df)
# 绘制直方图
daily_returns.hist()
# 绘图
plt.show()

# 合并绘制两个直方图
daily_returns['601398'].hist(label='601398')
daily_returns['601939'].hist(label='601939')
plt.legend(loc='upper right')
plt.show()
```

![1532508260900](/1532508260900.png)

![1532508276951](/1532508276951.png)

股票和市场的日收益分布和高斯分布非常相似。这个性质对 *日收益、月收益、年收益* 来说同样适用。

如果它们真的是高斯分布，那么我们就可以说它们是正态分布。

**但是假定收益是正态分布的，却是非常危险的。因为它忽略了峰度或者尾部。** *正是因为这样才造成了08年的金融风暴。*

#### Scatterplots (散点图)

这是区分各支股票日收益的另一种方法。

线性但离散的特点。



{% blockquote Beta系数 https://zh.wikipedia.org/wiki/Beta%E7%B3%BB%E6%95%B0 %}
贝他值（ $\beta$ 值）：
用以衡量基金之市场风险，或称系统性风险。其计算的方式为以过去12个月或24个月之基金月报酬率对同期市场月报酬率做回归，估计斜率系数而得，当 $\beta$ >1（$\beta$ < -1），表示基金坡动度较指数为大，当指数上扬 10%（下跌10%），基金会上扬超过 10%（下跌超过10%）；当 $\beta$ = 1，表示指数涨跌多少，基金就跟着变动多少。
{% endblockquote %}



{% blockquote 阿尔法系数 https://zh.wikipedia.org/wiki/%E8%AF%81%E5%88%B8%E6%8A%95%E8%B5%84%E5%9F%BA%E9%87%91#%E9%98%BF%E5%B0%94%E6%B3%95%E7%B3%BB%E6%95%B0 %}
阿尔法系数（ $\alpha$）是基金的实际收益和按照β系数计算的期望收益之间的差额。其计算方法如下：超额收益是基金的收益减去无风险投资收益（在中国为1年期银行定期存款收益）；期望收益是贝塔系数 $\beta$ 和市场收益的乘积，反映基金由于市场整体变动而获得的收益；超额收益和期望收益的差额即 $\alpha$ 系数。该系数越大越好。
{% endblockquote %}



##### Slope does not equal correlation (斜率 $\beta$ 系数与数据的相关性/拟合度无关)

可能有很低的斜率，但是数据拟合度非常高。反之亦然。

##### Scatterplots in python (散点图)

```python
df = pd.DataFrame()
df['000300'] = SohuDailyReader('000300', prefix='zs_').read()['Close']
df['601398'] = SohuDailyReader('601398').read()['Close']
df['601939'] = SohuDailyReader('601939').read()['Close']
# 计算日收益率
daily_returns = compute_daily_returns(df)
# 绘制 601398 相对于 000300 的散点图
daily_returns.plot(kind='scatter', x='000300', y='601398')
plt.show()
# 绘制 601939 相对于 000300 的散点图
daily_returns.plot(kind='scatter', x='000300', y='601939')
plt.show()
```

![1532570705884](/1532570705884.png)

![1532570720355](/1532570720355.png)

```python
import numpy as np

# beta系数和alpha系数
beta, alpha = np.polyfit(daily_returns['000300'], daily_returns['601939'], 1)

daily_returns.plot(kind='scatter', x='000300', y='601939')
# 绘制拟合线
plt.plot(daily_returns['000300'], beta * daily_returns['000300'] + alpha, '-',
         color='r')
plt.show()
print('beta=' + str(beta))
print('alpha=' + str(alpha))
```

```
beta=0.590256550806
alpha=-0.000246730309092
```

![1532571574686](/1532571574686.png)

### 投资组合

##### Daily portfolio values

[https://youtu.be/UweF-2-Tr9Y](https://youtu.be/UweF-2-Tr9Y)

```
投资组合假设：
start_val = 1000000 # 初始投资总额
start_date = 2011-01-01 # 初始投资日期
end_date = 2011-12-31 # 结束投资日期
# 投资组合：贵州茅台、中国平安、招商银行、格力电器
symbols = ['600519','601318','600036','000651'] 
# 比率分配
allocs = [0.4,0.4,0.1,0.1]
```

##### 如何计算投资组合每日的总价值：

[https://youtu.be/UweF-2-Tr9Y](https://youtu.be/UweF-2-Tr9Y)

1. 从价格 `DataFrame` 开始。
2. 价格归一化（`normed=prices/prices[0]`）。开始日期的数据始终为1.0。
3. 使用归一化以后的值乘以每支股票分配的资金比例（`alloced=normed*allocs`）。
4. 使用初始投资总额乘以3的结果（`pos_vals=alloced*start_val`）
5. 每一天的总价值：`port_val=pos_vals.sum(axis=1)`

![1532675498707](/1532675498707.png)

计算后的每日收益的第一天的收益始终为 *0*，所以应该去除。 `daily_returns=daily_returns[1:]` 

有了每日收益之后可以计算很多有趣的数据。**评估投资组合时的常用数据**：

* `cum_ret` 累计收益 `(port_val[-1]/port_val[0])-1`
* `avg_daily_ret` 平均收益 `daily_rets.mean()`
* `std_daily_ret` 每日收益标准差 `daily_rets.std()`
* `sharpe_ratio` 夏普比率

```python
import datetime
import pandas as pd
from finance_datareader_py.sohu.daily import SohuDailyReader

def compute_daily_returns(df):
    return df[:-1].values / df[1:] - 1

SYMBOLS = ['600519', '601318', '600036', '000651']
ALLOCS = [0.4, 0.4, 0.1, 0.1]
START = datetime.date(2009, 1, 1)
END = datetime.date(2011, 12, 31)

def get_datas(symbols, start, end):
    df = pd.DataFrame()
    df['000300'] = SohuDailyReader('000300', prefix='zs_', start=start,
                                   end=end).read()['Close']
    for symbol in symbols:
        df1 = SohuDailyReader(symbol, start=start, end=end).read()
        df1 = df1.rename(columns={'Close': symbol})
        df = df.join(df1[symbol])
    return df.fillna(method='bfill')  # 因为是倒序排序，所以使用bfill

df = get_datas(SYMBOLS, START, END)
df_ret = compute_daily_returns(df)
print(df)
print(df_ret)
print('-----------------')
print('平均收益:')
print(df_ret.mean())
print('-----------------')
print('每日收益标准差:')
print(df_ret.std())
print('-----------------')
print('累计收益:')
print(df.iloc[0] / df.iloc[-1] - 1)

# 移除指数列，并按照比率分配
alloced = df_nor.copy().drop('000300', axis=1) * ALLOCS
# 按照比率分配后的各支股票的每日价值
pos_vals = alloced * START_VALS
# 投资组合的每日价值
port_val = pos_vals.sum(axis=1)
```

```
-----------------
平均收益:
000300    0.000443
600519    0.000973
601318    0.000508
600036    0.000162
000651    0.000445
dtype: float64
-----------------
每日收益标准差:
000300    0.016803
600519    0.018983
601318    0.023065
600036    0.021895
000651    0.031399
dtype: float64
-----------------
累计收益:
000300    0.245773
600519    0.783539
601318    0.193761
600036   -0.057188
000651   -0.074906
dtype: float64
```

##### Sharpe ratio (夏普比率)

[https://youtu.be/5cqstpRndtI](https://youtu.be/5cqstpRndtI)

{% blockquote 夏普比率 http://wiki.mbalib.com/wiki/%E5%A4%8F%E6%99%AE%E6%AF%94%E7%8E%87 %}

　　现代投资理论的研究表明,风险的大小在决定组合的表现上具有基础性的作用。风险调整后的收益率就是一个可以同时对收益与风险加以考虑的综合指标,以期能够排除风险因素对绩效评估的不利影响。夏普比率就是一个可以同时对收益与风险加以综合考虑的三大经典指标之一。

　　投资中有一个常规的特点，即投资标的的预期报酬越高，投资人所能忍受的波动风险越高；反之，预期报酬越低，波动风险也越低。所以理性的投资人选择投资标的与投资组合的主要目的为：在固定所能承受的风险下，追求最大的报酬；或在固定的预期报酬下，追求最低的风险。

　　夏普比率计算公式：＝[E(Rp)－Rf]/σp

　　其中E(Rp)：投资组合预期报酬率

　　Rf：无风险利率

　　σp：投资组合的标准差

　　目的是计算投资组合每承受一单位总风险，会产生多少的超额报酬。比率依据资本市场线(Capital Market Line,CML)的观念而来，是市场上最常见的衡量比率。当投资组合内的资产皆为风险性资产时，适用夏普比率。夏普指数代表投资人每多承担一分风险，可以拿到几分报酬；若为正值，代表基金报酬率高过波动风险；若为负值，代表基金操作风险大过于报酬率。这样一来，每个投资组合都可以计算Sharpe Ratio,即投资回报与多冒风险的比例，这个比例越高，投资组合越佳。

　　举例而言，假如国债的回报是3%，而您的投资组合预期回报是15%，您的投资组合的标准偏差是6%，那么用15%－3%,可以得出12%（代表您超出无风险投资的回报），再用12%÷6%＝2，代表投资者风险每增长1%，换来的是2%的多余收益。

{% endblockquote %}

###### 以下计算夏普比率的公式使用：

`日收益 减去 日化无风险收益率 的均值 / 日收益 减去 日化无风险收益率 的标准差`

`S = mean(daily_rets - daily_rf) / std(daily_rets - daily_rf)`

什么是日化无风险收益率？视频中采用了 *伦敦银行同业拆放利率、3月期国债利率、0%*。

如何计算日化收益率？假设年收益为10%，每年有252个交易日。那么日收益率：

daily_rf = $\sqrt[252]{1.0+0.1}-1$

将 daily_rf 视为一个常数时（和将常数视作0的效果一样），可以将计算公式改为：

`S = mean(daily_rets - daily_rf) / std(daily_rets)`

> 夏普比率对于相同资产可以有相当大的变化。**取决于采样的频繁度**
>
> 如果每年采样股票价格，并且基于年化统计量计算，会得到一个数字；如果每月采样，会得到不同的数字；如果改成每日采样，又会得到另一个数字。
>
> **最初版本的夏普比率是一个年化的测量值。所以如果需要以非年化的采样来计算，那么需要加上一个调整因子来使其正常工作。**
>
> `SRannualized = K * SR`
>
> 调整因子（K）是每年的采样数量值的平方根。
>
> 假设使用的是每日采样，一年共有252个交易日。daily K = $\sqrt{252}$
>
> 假设使用的是每周采样，一年共有52个交易周。daily K = $\sqrt{52}$
>
> 假设使用的是每月采样，一年共有12个交易月。daily K = $\sqrt{12}$
>
> **即便某支股票一年只交易了80天，在以每日采样计算调整因子时，还是应该是用252来进行计算**

##### What is an optimizer（优化器）

* 用来寻找函数最小值
* 从数据中查找并建立参数化模型（从实验数据中找到一个多项式来拟合实验数据）
* 使用优化器来改善股票投资组合中的分配方式

```python
import scipy.optimize as spo

def f(X):
    Y = (X - 1.5) ** 2 + 0.5
    print("X={0},Y={1}".format(X, Y))
    return Y

Xguess = 2.0
min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
print('Minima found at:')
print("X={0},Y={1}".format(min_result.x, min_result.fun))
```

```
X=[ 2.],Y=[ 0.75]
X=[ 2.],Y=[ 0.75]
X=[ 2.00000001],Y=[ 0.75000001]
X=[ 0.99999999],Y=[ 0.75000001]
X=[ 1.5],Y=[ 0.5]
X=[ 1.5],Y=[ 0.5]
X=[ 1.50000001],Y=[ 0.5]
Optimization terminated successfully.    (Exit mode 0)
            Current function value: 0.5
            Iterations: 2
            Function evaluations: 7
            Gradient evaluations: 2
Minima found at:
X=[ 1.5],Y=0.5
```

```python
Xplot = np.linspace(0.5, 2.5, 21)
Yplot = f(Xplot)
plt.plot(Xplot, Yplot)
plt.plot(min_result.x, min_result.fun, 'ro')
plt.title('Minima of an objective function')
plt.show()
```

![1532659982849](/1532660052844.png)

##### Convex Problems (凸问题)

**凸集必定有局部最小值，同时这个局部最小值也就是全局最小值。**

##### 构建参数化模型

什么是参数化模型？`f(x) = mx+b`这是个关于 x 的函数，它有两个参数 m 和 b。

优化器就是通过不断的修改参数值并迭代函数，来找到函数的最优解。

```python
def get_portfoilo(symbols, start, end, allocs, start_values):
    """获取投资组合与沪深300指数的收益比较

    :param symbols: 投资组合
    :param start: 开始日期
    :param end: 结束日期
    :param allocs: 投资组合比率
    :param start_values: 初始总投资额
    :return:
    """
    df = get_datas(symbols, start, end)
    normed = normalization(df)
    alloced = normed.copy().drop('000300', axis=1) * allocs
    pos_vals = alloced * start_values
    port_val = pos_vals.sum(axis=1)
    return normalization(pd.DataFrame(port_val.copy(),
                                      columns=['Portfoilo']).join(df['000300']))

# 投资组合一年的表现与沪深300指数的比较
portpoilo = get_portfoilo(SYMBOLS, START, END, ALLOCS, START_VALS)
portpoilo.show()
plt.grid()
plt.show()
```

![1532677809156](/1532677939302.png)

```python
# 修改投资比率
portpoilo = get_portfoilo(SYMBOLS, START, END, [0.5, 0, 0, 0.5], START_VALS)
portpoilo.plot()
plt.grid()
plt.show()
```

![1532678552063](/1532678552063.png)

优化器的作用就在于确定如何找到最优的投资比率和股票组合。

### Types of funds（基金类型）

* ETF [交易所交易基金、交易所买卖基金](https://zh.wikipedia.org/wiki/ETF)
* Mutual Fund [共同基金](https://zh.wikipedia.org/wiki/%E5%85%B1%E5%90%8C%E5%9F%BA%E9%87%91)
* Hedge Fund [对冲基金](https://zh.wikipedia.org/wiki/%E5%AF%B9%E5%86%B2%E5%9F%BA%E9%87%91)

| **Parameter**                     | **Hedge Fund**                            | **Mutual Fund**                                  | **ETF**                                           |
| --------------------------------- | ----------------------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| **Return**                        | *Absolute return*                         | *Relative return*                                | *Relative return*                                 |
| **Management**                    | *Actively managed*                        | *Comparatively less actively managed*            | *Passively managed*                               |
| **Fees**                          | *Performance based fee*                   | *Percentage of assets managed fees*              | *–*                                               |
| **Transaction Price**             | *–*                                       | *NAV*                                            | *Quoted price*                                    |
| **Transparency**                  | *Information disclosed to investors only* | *Annually published reports and disclosure*      | *Daily disclosure of holdings*                    |
| **Regulation**                    | *Less regulation*                         | *Regulated by SEBI*                              | *Regulated by Securities and Exchange Commission* |
| **Liquidity**                     | *Low*                                     | *High*                                           | *High*                                            |
| **Cost**                          | *–*                                       | *High average expense ratio*                     | *Low average expense ratio*                       |
| **Investor Type**                 | *High net worth individuals*              | *Retail investors*                               | *Retail investors*                                |
| **Fractional Shares**             | *No*                                      | *Yes*                                            | *No*                                              |
| **Ownership of Fund Manager**     | *Substantial ownership*                   | *Non substantial ownership*                      | *–*                                               |
| **Owners**                        | *Few owners*                              | *Many owners*                                    | *–*                                               |
| **Minimum amount to be invested** | *High*                                    | *Low*                                            | *Low*                                             |
| **Tax**                           | *–*                                       | *High percentage of tax levied on capital gains* | *Comparatively lower tax percentages are levied*  |















