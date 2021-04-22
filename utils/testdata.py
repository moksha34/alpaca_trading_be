import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
from twelvedata import TDClient
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=os.environ.get("twelve-data-api"))



def get_stock_ts(stk,interval="1day",output=100,timezone="America/New_York"):
    ts = td.time_series(
    symbol=stk,
    interval=interval,
    outputsize=output,
    timezone=timezone,
    )
    pd=ts.as_pandas()
    return ts



def get_stock_with_vwap(ts):
    df=ts.with_vwap().as_pandas()
    return df["vwap"]


def add_rsi(ts,time_period=10):
    df=ts.with_rsi(time_period=time_period).as_pandas()
    df.rename(columns={"rsi": f"rsi{time_period}"},inplace=True)
    return df[f"rsi{time_period}"]



def get_stock_with_triple_sma(ts,short_period=20,medium_period=100,long_period=200):
    df=ts.with_sma(time_period=short_period).with_sma(time_period=medium_period).with_sma(time_period=long_period).as_pandas()
    df.rename(columns={"sma1": f"sma{short_period}","sma2": f"sma{medium_period}","sma3": f"sma{long_period}"},inplace=True)
    print(df.head())
    return df[[f"sma{short_period}",f"sma{medium_period}",f"sma{long_period}"]]
    
    
