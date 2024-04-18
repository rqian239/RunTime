import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
from pathlib import Path
from utils.Today_Game import scrape_Today_nba_schedule

from components.navbar import navbar_simple
from components.footer import footer
import ids

# Registers this file as a page within our Dash application
dash.register_page(__name__, path='/')

# Get the directory of the current script file
script_dir = Path(__file__).parent

# Paths
PATH_TO_SCHEDULE_CSV = script_dir / ".." / "data" / "nba-2023-UTC.csv"  # using pathlib library to find path to csv file
PATH_TO_BASKETBALL_GIF = "assets/images/nba_logo_and_players.gif" # Dash can recognize the assets folder

# Read the game schedule data from a CSV file
game_schedule_data = pd.read_csv(PATH_TO_SCHEDULE_CSV)

# Modify the "Game" column to contain "Home Team vs Away Team"
game_schedule_data['Game'] = game_schedule_data['Home Team'] + ' vs ' + game_schedule_data['Away Team']

# Navbar and footer imported here
nav = navbar_simple()
ftr = footer()

def build_team_schedule_body():
    schedule_df = scrape_Today_nba_schedule()
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
        # If schedule_df is empty or not a DataFrame
        schedule_body = dbc.Container(children=[html.P("No Games Today.")], class_name="text-center")
    
    return schedule_body

    

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("RunTime's NBA Portal", className="landing-page-title", id=ids.LANDING_HEADER),
                        html.Br(),
                        html.P(
                            """\
                            Embark on an unparalleled NBA journey with our innovative prediction tool! Utilizing the NBA API and a 
                            well-crafted algorithm, our application forecasts the outcomes of upcoming or potential matchups 
                            between NBA teams. With our user-friendly interface and real-time updates, you'll find yourself fully 
                            immersed in the excitement, whether seeking deeper insights as a passionate fan or making informed decisions
                            as a seasoned bettor. Join us now and experience the thrill of elevating your NBA experience with our 
                            cutting-edge prediction tool!""",
                            #style={'textAlign': 'center'}
                        ),
                        html.Br(),
                        dbc.Button("Learn More", id=ids.LEARN_MORE_BUTTON, href="/about", className="btn btn-lg btn-primary get-started-button"),
                    ],
                    md=6,
                    class_name="mt-4"
                ),
                dbc.Col(
                    [
                    # basketball gif
                    html.A(
                        href="https://www.behance.net/gallery/72162251/The-Next-NBA-logo-NBA-Logoman-Series",
                        children=[
                            html.Img(
                                src=PATH_TO_BASKETBALL_GIF,
                                width="100%",
                                height="auto",
                                className="landing-page-basketball-gif",
                                title="Images by Tyson Beck"
                            )
                        ],
                        target="_blank"
                    )
                    ],
                    className="centered mt-4",
                    md=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Popular NBA Websites", className="text-center mt-5"),
                    ],
                )
            ]
        ),
        dbc.Row(
            [
                # add buttons for each website
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "NBA.com",
                            color="danger",
                            className="mr-2",
                            href="https://www.nba.com/",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "Bleacher Report",
                            color="danger",
                            className="mr-2",
                            href="https://bleacherreport.com/nba%20",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "ESPN",
                            color="danger",
                            className="mr-2",
                            href="https://www.espn.com/nba/",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "Sports Illustrated",
                            color="danger",
                            className="mr-2",
                            href="https://www.si.com/nba",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "CBS Sports",
                            color="danger",
                            className="mr-2",
                            href="https://www.cbssports.com/nba/",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "HoopsHype",
                            color="danger",
                            className="mr-2",
                            href="https://hoopshype.com/",
                            external_link=True,
                            style={'width': '100%'}
                        )
                    ],
                ),
            ],
            className="centered mb-5",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Game Schedule", className="home-page-title", style={'textAlign': 'center'}),
                        html.Br(), 
                        html.P("To view the games scheduled for March and April of the 2023-2024 season, utilize the scroll bar to navigate through them.", style={'textAlign': 'center'}),
                        build_team_schedule_body()
                    ],
                )
            ],
            class_name="my-5",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        
                    ],
                    md=6
                ),
            ],
            class_name="mb-5",
        ),
    ],
    class_name="body-flex-wrapper",
)




# This is how Dash knows what the layout of the page is!
layout = html.Div([nav, body, ftr], className="make-footer-stick")


