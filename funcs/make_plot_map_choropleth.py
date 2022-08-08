
import numpy as np
import plotly.graph_objects as go
from matplotlib.colors import LinearSegmentedColormap, to_hex
import plotly.express as px

def make_plot_map_choropleth(df, var, country_names):
    """
    Plot the time series of a variable for a country.
    param df: 
    param var: 
    param country_names:
    return: map
    """
    
    # Data:
    df_plot = df.loc[df["location"].isin(country_names)]
    df_plot = df_plot.groupby(by = "location", as_index = False).last().dropna()
    df_plot = df_plot[["iso_code", "location", var]]
    
    # Palette:
    n_colors = 50
    my_colors = ["#A210B2", "#F37A09", "#F3EF09"]
    cmap = LinearSegmentedColormap.from_list("my_palette", my_colors)
    my_palette = [to_hex(j) for j in [cmap(i / n_colors) for i in np.array(range(n_colors))]]
    customdata = ["location", var]

    # Plot:
    fig = px.choropleth(
        data_frame = df_plot,
        locations = "iso_code",
        color = var,
        color_continuous_scale = my_palette,
        custom_data = customdata,
        projection = "natural earth",
        template = "plotly_dark"
    )
    fig.update_traces(
        hovertemplate = "<b>%{customdata[0]}<br>" +
                        var.title().replace("_", " ") + ": %{customdata[1]:,.0f}</b><extra></extra>",
        marker_line_width = 0
    )
    fig.update_layout(
        coloraxis = {
            "colorbar": {
                "title": "<b>" + var.title().replace("_", " ") + "</b>"
            }
        },
        font = dict(
            size = 18
        ),
        plot_bgcolor = "red",
        hoverlabel = dict(
            font_size = 18,
            font_family = "Rockwell"
        ),
        height = 800,
        geo_bgcolor = "rgba(0, 0, 0, 0)"
    )
    fig.update_geos(
        fitbounds = "locations",
        visible = True,
        showocean = True,
        oceancolor = "#2C2A5C"
    )    
    return(fig)

