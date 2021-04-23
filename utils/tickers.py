import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
import requests
import utils.dbclasses as dbclasses


def get_tickers_online(currency=None,exchange=None,type="EQUITY"):
    params={"format": "json","type": type}
    if currency and exchange:
        params.update({"currency": currency,"exchange": exchange})
    res=requests.get(os.environ["get_stock_url"],params=params,verify=False)
    
    return res.json()


def update_db_tickers(currency=None,exchange=None):
    ticker_input=get_tickers_online(currency=currency,exchange=exchange)
    ticker_list=ticker_input.get("data")
    session=dbclasses.get_session()
    for ticker in ticker_list:
        
        stock=dbclasses.Tickers()
        if ticker.get("symbol"):
            stock.symbol=ticker.get("symbol")
            stock.name=ticker.get("name")
            stock.currency=ticker.get("currency")
            stock.exchange=ticker.get("exchange")
            stock.country=ticker.get("country")
            stock.type=ticker.get("type")
            session.merge(stock)
    session.commit()        

def get_tickers():
    session=dbclasses.get_session()
    query_output=session.query(dbclasses.Tickers).all()
    ticker_dict_list=[{"label": f"{stk.symbol} - {stk.name}","value": stk.symbol} for stk in query_output]
    session.commit()
    return ticker_dict_list

     



if __name__=="__main__":
    print(get_tickers())

    


