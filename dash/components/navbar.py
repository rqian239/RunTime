import dash_bootstrap_components as dbc
import ids

def navbar_simple():
    link_style = {'color': 'white', 'font-size': '16px'}
    nav_items = [
        ("Home", "/", ids.NAVBAR_HOME_BUTTON),
        ("About", "/about", ids.NAVBAR_ABOUT_BUTTON),
        ("Teams", "/teams", ids.NAVBAR_TEAMS_BUTTON),
        ("Upcoming Games", "/upcominggames", ids.NAVBAR_UPCOMING_BUTTON),
        ("Fantasy Games", "/fantasygames", ids.NAVBAR_FANTASY_BUTTON),
    ]

    nav = dbc.NavbarSimple(
        children=[
            dbc.Col(
                dbc.NavItem(
                    dbc.NavLink(
                        label, 
                        href=link_href, 
                        style=link_style, 
                        id=button_id,
                        className="nav-link-custom"
                    ), 
                    style={'border-radius': '10px', 'margin-right': '10px'}
                ),
                width="auto"
            ) 
            for i, (label, link_href, button_id) in enumerate(nav_items)
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
