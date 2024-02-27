import dash
from dash import html

dash.register_page(__name__, path='/teams')

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('This is the Teams Page', style={'textAlign': 'center'})
])