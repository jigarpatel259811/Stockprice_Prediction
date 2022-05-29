class Tickers():
    def __init__(self):
        self.tickerId = 0 
        self.symbol = None # script name 
        self.sectype = None # STk,IND,FOREX
        self.curr = None # INR,USD,EUR
        self.exchange = None # NSE, SMART
        self.status = None
        self.df_bars = {} # dataframe
        self.df_news = {} # dataframe