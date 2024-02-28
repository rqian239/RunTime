import dash
from dash import html, dcc

dash.register_page(__name__, path='/upcominggames')

def get_game_options():
    return [
        {'label': 'Team 1', 'value': 'game1'},
        {'label': 'Team 2', 'value': 'game2'},
        {'label': 'Team 3', 'value': 'game3'}
    ]

def create_dropdown(id, options):
    return dcc.Dropdown(
        id=id,
        options=options,
        value=options[0]['value'],  # Set a default value
        style={'width': '400px'}
    )

# Separate layout for the dropdowns
dropdown_layout = html.Div([
    create_dropdown('left-dropdown', get_game_options()),
    html.Br(),
    create_dropdown('right-dropdown', get_game_options()),
], style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '60px', 'marginTop': '-125px'})

# Style boxes
nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'          # White
}


# Define styles for the box
box_style = {
    'border': '2px solid black',
    'padding': '20px',
    'width': '400px',
    'height': '400px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    'marginLeft': '175px'

}

about_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': 'calc(100% - 40px)', 
    'height': '100px',
    'background-color': 'darkred',
    'color': 'black',  
    'marginLeft': '20px', 
    'marginRight': '20px', 
    'marginTop': '-100px',
    'gridColumn': '1 / -1'  
}


# Main layout using CSS grid layout
layout = html.Div(style={'height': '100vh', 'display': 'grid', 'grid-template-columns': '1fr 1fr'}, children=[
    html.H1('Upcoming Games', style={'textAlign': 'center', 'grid-column': '1 / -1'}),
    html.Div("This is a separate box", style=about_box_style ),
    html.Div(dropdown_layout, style={'marginTop': '-10px', 'grid-column': '1 / -1'}),

    #html.Div("This is another box for options", style=options_box_style),

    html.Div("This is inside the left box", style={**box_style, 'marginTop': '-150px', 'grid-column': '1', 'marginLeft': '58px'}),
    html.Div("This is inside the right box", style={**box_style, 'marginTop': '-150px', 'grid-column': '2', 'marginLeft': '275px'})

    

])
