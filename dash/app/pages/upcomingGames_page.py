import dash
from dash import html, dcc

from data.nba_teams import get_all_team_options

dash.register_page(__name__, path='/upcominggames')


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
], style={'display': 'flex', 'justifyContent': 'center'})


# Separate layout for the dropdowns
dropdown_layout = html.Div([
    create_dropdown('left-dropdown', get_all_team_options()),
    html.Br(),
    create_dropdown('right-dropdown', get_all_team_options()),
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
    'width': '30%',
    'height': '500px',
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    'overflow': 'auto'  # Allow overflow to scroll if content exceeds height
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
    html.Div([
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Secondary card title", className="card-title"),
                html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text")
            ], className="card-body", style={'height': '250px'})  # Adjust height of the card body
        ], className="card text-white bg-secondary mb-3", style={'maxWidth': '60rem', 'margin': 'auto'})
    ], style={'marginTop': '10px'}),


    html.Div(dropdown_layout, style={'marginTop': '80px'}),
   
    html.Div(dropdown_layout_middle, style={'marginTop': '5%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
    
    html.Div([
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Primary card title", className="card-title"),
                html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text")
            ], className="card-body")
        ], className="card border-primary mb-3", style={'maxWidth': '20rem', 'margin': 'auto'})
    ], style={'marginTop': '20px'}),

    html.Div([
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Another card title", className="card-title"),
                html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text")
            ], className="card-body", style={'height': '500px'})
        ], className="card border-primary mb-3", style={'maxWidth': '30rem', 'margin': 'auto'})
    ], style={'marginTop': '10px', 'marginLeft': '20px', 'float': 'left'}),

    html.Div([
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Additional Card Title", className="card-title"),
                html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text")
            ], className="card-body", style={'height': '500px'})
        ], className="card border-primary mb-3", style={'maxWidth': '30rem', 'margin': 'auto'})
    ], style={'marginTop': '10px', 'marginRight': '20px', 'float': 'right'})

])
