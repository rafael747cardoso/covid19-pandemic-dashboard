
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

def content_page_map(
    opts_var_map
):
    """
    Make the content for the Map page.
    param opts_var_map:
    return: pg
    """

    pg = [
        html.Div(
            [
                dbc.Row(
                    [
                        # Map:
                        dbc.Col(
                            [
                                dcc.Graph(
                                    id = "map_choropleth",
                                    figure = {},
                                    className = "map-choropleth-box"
                                )
                            ],
                            width = 9
                        ),
                        # Variables:
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dbc.RadioItems(
                                            id = "chosen_var_map",
                                            options = opts_var_map,
                                            value = opts_var_map[0]["value"],
                                            inline = False
                                        )
                                    ],
                                    className = "radio-check-map-vars"
                                )
                            ],
                            width = 3
                        )
                    ]
                )
            ],
            className = "generic-page"
        )
    ]
    
    return(pg)

