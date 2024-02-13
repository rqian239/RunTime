# Main entry point for Dash

import dash
import dash_bootstrap_components as dbc

from dash import Dash, html
from components.navbar import navbar_simple

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL], use_pages=True)
app.title = 'RunTime'

nav = navbar_simple()

app.layout = html.Div([
    html.Div([nav]),        # This will show up for each page
    dash.page_container     # Page specific layouts
])

if __name__ == '__main__':
    app.run(debug=True)