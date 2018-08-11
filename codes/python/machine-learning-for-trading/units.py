import pandas as pd
from finance_datareader_py.sohu.daily import SohuDailyReader
from finance_datareader_py.eastmoney.daily import EastMoneyDailyReader
import matplotlib.pyplot as plt


def compute_daily_returns(df):
    """计算日收益"""
    return df[:-1].values / df[1:] - 1


def normalization(df):
    """数据归一化"""
    return df / df.iloc[-1]


def get_datas(symbols, start, end, type='ba'):
    """获取股票收盘价格数据

    * 读取时会加上 000300 的数据。
    * 读取的是后复权价格

    :param symbols: 单一股票代码或股票代码集合
    :param start: 开始日期
    :param end: 结束日期
    :param type: {None, 'fa', 'ba'}, 默认值 'ba'
        * None: 不复权（默认）
        * 'fa': 前复权
        * 'ba': 后复权
    :return: ''DataFrame''
    """
    df = pd.DataFrame()
    df['000300'] = SohuDailyReader('000300', prefix='zs_', start=start,
                                   end=end).read()['Close']
    if isinstance(symbols, str):
        df = _read_join_data(df, symbols, start, end, type=type)
    else:
        for symbol in symbols:
            df = _read_join_data(df, symbol, start, end, type=type)
    return df.fillna(method='bfill')  # 因为是倒序排序，所以使用bfill


def _read_join_data(df, symbol, start, end, type='ba'):
    """

    :param df:
    :param symbol:
    :param start:
    :param end:
    :param type: {None, 'fa', 'ba'}, 默认值 'ba'
        * None: 不复权（默认）
        * 'fa': 前复权
        * 'ba': 后复权
    :return: ''DataFraem''
    """
    # 具体股票采用后复权价格
    df1 = EastMoneyDailyReader(symbol, type=type, start=start,
                               end=end).read()
    df1 = df1.rename(columns={'Close': symbol})
    return df.join(df1[symbol])


def plot(df, x=None, y=None, kind='line', ax=None, subplots=False, sharex=None,
         sharey=False, layout=None, figsize=None, use_index=True, title=None,
         grid=None, legend=True, style=None, logx=False, logy=False,
         loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None,
         fontsize=None, colormap=None, table=False, yerr=None, xerr=None,
         secondary_y=False, sort_columns=False, **kwds):
    """绘图"""
    df.plot(x=x, y=y, kind=kind, ax=ax, subplots=subplots, sharex=sharex,
            sharey=sharey, layout=layout, figsize=figsize, use_index=use_index,
            title=title, grid=grid, legend=legend, style=style, logx=logx,
            logy=logy, loglog=loglog, xticks=xticks, yticks=yticks, xlim=xlim,
            ylim=ylim, rot=rot, fontsize=fontsize, colormap=colormap,
            table=table, yerr=yerr, xerr=xerr, secondary_y=secondary_y,
            sort_columns=sort_columns, **kwds)
    plt.show()
