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
                                html.H4("Quick Links", className="text-uppercase"),
                                # html.Div([
                                #     dbc.NavLink("Home", href="/", className="footer-link d-inline-flex"),
                                #     dbc.NavLink("About", href="/about", className="footer-link d-inline-flex"),
                                #     dbc.NavLink("Teams", href="/teams", className="footer-link d-inline-flex"),
                                #     dbc.NavLink("Upcoming Games", href="/upcominggames", className="footer-link d-inline-flex"),
                                #     dbc.NavLink("Fantasy Games", href="/fantasygames", className="footer-link d-inline-flex")
                                # ], className="d-flex flex-row justify-content-around"),  # Adjust justify-content as needed
                            ]),
                            class_name="text-center mt-3"
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(dbc.Button("Home", href="/", class_name="btn-link")),
                        dbc.Col(dbc.Button("About", href="/about", class_name="btn-link")),
                        dbc.Col(dbc.Button("Teams", href="/teams", class_name="btn-link")),
                        dbc.Col(dbc.Button("Upcoming Games", href="/upcominggames", class_name="btn-link")),
                        dbc.Col(dbc.Button("Fantasy Games", href="/fantasygames", class_name="btn-link")),
                    ],
                    class_name="text-center g-1 mb-4"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.H5("Created by the Runtime Terrors", className="text-center text-italic"),
                            ]),
                        ),
                    ],
                    # className="my-2",
                ),
                dbc.Row(
                    [
                        # dbc.Col(
                        #     html.Div([
                        #         html.H5("Quick Links", className="text-uppercase"),
                        #         dbc.NavLink("Home", href="/", className="footer-link"),
                        #         dbc.NavLink("About", href="/about", className="footer-link"),
                        #         dbc.NavLink("Teams", href="/teams", className="footer-link"),
                        #         dbc.NavLink("Upcoming Games", href="/upcominggames", className="footer-link"),
                        #         dbc.NavLink("Fantasy Games", href="/fantasygames", className="footer-link")
                        #     ]),
                        #     className="centered"
                        # ),
                        dbc.Col(
                            html.Div([
                                html.P("Nikitha Chintalapati, Ria Gandhi, Bryan Hernandez-Sanchez, Nivedha Natarajan, Richard Qian", className="mb-2"),
                                html.P("University of Florida 2024 🐊")
                            ]),
                            className="text-center text-italic",
                        ),
                    ],
                ),
            ],
            fluid=True,
        ),
        className="footer-styling",
    )
    return ftr
