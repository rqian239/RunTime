import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback_context, no_update
from dash.dependencies import Input, Output, State
import pandas as pd

from data.nba_teams import get_all_team_options
from components.navbar import navbar_simple
from components.footer import footer
from utils.functions import basic_team_info, detailed_team_info, get_team_championships, get_team_roster, get_social_media_links, get_league_standings
from utils.Team_Specific_Schedule import scrape_team_specific_schedule
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
    ],
    class_name="body-flex-wrapper",
)


def build_team_info_body(abbrev):

    team_name = basic_team_info(abbrev)[0]

    team_info_body = dbc.Container(
        children=[
            dbc.Container(
                id=ids.TEAM_INFO_HEADER,
                children=[
                    dbc.Row(
                        [
                            html.H1(f"{team_name}", className="text-center mb-4"),
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Button(
                                        id=ids.GENERAL_TEAM_INFO_BUTTON,
                                        children="General Info",
                                        color="info",
                                        className="mx-2",
                                        style={'width': '100%'}
                                    )
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Button(
                                        id=ids.ROSTER_BUTTON,
                                        children="Roster",
                                        color="info",
                                        className="mx-2",
                                        style={'width': '100%'}
                                    )
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Button(
                                        id=ids.TEAM_INFO_SCHEDULE_BUTTON,
                                        children="Schedule",
                                        color="info",
                                        className="mx-2",
                                        style={'width': '100%'}
                                    )
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Button(
                                        id=ids.STANDINGS_BUTTON,
                                        children="Standings",
                                        color="info",
                                        className="mx-2",
                                        style={'width': '100%'}
                                    )
                                ],
                            ),
                        ],
                        className="centered mb-3",
                    ),
                ],
            ),
            dbc.Container(
                id=ids.TEAM_INFO_BODY,
                children=build_general_team_info_body(abbrev)
            ),
        ]
    )
    return team_info_body

def build_roster_body(abbrev):
    # Get the roster DataFrame
    roster_df = get_team_roster(abbrev)
    
    # Create the roster table with bordered set to True
    roster_table = dbc.Table.from_dataframe(roster_df, striped=True, bordered=True, hover=True, className="table-bordered")

    # Define the gradient border color
    border_color = "#a932ff"  # Cyber color gradient

    # Add custom CSS to ensure the gradient border color
    roster_table.style = {
        "border": f"2px solid {border_color}",  # Use the defined border color
        "border-radius": "8px",  # Rounded corners
        "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for depth
        "font-size": "14px",  # Increase font size
        "color": "#333",  # Text color
        "margin": "auto"  # Center the table horizontally
    }

    # Add custom CSS to style the first row
    roster_table.children[0].children[0].style = {
        "font-weight": "bold",  # Make text bold
        "text-decoration": "underline",  # Underline text
        "color": "#a932ff",  # Set text color to neon purple
        "font-size": "16px",  # Increase font size
        "font-style": "italic"  # Make text italic
    }

    # Wrap the table in a container
    roster_body = dbc.Container(
        children=[roster_table],
        class_name="centered"
    )

    return roster_body





def build_general_team_info_body(abbrev):
    
    team_name, team_city, team_state, year_founded = basic_team_info(abbrev)

    detailed_team_info_df = detailed_team_info(abbrev)

    championships_df = get_team_championships(abbrev)
    num_championships = len(championships_df)

    championship_string = ', '.join(f"{row['YEARAWARDED']} ({row['OPPOSITETEAM']})" for index, row in championships_df.iterrows())
    championship_string = f"{num_championships} Championship{('' if num_championships == 1 else 's')} {(': ' if num_championships > 0 else '')}{championship_string}"

    facebook_link, twitter_link, instagram_link = get_social_media_links(abbrev)

    if "No Affiliate" not in detailed_team_info_df['DLEAGUEAFFILIATION'].iloc[0]:
        g_league_affiliate_str = f"This team's G League affiliate is the {detailed_team_info_df['DLEAGUEAFFILIATION'].iloc[0]}."
    else:
        g_league_affiliate_str = f"This team currently does not have a G League affiliate team."

    general_team_info_body = [
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
                                html.P("Navigate with the buttons above to discover more about this team!"),
                                dbc.Row(
                                    [
                                        dbc.Col(),  # These empty columns are added to squeeze the icons together more
                                        dbc.Col(),
                                        dbc.Col(
                                            html.A(
                                                href=facebook_link,
                                                children=[
                                                    html.Img(
                                                        src="../assets/images/facebook-white-icon.svg", 
                                                        className="social-media-icon"
                                                    ),
                                                ],
                                                target="_blank"
                                            ),
                                        ),
                                        dbc.Col(
                                            html.A(
                                                href=twitter_link,
                                                children=[
                                                    html.Img(
                                                        src="../assets/images/x-social-media-white-icon.svg", 
                                                        className="social-media-icon"
                                                    ),
                                                ],
                                                target="_blank"
                                            ),
                                        ),
                                        dbc.Col(
                                            html.A(
                                                href=instagram_link,
                                                children=[
                                                    html.Img(
                                                        src="../assets/images/instagram-white-icon.svg", 
                                                        className="social-media-icon"
                                                    ),
                                                ],
                                                target="_blank"
                                            ),
                                        ),
                                        dbc.Col(), # These empty columns are added to squeeze the icons together more
                                        dbc.Col(),
                                    ],
                                    class_name="justify-content-center align-items-center mt-5 g-1"
                                )
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

    return general_team_info_body

def build_team_schedule_body(abbrev):
 
    schedule_df = scrape_team_specific_schedule(abbrev)
    
    border_color = "#a932ff"  # Cyber color gradient

    if isinstance(schedule_df, pd.DataFrame):
        schedule_table = dbc.Table.from_dataframe(schedule_df, striped=True, bordered=True, hover=True)

        schedule_table.style = {
            "border": f"2px solid {border_color}",  # Use the defined border color
            "border-radius": "8px",  # Rounded corners
            "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for depth
            "font-size": "14px",  # Increase font size
            "color": "#333",  # Text color
            "margin": "auto"  # Center the table horizontally
        }

           # Add custom CSS to style the first row
        schedule_table.children[0].children[0].style = {

            "font-weight": "bold",  # Make text bold
            "text-decoration": "underline",  # Underline text
            "color": "#a932ff",  # Set text color to neon purple
            "font-size": "16px",  # Increase font size
            "font-style": "italic"  # Make text italic
        }

        schedule_body = dbc.Container(children=[schedule_table], class_name="centered")
    else:
        schedule_body = dbc.Container(children=[html.P("This team has no schedule.")], class_name="text-center")
    
    return schedule_body

def build_team_standings_body(abbrev):

    standings_df = get_league_standings(abbrev)

    standings_table = dbc.Table.from_dataframe(standings_df, striped=True,bordered=True, hover=True, className="table-bordered")

    border_color = "#a932ff"  # Cyber color gradient

        # Add custom CSS to ensure the gradient border color
    standings_table.style = {
        "border": f"2px solid {border_color}",  # Use the defined border color
        "border-radius": "8px",  # Rounded corners
        "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for depth
        "font-size": "14px",  # Increase font size
        "color": "#333",  # Text color
        "margin": "auto"  # Center the table horizontally
    }

       # Add custom CSS to style the first row
    standings_table.children[0].children[0].style = {
        "font-weight": "bold",  # Make text bold
        "text-decoration": "underline",  # Underline text
        "color": "#a932ff",  # Set text color to neon purple
        "font-size": "16px",  # Increase font size
        "font-style": "italic"  # Make text italic
    }

    # Create the standings body here
    team_standings_body = dbc.Container(
        children=[standings_table],
        class_name="text-center"
    )

    return team_standings_body


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

    standings_df = get_league_standings()  # Call a function to get the league standings data

    standings_body = dbc.Container(
        children=[
            dbc.Table.from_dataframe(standings_df, striped=True, bordered=True, hover=True)
        ],
        class_name="centered"
    )
    return standings_body
       
    
@callback(
    Output(ids.TEAM_INFO_BODY, 'children'),
    [Input(ids.ROSTER_BUTTON, 'n_clicks'),
     Input(ids.GENERAL_TEAM_INFO_BUTTON, 'n_clicks'),
     Input(ids.TEAM_INFO_SCHEDULE_BUTTON, 'n_clicks'),
     Input(ids.STANDINGS_BUTTON, 'n_clicks'),],
    [State(ids.TEAM_PAGE_DROPDOWN_MENU, 'value')]
)
def update_team_info(roster_clicks, general_info_clicks, schedule_clicks, standings_clicks, team_selection):
    ctx = callback_context
    
    if not ctx.triggered:
        return no_update  # No button was clicked, do nothing.

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Check which button was clicked
    if button_id == ids.ROSTER_BUTTON and roster_clicks:
        return build_roster_body(team_selection)
    elif button_id == ids.GENERAL_TEAM_INFO_BUTTON and general_info_clicks:
        return build_general_team_info_body(team_selection)
    elif button_id == ids.TEAM_INFO_SCHEDULE_BUTTON and schedule_clicks:
        return build_team_schedule_body(team_selection)
    elif button_id == ids.STANDINGS_BUTTON and standings_clicks:
        return build_team_standings_body(team_selection)
    else:
        return no_update  # If none match, do nothing.