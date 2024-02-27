import dash
from dash import html, dcc

dash.register_page(__name__, path='/upcominggames')

def get_game_options():
    return [
        {'label': 'Team 1', 'value': 'game1'},
        {'label': 'Team 2', 'value': 'game2'},
        {'label': 'Team 3', 'value': 'game3'}
    ]

def create_dropdown(id, options, position):
    return dcc.Dropdown(
        id=id,
        options=options,
        value=options[0]['value'],  # Set a default value
        style={'width': '400px', 'marginRight': '20px', 'float': position}
    )

# Separate layout for the dropdowns
dropdown_layout_left = html.Div([
    create_dropdown('left-dropdown', get_game_options(), "left"),
])

dropdown_layout_right = html.Div([
    create_dropdown('right-dropdown', get_game_options(), "right"),
])

# Style boxes
nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'          # White
}

# Define styles for the box
box_style_left = {
    'border': '2px solid black',
    'padding': '20px',
    'marginTop': '200px',
    'marginLeft': '100px',
    'width': '400px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text']
}

box_style_right = {
    'border': '2px solid black',
    'padding': '20px',
    'marginTop': '200px',
    'marginRight': '80px',
    'width': '400px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text']
}


# Main layout combining the dropdown layout with other elements
layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('Upcoming Games', style={'textAlign': 'center'}),
    html.Div(dropdown_layout_left, style={'marginTop': '150px', 'marginLeft': '100px'}),
    html.Div(dropdown_layout_right, style={'marginTop': '150px', 'marginRight': '80px'}),

    html.Div("This is inside the left box", style=box_style_left),
    html.Div("This is inside the right box", style=box_style_right)
    

])