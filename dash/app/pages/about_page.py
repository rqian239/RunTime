import dash
from dash import html

dash.register_page(__name__, path='/about')

about_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': 'calc(100% - 40px)', 
    'height': '300px',
    'background-color': 'darkred',
    'color': 'black',  
    'marginLeft': '20px', 
    'marginRight': '20px', 
    'marginTop': '40px',
    'gridColumn': '1 / -1'  
}

nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'         # White
}

box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'height': '200px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    #'marginLeft': '175px'

}

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('This is the About Page', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style ),
    html.Div("This is inside the left box", style={**box_style, 'marginTop': '10px', 'width': '900px', 'grid-column': '1', 'marginLeft': '50px'})
])