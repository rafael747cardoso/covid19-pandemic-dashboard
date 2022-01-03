
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Paths:
path_data = "data/"
path_assets = "assets/"
path_figs = "figs/"

# Modules:
import numpy as np
import pandas as pd
from datetime import datetime
import datatable as dt
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px
import plotly.graph_objects as go
import operator
from dash import Dash, dcc, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import base64
from scipy.stats import skew
import re

from funcs.get_data import get_data
from funcs.content_page_world import content_page_world
from funcs.content_page_continent import content_page_continent
from funcs.content_page_country import content_page_country
from funcs.content_page_map import content_page_map

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)

#----------------------------------------------------------------------------------------------------------------------
#################################################### ETL ##############################################################

# Data extraction from source:
df = get_data()


# Selects's options:
df_countries = df[df["iso_code"].str.contains("OWID") == False]
country_names = df_countries["location"].unique().tolist()
country_codes = df_countries["iso_code"].unique().tolist()
opts_countries = [{"label": country_names[i], "value": country_codes[i]} for i in range(len(country_names))]



#----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ##########################################################

app = Dash(
    name = __name__,
    external_stylesheets = [path_assets + "bootstrap.css"],
    suppress_callback_exceptions = True
)
server = app.server

#----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ##########################################################






#----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ###########################################################

# Load the icons:
icons = "figs/icons/"
icon_logo = base64.b64encode(open(icons + "icon_logo.png", "rb").read())
icon_world = base64.b64encode(open(icons + "icon_world.png", "rb").read())
icon_continent = base64.b64encode(open(icons + "icon_continent.png", "rb").read())
icon_country = base64.b64encode(open(icons + "icon_country.png", "rb").read())
icon_map = base64.b64encode(open(icons + "icon_map.png", "rb").read())

# Top navbar:
top_navbar = dbc.Navbar(
    dbc.Container(
        [
            # Dashboard logo:
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        html.Img(
                                            src = "data:image/png;base64,{}".format(icon_logo.decode()),
                                            height = "100px"
                                        ),
                                        html.H2(
                                            "Covid-19 Evolution",
                                            style = {"padding-top": "25px"}
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
            # Main navbar:
            dbc.Nav(
                [
                    # Page World:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(icon_world.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "World",
                                        href = "/page_world",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Page Continent:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(icon_continent.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Continent",
                                        href = "/page_continent",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Page Country:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(icon_country.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Country",
                                        href = "/page_country",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Page Map:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(icon_map.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Map",
                                        href = "/page_map",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    )
                ],
                navbar = True
            )
        ],
        class_name = "my-navbar"
    ),
    color = "#0D0629"
)

# Layout:
app.layout = html.Div(
    [
        dcc.Location(
            id = "url"
        ),
        top_navbar,
        html.Div(
            children = [],
            id = "page-content"
        )
    ]
)

# Make the pages:
@app.callback(
    Output(component_id = "page-content", component_property = "children"),
    [Input(component_id = "url", component_property = "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return content_page_world()
    elif pathname == "/page_world":
        return content_page_world()
    elif pathname == "/page_continent":
        return content_page_continent()
    elif pathname == "/page_country":
        return content_page_country(opts_countries = opts_countries)
    elif pathname == "/page_map":
        return content_page_map()


#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

app.run_server(debug = True)

# if __name__ == "__main__":
#     app.run_server(debug = True)


