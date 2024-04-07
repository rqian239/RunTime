import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options
from components.navbar import navbar_simple
from components.footer import footer
import ids


dash.register_page(__name__, path='/about')  # Change the path here

# Navbar and footer imported here
nav = navbar_simple()
ftr = footer()

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("About Us", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                            Welcome to the About Us Page!""",
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
                            className="card text-white bg-primary mb-3",
                            style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=15,  # 100% width for this column
                    align='center'  # Center align the column content
                )
            ],
            justify="center"  # Center align the row
        ),
        dbc.Row(
            [
                dbc.Col(width=100),  # Empty column to occupy space
            ]
        ),
        dbc.Row(
            [
                # Adding a new row for small cards
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Front-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Nivedha Natarajan", className="card-title"),
                                        html.P(
                                            "4th Year Computer Science Major",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Front-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Nikitha Chintalapati", className="card-title"),
                                        html.P(
                                            "4th Year Computer Science Major",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Bryan Hernandez", className="card-title"),
                                        html.P(
                                            "4th Year Computer Science Major",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Ria Manoj Gandhi", className="card-title"),
                                        html.P(
                                            "4th Year Computer Science Major",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Richard Qian", className="card-title"),
                                        html.P(
                                            "4th Year Computer Science Major",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                )
            ],
            justify="center"  # Center align the row
        )
    ]
)

# Assign the layout to the specific path
layout = layout = html.Div([nav, body, ftr], className="make-footer-stick")