import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
##########
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from utils.graph import generate_chart
from utils.tickers import get_tickers
from strategies.helpers import get_strategies
from datetime import date
from dash.dependencies import Input,Output,State


## INITIATE THE APP
app=Dash(__name__,external_stylesheets=[dbc.themes.SKETCHY])

app.layout= html.Div(children=[dbc.Jumbotron("SexyBack tester",className="display-3",style={"background": "#34495E"}),
dbc.Container(
      id="app_container",fluid=True,children=[
          dbc.Row(style={"background": "#E1BF2A" },
              children=[
                  dbc.Col( style={"margin": "5px"},md=4,lg=4,sm=4,xl=2,xs=12,children=[   

                      dcc.Dropdown(id="stock_dropdown",placeholder="select a stock",
                      options=get_tickers(),multi=True)

                         ]),## COL FOR STOCK_PICKER
                   ##########################
                   dbc.Col(md=4,lg=4,sm=4,xl=2,xs=12,children=[ 
                         dcc.DatePickerRange(id="date_range",start_date_placeholder_text="Start Period",
                         end_date_placeholder_text="End Period",
                         calendar_orientation='vertical',
                         start_date=date(2017,1,1)
                        ) ]),### COL FOR DATE_PICKER
                     dbc.Col( style={"margin": "5px"},md=4,lg=4,sm=4,xl=2,xs=12,children=[   

                      dcc.Dropdown(id="test_name",placeholder="select a strategy",
                      options=get_strategies(),multi=False)

                         ]),#COL FOR STRATEGY PICKER 
                     dbc.Col( style={"margin": "5px"},md=4,lg=4,sm=4,xl=2,xs=12,children=[   

                      dbc.Button("Submit",id="submit",color="dark")

                         ]),


                ]),
                dbc.Row(id="charts_area",style={"background": "#29439B" },
              children=[ ])           
                
                
                
                 ## row

             ]) ### Container 

    # dcc.Graph(id="test",figure=generate_chart())


])

@app.callback(
    Output("charts_area","children"),
    Input("submit","n_clicks"),
    State("stock_dropdown","value"),
    State("date_range","start_date"),
    State("date_range","end_date")
    
)
def draw_charts(submit_num,stks,start_date,end_date):

    print(submit_num,stks,start_date,end_date)
    all_children=[]
    for _ in range(len(stks)):
        grph=dbc.Col(md=12,lg=12,sm=12,xl=12,xs=12,children=[
        dcc.Graph(figure=generate_chart())
        ])
        all_children.append(grph)
    
    return all_children




if __name__=="__main__":
    app.run_server(debug=True)
    

