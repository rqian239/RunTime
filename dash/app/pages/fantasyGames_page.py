import dash
from dash import html, dcc

from data.nba_teams import get_all_team_options

dash.register_page(__name__, path='/fantasygames')


def get_model_options():
    return [
        {'label': 'Wins/Losses', 'value': 'wins_losses'},
        {'label': 'Scores', 'value': 'scores'},
        {'label': 'Player Statistics', 'value': 'player_stats'},
        {'label': 'Team Statistics', 'value': 'team_stats'}
    ]

def create_dropdown(id, options):
    return dcc.Dropdown(
        id=id,
        options=options,
        value=options[0]['value'],  # Set a default value
        style={'width': '400px'}
    )

dropdown_layout_middle = html.Div([
    create_dropdown('middle-dropdown', get_model_options()),
])

# Separate layout for the dropdowns
dropdown_layout = html.Div([
    create_dropdown('left-dropdown', get_all_team_options()),
    html.Br(),
    create_dropdown('right-dropdown', get_all_team_options()),
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
    'height': '500px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    #'marginLeft': '175px'

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
    'marginTop': '40px'
}

middle_box_style = {
    **box_style,
    'height': '300px', 
    'marginLeft': '1000px', 
}

# Main layout using CSS grid layout
layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('Fantasy Games', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style ),
    html.Div(dropdown_layout, style={'marginTop': '80px'}),
   
    html.Div(dropdown_layout_middle, style={'marginTop': '60px', 'marginLeft': '537px', 'textAlign': 'center'}),
    html.Div("This is the middle box", style={**middle_box_style, 'marginTop': '20px', 'marginLeft': 'auto', 'marginRight': 'auto'}),

    html.Div("This is inside the left box", style={**box_style, 'marginTop': '-450px', 'grid-column': '1', 'marginLeft': '58px'}),
    html.Div("This is inside the right box", style={**box_style, 'marginTop': '-500px', 'grid-column': '2', 'marginLeft': '1010px'}),

   

])