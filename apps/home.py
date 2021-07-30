import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to the Supermarket sales dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Hi! My name is Yudha and this is my milestone project'),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children='It consists of three main pages: Explore Data, which gives an overview of the historical sales from 3 different Supermarket, '
                'Hypothesis Testing and '
                'here at dashboard where you can get the original dataset and visit my Github page'),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the original dataset here',
                        className="text-center"),
                        dbc.Button("Supermarket sales Dataset",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales?select=supermarket_sales+-+Sheet1.csv",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit my Github Page',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/ycmy28",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])