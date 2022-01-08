
import numpy as np
import plotly.graph_objects as go
from matplotlib.colors import LinearSegmentedColormap, to_hex

def make_plot_country_trajectories(df, var, mov_avg_period, countries_codes, scale, opts_var):
    """
    Plot the time series of a variable for a country.
    param df: 
    param var: 
    param mov_avg_period:
    param countries_codes: 
    param scale: 
    param opts_var:
    return: fig
    """
    
    # Filter the data:
    df_plot = df.loc[df["iso_code"].isin(countries_codes), 
                     ["iso_code", "location", "date", var + "_new", var + "_total"]]

    # Axes names:
    var_name = [opts_var[i]["label"] for i in range(len(opts_var)) if opts_var[i]["value"] == var][0]
    x_var_name = "New " + var_name
    y_var_name = "Total " + var_name
    
    # Plot:
    lvls = countries_codes
    n_levels = len(lvls)
    cmap = LinearSegmentedColormap.from_list("my_palette", ["#111539", "#97A1D9"])
    my_palette = [to_hex(j) for j in [cmap(i / n_levels) for i in np.array(range(n_levels))]]

    fig = go.Figure()
    for l, lvl in enumerate(lvls):
        fig.add_trace(
            go.Scatter(
                x = df_plot[var + "_total"][df_plot["iso_code"] == lvl],
                y = df_plot[var + "_new"][df_plot["iso_code"] == lvl],
                mode = "lines",
                line = {
                    "width": 5,
                    "color": my_palette[l]
                },
                name = lvl,
                hovertemplate = "<b>" + x_var_name + ": %{x:}<br>" +
                                        y_var_name + ": %{y:}<br>" +
                                        "Country: " + lvl +
                                        "</b><extra></extra>"
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
            "gridcolor": "rgba(255, 255, 255, 0.1)",
            "type": scale
        },
        font = {
            "size": 18,
            "color": "white",
            "family": "Helvetica"
        },
        showlegend = False,
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

