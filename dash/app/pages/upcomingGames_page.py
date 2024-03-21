import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options

import ids


dash.register_page(__name__, path='/upcominggames')  # Change the path here

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Upcoming Games", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                            Step into the future of NBA analysis with our groundbreaking predictive game statistics model. 
                            Harnessing the power of cutting-edge algorithms, we delve deep into team matchups to forecast 
                            outcomes with unprecedented accuracy. From player performance projections to strategic insights, 
                            our innovative approach revolutionizes how we understand the game. Join us as we redefine the 
                            landscape of sports analytics, unlocking the potential of tomorrow's NBA matchups today. .""",
                            style={'textAlign': 'center'}
                        ),
                    ],
                    width=12  # Full width for this column
                )
            ]
        ),
        dbc.Row(
            [
                # Adding the first card with dropdown
                dbc.Col(
                    [
            
                        dcc.Dropdown(
                        id=ids.UPCOMING_DROPDOWN_MENU_1,
                        options=get_all_team_options(),  # Options generated from the function
                        placeholder="Select a Team",  # Placeholder text for the dropdown
                        style={'width': '100%'}  # Set the width of the dropdown
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Card 1"),
                                dbc.CardBody(
                                    [
                                        html.H4("Card title", className="card-title"),
                                        html.P(
                                            "This is some text inside the card body. You can add any content you want here.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        ),
                    ],
                    width=4  # 33% width for this column
                ),
                # Adding the second card with dropdown
                dbc.Col(
                    [
                        dbc.DropdownMenu(
                            label="Select Team",
                            id=ids.UPCOMING_DROPDOWN_MENU_2,
                            style={'overflowY': 'auto', 'marginBottom': '10px'}  # Add marginBottom to add space between dropdown and card
                        ),
                         dbc.Card(
                            [
                                dbc.CardHeader("Card 2"),
                                dbc.CardBody(
                                    [
                                        html.H4("Card title", className="card-title"),
                                        html.P(
                                            "This is some text inside the card body. You can add any content you want here.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        ),
                    ],
                    width=4  # 33% width for this column
                ),
                # Adding the third card with dropdown
                dbc.Col(
                    [
                         dcc.Dropdown(
                        id=ids.UPCOMING_DROPDOWN_MENU_3,
                        options=get_all_team_options(),  # Options generated from the function
                        placeholder="Select a Team",  # Placeholder text for the dropdown
                        style={'width': '100%'}  # Set the width of the dropdown
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Card 3"),
                                dbc.CardBody(
                                    [
                                        html.H4("Card title", className="card-title"),
                                        html.P(
                                            "This is some text inside the card body. You can add any content you want here.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        ),
                    ],
                    width=4  # 33% width for this column
                )
            ]
        )
    ]
)

# Assign the layout to the specific path
layout = body

# Create a Dash app instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Run the Dash server
if __name__ == '__main__':
    app.run_server(debug=True)
