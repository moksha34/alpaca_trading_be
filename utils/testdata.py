import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
from twelvedata import TDClient
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=os.environ.get("twelve-data-api"))
from talib import abstract
import yfinance as yf
import pandas as pd
import numpy as np



##  get stock data as dataframe ######

def get_stock_df(stk,interval,start,end):
    df=None
    try:
        ts = td.time_series(symbol=stk,
        interval=interval,
        start_date=start,
        end_date=end,
        outputsize=1000,
        order="ASC"
        )
        df=ts.as_pandas()
        
       
        
    except Exception as e:
        df=yf.download(tickers=stk,interval=interval[:2],start=start,end=end)
        df.index.rename("datetime",inplace=True)
        df.rename(columns={"Open": "open","Close": "close","Low": "low","High": "high","volume": "volume"},inplace=True)
       
      
    return df    

        
def get_sma_col(df,lookback_period):
    sma=abstract.Function("sma")
    return sma(df,timeperiod=lookback_period)

def get_rsi_col(df,lookback_period):
    rsi=abstract.Function("RSI")
    return rsi(df,timeperiod=lookback_period)

def get_macd_cols(df,fastperiod=12, slowperiod=26, signalperiod=9):
    macd=abstract.Function("MACD")
    return macd(df,fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)



# df=get_stock_df("AAPL",'1day',"2020-1-1","2020-3-1")

# df[["macd","macd_signal","macdhist"]]=get_macd_cols(df)
    
# print(df.tail())    

