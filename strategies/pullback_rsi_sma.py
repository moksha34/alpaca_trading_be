import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import utils.testdata as td
import numpy as np

def generate_backtest_signals(stk,start,end):
    ''' this is a pull back strategy picked from youtube by rayner teo
    ref: https://youtu.be/W8ENIXvcGlQ
 
    strategy pre-req:  current closeprices must be over 200 moving avg -- long-term uptrend

    entry: 10-period rsi below 30 (buy next day open)

    exit: 10-period rsi aboe 40 or after 10 days (sell next day's open )
               
    '''
    df=td.get_stock_df(stk,"1day",start,end)
    df["rsi10"]=td.get_rsi_col(df,10)
    df["sma200"]=td.get_sma_col(df,200)
    signals=[]
    bought=0
    sold=0
    bought_date=None
    dfcopy=df.reset_index()
    for rec in dfcopy.to_dict("records"):
        if not bought:
            if rec["rsi10"]<30 and rec["close"] >rec["sma200"]:
                bought=1
                signal=1
                bought_date=rec["datetime"]
            else:
                signal=0
        elif bought and bought_date:
            if rec["rsi10"]>40 or (rec["datetime"]-bought_date).days >10:
                bought=0
                signal=-1
                bought_date=None
        else:
            signal=0
        signals.append(signal)
    df["signals"]=np.array(signals)
    return df[df["signals"] != 0]


    
    
   
    
print(generate_backtest_signals("spx","2019-1-1","2021-1-1"))    