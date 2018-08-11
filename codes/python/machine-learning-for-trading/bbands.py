"""布林带相关"""

import units
import datetime
import pandas as pd


def get_Top_and_Bottom(symbol, start, end, N=20, K=2):
    """获取满足布林带穿越布林带数据

    :param symbol:
    :param start:
    :param end:
    :param N:
    :param K:
    :return:
    """
    df = get_bbands(symbol, start, end, N, K)
    t = df.query('Close_Adj>=top')
    t['t'] = 'T'
    b = df.query('Close_Adj<=bottom')
    b['t'] = 'B'
    return pd.concat([t, b]).sort_index()


def get_bbands(symbol, start, end, N=20, K=2):
    """返回布林带数据

    :param symbol:
    :param start:
    :param end:
    :param N: 天数
    :param K: 标准差
    :return: ''DataFrame''
    """
    df = units.get_datas(symbol, start, end)
    df.sort_index(inplace=True)
    df = df[[symbol]]
    df = df.rename(columns={symbol: 'Close_Adj'})
    df['mean_' + str(N)] = df['Close_Adj'].rolling(N).mean()
    df['tmp2'] = df['Close_Adj'].rolling(N).std()
    df['top'] = df['mean_' + str(N)] + K * df['tmp2']
    df['bottom'] = df['mean_' + str(N)] - K * df['tmp2']
    return df.drop(labels='tmp2', axis=1)
