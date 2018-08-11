import datetime
import json
import time
import unittest

from finance_datareader_py.csindex import get_stock_holdings
from finance_datareader_py.sina import get_dividends
from finance_datareader_py.sohu.daily import SohuDailyReader

import bbands


class MyTestCase(unittest.TestCase):
    def test_something(self):
        lst = get_stock_holdings('000016')  # 获取上证50指数成分股列表
        N = 20
        K = 2
        start = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        S = {}
        # f = 'symbols'
        # os.makedirs(f, exist_ok=True)
        for symbol in lst['symbol']:
            try:
                S[symbol] = self._cal_bbands(symbol, start, end, N, K)
                # bbands.get_bbands(symbol, start, end, N, K).to_csv(symbol + '.csv')
            except:
                continue
        print(S)
        with open('s.json', mode='wt+', encoding='utf-8') as file:
            json.dump(S, file)

    def test_plot(self):
        """绘制图表"""
        import matplotlib.pyplot as plt
        start = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        df = bbands.get_bbands('600016', start=start,
                               end=end)
        df['2017-2-15':'2017-3-10'][['Close_Adj', 'top', 'bottom']].plot()
        plt.axvline('2017-2-17', color='r', linestyle='dashed')
        plt.axvline('2017-3-3', color='r', linestyle='dashed')
        plt.show()

    def _cal_bbands(self, symbol, start, end, N, K):
        """计算、打印、保存布林带信息"""
        df_bbands = bbands.get_Upper_and_Lower(symbol,
                                               start=start,
                                               end=end,
                                               N=N, K=K)
        df = SohuDailyReader(symbol, start=start, end=end).read()
        df_bbands = df_bbands.join(df, how='left')
        holding_count = 0  # 当前持仓数量
        for date in df_bbands.index:
            if df_bbands.at[date, 'T'] == 'S' and holding_count != 0:
                # 卖出操作
                df_bbands.at[date, 'C'] = abs(holding_count)
                holding_count = 0
            if df_bbands.at[date, 'T'] == 'B':
                # 买入操作
                df_bbands.at[date, 'C'] = -100
                holding_count = holding_count - 100
        df_bbands = self._cal_dividends(symbol, start, end, df_bbands)
        df_bbands = self._cal_sum(df_bbands)
        print(df_bbands)
        earning = self._cal_earning(df_bbands)
        holding_sum = self._cal_holding_sum(df_bbands)
        print('{0} : {1}/{2}'.format(symbol, earning + holding_sum,
                                     holding_sum))
        # S[symbol] = {'earning': earning + holding_sum,
        #              'holding_sum': holding_sum}
        print('-----------------------------------------------------------')
        time.sleep(10)
        df_bbands.to_csv(symbol + '_bbands.csv')
        df.to_csv(symbol + '.csv')
        return {'earning': earning + holding_sum,
                'holding_sum': holding_sum}

    def _cal_sum(self, df):
        """计算持仓花费"""
        if df.empty or 'C' not in df.columns:
            return df
        df['Sum'] = df['Close'] * df['C']
        return df

    def _cal_earning(self, df):
        """计算收益（包含当前占用的持仓资金)"""
        if df.empty or 'Sum' not in df.columns:
            return 0
        df = self._cal_sum(df)
        return df.dropna()['Sum'].sum()

    def _cal_holding_sum(self, df):
        """计算当前持仓资金占用"""
        if df.empty or 'T' not in df.columns:
            return 0
        sum = 0
        for index in df.sort_index(ascending=False).index:
            if df.at[index, 'T'] == 'B':
                sum = sum + df.at[index, 'Sum']
            elif df.at[index, 'T'] == 'S':
                break
        return abs(sum)

    def _cal_dividends(self, symbol, start, end, df):
        """附加分红数据到持仓"""
        if df.empty or 'C' not in df.columns:
            return df
        divs = get_dividends(symbol)
        zz = divs[0].sort_index()[start:end]
        df_s = df[df['C'] > 0]
        for i in range(len(df_s.index)):
            index = df_s.index[i]
            last = df_s.index[i - 1] if i > 0 else None
            zz_sum = zz[last:index]['转增(股)'].sum()
            # Todo
            df.at[index, 'C'] = df.at[index, 'C'] * (1 + zz_sum / 10)
        return df


if __name__ == '__main__':
    unittest.main()
