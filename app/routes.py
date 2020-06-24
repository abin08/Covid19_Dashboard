import json
from flask import make_response
from flask import render_template
from app import app
from app import covid


@app.route("/dashboard")
def dashboard():
    total_info = {}
    dataframe = covid.get_covid_data()
    
    top_ten_confirmed = covid.top_ten_confirmed(dataframe).to_json()
    top_ten_recovered = covid.top_ten_recovered(dataframe).to_json()
    top_ten_deaths = covid.top_ten_deaths(dataframe).to_json()

    total_info['total_confirmed'] = int(covid.total_confirmed(dataframe))
    total_info['total_recovered'] = int(covid.total_recovered(dataframe))
    total_info['total_deaths'] = int(covid.total_deaths(dataframe))
    total_info['total_active'] = total_info['total_confirmed'] - total_info['total_recovered'] - total_info['total_deaths']

    total_info = json.dumps(total_info)
    
    return render_template(
        "index.html", 
        total_info=total_info, 
        top_ten_confirmed=top_ten_confirmed, 
        top_ten_recovered=top_ten_recovered, 
        top_ten_deaths=top_ten_deaths
    )


@app.route("/test")
def test():
    total_info = {}
    dataframe = covid.get_covid_data()
    
    top_ten_confirmed = covid.top_ten_confirmed(dataframe).to_json()
    
    return top_ten_confirmed
