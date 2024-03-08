import dash
from dash import html, dcc

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

# Options for the dropdown
dropdown_options = [
        {'label': 'Atlanta Hawks', 'value': 'team1'},
        {'label': 'Boston Celtics', 'value': 'team2'},
        {'label': 'Brooklyn Nets', 'value': 'team3'},
        {'label': 'Charlotte Hornets', 'value': 'team4'},
        {'label': 'Chicago Bulls', 'value': 'team5'},
        {'label': 'Cleveland Cavaliers', 'value': 'team6'},
        {'label': 'Dallas Mavericks', 'value': 'team7'},
        {'label': 'Denver Nuggets', 'value': 'team8'},
        {'label': 'Detroit Pistons', 'value': 'team9'},
        {'label': 'Golden State Warriors', 'value': 'team10'},
        {'label': 'Houston Rockets', 'value': 'team11'},
        {'label': 'Indiana Pacers', 'value': 'team12'},
        {'label': 'Los Angeles Clippers', 'value': 'team13'},
        {'label': 'Los Angeles Lakers', 'value': 'team14'},
        {'label': 'Memphis Grizzlies', 'value': 'team15'},
        {'label': 'Miami Heat', 'value': 'team16'},
        {'label': 'Milwaukee Bucks', 'value': 'team17'},
        {'label': 'Minnesota Timberwolves', 'value': 'team18'},
        {'label': 'New Orleans Pelicans', 'value': 'team19'},
        {'label': 'New York Knicks', 'value': 'team20'},
        {'label': 'Oklahoma City Thunder', 'value': 'team21'},
        {'label': 'Orlando Magic', 'value': 'team22'},
        {'label': 'Philadelphia 76ers', 'value': 'team23'},
        {'label': 'Phoenix Suns', 'value': 'team24'},
        {'label': 'Portland Trail Blazers', 'value': 'team25'},
        {'label': 'Sacramento Kings', 'value': 'team26'},
        {'label': 'San Antonio Spurs', 'value': 'team27'},
        {'label': 'Toronto Raptors', 'value': 'team28'},
        {'label': 'Utah Jazz', 'value': 'team29'},
        {'label': 'Washington Wizards', 'value': 'team30'}
    ]

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
        options=dropdown_options,
        value='option1',  # Default value
        style={'width': '50%', 'margin': '30px', 'marginTop': '20px', 'textAlign': 'left'}
    ),
    html.Div("This is inside the left box", style={**box_style, 'marginTop': '10px', 'width': '900px', 'grid-column': '1', 'marginLeft': '50px'}),
    html.Div("This is inside the image box", style={**box_style, 'marginTop': '-500px', 'grid-column': '1', 'width': '450px', 'marginLeft': '975px'}),
])
