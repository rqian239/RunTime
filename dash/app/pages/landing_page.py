import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Register the page with a specific path
dash.register_page(__name__, path='/')

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("RunTime's Game Simulator", className="home-page-title", style={'textAlign': 'center', 'margin': 'auto'}),
                        html.Br(),
                        html.P(
                            """\
                            Welcome! Experience the thrill of the NBA like never before with our innovative game predictor! \n Our application harnesses the power of advanced analytics 
                            to provide you with accurate predictions for upcoming NBA games. Delve into detailed player stats, team performances, and historical data to make 
                            informed decisions. Whether you're a passionate fan or a seasoned bettor, our intuitive interface and real-time updates will keep you at the edge of
                            your seat. Join us now and elevate your NBA experience with our cutting-edge game predictor!""",
                            style={'textAlign': 'center'}
                        ),
                    ],
                )
            ]
        ),
        # Loop through months and create tables for each
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H2("Game Schedule", className="home-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P("To view the games for the 2023 - 2024 season,", style={'textAlign': 'center'}),
                        html.P(" please click on the month!", style={'textAlign': 'center'})     
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                # Pagination controls
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Ul(
                                    className="pagination",
                                    children=[
                                        html.Li(
                                            className="page-item active" if month == 'March' else "page-item",
                                            children=html.A(
                                                className="page-link",
                                                href=f"#{month.lower()}",
                                                id=f"link-{month.lower()}",
                                                children=month
                                            )
                                        )
                                        for month in ['March', 'April']
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Table(
                                            className="table table-bordered table-hover",
                                            id=f"table-{month.lower()}",
                                            children=[
                                                html.Thead(
                                                    html.Tr(
                                                        [
                                                            html.Th("Game"),
                                                            html.Th("Date"),
                                                            html.Th("Time")
                                                        ]
                                                    )
                                                ),
                                                html.Tbody(
                                                    [
                                                        html.Tr(
                                                            [
                                                                html.Th(f"Game {i}"),
                                                                html.Td(f"Date {i}"),
                                                                html.Td(f"Time {i}")
                                                            ]
                                                        )
                                                        for i in range(1, 4)
                                                    ]
                                                )
                                            ]
                                        )
                                    ],
                                    id=month.lower(),
                                    style={"display": "block" if month == 'March' else "none", 'margin': 'auto'}
                                )
                                for month in ['March', 'April']
                            ]
                        )
                    ]
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
