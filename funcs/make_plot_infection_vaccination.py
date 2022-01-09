
import numpy as np
import plotly.graph_objects as go

def make_plot_infection_vaccination(df,
                                    country_codes):
    """
    Plot the relation between infection cases and full vaccination by country.
    param df: 
    param country_codes:
    return: fig
    """

    df_plot = df.loc[df["iso_code"].isin(country_codes)].groupby(by = "location").tail(1)[["location",
                                                                                           "cases_total",
                                                                                           "vaccinated_fully"]].dropna()
    x_var_name = "Fully vaccinated"
    y_var_name = "Total Cases"

    fig = go.Figure(
        data = go.Scatter(
            x = df_plot["cases_total"],
            y = df_plot["vaccinated_fully"],
            mode = "markers",
            marker = {
                "size": 10,
                "color": "#FFC300"
            },
            text = df_plot["location"],
            hovertemplate = "<b>%{text}<br>" + 
                            x_var_name + ": %{x:,.0f}<br>" +
                            y_var_name + ": %{y:,.0f}<br></b><extra></extra>"
        )
    )
    fig.update_layout(
        xaxis = {
            "title": "<b>" + x_var_name + "</b>",
            "titlefont": {
                "size": 20,
                "color": "white"
            },
            "tickfont": {
                "size": 18,
                "color": "white"
            },
            "gridcolor": "rgba(255, 255, 255, 0.1)"
        },
        yaxis = {
            "title": "<b>" + y_var_name + "</b>",
            "titlefont": {
                "size": 20,
                "color": "white",
                "family": "Helvetica"
            },
            "tickfont": {
                "size": 18,
                "color": "white",
                "family": "Helvetica"
            },
            "gridcolor": "rgba(255, 255, 255, 0.1)"
        },
        font = {
            "size": 18,
            "color": "white",
            "family": "Helvetica"
        },
        showlegend = True,
        paper_bgcolor = "rgba(0, 0, 0, 0)",
        plot_bgcolor = "rgba(0, 0, 0, 0)",
        hoverlabel = {
            "font_size": 18,
            "font_family": "Helvetica"
        },
        margin = {
            "l": 10,
            "r": 10,
            "t": 10,
            "b": 10
        }
    )
    return (fig)

