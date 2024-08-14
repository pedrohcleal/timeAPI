from typing import Union, List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from .handler import get_temperature
from fastapi.responses import JSONResponse
from db_config import get_database, get_db_connection
import asyncpg
from .crud import select_all_cities, select_all_countries, select_city, select_country, insert_city, insert_country


app = FastAPI()

class CountriesResponse(BaseModel):
    countries: List[str]

class CitiesResponse(BaseModel):
    cities: List[str]

class TemperatureResponse(BaseModel):
    temperature: Union[float, str]


@app.get("/all/countries", response_model=CountriesResponse)
def all_countries(db: asyncpg.connection.Connection = Depends(get_db_connection)):
    with get_db_connection() as dbs:
        pass
        
    return CountriesResponse(['city'])


@app.get("/all/cities", response_model=CitiesResponse)
def all_cities(db: asyncpg.connection.Connection = Depends(get_db_connection)):
    return CitiesResponse(['city'])


@app.get("/{country}/{city}", response_model=TemperatureResponse,)
def read_item(country: str, city: str, db: asyncpg.connection.Connection = Depends(get_db_connection)):
    # if country not in countries:
    #     raise HTTPException(status_code=404, detail="Country not located")
    # if city not in cities:
    #     raise HTTPException(status_code=404, detail="City not located")
    
    temperature = get_temperature(country, city)
    return TemperatureResponse(temperature=temperature)
