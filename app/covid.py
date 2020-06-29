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


def top_ten_confirmed_df(df):
    df_top_10 = df.nlargest(10, "Confirmed")
    df_top_10_confirmed = df_top_10[["Country_Region", "Confirmed"]]
    return df_top_10_confirmed


def top_ten_recovered_df(df):
    df_top_10 = df.nlargest(10, "Recovered")
    df_top_10_recovered = df_top_10[["Country_Region", "Recovered"]]
    return df_top_10_recovered


def top_ten_deaths_df(df):
    df_top_10 = df.nlargest(10, "Deaths")
    df_top_10_deaths = df_top_10[["Country_Region", "Deaths"]]
    return df_top_10_deaths
    

def get_covid_data():
    covid_data = get_data()
    covid_dataframe = get_dataframe(covid_data)
    return covid_dataframe


def get_top10_confirmed(df):
    """ Returns top ten confirmed countries in json format"""
    top_ten_confirmed = {}
    df_top_ten_confirmed = top_ten_confirmed_df(df)
    top_ten_confirmed['country'] = list(df_top_ten_confirmed['Country_Region'].values)
    top_ten_confirmed['confirmed'] = list(map(lambda x: int(x), list(df_top_ten_confirmed['Confirmed'].values)))
    return json.dumps(top_ten_confirmed)


def get_top10_recovered(df):
    """ Returns top ten recovered countries in json format"""
    top_ten_recovered = {}
    df_top_ten_recovered = top_ten_recovered_df(df)
    top_ten_recovered['country'] = list(df_top_ten_recovered['Country_Region'].values)
    top_ten_recovered['recovered'] = list(map(lambda x: int(x), list(df_top_ten_recovered['Recovered'].values)))
    return json.dumps(top_ten_recovered)


def get_top10_deaths(df):
    """ Returns top ten deaths of countries in json format"""
    top_ten_deaths = {}
    df_top_ten_deaths = top_ten_deaths_df(df)
    top_ten_deaths['country'] = list(df_top_ten_deaths['Country_Region'].values)
    top_ten_deaths['deaths'] = list(map(lambda x: int(x), list(df_top_ten_deaths['Deaths'].values)))
    return json.dumps(top_ten_deaths)
