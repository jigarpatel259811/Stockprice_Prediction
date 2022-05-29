from matplotlib import ticker
import pandas as pd 
import traceback
import csv
from Ticker import Tickers
import yfinance as yf
from yahoofinancials import YahooFinancials


tickers_collection = {}


class Main():
    def __init__(self) -> None:
        try:
            self.load_tickers()
            self.load_historydata()
        except Exception as ex:
            print(traceback.format_exc())
    def load_tickers(self): # load tickers from csv file using csv dict module
        try:
            tickers_df =  pd.read_csv("Tickers.csv")
            # loop on df and create tickers obj
            for row in tickers_df:
                tickers = Tickers()
                tickers.tickerId = len(tickers_collection) + 1
                tickers.symbol = row[0]

                tickers_collection[tickers.tickerId] = tickers
        except Exception as ex:
            print(traceback.format_exc())
    
    def load_historydata(self): # historydata from csv or yahoo
        try:
            for tickers in tickers_collection:
                tickers.symbol # using this download history data from source


        except Exception as ex:
            print(traceback.format_exc())
'''
data = yf.download( 
    tickers = "SPY AAPL MSFT",
    period = "ytd",
    interval = "1m",
    group_by = 'ticker',
    auto_adjust = True,
    prepost = True,
    threads = True,
    proxy = None )
'''
aapl_df = yf.download('AAPL')

main = Main()
