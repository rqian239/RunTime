import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from data.nba_teams import get_all_team_options
from components.navbar import navbar_simple
from components.footer import footer
from utils.functions import basic_team_info, detailed_team_info, get_team_championships
from utils.functions import get_top_left_pixel_color
from assets.links_to_nba_logo_gifs import nba_logo_gifs_links

from dash import callback

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
            class_name="my-4"
        ),
        dbc.Row(
            children=[
                # This is where we display team info with a callback
            ],
            id=ids.TEAM_PAGE_CONTENT,
            class_name="my-4",
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


def build_team_info_body(abbrev):

    team_name, team_city, team_state, year_founded = basic_team_info(abbrev)

    detailed_team_info_df = detailed_team_info(abbrev)

    championships_df = get_team_championships(abbrev)
    num_championships = len(championships_df)

    championship_string = ', '.join(f"{row['YEARAWARDED']} ({row['OPPOSITETEAM']})" for index, row in championships_df.iterrows())
    championship_string = f"{num_championships} Championship{('' if num_championships == 1 else 's')} {(': ' if num_championships > 0 else '')}{championship_string}"


    if "No Affiliate" not in detailed_team_info_df['DLEAGUEAFFILIATION'].iloc[0]:
        g_league_affiliate_str = f"This team's G League affiliate is the {detailed_team_info_df['DLEAGUEAFFILIATION'].iloc[0]}."
    else:
        g_league_affiliate_str = f"This team currently does not have a G Leagure affiliate team."

    team_info_body = dbc.Container(
        children=[
            dbc.Container(
                id=ids.TEAM_INFO_HEADER,
                children=[
                    dbc.Row(
                    [
                        html.H1(f"{team_name}", className="text-center"),
                    ],
                    class_name="mb-2"
                    ),
                ],
            ),
            dbc.Container(
                id=ids.TEAM_INFO_BODY,
                children=[
                    dbc.Row(
                        [
                            html.P(f"{'🏆' * num_championships}"),
                            html.P(f"{championship_string}", style={"font-size" : "small"}),
                        ],
                        class_name="text-center mb-4"
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                    children=[
                                        html.P(f"""The {team_name} are based in {team_city}, {team_state} and were founded in {year_founded}. The {detailed_team_info_df['NICKNAME'].iloc[0]} play in {detailed_team_info_df['ARENA'].iloc[0]}.
                                            The current head coach of the {team_name} is {detailed_team_info_df['HEADCOACH'].iloc[0]}, the GM is {detailed_team_info_df['GENERALMANAGER'].iloc[0]}, and the owner is {detailed_team_info_df['OWNER'].iloc[0]}. 
                                            {g_league_affiliate_str}
                                            """),
                                            html.Br(),
                                            html.P("Navigate with the buttons below to discover more about this team!")
                                        ],
                                    )
                                ],
                                class_name="centered",
                                style={ "font-size" : "larger" },
                            ),
                            dbc.Col(
                                [
                                    # Animated NBA Logo gif
                                    html.A(
                                        href="https://www.behance.net/gallery/100429525/NBA-Logos-Looped-Bleacher-Report",
                                        children=[
                                            html.Img(
                                                id=ids.TEAM_LOGO_GIF,
                                                src=f"../assets/images/looped_nba_logos/{abbrev}_animated_logo.gif",
                                                width="45%",
                                                height="auto",
                                                # className="landing-page-basketball-gif",
                                                title="Animated logos created by Vincent Portolan for Bleacher Report",
                                                className="animated-logo-gif",
                                                style={'border-color': f'{get_top_left_pixel_color(f"./assets/images/looped_nba_logos/{abbrev}_animated_logo.gif")}'},
                                            )
                                        ],
                                        target="_blank",
                                    )
                                ],
                                class_name="centered"
                            )
                        ]
                    )
                ]
            ),
        ]
    )
    return team_info_body

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")


@callback(
    Output(ids.TEAM_PAGE_CONTENT, 'children'),
    Input(ids.TEAM_PAGE_DROPDOWN_MENU, 'value')
)
def display_team_info(team_selection):
    if team_selection is None:
        return html.Div(html.P("Please select a team with the dropdown menu."), className="text-center")
    else:
        return build_team_info_body(team_selection)
