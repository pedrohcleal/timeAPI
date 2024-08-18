from typing import Union, List
from fastapi import FastAPI, HTTPException, Depends
from handler import get_temperature
from fastapi import FastAPI
from crud import get_all_cities, get_all_countries, get_db_connection

app = FastAPI()


@app.get("/all/countries")
async def read_all_countries():
    with get_db_connection() as conn:
        countries = get_all_countries(conn)
    return countries

@app.get("/all/cities")
async def read_all_cities():
    with get_db_connection() as conn:
        cities = get_all_cities(conn)
    return cities


@app.get("/{country}/{city}")
async def read_item(country: str, city: str):
    # if country not in countries:
    #     raise HTTPException(status_code=404, detail="Country not located")
    # if city not in cities:
    #     raise HTTPException(status_code=404, detail="City not located")
    
    temperature = get_temperature(country, city)
    return temperature
