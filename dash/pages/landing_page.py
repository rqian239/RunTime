import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('This is the Landing Page', style={'textAlign': 'center'})
])