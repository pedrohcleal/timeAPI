from typing import Union
from fastapi import FastAPI
import json
from countries import countries
from cities import cities

from handler import get_temperature

app = FastAPI()


@app.get("/all/countries")
def all_countries():
    return {"countries": countries}

@app.get("/all/cities")
def all_cities():
    return {"countries": countries}


@app.get("/{country}/{city}")
def read_item(country, city):
    # if country not in countries:
    #     return json.dumps('Country not located')
    # if city not in country:
    #     return json.dumps('City not located')
    
    temperature = get_temperature(country, city)
    return json.dumps(temperature,ensure_ascii=False )