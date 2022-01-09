
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
from funcs.get_card_values import get_card_values
from funcs.make_plot_time_series import make_plot_time_series
from funcs.make_plot_trajectories import make_plot_trajectories

# Display options:
pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 300)
pd.set_option("display.max_rows", 300)

#----------------------------------------------------------------------------------------------------------------------
#################################################### ETL ##############################################################

# Data extraction from source:
df = get_data()

# Select options:
df_countries = df[df["iso_code"].str.contains("OWID") == False]
country_names = df_countries["location"].unique().tolist()
country_codes = df_countries["iso_code"].unique().tolist()
opts_countries = [{"label": country_names[i], "value": country_codes[i]} for i in range(len(country_names))]
opts_var_cases = [
    {"label": "Total Cases", "value": "cases_total"},
    {"label": "New Cases", "value": "cases_new"},
    {"label": "New Cases (smoothed)", "value": "cases_new_smoothed"},
    {"label": "Total Cases per million", "value": "cases_total_per_million"},
    {"label": "New Cases per million", "value": "cases_new_per_million"},
    {"label": "New Cases per million (smoothed)", "value": "cases_new_smoothed_per_million"}
]
opts_var_deaths = [
    {"label": "Total Deaths", "value": "deaths_total"},
    {"label": "New Deaths", "value": "deaths_new"},
    {"label": "New Deaths (smoothed)", "value": "deaths_new_smoothed"},
    {"label": "Total Deaths per million", "value": "deaths_total_per_million"},
    {"label": "New Deaths per million", "value": "deaths_new_per_million"},
    {"label": "New Deaths per million (smoothed)", "value": "deaths_new_smoothed_per_million"}
]
opts_var_vaccinated = [
    {"label": "Vaccinated", "value": "vaccinated"},
    {"label": "Fully Vaccinated", "value": "vaccinated_fully"},
    {"label": "Percent of Vaccinated", "value": "vaccinated_pct"},
    {"label": "Percent of Fully Vaccinated", "value": "vaccinated_fully_pct"}
]
opts_scales = [
    {"label": "Linear", "value": "linear"},
    {"label": "Log10", "value": "log"}
]
opts_var_trajectories = [
    {"label": "Cases", "value": "cases"},
    {"label": "Deaths", "value": "deaths"}
]
opts_mov_avg_period = [
    {"label": "1 day", "value": "1"},
    {"label": "7 days", "value": "7"},
    {"label": "14 days", "value": "14"},
    {"label": "30 days", "value": "30"}
]
continents = df["continent"].dropna().unique().tolist()
continents.sort()
opts_continents = [{"label": i, "value": i} for i in continents]



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

############ World

###### Plots

### Time Series

# Cases:
@app.callback(
    Output(component_id = "plot_world_time_series_cases", component_property = "figure"),
    [
        Input(component_id = "chosen_var_world_time_series_cases", component_property = "value"),
        Input(component_id = "chosen_scale_world_time_series_cases", component_property = "value")
    ]
)
def update_plot_world_time_series_cases(var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = "World",
                                 location_type = "world",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_cases))

# Deaths:
@app.callback(
    Output(component_id = "plot_world_time_series_deaths", component_property = "figure"),
    [
        Input(component_id = "chosen_var_world_time_series_deaths", component_property = "value"),
        Input(component_id = "chosen_scale_world_time_series_deaths", component_property = "value")
    ]
)
def update_plot_world_time_series_deaths(var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = "World",
                                 location_type = "world",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_deaths))

# Vaccinated:
@app.callback(
    Output(component_id = "plot_world_time_series_vaccinated", component_property = "figure"),
    [
        Input(component_id = "chosen_var_world_time_series_vaccinated", component_property = "value"),
        Input(component_id = "chosen_scale_world_time_series_vaccinated", component_property = "value")
    ]
)
def update_plot_world_time_series_vaccinated(var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = "World",
                                 location_type = "world",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_vaccinated))

############ Continent

###### Flag

# Image of the country's flag:
@app.callback(
    Output(component_id = "continent_flag", component_property = "src"),
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_continent_flag(continent_name):
    try:
        flag_continent = base64.b64encode(open("figs/flags/" + continent_name + ".png", "rb").read())
        flag_continent_encoded = "data:image/png;base64,{}".format(flag_continent.decode())
        return (flag_continent_encoded)
    except (Exception,):
        return("")

###### Cards

# Card continent total cases:
@app.callback(
    [
        Output(component_id = "card_continent_total_cases", component_property = "children"),
        Output(component_id = "card_continent_total_cases_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_total_cases(continent_name):
    return(get_card_values(df = df,
                           var = "cases_total",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent total deaths:
@app.callback(
    [
        Output(component_id = "card_continent_total_deaths", component_property = "children"),
        Output(component_id = "card_continent_total_deaths_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_total_deaths(continent_name):
    return(get_card_values(df = df,
                           var = "deaths_total",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent fully vaccinated:
@app.callback(
    [
        Output(component_id = "card_continent_fully_vaccinated", component_property = "children"),
        Output(component_id = "card_continent_fully_vaccinated_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_fully_vaccinated(continent_name):
    return(get_card_values(df = df,
                           var = "vaccinated_fully",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent population:
@app.callback(
    [
        Output(component_id = "card_continent_population", component_property = "children"),
        Output(component_id = "card_continent_population_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_population(continent_name):
    return(get_card_values(df = df,
                           var = "population",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent new cases:
@app.callback(
    [
        Output(component_id = "card_continent_new_cases", component_property = "children"),
        Output(component_id = "card_continent_new_cases_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_new_cases(continent_name):
    return(get_card_values(df = df,
                           var = "cases_new",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent new deaths:
@app.callback(
    [
        Output(component_id = "card_continent_new_deaths", component_property = "children"),
        Output(component_id = "card_continent_new_deaths_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_new_deaths(continent_name):
    return(get_card_values(df = df,
                           var = "deaths_new",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent percent of fully vaccinated:
@app.callback(
    [
        Output(component_id = "card_continent_pct_fully_vaccinated", component_property = "children"),
        Output(component_id = "card_continent_pct_fully_vaccinated_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_pct_fully_vaccinated(continent_name):
    return(get_card_values(df = df,
                           var = "vaccinated_fully_pct",
                           location_id = continent_name,
                           location_type = "continent"))

# Card continent gdp_per_capita:
@app.callback(
    [
        Output(component_id = "card_continent_gdp_per_capita", component_property = "children"),
        Output(component_id = "card_continent_gdp_per_capita_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_card_continent_gdp_per_capita(continent_name):
    return(get_card_values(df = df,
                           var = "gdp_per_capita",
                           location_id = continent_name,
                           location_type = "continent"))

# Last data date:
@app.callback(
    Output(component_id = "continent_last_data_date", component_property = "children"),
    [
        Input(component_id = "chosen_continent", component_property = "value")
    ]
)
def update_continent_last_data_date(continent_name):
    last_date = df.loc[df["location"] == continent_name, "date"].iloc[-1]
    last_date = last_date[8:10] + "/" + last_date[5:7] + "/" + last_date[0:4]
    last_date = "Dataset updated in " + last_date
    return(last_date)

###### Plots

### Time Series

# Cases:
@app.callback(
    Output(component_id = "plot_continent_time_series_cases", component_property = "figure"),
    [
        Input(component_id = "chosen_continent", component_property = "value"),
        Input(component_id = "chosen_var_continent_time_series_cases", component_property = "value"),
        Input(component_id = "chosen_scale_continent_time_series_cases", component_property = "value")
    ]
)
def update_plot_continent_time_series_cases(continent_name, var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = continent_name,
                                 location_type = "continent",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_cases))

# Deaths:
@app.callback(
    Output(component_id = "plot_continent_time_series_deaths", component_property = "figure"),
    [
        Input(component_id = "chosen_continent", component_property = "value"),
        Input(component_id = "chosen_var_continent_time_series_deaths", component_property = "value"),
        Input(component_id = "chosen_scale_continent_time_series_deaths", component_property = "value")
    ]
)
def update_plot_continent_time_series_deaths(continent_name, var, scale):
    return(make_plot_time_series(df = df,
                                         location_id = continent_name,
                                         location_type = "continent",
                                         var = var,
                                         scale = scale,
                                         opts_var = opts_var_deaths))

# Vaccinated:
@app.callback(
    Output(component_id = "plot_continent_time_series_vaccinated", component_property = "figure"),
    [
        Input(component_id = "chosen_continent", component_property = "value"),
        Input(component_id = "chosen_var_continent_time_series_vaccinated", component_property = "value"),
        Input(component_id = "chosen_scale_continent_time_series_vaccinated", component_property = "value")
    ]
)
def update_plot_continent_time_series_vaccinated(continent_name, var, scale):
    return(make_plot_time_series(df = df,
                                         location_id = continent_name,
                                         location_type = "continent",
                                         var = var,
                                         scale = scale,
                                         opts_var = opts_var_vaccinated))

### Trajectories

@app.callback(
    Output(component_id = "plot_continent_trajectories", component_property = "figure"),
    [
        Input(component_id = "chosen_var_continent_trajectories", component_property = "value"),
        Input(component_id = "chosen_mov_avg_period_continent_trajectories", component_property = "value"),
        Input(component_id = "chosen_continents_continent_trajectories", component_property = "value"),
        Input(component_id = "chosen_scale_continent_trajectories", component_property = "value")
    ]
)
def update_plot_continent_time_series_vaccinated(var, mov_avg_period, continents_names, scale):
    return(make_plot_trajectories(df = df,
                                  var = var,
                                  mov_avg_period = mov_avg_period,
                                  locations_id = continents_names,
                                  locations_type = "continent",
                                  scale = scale,
                                  opts_var = opts_var_trajectories))

############ Country

###### Flag

# Image of the country's flag:
@app.callback(
    Output(component_id = "country_flag", component_property = "src"),
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_country_flag(country_code):
    try:
        flag_country = base64.b64encode(open("figs/flags/" + country_code + ".gif", "rb").read())
        flag_country_encoded = "data:image/png;base64,{}".format(flag_country.decode())
        return (flag_country_encoded)
    except (Exception,):
        return("")

###### Cards

# Card country total cases:
@app.callback(
    [
        Output(component_id = "card_country_total_cases", component_property = "children"),
        Output(component_id = "card_country_total_cases_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_total_cases(country_code):
    return(get_card_values(df = df,
                           var = "cases_total",
                           location_id = country_code,
                           location_type = "country"))

# Card country total deaths:
@app.callback(
    [
        Output(component_id = "card_country_total_deaths", component_property = "children"),
        Output(component_id = "card_country_total_deaths_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_total_deaths(country_code):
    return(get_card_values(df = df,
                           var = "deaths_total",
                           location_id = country_code,
                           location_type = "country"))

# Card country fully vaccinated:
@app.callback(
    [
        Output(component_id = "card_country_fully_vaccinated", component_property = "children"),
        Output(component_id = "card_country_fully_vaccinated_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_fully_vaccinated(country_code):
    return(get_card_values(df = df,
                           var = "vaccinated_fully",
                           location_id = country_code,
                           location_type = "country"))

# Card country population:
@app.callback(
    [
        Output(component_id = "card_country_population", component_property = "children"),
        Output(component_id = "card_country_population_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_population(country_code):
    return(get_card_values(df = df,
                           var = "population",
                           location_id = country_code,
                           location_type = "country"))

# Card country new cases:
@app.callback(
    [
        Output(component_id = "card_country_new_cases", component_property = "children"),
        Output(component_id = "card_country_new_cases_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_new_cases(country_code):
    return(get_card_values(df = df,
                           var = "cases_new",
                           location_id = country_code,
                           location_type = "country"))

# Card country new deaths:
@app.callback(
    [
        Output(component_id = "card_country_new_deaths", component_property = "children"),
        Output(component_id = "card_country_new_deaths_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_new_deaths(country_code):
    return(get_card_values(df = df,
                           var = "deaths_new",
                           location_id = country_code,
                           location_type = "country"))

# Card country percent of fully vaccinated:
@app.callback(
    [
        Output(component_id = "card_country_pct_fully_vaccinated", component_property = "children"),
        Output(component_id = "card_country_pct_fully_vaccinated_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_pct_fully_vaccinated(country_code):
    return(get_card_values(df = df,
                           var = "vaccinated_fully_pct",
                           location_id = country_code,
                           location_type = "country"))

# Card country gdp_per_capita:
@app.callback(
    [
        Output(component_id = "card_country_gdp_per_capita", component_property = "children"),
        Output(component_id = "card_country_gdp_per_capita_last_date", component_property = "children"),
    ],
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_card_country_gdp_per_capita(country_code):
    return(get_card_values(df = df,
                           var = "gdp_per_capita",
                           location_id = country_code,
                           location_type = "country"))

# Last data date:
@app.callback(
    Output(component_id = "country_last_data_date", component_property = "children"),
    [
        Input(component_id = "chosen_country", component_property = "value")
    ]
)
def update_country_last_data_date(country_code):
    last_date = df.loc[df["iso_code"] == country_code, "date"].iloc[-1]
    last_date = last_date[8:10] + "/" + last_date[5:7] + "/" + last_date[0:4]
    last_date = "Dataset updated in " + last_date
    return(last_date)

###### Plots

### Time Series

# Cases:
@app.callback(
    Output(component_id = "plot_country_time_series_cases", component_property = "figure"),
    [
        Input(component_id = "chosen_country", component_property = "value"),
        Input(component_id = "chosen_var_country_time_series_cases", component_property = "value"),
        Input(component_id = "chosen_scale_country_time_series_cases", component_property = "value")
    ]
)
def update_plot_country_time_series_cases(country_code, var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = country_code,
                                 location_type = "country",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_cases))

# Deaths:
@app.callback(
    Output(component_id = "plot_country_time_series_deaths", component_property = "figure"),
    [
        Input(component_id = "chosen_country", component_property = "value"),
        Input(component_id = "chosen_var_country_time_series_deaths", component_property = "value"),
        Input(component_id = "chosen_scale_country_time_series_deaths", component_property = "value")
    ]
)
def update_plot_country_time_series_deaths(country_code, var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = country_code,
                                 location_type = "country",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_deaths))

# Vaccinated:
@app.callback(
    Output(component_id = "plot_country_time_series_vaccinated", component_property = "figure"),
    [
        Input(component_id = "chosen_country", component_property = "value"),
        Input(component_id = "chosen_var_country_time_series_vaccinated", component_property = "value"),
        Input(component_id = "chosen_scale_country_time_series_vaccinated", component_property = "value")
    ]
)
def update_plot_country_time_series_vaccinated(country_code, var, scale):
    return(make_plot_time_series(df = df,
                                 location_id = country_code,
                                 location_type = "country",
                                 var = var,
                                 scale = scale,
                                 opts_var = opts_var_vaccinated))

### Trajectories

@app.callback(
    Output(component_id = "plot_country_trajectories", component_property = "figure"),
    [
        Input(component_id = "chosen_var_country_trajectories", component_property = "value"),
        Input(component_id = "chosen_mov_avg_period_country_trajectories", component_property = "value"),
        Input(component_id = "chosen_countries_country_trajectories", component_property = "value"),
        Input(component_id = "chosen_scale_country_trajectories", component_property = "value")
    ]
)
def update_plot_country_time_series_vaccinated(var, mov_avg_period, countries_codes, scale):
    return(make_plot_trajectories(df = df,
                                  var = var,
                                  mov_avg_period = mov_avg_period,
                                  locations_id = countries_codes,
                                  locations_type = "country",
                                  scale = scale,
                                  opts_var = opts_var_trajectories))

############ Map








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
        return content_page_world(df = df,
                                  opts_var_cases = opts_var_cases,
                                  opts_var_deaths = opts_var_deaths,
                                  opts_var_vaccinated = opts_var_vaccinated,
                                  opts_scales = opts_scales,
                                  country_codes = country_codes)
    elif pathname == "/page_world":
        return content_page_world(df = df,
                                  opts_var_cases = opts_var_cases,
                                  opts_var_deaths = opts_var_deaths,
                                  opts_var_vaccinated = opts_var_vaccinated,
                                  opts_scales = opts_scales,
                                  country_codes = country_codes)
    elif pathname == "/page_continent":
        return content_page_continent(opts_continents = opts_continents,
                                      opts_var_cases = opts_var_cases,
                                      opts_var_deaths = opts_var_deaths,
                                      opts_var_vaccinated = opts_var_vaccinated,
                                      opts_scales = opts_scales,
                                      opts_var_trajectories = opts_var_trajectories,
                                      opts_mov_avg_period = opts_mov_avg_period)
    elif pathname == "/page_country":
        return content_page_country(opts_countries = opts_countries,
                                    opts_var_cases = opts_var_cases,
                                    opts_var_deaths = opts_var_deaths,
                                    opts_var_vaccinated = opts_var_vaccinated,
                                    opts_scales = opts_scales,
                                    opts_var_trajectories = opts_var_trajectories,
                                    opts_mov_avg_period = opts_mov_avg_period)
    elif pathname == "/page_map":
        return content_page_map()


#----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard ######################################################

app.run_server(debug = True)

# if __name__ == "__main__":
#     app.run_server(debug = True)


