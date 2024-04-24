import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options
from dash.dependencies import Input, Output, State
from dash import callback

from data.nba_teams import all_nba_teams

from components.navbar import navbar_simple
from components.footer import footer
import ids
from utils.todays_games import scrape_todays_nba_schedule
from utils.elo_predict import get_winner


dash.register_page(__name__, path='/upcominggames')  # Change the path here

# Navbar and footer imported here
nav = navbar_simple()
ftr = footer()


# def build_team_schedule_body():
#     schedule_df = scrape_upcoming_nba_schedule()
#     border_color = "#834847"  # Cyber color gradient

#     if isinstance(schedule_df, pd.DataFrame) and not schedule_df.empty:
#         # If schedule_df is a non-empty DataFrame
#         schedule_table = dbc.Table.from_dataframe(schedule_df, striped=True, bordered=True, hover=True)

#         schedule_table.style = {
#             "border": f"2px solid {border_color}",  # Use the defined border color
#             "border-radius": "8px",  # Rounded corners
#             "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for depth
#             "font-size": "14px",  # Increase font size
#             "color": "#333",  # Text color
#             "margin": "auto"  # Center the table horizontally
#         }

#         schedule_body = dbc.Container(children=[schedule_table], class_name="centered")
#     else:
#         schedule_body = dbc.Container(children=[html.P("No Games Today.")], class_name="text-center")
        
#     return schedule_body

# Define the layout for the page
def build_todays_game_table():

    todays_games_df = scrape_todays_nba_schedule()

    if todays_games_df is None:
        return html.Div(html.P("There are no NBA games scheduled for today."), className="centered")

    predictions = []

    for index, row in todays_games_df.iterrows():
        home = all_nba_teams[row["Home Team"]]
        away = all_nba_teams[row["Visitor Team"]]
        predictions_df = get_winner(home, away)
        predictions_df = predictions_df[['Expected_Winner', 'Winner_Probability', 'Point_Spread']]
        predictions.append(predictions_df)
    
    predictions_df = pd.concat(predictions, ignore_index=True)

    # Merge the prediction dataframe with the original schedule dataframe
    todays_predictions_df = pd.concat([todays_games_df, predictions_df], axis=1)


    todays_game_table = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Home Team", style={'text-align': 'center'}),
                    html.Th("Visitor Team", style={'text-align': 'center'}),
                    html.Th("Date", style={'text-align': 'center'}),
                    html.Th("Time", style={'text-align': 'center'}),
                    html.Th("Predicted Winner", style={'text-align': 'center'}),
                    html.Th("Win Probability", style={'text-align': 'center'}),
                    html.Th("Point Spread", style={'text-align': 'center'}),
                ]
            )
        ),
        html.Tbody(
            [
                html.Tr(
                    [
                        html.Td(game["Home Team"]),
                        html.Td(game["Visitor Team"]),
                        html.Td(game["Date"]),
                        html.Td(game["Time"]),
                        html.Td(game["Expected_Winner"]),
                        html.Td(game["Winner_Probability"]),
                        html.Td(game["Point_Spread"]),
                        
                    ]
                )
                for index, game in todays_predictions_df.iterrows()
            ]
        )
    ]

    return todays_game_table

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Today's Games", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                                Welcome! Here you can find today's NBA games and the projected winner of each matchup! Navigate
                                through the page to study relevant team statistics ahead of today's games.

                                We use Nate Silver's Elo metric to predict the winner!
                            """,
                            className="centered"
                        ),
                    ],
                    width=12  # Full width for this column
                )
            ]
        ),
        dbc.Row(
            [   
                # html.H2("Today's NBA Games", className="home-page-title", style={'textAlign': 'center'}),
                # html.Br(),
                # html.P("Scroll to view the list of scheduled games, including the home and visitor teams, along with the game date and time.", style={'textAlign': 'center'}),
                html.Br(),
                html.Div(
                    [
                        html.Table(
                            className="table table-bordered table-hover",
                            children=build_todays_game_table()
                        )
                    ],
                    style={'maxHeight': '400px', 'overflowY': 'scroll', 'border': '2px solid #cccccc', 'border-radius': '5px'}
                ),
            ],
        ),
    ],
    class_name="body-flex-wrapper",
)

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")