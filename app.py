
#----------------------------------------------------------------------------------------------------------------------
################################################## Header #############################################################

# Paths:
path_data = "data/"
path_assets = "assets/"
path_figs = "figs/"

# Modules:
import numpy as np
import pandas as pd
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
from funcs.content_page_home import content_page_home
from funcs.content_page_table import content_page_table
from funcs.content_page_plots import content_page_plots

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)

#----------------------------------------------------------------------------------------------------------------------
#################################################### Data #############################################################





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

# Images for logo and tabs:
logo_filename = "dash_logo.png"
logo_image = base64.b64encode(open(logo_filename, "rb").read())
home_tab_filename = "home_tab.png"
home_tab_image = base64.b64encode(open(home_tab_filename, "rb").read())
table_tab_filename = "table_tab.png"
table_tab_image = base64.b64encode(open(table_tab_filename, "rb").read())
plots_tab_filename = "plots_tab.png"
plots_tab_image = base64.b64encode(open(plots_tab_filename, "rb").read())

# Top navbar:
top_navbar = dbc.Navbar(
    dbc.Container(
        [
            # Dashboard logo:
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src = "data:image/png;base64,{}".format(logo_image.decode()),
                                height = "60px"
                            )
                        )
                    ]
                )
            ),
            # Main navbar:
            dbc.Nav(
                [
                    # Home:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(home_tab_image.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Home",
                                        href = "/",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Table:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(table_tab_image.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Table",
                                        href = "/page_table",
                                        active = "exact"
                                    ),
                                    class_name = "card-tab-body"
                                )
                            ],
                            class_name = "card-tab-icon"
                        )
                    ),
                    # Plots:
                    dbc.NavItem(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src = "data:image/png;base64,{}".format(plots_tab_image.decode()),
                                    top = True,
                                    class_name = "tab-icon"
                                ),
                                dbc.CardBody(
                                    dbc.NavLink(
                                        "Plots",
                                        href = "/page_plots",
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
        return content_page_home()
    elif pathname == "/page_table":
        return content_page_table()
    elif pathname == "/page_plots":
        return content_page_plots()


#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

app.run_server(debug = True)

# if __name__ == "__main__":
#     app.run_server(debug = True)


