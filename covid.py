import pandas as pd
import requests
import json
from datetime import datetime

DATA_URL = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json"


def get_data():
    response = requests.get(DATA_URL).json()
    return response['features']


def convert_time(t):
  t = int(t) / 1000
  return datetime.fromtimestamp(t)


def get_dataframe(json_data):
    df = pd.DataFrame(json_data)
    attributes_list = df['attributes'].tolist()
    attributes_df = pd.DataFrame(attributes_list)
    attributes_df = attributes_df.set_index('OBJECTID')
    # attributes_df['Last_Update'] = attributes_df['Last_Update'].apply(convert_time)
    country_total_df = attributes_df.groupby("Country_Region", as_index=False).agg({
        "Confirmed": "sum",
        "Recovered": "sum",
        "Deaths": "sum"
    })
    return country_total_df


def handle_missing_data(df):
    pass


def total_confirmed(df):
    return df["Confirmed"].sum()


def total_recovered(df):
    return df["Recovered"].sum()


def total_deaths(df):
    return df["Deaths"].sum()


def top_ten_confirmed(df):
    df_top_10 = df.nlargest(10, "Confirmed")
    df_top_10_confirmed = df_top_10[["Country_Region", "Confirmed"]]
    df_top_10_confirmed.rename(columns={'Confirmed': 'Top_ten_confirmed'}, inplace=True)
    return df_top_10_confirmed.set_index("Country_Region").to_json()


def top_ten_recovered(df):
    df_top_10 = df.nlargest(10, "Recovered")
    df_top_10_recovered = df_top_10[["Country_Region", "Recovered"]]
    df_top_10_recovered.rename(columns={'Recovered': 'Top_ten_recovered'}, inplace=True)
    return df_top_10_recovered.set_index("Country_Region").to_json()


def top_ten_deaths(df):
    df_top_10 = df.nlargest(10, "Deaths")
    df_top_10_deaths = df_top_10[["Country_Region", "Deaths"]]
    df_top_10_deaths.rename(columns={'Deaths': 'Top_ten_deaths'}, inplace=True)
    return df_top_10_deaths.set_index("Country_Region").to_json()
    

def get_covid_data():
    covid_data = get_data()
    covid_dataframe = get_dataframe(covid_data)
    return covid_dataframe