import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

dash.register_page(__name__, path='/')

# Read the game schedule data from a CSV file
game_schedule_data = pd.read_csv(r'C:\Users\natar\OneDrive\Desktop\RunTime\RunTime\dash\data\nba-2023-UTC.csv')

# Modify the "Game" column to contain "Home Team vs Away Team"
game_schedule_data['Game'] = game_schedule_data['Home Team'] + ' vs ' + game_schedule_data['Away Team']

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("RunTime's Game Simulator", className="home-page-title"),
                        html.Br(),
                        html.P(
                            """\
                            Welcome! Experience the thrill of the NBA like never before with our innovative game predictor! \n Our application harnesses the power of advanced analytics 
                            to provide you with accurate predictions for upcoming NBA games. Delve into detailed player stats, team performances, and historical data to make 
                            informed decisions. Whether you're a passionate fan or a seasoned bettor, our intuitive interface and real-time updates will keep you at the edge of
                            your seat. Join us now and elevate your NBA experience with our cutting-edge game predictor!""",
                            #style={'textAlign': 'center'}
                        ),
                    ],
                    md=6
                ),
                dbc.Col(
                    [
                    # basketball gif
                        html.Img(
                            src="dash\assets\images\basketball.gif",
                            width="80%",
                            height="auto",
                            className="spinning-globe-gif"
                        )
                    ],
                    className="centered",
                    md=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button("Learn More about the Project and the Team", id="learn-more-button", href="/about", className="btn btn-lg btn-primary get-started-button"),
                    ],
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H2("Top NBA Websites", className="websites-title", style={'textAlign': 'center'}),
                        html.Br()
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
            ],
            className="centered",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H2("Game Schedule", className="home-page-title", style={'textAlign': 'center'}),
                        html.Br(), 
                        html.P("To view the games scheduled for March and April of the 2023-2024 season, utilize the scroll bar to navigate through them.", style={'textAlign': 'center'})
                    ],
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("March", className="home-page-title", style={'textAlign': 'center'}),
                        html.Div(
                            [
                                html.Table(
                                    className="table table-bordered table-hover",
                                    children=[
                                        html.Thead(
                                            html.Tr(
                                                [
                                                    html.Th("Game", style={'text-align': 'center'}),
                                                    html.Th("Date", style={'text-align': 'center'}),
                                                    html.Th("Location", style={'text-align': 'center'})
                                                ]
                                            )
                                        ),
                                        html.Tbody(
                                            [
                                                html.Tr(
                                                    [
                                                        html.Td(game["Game"]),
                                                        html.Td(game["Date"]),
                                                        html.Td(game["Location"])
                                                    ]
                                                )
                                                for index, game in game_schedule_data.iterrows()
                                                if pd.to_datetime(game["Date"], dayfirst=True).month_name() == 'March'
                                            ]
                                        )
                                    ]
                                )
                            ],
                            style={'maxHeight': '400px', 'overflowY': 'scroll', 'border': '2px solid #cccccc', 'border-radius': '5px'}
                        )
                    ],
                    md=6
                ),
                dbc.Col(
                    [
                        html.H2("April", className="home-page-title", style={'textAlign': 'center'}),
                        html.Div(
                            [
                                html.Table(
                                    className="table table-bordered table-hover",
                                    children=[
                                        html.Thead(
                                            html.Tr(
                                                [
                                                    html.Th("Game", style={'text-align': 'center'}),
                                                    html.Th("Date", style={'text-align': 'center'}),
                                                    html.Th("Location", style={'text-align': 'center'})
                                                ]
                                            )
                                        ),
                                        html.Tbody(
                                            [
                                                html.Tr(
                                                    [
                                                        html.Td(game["Game"]),
                                                        html.Td(game["Date"]),
                                                        html.Td(game["Location"])
                                                    ]
                                                )
                                                for index, game in game_schedule_data.iterrows()
                                                if pd.to_datetime(game["Date"], dayfirst=True).month_name() == 'April'
                                            ]
                                        )
                                    ]
                                )
                            ],
                            style={'maxHeight': '400px', 'overflowY': 'scroll','border': '2px solid #cccccc', 'border-radius': '5px'}
                        )
                    ],
                    md=6
                )
            ]
        )
    ]
)

# Create a Dash app instance
app = dash.Dash(__name__)

# Assign the layout to the specific path
layout = body

# Run the Dash server
if __name__ == '__main__':
    app.run_server(debug=True)
