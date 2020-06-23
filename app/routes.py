import json
from flask import make_response
from app import app
from app import covid


@app.route("/")
def dashboard():
    total_info = {}
    dataframe = covid.get_covid_data()
    
    top_ten_confirmed = covid.top_ten_confirmed(dataframe).to_json()
    top_ten_recovered = covid.top_ten_recovered(dataframe).to_json()
    top_ten_deaths = covid.top_ten_deaths(dataframe).to_json()

    total_info['total_confirmed'] = int(covid.total_confirmed(dataframe))
    total_info['total_recovered'] = int(covid.total_recovered(dataframe))
    total_info['total_deaths'] = int(covid.total_deaths(dataframe))
    total_info = json.dumps(total_info)
    
    print(top_ten_confirmed)
    print(top_ten_deaths)
    print(top_ten_recovered)
    
    return "dashboard"


@app.route("/covid_info")
def total_covid_info():
    total_info = {}
    dataframe = covid.get_covid_data()
    total_info['total_confirmed'] = int(covid.total_confirmed(dataframe))
    total_info['total_recovered'] = int(covid.total_recovered(dataframe))
    total_info['total_deaths'] = int(covid.total_deaths(dataframe))
    return total_info


@app.route("/top_ten_confirmed")
def top_ten_confirmed():
    dataframe = covid.get_covid_data()
    top_ten_confirmed = covid.top_ten_confirmed(dataframe).to_json()
    response = make_response(top_ten_confirmed)
    response.headers['Content-Type'] = 'application/json'
    return response