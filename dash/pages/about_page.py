import dash
import dash_bootstrap_components as dbc
from dash import html

# Register the page
dash.register_page(__name__, path='/about')

# Define the styles
about_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': '60%',  # Adjust width as needed
    'height': '300px',  # Adjust height as needed
    'background-color': 'darkred',
    'color': 'white',  # Change text color to white
    'margin': '40px auto',  # Centering the box horizontally with top margin
}

nba_colors = {
    'background': '#1A477B',  # Blue
    'text': '#FFFFFF'         # White
}

small_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': 'calc(20% - 20px)',  # Adjust width as needed for 5 columns
    'height': 'calc(25vh - 40px)',  # Adjust height as needed (25vh is a quarter of the viewport height)
    'background-color': nba_colors['background'],
    'color': nba_colors['text'],
    'margin': '10px 0 10px 10px',  # Margin between small boxes (added margin-left)
    'display': 'inline-block'  # Make small boxes appear side by side
}

# Creating 5 small blue cards using the provided card template
small_blue_cards = html.Div(
    [
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Primary card title", className="card-title"),
                html.P("info", className="card-text")
            ], className="card-body")
        ], className="card border-primary mb-3", style=small_box_style)
        for _ in range(5)
    ],
    style={'display': 'flex', 'justifyContent': 'space-between', 'width': '80%', 'margin': 'auto'}  # Adjust container width and center it horizontally
)

# Red card using the provided template
red_card = html.Div(
    [
        html.Div([
            html.Div("Header", className="card-header"),
            html.Div([
                html.H4("Secondary card title", className="card-title"),
                html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text")
            ], className="card-body")
        ], className="card border-secondary mb-3", style={'maxWidth': '100rem', 'height': '400px', 'backgroundColor': 'darkred', 'color': 'white', 'margin': '40px auto 0', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'})  # Adjust height and width here
    ]
)

# Define the layout
layout = html.Div(style={'height': '100vh', 'background-color': 'black', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
    html.H1('This is the About Page', style={'textAlign': 'center', 'color': 'white', 'marginTop': '50px', 'fontWeight': 'bold'}),  # Adding fontWeight for boldness
    red_card,
    small_blue_cards
])
