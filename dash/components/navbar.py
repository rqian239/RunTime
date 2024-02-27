# Navigation Bar Component

import dash_bootstrap_components as dbc

def navbar_simple():
    link_style = {'color': 'white'}
    nav_items = [
        ("Home", "/"),
        ("About", "/about"),
        ("Teams", "/teams"),
        ("Upcoming Games", "/upcominggames"),
        ("Fantasy Games", "/fantasygames"),
    ]

    nav = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(label, href=link_href, style=link_style)) for label, link_href in nav_items
        ],
        brand="RunTime 🏀",
        brand_href="/",
        sticky="top",
        color='dark',
        dark=True
    )

    return nav