
from dash import html, dcc
import dash_bootstrap_components as dbc
import base64
from funcs.get_card_values import get_card_values
from funcs.make_plot_infection_vaccination import make_plot_infection_vaccination

def content_page_world(
        df,
        opts_var_cases,
        opts_var_deaths,
        opts_var_vaccinated,
        opts_scales,
        country_codes
):
    """
    Make the content for the World page.
    param opts_var_cases:
    param opts_var_deaths:
    param opts_var_vaccinated:
    param opts_scales:
    param country_codes:
    return: pg
    """
    
    last_date = df.loc[df["location"] == "World", "date"].iloc[-1]
    last_date = last_date[8:10] + "/" + last_date[5:7] + "/" + last_date[0:4]
    last_date_world = "Dataset updated in " + last_date

    pg = [
        html.Div(
            [

                ### Cards

                # First row of info cards:
                dbc.Row(
                    [
                        # Card of total cases:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "cases_total",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_total_cases",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Cases",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "cases_total",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_total_cases_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of total deaths:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "deaths_total",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_total_deaths",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Deaths",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "deaths_total",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_total_deaths_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of fully vaccinated:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "vaccinated_fully",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_fully_vaccinated",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Fully Vaccinated",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "vaccinated_fully",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_fully_vaccinated_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of population:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "population",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_population",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Population",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "population",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_population_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        )
                    ],
                    className = "row-cards-info"
                ),
                # Second row of info cards:
                dbc.Row(
                    [
                        # Card of new cases:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "cases_new",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_new_cases",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "New Cases",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "cases_new",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_new_cases_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of new deaths:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "deaths_new",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_new_deaths",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "New Deaths",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "deaths_new",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_new_deaths_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of percent of fully vaccinated:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "vaccinated_fully_pct",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_pct_fully_vaccinated",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Percent of Fully Vaccinated",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "vaccinated_fully_pct",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_pct_fully_vaccinated_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        ),
                        # Card of GDP per capita:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "gdp_per_capita",
                                                            location_id = "",
                                                            location_type = "world")[0],
                                            id = "card_world_gdp_per_capita",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "GDP per capita",
                                            className = "card-info-footer"
                                        ),
                                        html.Div(
                                            get_card_values(df = df,
                                                            var = "gdp_per_capita",
                                                            location_id = "",
                                                            location_type = "world")[1],
                                            id = "card_world_gdp_per_capita_last_date",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 3
                        )
                    ],
                    className = "row-cards-info"
                ),
                # Date of last data and source:
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    last_date_world,
                                    id = "world_last_data_date",
                                    className = "last-data-date"
                                )
                            ],
                            width = 4,
                            className = "last-data-col"
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "Source: ",
                                            className = "data-source-name"
                                        ),
                                        html.A(
                                            "https://github.com/owid/covid-19-data/tree/master/public/data/",
                                            href = "https://github.com/owid/covid-19-data/tree/master/public/data/",
                                            className = "data-source-link"
                                        )
                                    ],
                                    className = "data-source"
                                )
                            ],
                            width = 8,
                            className = "data-source-col"
                        )
                    ],
                    className = "last-data-date-and-data-source"
                ),

                ### Plots

                dbc.Tabs(
                    [
                        # Time series:
                        dbc.Tab(
                            [
                                dbc.Row(
                                    [
                                        # Cases:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            "Cases",
                                                            className = "card-plot-header"
                                                        ),
                                                        # Variable:
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_world_time_series_cases",
                                                                        options = opts_var_cases,
                                                                        value = opts_var_cases[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        # Scale:
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_world_time_series_cases",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        # Plot:
                                                        dcc.Graph(
                                                            id = "plot_world_time_series_cases",
                                                            figure = {}
                                                        )
                                                    ],
                                                    className = "card-plot"
                                                )
                                            ],
                                            width = 4
                                        ),

                                        # Deaths:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            "Deaths",
                                                            className = "card-plot-header"
                                                        ),
                                                        # Variable:
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_world_time_series_deaths",
                                                                        options = opts_var_deaths,
                                                                        value = opts_var_deaths[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        # Scale:
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_world_time_series_deaths",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        # Plot:
                                                        dcc.Graph(
                                                            id = "plot_world_time_series_deaths",
                                                            figure = {}
                                                        )
                                                    ],
                                                    className = "card-plot"
                                                )
                                            ],
                                            width = 4
                                        ),

                                        # Vaccinated:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            "Vaccinated",
                                                            className = "card-plot-header"
                                                        ),
                                                        # Variable:
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_world_time_series_vaccinated",
                                                                        options = opts_var_vaccinated,
                                                                        value = opts_var_vaccinated[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        # Scale:
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_world_time_series_vaccinated",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        # Plot:
                                                        dcc.Graph(
                                                            id = "plot_world_time_series_vaccinated",
                                                            figure = {}
                                                        )
                                                    ],
                                                    className = "card-plot"
                                                )
                                            ],
                                            width = 4
                                        )
                                    ],
                                    className = "row-time-series"
                                )
                            ],
                            label = "Time Series",
                            className = "tab-time-series"
                        ),

                        # Infection x Vaccination:
                        dbc.Tab(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            id = "plot_world_infection_vaccination",
                                                            figure = make_plot_infection_vaccination(df = df,
                                                                                                     country_codes = country_codes)
                                                        )
                                                    ],
                                                    className = "card-plot"
                                                )
                                            ],
                                            width = 12
                                        )
                                    ],
                                    className = "row-infection-vaccination"
                                )
                            ],
                            label = "Infection x Vaccination",
                            className = "tab-infection-vaccination"
                        )
                    ],
                    className = "tabs-plots"
                )
            ],
            className = "generic-page"
        )
    ]

    return (pg)

