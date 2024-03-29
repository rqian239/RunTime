import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options

import ids


dash.register_page(__name__, path='/fantasygames')  # Change the path here

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Fantasy Games", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                            Welcome to the Fantasy Games Page! Dive into the world of fantasy sports and games with ease! 
                            Discover exciting adventures, challenge your friends, and compete for glory in virtual arenas.
                            Whether you're a seasoned player seeking new challenges or a beginner looking to start your journey,
                            this page is your ultimate destination for all things fantasy games.""",
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
                        id=ids.FANTASY_DROPDOWN_MENU_1,
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
                            id=ids.FANTASY_DROPDOWN_MENU_2,
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
                        id=ids.FANTASY_DROPDOWN_MENU_3,
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
