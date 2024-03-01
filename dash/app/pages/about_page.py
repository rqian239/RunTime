import dash
from dash import html

dash.register_page(__name__, path='/about')

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('This is the About Page', style={'textAlign': 'center'})
])