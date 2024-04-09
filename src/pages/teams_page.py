import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options
from data.teamdetails import TeamDetails 
# from data.teamID_teamName import nba_teams_ids
from components.navbar import navbar_simple
from components.footer import footer
import ids

dash.register_page(__name__, path='/teams')

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
                        html.Div(
                            children = [
                                html.H1("Teams Page", className="team-page-title text-center")
                            ],
                            id=ids.TEAM_PAGE_TITLE
                        ),
                    ],
                    width=12  # Full width for this column
                )
            ],
            class_name="my-4"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            children = [
                                html.P(
                                    """\
                                    Welcome to the Team Info Page. Here you will be able to quickly search for up-to-date information about your NBA team.
                                    Look up recent box scores, your team's schedule, or in-depth statistics all in one place. Select an NBA team using the dropdown below.""",
                                    className="text-center"
                                )
                            ],
                            id=ids.TEAM_PAGE_DESCRIPTION
                        )
                    ],
                    width=12  # Full width for this column
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id=ids.TEAM_PAGE_DROPDOWN_MENU,
                        options=get_all_team_options(),
                        placeholder="Select a Team",  # Placeholder text for the dropdown
                        className="dropdown-styling",
                        style={'width': '100%'}
                    ),
                    md=6,
                    class_name="center-content"
                )
            ],
            justify="center",
            class_name="mb-4"
        ),
        # dbc.Row(
        #     [
        #         # First card taking up 70% width
        #         dbc.Col(
        #             [
        #                 dbc.Card(
        #                     [
        #                         dbc.CardHeader("Header"),
        #                         dbc.CardBody(
        #                             [
        #                                 html.H4("Team Information", className="card-title"),
        #                                 html.P(
        #                                     "This is some text inside the card body. Will be adding tea info based on selection in dropdown.",
        #                                     className="card-text"
        #                                 )
        #                             ]
        #                         )
        #                     ],
        #                     className="border-primary mb-3",
        #                     style={"maxWidth": "70rem"}  # Adjust the maxWidth here to make the card wider
        #                 ),
        #             ],
        #             width=8,  # 70% width for this column
        #             md=9  # Adjust the column size for medium-sized screens
        #         ),
        #         # Second card taking up 30% width
        #         dbc.Col(
        #             [
        #                 dbc.Card(
        #                     [
        #                         dbc.CardHeader("Header"),
        #                         dbc.CardBody(
        #                             [
        #                                 html.H4("Team Image", className="card-title"),
        #                                 html.P(
        #                                     "This is some text inside the card body. You can add any content you want here.",
        #                                     className="card-text"
        #                                 )
        #                             ]
        #                         )
        #                     ],
        #                     className="border-primary mb-3",
        #                     style={"maxWidth": "20rem"}  # Adjust the maxWidth here to make the card wider
        #                 ),
        #             ],
        #             width=4,  # 30% width for this column
        #             md=3  # Adjust the column size for medium-sized screens
        #         ),
        #     ],
        # ),
    ],
    class_name="body-flex-wrapper",
)

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")
