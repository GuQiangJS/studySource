import unittest
from finance_datareader_py.csindex import get_stock_holdings
from finance_datareader_py.sohu.daily import SohuDailyReader
import datetime
import bbands
import units


class MyTestCase(unittest.TestCase):
    def test_something(self):
        lst = get_stock_holdings('000300')  # 获取沪深300指数成分股列表
        N = 20
        K = 2
        start = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        for symbol in lst['symbol']:
            df_bbands = bbands.get_Top_and_Bottom(symbol,
                                                  start=start,
                                                  end=end,
                                                  N=N, K=K)
            df = SohuDailyReader(symbol, start=start, end=end).read()
            units.plot(
                df_bbands[datetime.date(2017, 3, 1):datetime.date(2017, 4, 21)])
            units.plot(
                df_bbands[datetime.date(2017, 5, 24):datetime.date(2017, 6, 1)])
            units.plot(df_bbands[
                       datetime.date(2017, 7, 12):datetime.date(2017, 7, 18)])
            units.plot(df_bbands[
                       datetime.date(2017, 10, 9):datetime.date(2017, 12, 16)])
            df_bbands = df_bbands.join(df, how='left')
            print(df_bbands)
            # df_bbands.to_csv(symbol + '.csv')
            break


if __name__ == '__main__':
    unittest.main()
