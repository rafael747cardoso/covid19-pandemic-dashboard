
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
    x_var_name = "Total " + var_name
    y_var_name = "New " + var_name
    
    # Plot:
    n_colors = len(countries_codes)
    my_colors = ["#F64011", "#F69111", "#F6F511", "#9FF611", "#11F6E0", "#DF11F6"]
    cmap = LinearSegmentedColormap.from_list("my_palette", my_colors)
    my_palette = [to_hex(j) for j in [cmap(i / n_colors) for i in np.array(range(n_colors))]]
    fig = go.Figure()
    lvls = countries_codes
    for l, lvl in enumerate(lvls):
        # Filter the country:
        country_name = df_plot["location"][df_plot["iso_code"] == lvl].iloc[0]
        df_country = df_plot[df_plot["iso_code"] == lvl]
        
        # Add the moving average:
        mov_avg_period = int(mov_avg_period)
        X = df_country[var + "_total"].values
        X = [np.mean(X[i:(i + mov_avg_period)]) for i in range(0, len(X) - mov_avg_period, 1)]
        Y = df_country[var + "_new"].values
        Y = [np.mean(Y[i:(i + mov_avg_period)]) for i in range(0, len(Y) - mov_avg_period, 1)]
        
        # Plot the trace:
        fig.add_trace(
            go.Scatter(
                x = X,
                y = Y,
                mode = "lines",
                line = {
                    "width": 3,
                    "color": my_palette[l]
                },
                text = df_country["date"],
                name = country_name,
                hovertemplate = "<b>" + x_var_name + ": %{x:,.0f}<br>" +
                                        y_var_name + ": %{y:,.0f}<br>" +
                                        "Country: " + country_name + "<br>"
                                        "Date: %{text}" + 
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
            "gridcolor": "rgba(255, 255, 255, 0.1)",
            "type": scale
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

