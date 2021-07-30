import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import dash
import plotly.express as px

#from statsmodels.stats.anova import anova_lm
import scipy.stats as stats
import researchpy as rp
from app import app
from datetime import datetime

# Data Preprocessing
df = pd.read_csv('supermarket_sales - Sheet1.csv')
df_ttest = df.groupby(['Branch','Date']).sum().reset_index()[['Branch', 'Date','gross income']].sort_values('Date').reset_index(drop=True)
df_ttest['Date_New'] = [datetime.strptime(i,'%m/%d/%Y') for i in df_ttest.Date]
df_ttest['Day'] = [i.date().day for i in df_ttest.Date_New]
df_ttest.head()
Date_period = []

for i in df_ttest.Day:
    if i < 16:
        Date_period.append("First Half of Month")
    else:
        Date_period.append("Second Half of Month")
    
df_ttest['Date_period'] = Date_period
summary, results = rp.ttest(group1= df_ttest['gross income'][df_ttest['Date_period'] == 'First Half of Month'], group1_name= "First Half of Month",
                            group2= df_ttest['gross income'][df_ttest['Date_period'] == 'Second Half of Month'], group2_name= "Second Half of Month")
stats.ttest_ind(df_ttest['gross income'][df_ttest['Date_period'] == 'First Half of Month'],
                df_ttest['gross income'][df_ttest['Date_period'] == 'Second Half of Month'])

#yangon = df.loc[df['City'] == 'Yangon']
#from statsmodels.tsa.stattools import adfuller
#test_result = adfuller(yangon['Total'])
#test_result

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Hypothesis Testing",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H3('Objective'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('Dataset yang digunakan adalah data total penjualan dari tiap supermarket dan melakukan uji hipotesis terhadap dataset tersebut'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H3("Method"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('Metode yang akan digunakan dalam analisa ini adalah The Dickey Fuller Test'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('hal yang diuji yaitu adalah stationarity tes dari dataset penjualan di kota yangon'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('-H0 = kemungkinan dataset tidak statsioner'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('-H1 = dataset statsioner'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H3("Confidence interval & critical value"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('analisa ini menggunakan confidence interval = 95%, dengan critical value=5%'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H3("Hypothesis testing"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('dari hasil testing, kita mendapat nilai p-value sebesar 2.03e-30'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('-H0 diterima jika uji statistik berada diluar critical value'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('-H1 diterima dan H0 ditolak jika uji statistik berada didalam critical value'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('-dari hasil p-value yang lebih kecil dari critcial value maka H0 ditolak dan dataset total penjualan di kota Yangon stasioner'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H6('Case2: membandingkan first half of month dan second half of month dari sisi gross income.'),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(id="slct_branch",
                 options=[
                     {"label": "A", "value": "A"},
                     {"label": "B", "value": "B"},
                     {"label": "C", "value": "C"},],
                 multi=False,
                 value="A",
                 style={'width': "40%"}
                 ),
                className="mb-4, custom-dropdown"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(id='output_container', children=[]),
                className="mb-4, mt-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H1("", style={'text-align': 'center'}),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='my_bee_map4', figure={})
            )
        ])
    ])
 
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map4', component_property='figure'),
    ],
    [Input(component_id='slct_branch', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The branch chosen by user was: {}".format(option_slctd)

    df4 = df_ttest.groupby(['Date_period','Branch']).sum().reset_index()
    df4 = df4[df4["Branch"] == option_slctd]

    # Plotly Express
    fig4 = px.bar(df4, x="Date_period", y="gross income", color = "Date_period", barmode="group", title = "Gross Income per Period of Month: There are no significant difference between First Half of Month and Second Half of Month with T-test p-value is 0.29241")

    
    return container, fig4

