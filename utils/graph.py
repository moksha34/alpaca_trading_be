import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
import plotly.graph_objects as go
import utils.test_data as td
import plotly.offline as pyo


fig=go.Figure()
test_data=td.get_stock_pd("tsla",output=100)
fig.add_trace(go.Candlestick(open=test_data.open,close=test_data.close,low=test_data.low,high=test_data.high))
pyo.plot(fig)


