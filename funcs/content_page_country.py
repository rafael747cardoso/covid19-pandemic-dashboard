
from dash import html, dcc
import dash_bootstrap_components as dbc

def content_page_country(
    opts_countries,
    opts_var_cases,
    opts_var_deaths,
    opts_var_vaccinated,
    opts_scales,
    opts_var_trajectories,
    opts_mov_avg_period
):
    """
    Make the content for the Country page.
    param opts_countries:
    param opts_var_cases:
    param opts_scales:
    param opts_var_trajectories:
    param opts_mov_avg_period:
    return: pg
    """

    pg = [
        html.Div(
            [
                ### Select the country
                
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    "Choose the country",
                                    className = "filter-title"
                                ),
                                dbc.Select(
                                    id = "chosen_country",
                                    options = opts_countries,
                                    value = opts_countries[0]["value"]
                                )
                            ],
                            width = 4
                        )
                    ],
                    className = "my-select"
                ),

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
                                            [],
                                            id = "card_country_total_cases",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Cases",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
                        ),
                        # Card of total deaths:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "10000000",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Deaths",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
                        ),
                        # Card of fully vaccinated:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "2000000000",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Total Fully Vaccinated",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
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
                                            "100000",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "New Cases",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
                        ),
                        # Card of new deaths:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "10000",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "New Deaths",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
                        ),
                        # Card of percent of fully vaccinated:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "42" + " %",
                                            className = "card-info-body"
                                        ),
                                        html.Div(
                                            "Percent of Fully Vaccinated",
                                            className = "card-info-footer"
                                        ),
                                    ],
                                    className = "card-info"
                                )
                            ],
                            width = 4
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
                                    [],
                                    id = "last_data_date",
                                    className = "last-data-date"
                                ),
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
                            width = 12
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
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_country_time_series_cases",
                                                                        options = opts_var_cases,
                                                                        value = opts_var_cases[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_country_time_series_cases",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_country_time_series_cases",
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
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_country_time_series_deaths",
                                                                        options = opts_var_deaths,
                                                                        value = opts_var_deaths[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_country_time_series_deaths",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_country_time_series_deaths",
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
                                                        html.Div(
                                                            [
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_country_time_series_vaccinated",
                                                                        options = opts_var_vaccinated,
                                                                        value = opts_var_vaccinated[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_country_time_series_vaccinated",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_country_time_series_vaccinated",
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
                        
                        # Trajectories:
                        dbc.Tab(
                            [
                                # Row of filters:
                                dbc.Row(
                                    [
                                        # Variable:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    "Variable",
                                                    className = "filter-title"
                                                ),
                                                dbc.Select(
                                                    id = "chosen_var_country_trajectories",
                                                    options = opts_var_trajectories,
                                                    value = opts_var_trajectories[0]["value"]
                                                )
                                            ],
                                            width = 4
                                        ),
                                        # Period:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    "Moving average period",
                                                    className = "filter-title"
                                                ),
                                                dbc.Select(
                                                    id = "chosen_var_country_mov_avg_period",
                                                    options = opts_mov_avg_period,
                                                    value = opts_mov_avg_period[0]["value"]
                                                )
                                            ],
                                            width = 4
                                        ),
                                        # Country:
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    "Countries",
                                                    className = "filter-title"
                                                ),
                                                dbc.Select(
                                                    id = "chosen_var_country_countries",
                                                    options = opts_countries,
                                                    value = opts_countries[0]["value"]
                                                )
                                            ],
                                            width = 4
                                        )
                                    ],
                                    className = "row-trajectories"
                                ),
                                
                                # Trajectory plot:
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                dbc.RadioItems(
                                                                    id = "chosen_scale_country_trajectory",
                                                                    options = opts_scales,
                                                                    value = opts_scales[0]["value"],
                                                                    inline = True
                                                                )
                                                            ],
                                                            className = "radio-check-scale"
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_country_trajectory",
                                                            figure = {}
                                                        )
                                                    ],
                                                    className = "card-plot"
                                                )
                                            ],
                                            width = 12
                                        )
                                    ],
                                    className = "row-trajectories"
                                )

                            ],
                            label = "Trajectories",
                            className = "tab-trajectories"
                        )
                    ],
                    className = "tabs-plots"
                )
            ],
            className = "generic-page"
        )
    ]
    
    return(pg)

