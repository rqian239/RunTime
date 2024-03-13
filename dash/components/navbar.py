import dash_bootstrap_components as dbc
import ids

def navbar_simple():
    link_style = {'color': 'white', 'font-size': '16px'}
    nav_items = [
        ("Home", "/", "primary"),
        ("About", "/about", "primary"),
        ("Teams", "/teams", "primary"),
        ("Upcoming Games", "/upcominggames", "primary"),
        ("Fantasy Games", "/fantasygames", "primary"),
    ]

    nav = dbc.NavbarSimple(
        children=[
            dbc.Col(
                dbc.NavItem(
                    dbc.NavLink(
                        label, 
                        href=link_href, 
                        style=link_style, 
                        className="nav-link-custom"
                    ), 
                    style={'border-radius': '10px', 'margin-right': '10px'}
                ),
                width="auto"
            ) 
            for i, (label, link_href, _) in enumerate(nav_items)
        ],
        brand="RunTime 🏀",
        brand_href="/",
        sticky="top",
        color='dark',
        dark=True,
        style={'padding': '10px', 'border-radius': '10px'},
        id=ids.NAVBAR
    )

    return nav
