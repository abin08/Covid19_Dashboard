import json
from flask import make_response
from flask import render_template
from flask import jsonify
from app import app
from app import covid


@app.route("/")
def dashboard():
    total_info = {}

    dataframe, last_updated = covid.get_covid_data()
    top_ten_confirmed = covid.get_top10_confirmed(dataframe)
    top_ten_recovered = covid.get_top10_recovered(dataframe)
    top_ten_deaths = covid.get_top10_deaths(dataframe)
    
    total_info['last_updated'] = str(last_updated)
    total_info['total_confirmed'] = int(covid.total_confirmed(dataframe))
    total_info['total_recovered'] = int(covid.total_recovered(dataframe))
    total_info['total_deaths'] = int(covid.total_deaths(dataframe))
    total_info['total_active'] = total_info['total_confirmed'] - total_info['total_recovered'] - total_info['total_deaths']

    total_info = json.dumps(total_info)
    app.logger.info("Processed and created aggregations")
    return render_template(
        "index.html", 
        total_info=total_info, 
        top_ten_confirmed=top_ten_confirmed, 
        top_ten_recovered=top_ten_recovered, 
        top_ten_deaths=top_ten_deaths
    )
