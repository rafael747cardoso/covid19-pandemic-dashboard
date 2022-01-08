
import numpy as np

def get_card_values(df, var, country_code):
    """
    Filter the dataframe to take the last data and date of the variable.
    param df: 
    param var: 
    return: x, last_update
    """

    # Take the last valid data:
    df_last = df.loc[df["iso_code"] == country_code, ["date", var]].dropna().tail(1)

    if df_last.shape[0] == 0:
        x = "-"
        last_date = "-"
    else:
        x = df_last[var].values[0]
        last_date = df_last["date"].values[0]
    
        # Format the date and the value:
        last_date = last_date[8:10] + "/" + last_date[5:7] + "/" + last_date[0:4]
        if np.isnan(x):
            x = "-"
        else:
            if var == "vaccinated_fully_pct":
                x = "{:,.2f}".format(x) + " %"
            else:
                if var == "gdp_per_capita":
                    x = "$ {:,d}".format(int(x))
                else:
                    x = "{:,d}".format(int(x))

    return (x, last_date)

