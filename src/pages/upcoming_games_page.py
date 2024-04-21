import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options
from dash.dependencies import Input, Output, State
from dash import callback


from components.navbar import navbar_simple
from components.footer import footer
import ids
from utils.Upcoming_Games import scrape_upcoming_nba_schedule


dash.register_page(__name__, path='/upcominggames')  # Change the path here

# Navbar and footer imported here
nav = navbar_simple()
ftr = footer()


def build_team_schedule_body():
    schedule_df = scrape_upcoming_nba_schedule()
    border_color = "#834847"  # Cyber color gradient

    if isinstance(schedule_df, pd.DataFrame) and not schedule_df.empty:
        # If schedule_df is a non-empty DataFrame
        schedule_table = dbc.Table.from_dataframe(schedule_df, striped=True, bordered=True, hover=True)

        schedule_table.style = {
            "border": f"2px solid {border_color}",  # Use the defined border color
            "border-radius": "8px",  # Rounded corners
            "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for depth
            "font-size": "14px",  # Increase font size
            "color": "#333",  # Text color
            "margin": "auto"  # Center the table horizontally
        }

        schedule_body = dbc.Container(children=[schedule_table], class_name="centered")
    else:
        schedule_body = dbc.Container(children=[html.P("No Games Today.")], class_name="text-center")
        
    return schedule_body

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
                            Welcome to the Upcoming Games Page! Dive into the world of fantasy sports and games with ease! 
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
               dbc.Row(
            [
                # Adding the dropdown
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id=ids.UPCOMING_GAMES_DROPDOWN_LEFT,
                            options=get_all_team_options(),  # Options generated from the function
                            placeholder="Select a Team",  # Placeholder text for the dropdown
                            style={'width': '100%'}  # Set the width of the dropdown
                        ),
                    ],
                    width=5 # 33% width for this column
                ),
                # Adding the table to display the schedule
                dbc.Col(
                    [
                        html.Div(id = ids.UPCOMING_GAMES_OUTPUT)
                    ],
                    width=7  # 33% width for this column
                ),
            ],
        ),
                # Adding the second card with dropdown
                
                dbc.Col(
                    [
                         html.H2("Current NBA Schedule", className="home-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P("Scroll to view the list of scheduled games, including the home and visitor teams, along with the game date and time.", style={'textAlign': 'center'}),
                        html.Br(),
                        html.Div(
                            [
                                html.Table(
                                    className="table table-bordered table-hover",
                                    children=[
                                        html.Thead(
                                            html.Tr(
                                                [
                                                    html.Th("Home Team", style={'text-align': 'center'}),
                                                    html.Th("Visitor Team", style={'text-align': 'center'}),
                                                    html.Th("Date", style={'text-align': 'center'}),
                                                    html.Th("Time", style={'text-align': 'center'}),
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
                                                        #html.Td(game["Predicted Winner"]),
                                                        #html.Td(game["Winner Probability"]),
                                                        
                                                    ]
                                                )
                                                for index, game in scrape_upcoming_nba_schedule().iterrows()
                                            ]
                                        )
                                    ]
                                )
                            ],
                            style={'maxHeight': '400px', 'overflowY': 'scroll', 'border': '2px solid #cccccc', 'border-radius': '5px'}
                        ),

                    ],
                    width=7  # 33% width for this column
                ),
            ],
        ),
    ],
    class_name="body-flex-wrapper",
)

@callback(
    Output(ids.UPCOMING_GAMES_OUTPUT, 'children'),
    [Input(ids.UPCOMING_GAMES_DROPDOWN_LEFT, 'value')]
)
def update_table(selected_team):
    print("Selected team:", selected_team)  # Debugging line
    if selected_team:
        # Call the scraping function with the selected team
        print("Schedule DataFrame:")  # Debugging line
        return html.P(selected_team)
    else:
        return html.P("Please select a team", className="text-center")

# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")