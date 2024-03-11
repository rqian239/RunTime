import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

from data.nba_teams import get_all_team_options

dash.register_page(__name__, path='/teams')

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Teams", className="home-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                            Welcome to the Teams Page! Delve into the heart of NBA teams with ease! Discover fascinating insights into 
                            team history, player profiles, coaching staff, and in-depth statistics. Use the search tab to swiftly locate
                            your favorite team and uncover a treasure trove of information. Whether you're a dedicated fan seeking 
                            detailed analysis or a casual observer looking to learn more, this page is your ultimate destination for all 
                            things NBA teams.""",
                            style={'textAlign': 'center'}
                        ),
                    ],
                ),
            ]
        ),
    ]
)

# Assign the layout to the specific path
layout = body

# Create a Dash app instance
app = dash.Dash(__name__)

# Run the Dash server
if __name__ == '__main__':
    app.run_server(debug=True)
