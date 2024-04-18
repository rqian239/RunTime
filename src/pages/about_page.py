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
                                        html.H4("Ria Gandhi", className="card-title"),
                                        html.Img(src=image_path2, alt="Ria Gandhi", className="card-img-top"),

                                        
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
                                    Hello, I'm Nivedha Natarajan, a Front-End Developer on our project team. I am a 4th year Computer 
                                    Science student. My focus on web development and design has allowed me to deepen my understanding of implementing frontend solutions 
                                    for full-stack applications. I've enjoyed the opportunity to enhance my skills in this area and 
                                    contribute to our project's success.
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
                                    My name is Nikitha Chintalapati and I am a 4th-year Computer Science major with a minor in 
                                    Digital Arts and Sciences. I have a wide skillset ranging from Software Engineering to Game Design, and I love 
                                    showcasing my skills through different opportunities that allow me to be creative. In my free time, I enjoy exploring the intersection 
                                    of technology and art, experimenting with new software tools and techniques to push the boundaries of what's possible. Whether it's 
                                    coding a new algorithm or mastering a new design tool, I'm always eager to expand my knowledge and refine my skills.
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
                                    Hello, my name is Bryan Hernandez-Sanchez and I am a 4th year computer science student at The 
                                    University of Florida! I'm originally from Miami, Florida and I am one of Runtime's Backend 
                                    developers. I agreed to work on Runtime because of the massive sports-betting craze that has 
                                    been happening all around campus, and I wanted to see if I can help garner more attention to it 
                                    via our prediction model and website! 

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
                                    Hi there, I'm Ria, currently pursuing a major in Computer Science with a minor in Engineering Innovation.
                                    Fueled by interest in the intersection of business and technology, I have experience in both research and 
                                    a software engineering internship. Combining my passion for sports, I ideated an innovative service tailored 
                                    for college student-athletes during an entrepreneurship class at UF. Currently, my interest lies in exploring 
                                    ERP software and other cutting-edge business technologies.
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
                                    Hello, my name is Richard, and I am a CS major and Math minor here at UF! I am a huge Toronto Raptors
                                    fan and, overall, a big fan of basketball. Python is also one of my favorite programming languages, 
                                    which is used extensively in this project. I am also interested in data analytics, statistical modeling, 
                                    and data visualization.
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
