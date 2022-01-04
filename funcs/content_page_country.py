
from dash import html
import dash_bootstrap_components as dbc

def content_page_country(
    opts_countries
):
    """
    Make the content for the Country page.
    param opts_countries:
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
                )
                
                ### Plots
                
                
                
                
                
            ],
            className = "generic-page"
        )
    ]
    
    return(pg)

