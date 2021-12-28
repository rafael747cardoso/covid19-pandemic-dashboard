
import pandas as pd
from datetime import datetime

def get_data():
    """
    Get the data from the source and check for bugs.
    """
    
    # System datetime for the logs:
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    # Download the data from the source:
    try:
        df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
        read_from_source = True
    except (Exception,):
        df = pd.read_csv("data/owid-covid-data_last_ok.csv")
        read_from_source = False
        with open("error_logs.txt", "a") as file:
            file.write(current_time + " Problem in the https request.\n")
    
    if read_from_source:
        # Filter the relevant variables:
        variables = [
            "iso_code",
            "continent",
            "location",
            "date",
            "total_cases",
            "new_cases",
            "new_cases_smoothed",
            "total_cases_per_million",
            "new_cases_per_million",
            "new_cases_smoothed_per_million",
            "total_deaths",
            "new_deaths",
            "new_deaths_smoothed",
            "total_deaths_per_million",
            "new_deaths_per_million",
            "new_deaths_smoothed_per_million",
            "people_vaccinated",
            "people_fully_vaccinated",
            "people_vaccinated_per_hundred",
            "people_fully_vaccinated_per_hundred",
            "population"
        ]
        try:
            df = df[variables]
            vars_names_bug = False
        except (Exception,):
            df = pd.read_csv("data/owid-covid-data_last_ok.csv")
            df = df[variables]
            with open("error_logs.txt", "a") as file:
                file.write(current_time + " Variables names changed in the source.\n")
            vars_names_bug = True
        
        if not vars_names_bug:
            # Change variables names:
            df = df.rename(columns = {
                "total_cases": "cases_total",
                "new_cases": "cases_new",
                "new_cases_smoothed": "cases_new_smoothed",
                "total_cases_per_million": "cases_total_per_million",
                "new_cases_per_million": "cases_new_per_million",
                "new_cases_smoothed_per_million": "cases_new_smoothed_per_million",
                "total_deaths": "deaths_total",
                "new_deaths": "deaths_new",
                "new_deaths_smoothed": "deaths_new_smoothed",
                "total_deaths_per_million": "deaths_total_per_million",
                "new_deaths_per_million": "deaths_new_per_million",
                "new_deaths_smoothed_per_million": "deaths_new_smoothed_per_million",
                "people_vaccinated": "vaccinated",
                "people_fully_vaccinated": "vaccinated_fully",
                "people_vaccinated_per_hundred": "vaccinated_pct",
                "people_fully_vaccinated_per_hundred": "vaccinated_fully_pct"
            })

        # Check the dtypes:
        boo = False
        for tp in df.dtypes[:4]:
            if tp != "object":
                boo = True
        for tp in df.dtypes[4:]:
            if tp != "float64":
                boo = True
        if boo:
            with open("error_logs.txt", "a") as file:
                file.write(current_time + " Variables data types changed in the source.\n")
        
        # Save the backup of the last csv downloaded:
        df.to_csv("data/owid-covid-data_last_ok.csv",
                  sep = ",",
                  index = False)

    return(df)

