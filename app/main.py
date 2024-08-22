from fastapi import FastAPI
from app.handler import get_temperature
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.crud import get_all_cities, get_all_countries
from app.db_config import get_db_connection


app = FastAPI()


@app.get("/")
async def get_main() -> JSONResponse:
    return JSONResponse(content="Server OK", status_code=200)


@app.get("/all/countries")
async def read_all_countries() -> JSONResponse:
    with get_db_connection() as conn:
        countries = get_all_countries(conn)
    return JSONResponse(content={"countries": countries}, status_code=200)


@app.get("/all/cities")
async def read_all_cities() -> JSONResponse:
    with get_db_connection() as conn:
        cities = get_all_cities(conn)
    return JSONResponse(content={"cities": cities}, status_code=200)


@app.get("/{country}/{city}")
async def read_item(country: str, city: str) -> JSONResponse:
    with get_db_connection() as conn:
        cities = get_all_cities(conn)
        countries = get_all_countries(conn)
    if country not in countries:
        raise HTTPException(status_code=404, detail="Country not located")
    if city not in cities:
        raise HTTPException(status_code=404, detail="City not located")

    temperature = get_temperature(country, city)
    return JSONResponse(content={"temperature": temperature}, status_code=200)
