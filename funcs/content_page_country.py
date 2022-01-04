
from dash import html, dcc
import dash_bootstrap_components as dbc

def content_page_country(
    opts_countries,
    opts_var_cases,
    opts_var_deaths,
    opts_var_vaccinated,
    opts_scales
):
    """
    Make the content for the Country page.
    param opts_countries:
    param opts_var_cases:
    param opts_scales:
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
                                )
                            ],
                            width = 4
                        )
                    ],
                    className = "main-geo-select-header"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Select(
                                    id = "chosen_country",
                                    options = opts_countries,
                                    value = opts_countries[0]["value"]
                                )
                            ],
                            width = 4
                        )
                    ],
                    className = "main-geo-select-body"
                ),

                ### Cards
                
                # First row of info cards:
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            "100000000",
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
                                    "Updated in 03/01/2022",
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
                                                                    "Select the variable",
                                                                    className = "card-plot-select-title"
                                                                ),
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_cases_time_series",
                                                                        options = opts_var_cases,
                                                                        value = opts_var_cases[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        dbc.RadioItems(
                                                            id = "chosen_scale_cases_time_series",
                                                            options = opts_scales,
                                                            value = opts_scales[0]["value"],
                                                            inline = True
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_time_series_cases",
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
                                                                    "Select the variable",
                                                                    className = "card-plot-select-title"
                                                                ),
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_deaths_time_series",
                                                                        options = opts_var_deaths,
                                                                        value = opts_var_deaths[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        dbc.RadioItems(
                                                            id = "chosen_scale_deaths_time_series",
                                                            options = opts_scales,
                                                            value = opts_scales[0]["value"],
                                                            inline = True
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_time_series_deaths",
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
                                                                    "Select the variable",
                                                                    className = "card-plot-select-title"
                                                                ),
                                                                html.Div(
                                                                    dbc.Select(
                                                                        id = "chosen_var_vaccinated_time_series",
                                                                        options = opts_var_vaccinated,
                                                                        value = opts_var_vaccinated[0]["value"]
                                                                    ),
                                                                    className = "card-plot-select"
                                                                )
                                                            ]
                                                        ),
                                                        dbc.RadioItems(
                                                            id = "chosen_scale_vaccinated_time_series",
                                                            options = opts_scales,
                                                            value = opts_scales[0]["value"],
                                                            inline = True
                                                        ),
                                                        dcc.Graph(
                                                            id = "plot_time_series_vaccinated",
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
                                "dasfsdfsdf"
                                
                                
                                
                                
                                
                                
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

