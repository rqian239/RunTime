# This is an initial attempt at implementing e2e testing with this dash app
# IT CURRENTLY DOES NOT WORK!

from dash.testing.application_runners import import_app

import app.ids as ids

def test_layout(dash_duo):
    app = import_app("../app/dash_app.py")  # Import dash app
    dash_duo.start_server(app)
    assert dash_duo.find_element(f"#{ids.NAVBAR}")  # Check the navbar is there
