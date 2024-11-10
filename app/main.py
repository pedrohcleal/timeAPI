from fastapi import FastAPI
from app.handler import get_temperature, update_pairs_city_country
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.crud import get_all_cities, get_all_countries
from app.db_config import get_db_connection
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Lista de origens permitidas
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os headers
)


@app.get("/")
async def health_check() -> JSONResponse:
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
async def temperature_city(country: str, city: str) -> JSONResponse:
    with get_db_connection() as conn:
        cities = get_all_cities(conn)
        countries = get_all_countries(conn)
    if country not in countries:
        raise HTTPException(status_code=404, detail="Country not located")
    if city not in cities:
        raise HTTPException(status_code=404, detail="City not located")

    temperature = get_temperature(country, city)
    return JSONResponse(content={"temperature": temperature}, status_code=200)


@app.get("/update_pairs_city_country")
async def update_pairs() -> JSONResponse:
    with get_db_connection() as conn:
        fails = update_pairs_city_country(conn)
    return JSONResponse(
        content={"message": "Pares atualizados", "falhas": fails}, status_code=200
    )
