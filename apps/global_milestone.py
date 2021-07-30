import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from pandas.io.formats.format import DataFrameFormatter
from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
# Data Preprocessing
df = pd.read_csv('supermarket_sales - Sheet1.csv')
df.head()
df_ttest = df.groupby(['Branch','Date']).sum().reset_index()[['Branch', 'Date','gross income']].sort_values('Date').reset_index(drop=True)
df_ttest['Date_New'] = [datetime.strptime(i,'%m/%d/%Y') for i in df_ttest.Date]
df_ttest['Day'] = [i.date().day for i in df_ttest.Date_New]

layout = html.Div([

    html.H1("Supermarket Branch Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_branch",
                 options=[
                     {"label": "A", "value": "A"},
                     {"label": "B", "value": "B"},
                     {"label": "C", "value": "C"},],
                 multi=False,
                 value="A",
                 style={'width': "40%"}
                 ),

    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}),

    html.Div([

    html.H1("", style={'text-align': 'center'}),

    dcc.Graph(id='my_bee_map2', figure={}),  
    
    html.Div([

    html.H1("", style={'text-align': 'center'}),

    dcc.Graph(id='my_bee_map3', figure={}),

    html.Div([

    html.H1("", style={'text-align': 'center'}),

    dcc.Graph(id='my_bee_map5', figure={}),

    html.Div([
    html.Img(src=app.get_asset_url('wordcloud.png'),style={ 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    
])        
        
])
    
])

])

]) 

# ------------------------------------------------------------------------------

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output('my_bee_map', 'figure'),
     Output('my_bee_map2', 'figure'),
     Output('my_bee_map3', 'figure'),
     Output('my_bee_map5', 'figure')
    ],
    [Input('slct_branch', 'value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The branch chosen by user was: {}".format(option_slctd)

    df1 = df.groupby(['Date','Branch']).sum().reset_index(drop=False)
    df1['year_month'] = [i[-4:]+i[:1] for i in df1.Date]
    df1 = df1[df1["Branch"] == option_slctd]
    
    df2 = df.groupby(['Gender','Branch']).sum().reset_index()
    df2 = df2[df2["Branch"] == option_slctd]
    
    df3 = df.groupby(['Product line','Branch']).sum().reset_index()
    df3 = df3[df3["Branch"] == option_slctd]

    df5 = df.groupby(['Date','Branch']).mean().reset_index(drop=False)
    df5 = df5[df5["Branch"] == option_slctd]

    # Plotly Express
    fig = px.line(df1, x="Date", y="gross income",title="Gross Income Trend")
    fig2 = px.bar(df2, x="Gender", y="gross income", color = "Gender", barmode="group",title = "Gross Income per Gender")
    fig3 = px.bar(df3, x="Product line", y="gross income", barmode="group", title = "Gross Income per Product Line")
    fig5 = px.line(df5, x="Date", y="Rating",title="Average Rating Trend")
    
    return fig, fig2, fig3, fig5