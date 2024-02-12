import dash
import dash_bootstrap_components as dbc

from dash import Dash, html

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL], use_pages=True)
app.title = 'RunTime'

app.layout = html.Div([
    html.Div(children='Hello World'),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)