import dash
from dash import html, dcc

from data.nba_teams import get_all_team_options
import ids

dash.register_page(__name__, path='/upcominggames')


def get_model_options():
    return [
        {'label': 'Wins/Losses', 'value': 'wins_losses'},
        {'label': 'Scores', 'value': 'scores'},
        {'label': 'Player Statistics', 'value': 'player_stats'},
        {'label': 'Team Statistics', 'value': 'team_stats'}
    ]

def create_dropdown(_id, options):
    return dcc.Dropdown(
        id=_id,
        options=options,
        value=options[0]['value'],  # Set a default value
        style={'width': '400px'}
    )

dropdown_layout_middle = html.Div([
    create_dropdown(ids.UPCOMING_GAMES_DROPDOWN_MIDDLE, get_model_options()),
], style={'display': 'flex', 'justifyContent': 'center'})


# Separate layout for the dropdowns
dropdown_layout = html.Div([
    create_dropdown(ids.UPCOMING_GAMES_DROPDOWN_LEFT, get_all_team_options()),
    html.Br(),
    create_dropdown(ids.UPCOMING_GAMES_DROPDOWN_RIGHT, get_all_team_options()),
], style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '2%', 'marginTop': '-5%'})

# Style boxes
nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'          # White
}


# Define styles for the box
box_style = {
    'border': '2px solid black',
    'padding': '1%',
    'width': '28.5%',
    'height': '500px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text']

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
    'height': '30%',
    'width': '27%'
}

# Main layout using CSS grid layout
layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('Upcoming Games', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style ),
    html.Div(dropdown_layout, style={'marginTop': '80px'}),
   
    html.Div(dropdown_layout_middle, style={'marginTop': '5%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
    html.Div("This is the middle box", style={**middle_box_style, 'marginTop': '20px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
    html.Div([
            html.Div("This is inside the left box", style={**box_style, 'marginTop': '-30%'}),
            html.Div("This is inside the right box", style={**box_style, 'marginTop': '-30%'}),
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '2%'}),

   

])