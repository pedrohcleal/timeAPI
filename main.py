from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from .handler import get_temperature
from fastapi.responses import JSONResponse


app = FastAPI()

with open('countries.json') as f:
    countries: List[str] = json.load(f)

with open('cities.json') as f:
    cities: List[str] = json.load(f)

class CountriesResponse(BaseModel):
    countries: List[str]

class CitiesResponse(BaseModel):
    cities: List[str]

class TemperatureResponse(BaseModel):
    temperature: Union[float, str]


@app.get("/all/countries", response_model=CountriesResponse)
def all_countries():
    return CountriesResponse(countries=countries)


@app.get("/all/cities", response_model=CitiesResponse)
def all_cities():
    return CitiesResponse(cities=cities)


@app.get("/{country}/{city}", response_model=TemperatureResponse)
def read_item(country: str, city: str):
    # if country not in countries:
    #     raise HTTPException(status_code=404, detail="Country not located")
    # if city not in cities:
    #     raise HTTPException(status_code=404, detail="City not located")
    
    temperature = get_temperature(country, city)
    return TemperatureResponse(temperature=temperature)
