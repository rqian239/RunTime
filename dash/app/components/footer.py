import dash
import dash_bootstrap_components as dbc
from dash import html


def footer():

    ftr = html.Div(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("Runtime Terrors", className="text-uppercase footer-title"),
                            ]),
                            className="centered"
                        ),
                    ],
                    style={"margin-bottom": "30px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("Quick Links", className="text-uppercase"),
                                dbc.NavLink("Home", href="/", className = "footer-link"),
                                dbc.NavLink("About", href="/about", className = "footer-link"),
                                dbc.NavLink("Teams", href="/teams", className = "footer-link"),
                                dbc.NavLink("Upcoming Games", href="/upcominggames", className = "footer-link"),
                                dbc.NavLink("Fantasy Games", href="/fantasygames", className = "footer-link")                               
                            ]),
                            className="centered"
                        ),
                        dbc.Col(
                            html.Div([
                                html.Br(),
                                html.Br(),
                                html.P("🌎🌍🌏"),
                            ]),
                            className="centered",
                            md=2
                        ),
                        dbc.Col(
                            html.Div([
                                html.P("Richard Qian"),
                                html.P("William Sobczak"),
                                html.P("Nikhil Pandya"),
                            ]),
                            className="centered"
                        ),
                    ],
                    className="justify-content-center"
                ),
            ],
            fluid=True,
        ),
        className="p-5 mt-5 bg-light",
        style={"margin-top": "30px"},
    )
    return ftr