
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
                # Select the country:
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
                    className = "main-geo-select"
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
                    className = "main-geo-select"
                ),

                # Cards:
                
                
                
            ],
            className = "generic-page"
        )
    ]
    
    return(pg)

