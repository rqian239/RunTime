import dash
from dash import html, dcc

from data.nba_teams import get_all_team_options

dash.register_page(__name__, path='/teams')

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

# Define styles for the box
nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'         # White
}

box_style = {
    'border': '2px solid black',
    'padding': '20px',
    'height': '500px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    #'marginLeft': '175px'

}

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('Teams Page', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style ),
    dcc.Dropdown(
        id='team-dropdown',
        options=get_all_team_options(),
        value='option1',  # Default value
        style={'width': '50%', 'margin': '30px', 'marginTop': '20px', 'textAlign': 'left'}
    ),
    html.Div("This is inside the left box", style={**box_style, 'marginTop': '10px', 'width': '900px', 'grid-column': '1', 'marginLeft': '50px'}),
    html.Div("This is inside the image box", style={**box_style, 'marginTop': '-500px', 'grid-column': '1', 'width': '450px', 'marginLeft': '975px'}),
])
