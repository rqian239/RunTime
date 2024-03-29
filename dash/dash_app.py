# Main entry point for Dash

# COMMENT THIS OUT FOR NOW - this section is no longer needed since I deleted the "app" directory
# # --------------------------------------------------------
# import sys
# from pathlib import Path


# # This is needed so that imports work in this project
# # Not best practice but it makes files within the dash/ directory visible by Python interpreter

# src_dir = Path(__file__).resolve().parent.parent
# # print(src_dir)
# sys.path.append(str(src_dir))
# # --------------------------------------------------------

import dash
import dash_bootstrap_components as dbc

from dash import Dash, html
from components.navbar import navbar_simple
from components.footer import footer

# Define the app here and choose the DBC theme
# Themes listed here: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR], use_pages=True)
app.title = 'RunTime'

nav = navbar_simple()
foo = footer()

colors = {
    #'background': '#FFFFFF',  # Light purple, reminiscent of basketball courts
    #'text': '#FF5733'         # Vibrant orange, representing the basketball
}

app.layout = html.Div(style={'margin': '0', 'padding': '0', 'font-family': 'Arial, sans-serif'}, children=[
    html.Div([nav]),        # This will show up for each page
    dash.page_container,    # Page specific layouts
    html.Div(foo)
])

if __name__ == '__main__':
    app.run(debug=True)