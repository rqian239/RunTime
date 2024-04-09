import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from data.nba_teams import get_all_team_options
from components.navbar import navbar_simple
from components.footer import footer
import ids


dash.register_page(__name__, path='/about')  # Change the path here

# Navbar and footer imported here
nav = navbar_simple()
ftr = footer()
image_path = "/assets/images/nivedha.jpeg"
image_path2 = "/assets/images/ria.jpg"
image_path3 = "/assets/images/richard.jpg"
image_path4 = "/assets/images/bryan.jpg"
image_path5 = "/assets/images/nikki.jpg"

# Define the layout for the page
body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("About Us", className="team-page-title", style={'textAlign': 'center'}),
                        html.Br(),
                        html.P(
                            """\
                           Thank you for visiting our About Us page. Here, we'd like to introduce you to the team behind our project 
                           and provide insights into our mission and vision. Get to know the talented individuals who have contributed 
                           their expertise and passion to make this project possible.
                            """,
                            style={'textAlign': 'center'}
                        ),
                    ],
                    width=12  # Full width for this column
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(width=100),  # Empty column to occupy space
            ]
        ),
        dbc.Row(
            [
                # Adding a new row for small cards
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Front-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Nivedha Natarajan", className="card-title"),
                                        html.Img(src=image_path, alt="Nivedha Natarajan", className="card-img-top"),

                                    
            
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Front-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Nikitha Chintalapati", className="card-title"),
                                        html.Img(src=image_path5, alt="Nikitha Chintalapai", className="card-img-top"),


                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Bryan Hernandez", className="card-title"),
                                        html.Img(src=image_path4, alt="Bryan Hernandez", className="card-img-top"),

                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Ria Manoj Gandhi", className="card-title"),
                                        html.Img(src=image_path2, alt="Ria Manoj Gandhi", className="card-img-top"),

                                        
                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                ),
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Back-End Developer"),
                                dbc.CardBody(
                                    [
                                        html.H4("Richard Qian", className="card-title"),
                                        html.Img(src=image_path3, alt="Richard Qian", className="card-img-top"),

                                    ]
                                )
                            ],
                            className="border-primary mb-3",
                            style={"maxWidth": "20rem", "width": "auto", "margin": "auto"}  # Adjust the maxWidth and width here
                        ),
                    ],
                    width=2,  # Adjusted width for this column
                    align='center'  # Center align the column content
                )
            ],
            justify="center"  # Center align the row
        ),
        dbc.Row(
    [
        # Adding the first card with dropdown
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Nivedha Natarajan"),
                        dbc.CardBody(
                            [
                                html.P(
                                    """
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. 
                                    Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. 
                                    Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris 
                                    massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent 
                                    per conubia nostra, per inceptos himenaeos.
                                    """,
                                    className="card-text"
                                )
                            ]
                        )
                    ],
                    className="card text-white bg-primary mb-3",
                    style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                ),
            ],
            width=15,  # 100% width for this column
            align='center'  # Center align the column content
        )
    ],
    justify="center"  # Center align the row
),
dbc.Row(
    [
        # Adding the first card with dropdown
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Nikitha Chintalapati"),
                        dbc.CardBody(
                            [
                                html.P(
                                    """
                                    Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. 
                                    Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed 
                                    convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus 
                                    risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula 
                                    lacinia aliquet. Mauris ipsum.
                                    """,
                                    className="card-text"
                                )
                            ]
                        )
                    ],
                    className="card text-white bg-primary mb-3",
                    style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                ),
            ],
            width=15,  # 100% width for this column
            align='center'  # Center align the column content
        )
    ],
    justify="center"  # Center align the row
),
dbc.Row(
    [
        # Adding the first card with dropdown
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Bryan Hernandez"),
                        dbc.CardBody(
                            [
                                html.P(
                                    """
                                    Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat 
                                    condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, 
                                    per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor 
                                    neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. 
                                    Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. 
                                    Proin quam. Etiam ultrices.
                                    """,
                                    className="card-text"
                                )
                            ]
                        )
                    ],
                    className="card text-white bg-primary mb-3",
                    style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                ),
            ],
            width=15,  # 100% width for this column
            align='center'  # Center align the column content
        )
    ],
    justify="center"  # Center align the row
),
dbc.Row(
    [
        # Adding the first card with dropdown
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Ria Manoj Gandhi"),
                        dbc.CardBody(
                            [
                                html.P(
                                    """
                                    Suspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus 
                                    magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum 
                                    magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices 
                                    posuere cubilia Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. 
                                    In vel mi sit amet augue congue elementum. Morbi in ipsum sit amet pede facilisis laoreet. 
                                    Donec lacus nunc, viverra nec, blandit vel, egestas et, augue. Vestibulum tincidunt 
                                    malesuada tellus. Ut ultrices ultrices enim.
                                    """,
                                    className="card-text"
                                )
                            ]
                        )
                    ],
                    className="card text-white bg-primary mb-3",
                    style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                ),
            ],
            width=15,  # 100% width for this column
            align='center'  # Center align the column content
        )
    ],
    justify="center"  # Center align the row
),
dbc.Row(
    [
        # Adding the first card with dropdown
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Richard Qian"),
                        dbc.CardBody(
                            [
                                html.P(
                                    """
                                    Curabitur sit amet mauris. Morbi in dui quis est pulvinar ullamcorper. Nulla facilisi. 
                                    Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a tortor. Integer 
                                    id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices 
                                    sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. Vestibulum 
                                    nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan porttitor, 
                                    cursus quis, aliquet eget, justo.
                                    """,
                                    className="card-text"
                                )
                            ]
                        )
                    ],
                    className="card text-white bg-primary mb-3",
                    style={"maxWidth": "80rem", "width": "100%", "margin": "auto"}  # Adjust the maxWidth and width here
                ),
            ],
            width=15,  # 100% width for this column
            align='center'  # Center align the column content
        )
    ],
    justify="center"  # Center align the row
)
    ],
    class_name="body-flex-wrapper",
)

# Assign the layout to the specific path
layout = layout = html.Div([nav, body, ftr], className="make-footer-stick")
