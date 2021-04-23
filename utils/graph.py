import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
import plotly.graph_objects as go
import utils.testdata as td
import plotly.offline as pyo
from plotly.subplots import make_subplots
import pandas as pd


def add_cdl_graph(fig,df,row=1,col=1):
    fig.append_trace(go.Candlestick(x=df.index,open=df.open,close=df.close,low=df.low,high=df.high),row=row,col=col)
    fig.update(layout_xaxis_rangeslider_visible=False)
    return fig

def add_rsi_graph(fig,df,column="rsi",color="orange",row=1,col=1):
    fig.append_trace(go.Scatter(x=df.index,y=df[column],name=column,mode="lines",line=dict(color=color)),row=row,col=col)
    return fig

def add_sma_graph(fig,df,column="sma",color="blue",row=1,col=1):
    fig.append_trace(go.Scatter(x=df.index,y=df[column],name=column,mode="lines",line=dict(color=color)),row=row,col=col)
    fig.update(layout_xaxis_rangeslider_visible=False)
    return fig    


def generate_chart():
    fig=make_subplots(rows=2,cols=1,row_heights=[0.7,0.3])
    df=td.get_stock_df("tsla","1day","2020-1-1","2021-1-1")
    df["sma20"]=td.get_sma_col(df,20)
    df["rsi10"]=td.get_rsi_col(df,10)
    add_cdl_graph(fig,df,row=1,col=1)
    add_rsi_graph(fig,df,column="rsi10",row=2,col=1)
    add_sma_graph(fig,df,column="sma20",color="green",row=1,col=1)
    return fig






