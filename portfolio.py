import datetime
from random import random
import time

##STEP1.  CREATE A  PORTFOLIO


class Portfolio(object):


    def __init__(self,starting_balance,account_start_date,watchlist=[]):
        self.initial_account=starting_balance
        self.cash=starting_balance
        self.start_date=account_start_date
        self.watchlist=watchlist
        self.holdings=[]
        ## holdings will list of  dicts symbol: stk,qty: qty,current_price: 
        
    
    @property
    def distribution(self):
        dist={}
        stk_total=0            
        for stk in self.holdings:
            stk_portion=stk.get("qty")*stk.get("curr_price")
            stk_dist=100*(stk_portion/self.current_balance)
            stk_total += stk_portion
            dist[stk.get("symbol")]=stk_dist
        cash_dist=100*(self.cash/self.current_balance)
        dist["cash"]=cash_dist
        return dist


    @property
    def current_balance(self):
        stk_total=0            
        for stk in self.holdings:
            stk_portion=stk.get("qty")*stk.get("curr_price")
            stk_total += stk_portion
        return self.cash+stk_total    



    def update_account(self,stks):
        ''' stks here is list of stk with symbol and current_price '''
        for position in self.holdings:
            if stks.get(position.get("symbol")):
                position["curr_price"]=stks[position.get("symbol")].get("curr_price")
        return True       
         
    
    def add_position(self,stk,qty):
        '''stk here is a dict with symbol and curr_price  
        if the stock doesnt exist in holdings we add to the holdings, if exists,we edit'''
        stkamount=stk["curr_price"]*qty
        if self.cash < stkamount:
            raise ValueError("insufficient_balance")
        else:
            self.cash=self.cash-stkamount
            existing_position=0
            for position in self.holdings:
                if position.get("symbol")==stk.get("symbol"):                    
                    position["price_paid"]=((position.get("qty")*position.get("price_paid"))+stkamount)/((position.get("qty"))+qty)
                    position["qty"] +=qty
                    existing_position=1
            if not existing_position:
                position_dict={"symbol": stk.get("symbol"),"qty": qty,"price_paid": stk.get("curr_price"),"curr_price": stk.get("curr_price")  } 
                self.holdings.append(position_dict)    
        return True

    def sell_position(self,stk,qty):
        '''stk here is a dict with symbol and curr_price to sell'''
        stkamount=stk["curr_price"]*qty
        exisitng_position=0
        for position in self.holdings:
            if position.get("symbol")==stk.get("symbol"):
                if position["qty"] < qty:
                    raise ValueError("not enough shares, check the portfolio")
                else:
                    position["qty"] = position["qty"]-qty
                    if position["qty"]==0:
                        self.holdings.remove(position)
                    self.cash +=stkamount    
                existing_position=1
        if not existing_position:
            raise ValueError("unknown security/stock")
        return True 








# stks={"AAPL": {"symbol": "AAPL","curr_price": random()*150+1},"TSLA": {"symbol": "TSLA","curr_price": random()*750+1 }}
# my_pr=Portfolio(10000,"2021-1-1")
# my_pr.add_position(stks["AAPL"],5)    
# my_pr.add_position(stks["TSLA"],5)
# for i in range(100):
#     stks={"AAPL": {"symbol": "AAPL","curr_price": random()*150+1},"TSLA": {"symbol": "TSLA","curr_price": random()*750+1 }}
#     my_pr.update_account(stks)
#     print(my_pr.holdings)
#     print(my_pr.current_balance)
#     time.sleep(1)


      
