import dash
from dash import html

dash.register_page(__name__, path='/')

about_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': 'calc(100% - 40px)', 
    'height': '100px',
    'background-color': 'darkred',
    'color': 'black',  
    'marginLeft': '20px', 
    'marginRight': '20px', 
    'marginTop': '40px',
    'gridColumn': '1 / -1'  
}


layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('This is the Landing Page', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style )
])