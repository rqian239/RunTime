import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamDetails
from data.nba_teams import get_all_team_options
from data.teamdetails import TeamDetails 
# from data.teamID_teamName import nba_teams_ids
from components.navbar import navbar_simple
from components.footer import footer
import ids

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
                        html.Br(),
                        html.H1("Teams", className="team-page-title", style={'textAlign': 'center'}),
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
                    width=12  # Full width for this column
                )
            ]
        ),
        dbc.Row(
            [
                # Adding an empty dropdown menu with longer dropdown
                dbc.Col(
                    [
                        html.Br(),
                        dcc.Dropdown(
                            id=ids.TEAM_PAGE_DROPDOWN_MENU,
                            options=get_all_team_options(),  # Options generated from the function
                            placeholder="Select a Team",  # Placeholder text for the dropdown
                            style={'width': '100%'}  # Set the width of the dropdown
                        ),
                        html.Br()
                    ],
                    md=6
                )
            ]
        ),
        dbc.Row(
            [
                # First card taking up 70% width
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Header"),
                                dbc.CardBody(
                                    [
                                        html.H4("Team Information", className="card-title"),
                                        html.P(
                                            "This is some text inside the card body. Will be adding tea info based on selection in dropdown.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "70rem"}  # Adjust the maxWidth here to make the card wider
                        ),
                    ],
                    width=8,  # 70% width for this column
                    md=9  # Adjust the column size for medium-sized screens
                ),
                # Second card taking up 30% width
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Header"),
                                dbc.CardBody(
                                    [
                                        html.H4("Team Image", className="card-title"),
                                        html.P(
                                            "This is some text inside the card body. You can add any content you want here.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem"}  # Adjust the maxWidth here to make the card wider
                        ),
                    ],
                    width=4,  # 30% width for this column
                    md=3  # Adjust the column size for medium-sized screens
                ),
            ],
        ),
    ],
    class_name="body-flex-wrapper",
)

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")

@app.callback(
    [Output("team-info-title", "children"),
     Output("team-info-content", "children")],
    [Input(ids.TEAM_PAGE_DROPDOWN_MENU, "value")]
)
def update_team_info(selected_team):
    print("Selected team:", selected_team)  # Debugging output
    if selected_team:
        # Retrieve team ID based on the selected team name
        all_teams = teams.get_teams()
        team_id = None
        for team in all_teams:
            if team['full_name'] == selected_team:
                team_id = team['id']
                break
        print("Selected team ID:", team_id)  # Debugging output
        if team_id:
            # Initialize the TeamDetails class with the specified team_id
            team_details = TeamDetails(team_id=team_id)
            # Get the team details data frame
            nba_team_details_df = team_details.get_data_frames()[0]
            print("Team details DataFrame:", nba_team_details_df)  # Debugging output
            return "Team Information", html.Table(
                # You can adjust the format as per your preference
                # Here, I'm converting DataFrame to HTML table for display
                [html.Tr([html.Th(col) for col in nba_team_details_df.columns])] +
                [html.Tr([html.Td(nba_team_details_df.iloc[i][col]) for col in nba_team_details_df.columns]) for i in range(len(nba_team_details_df))])
        else:
            return "Team Information", "No information available for the selected team."
    else:
        return "Team Information", ""
