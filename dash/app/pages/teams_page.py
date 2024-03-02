import dash
from dash import html, dcc

dash.register_page(__name__, path='/teams')

about_box_style = {
    'border': '2px solid black',
    'padding': '10px',
    'width': 'calc(100% - 40px)', 
    'height': '100px',
    'background-color': 'darkred',
    'color': 'black',  
    'marginLeft': '20px', 
    'marginRight': '20px', 
    'marginTop': '40px',
    'gridColumn': '1 / -1'  
}

# Options for the dropdown
dropdown_options = [
    {'label': 'Option 1', 'value': 'option1'},
    {'label': 'Option 2', 'value': 'option2'},
    {'label': 'Option 3', 'value': 'option3'}
]

layout = html.Div(style={'height': '100vh'}, children=[
    html.H1('Teams Page', style={'textAlign': 'center'}),
    html.Div("This is a separate box", style=about_box_style ),
    dcc.Dropdown(
        id='team-dropdown',
        options=dropdown_options,
        value='option1',  # Default value
        style={'width': '50%', 'margin': '30px', 'marginTop': '20px', 'textAlign': 'left'}
    )
    
])
