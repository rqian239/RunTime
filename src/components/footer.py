import dash_bootstrap_components as dbc
from dash import html


def footer():

    ftr = html.Div(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4("Quick Links", className="text-uppercase text-white"),
                                html.Div([
                                    dbc.Button("Home", href="/", color="danger", className="btn btn-primary btn-link mr-2"),
                                    dbc.Button("About", href="/about", color="danger", className="btn btn-primary btn-link mr-2"),
                                    dbc.Button("Teams", href="/teams", color="danger", className="btn btn-primary btn-link mr-2"),
                                    dbc.Button("Upcoming Games", href="/upcominggames", color="danger", className="btn btn-primary btn-link mr-2"),
                                    dbc.Button("Fantasy Games", href="/fantasygames", color="danger", className="btn btn-primary btn-link mr-2"),
                                ], className="btn-group"),  # Adding btn-group class to make buttons horizontal
                            ],
                            className="text-center mt-3"
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("Created by the Runtime Terrors", className="text-center text-white", style={'font-style': 'italic'}),
                            ]),
                        ),
                    ],
                    className="my-2",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.P("Nikitha Chintalapati, Ria Gandhi, Bryan Hernandez-Sanchez, Nivedha Natarajan, Richard Qian", className="mb-2 text-white"),
                                html.P("University of Florida 2024 🐊", className="text-white", style={'font-style': 'italic'})
                            ]),
                            className="text-center",
                        ),
                    ],
                ),
            ],
            fluid=True,
        ),
        className="footer-styling bg-light-purple",
    )
    return ftr
