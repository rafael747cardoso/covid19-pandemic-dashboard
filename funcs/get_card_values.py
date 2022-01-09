
import numpy as np

def get_card_values(df, var, location_id, location_type):
    """
    Filter the dataframe to take the last data and date of the variable.
    param df: 
    param var: 
    return: x, last_update
    """

    # Take the last valid data:
    if location_type == "country":
        df_last = df.loc[df["iso_code"] == location_id, ["date", var]].dropna().tail(1)
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

    if location_type == "continent":
        if var == "gdp_per_capita":
            df_last = df.loc[df["continent"] == location_id, ["date",
                                                              var,
                                                              "location"]].dropna().groupby(by = "location",
                                                                                            axis = 0).tail(1)
            x = df_last[var].mean()
            x = "$ {:,d}".format(int(x))
            last_date = df_last["date"].max()  
            
        else:
            df_last = df.loc[df["location"] == location_id, ["date", var]].dropna().tail(1)
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

