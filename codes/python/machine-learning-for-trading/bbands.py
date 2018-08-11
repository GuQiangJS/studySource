"""布林带相关"""

import pandas as pd

import units


def get_Upper_and_Lower(symbol, start, end, N=20, K=2):
    """获取满足穿越布林带的数据

    :param symbol:
    :param start:
    :param end:
    :param N:
    :param K:
    :return:
    """
    df = get_bbands(symbol, start, end, N, K)
    t = df[(df['Close_Adj'] <= df['top'])
               & (df['Close_Adj'].shift(1) >= df['top'].shift(1))]
    t['T'] = 'S'
    b = df[(df['Close_Adj'] >= df['bottom'])
               & (df['Close_Adj'].shift(1) <= df['bottom'].shift(1))]
    b['T'] = 'B'
    return pd.concat([t, b]).sort_index()


def get_bbands(symbol, start, end, N=20, K=2):
    """返回布林带数据

    :param symbol:
    :param start:
    :param end:
    :param N: 天数
    :param K: 标准差
    :return: ''DataFrame'':
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
