
import plotly.graph_objects as go

def make_plot_country_time_series(df, country_code, var, scale, opts_var):
    """
    Plot the time series of a variable for a country.
    param df: 
    param country_code: 
    param var: 
    param scale: 
    param opts_var:
    return: fig
    """
    
    # Filter the data:
    df_plot = df.loc[df["iso_code"] == country_code, [var, "date"]]
    
    # Axes names:
    x_var_name = "Date"
    y_var_name = [opts_var[i]["label"] for i in range(len(opts_var)) if opts_var[i]["value"] == var][0]
    
    # Plot:
    fig = go.Figure(
        data = go.Scatter(
            x = df_plot["date"],
            y = df_plot[var],
            mode = "lines",
            line = {
                "width": 2,
                "color": "#FFA800"
            },
            hovertemplate = "<b>" + x_var_name + ": %{x}<br>" +
                                    y_var_name + ": %{y:}<br></b><extra></extra>"
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

