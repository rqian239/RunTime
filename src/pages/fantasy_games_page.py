import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback

from dash.dependencies import Input, Output, State

from data.nba_teams import get_all_team_options
from components.navbar import navbar_simple
from components.footer import footer

from utils.elo_predict import get_winner

import ids


dash.register_page(__name__, path='/fantasygames')  # Change the path here

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
                        html.H1("Fantasy Games", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                            Welcome to the Fantasy Games Page! Set a matchup between any two NBA teams and see which one is
                            projected to win. Use the dropdowns to select your home and away teams!

                            We use Nate Silver's Elo metric to predict the winner!
                            """,
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
                        html.H2("Home Team", className="centered"),
                        html.Br(),
                        dcc.Dropdown(
                        id=ids.FANTASY_DROPDOWN_HOME,
                        options=get_all_team_options(),  # Options generated from the function
                        placeholder="Select a Team",  # Placeholder text for the dropdown
                        style={'width': '100%'}  # Set the width of the dropdown
                        ),
                        # dbc.Card(
                        #     [
                        #         dbc.CardHeader("Card 1"),
                        #         dbc.CardBody(
                        #             [
                        #                 html.H4("Card title", className="card-title"),
                        #                 html.P(
                        #                     "This is some text inside the card body. You can add any content you want here.",
                        #                     className="card-text"
                        #                 )
                        #             ]
                        #         )
                        #     ],
                        #     className="border-primary mb-3",
                        #     style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        # ),
                    ],
                    width=4  # 33% width for this column
                ),
                # Adding the second card with dropdown
                dbc.Col(
                    [
                        # dbc.DropdownMenu(
                        #     label="Select Team",
                        #     id=ids.FANTASY_DROPDOWN_MENU_2,
                        #     style={'overflowY': 'auto', 'marginBottom': '10px'}  # Add marginBottom to add space between dropdown and card
                        # ),
                        #  dbc.Card(
                        #     [
                        #         dbc.CardHeader("Card 2"),
                        #         dbc.CardBody(
                        #             [
                        #                 html.H4("Card title", className="card-title"),
                        #                 html.P(
                        #                     "This is some text inside the card body. You can add any content you want here.",
                        #                     className="card-text"
                        #                 )
                        #             ]
                        #         )
                        #     ],
                        #     className="border-primary mb-3",
                        #     style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        # ),
                    ],
                    width=4  # 33% width for this column
                ),
                # Adding the third card with dropdown
                dbc.Col(
                    [
                        html.H2("Away Team", className="centered"),
                        html.Br(),
                        dcc.Dropdown(
                        id=ids.FANTASY_DROPDOWN_AWAY,
                        options=get_all_team_options(),  # Options generated from the function
                        placeholder="Select a Team",  # Placeholder text for the dropdown
                        style={'width': '100%'}  # Set the width of the dropdown
                        ),
                        # dbc.Card(
                        #     [
                        #         dbc.CardHeader("Card 3"),
                        #         dbc.CardBody(
                        #             [
                        #                 html.H4("Card title", className="card-title"),
                        #                 html.P(
                        #                     "This is some text inside the card body. You can add any content you want here.",
                        #                     className="card-text"
                        #                 )
                        #             ]
                        #         )
                        #     ],
                        #     className="border-primary mb-3",
                        #     style={"maxWidth": "30rem"}  # Adjust the maxWidth here
                        # ),
                    ],
                    width=4  # 33% width for this column
                ),
            ],
        ),
        dbc.Row(
            id=ids.FANTASY_PAGE_CONTENT,
            children=[

            ],
            class_name="my-4",
        ),
    ],
    class_name="body-flex-wrapper",
)

def build_fantasy_content_body(home, away):
    predicted_outcome_df = get_winner(home, away)

    # Format the matchup details
    matchup_details = f"{home} vs {away}"

    # Create a header with the matchup details
    header = dbc.Row(
        dbc.Col(html.H2(matchup_details, className="text-center"))
    )

    # Style the DataFrame output
    styled_table = dbc.Row(
        dbc.Col(
            dbc.Table.from_dataframe(
                predicted_outcome_df,
                striped=True,
                bordered=True,
                hover=True,
                className="table-bordered",
                style={"font-size": "14px", "margin": "auto", "width": "90%", "border": "2px solid #a932ff", "margin": "auto"}  # Add neon purple border and center horizontally
            ),
            width={"size": 10, "offset": 1}  # Center the column
        )
    )


    # Combine the header and the styled DataFrame output into a container
    fantasy_content_body = dbc.Container(
        children=[header, styled_table],
        className="my-4"
    )

    return fantasy_content_body

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")

@callback(
    Output(ids.FANTASY_PAGE_CONTENT, 'children'),
    [Input(ids.FANTASY_DROPDOWN_HOME, 'value'),
     Input(ids.FANTASY_DROPDOWN_AWAY, 'value')]
)
def simulate_fantasy_game(home, away):
    if home is None or away is None:
        return html.Div(html.P("Please select two teams."), className="text-center")
    else:
        return build_fantasy_content_body(home, away)