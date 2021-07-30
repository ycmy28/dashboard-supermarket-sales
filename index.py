import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
from app import app
from app import server
 
from apps import hypothesis,home,global_milestone
 
app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Explore Data", href='/apps/global_milestone')),
            dbc.NavItem(dbc.NavLink("Hypothesis Testing", href='/apps/hypothesis'))
        ],
        brand="Dashboard",
        brand_href="/apps/home",
        color="dark",
        dark=True,
        sticky='top'
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])
 
 
@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    if pathname == '/apps/global_milestone':
        return global_milestone.layout
    elif pathname == '/apps/hypothesis':
        return hypothesis.layout
    else:
        return home.layout
 
 
if __name__ == '__main__':
    app.run_server(debug=True)
