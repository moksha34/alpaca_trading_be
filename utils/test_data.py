import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
from twelvedata import TDClient
# Initialize client - apikey parameter is requiered
td = TDClient(apikey=os.environ.get("twelve-data-api"))



def get_stock_pd(stk,interval="1day",output=500,timezone="America/New_York"):
    ts = td.time_series(
    symbol=stk,
    interval=interval,
    outputsize=output,
    timezone=timezone,
    )
    pd=ts.as_pandas()
    return pd


def get_stock_ts(stk,interval="1day",output=500,timezone="America/New_York"):
    ts = td.time_series(
    symbol=stk,
    interval=interval,
    outputsize=output,
    timezone=timezone,
    )
    return ts
pd=get_stock_ts("AAPL")    
pd.as_plotly_figure().show()