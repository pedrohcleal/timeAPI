import requests
from bs4 import BeautifulSoup as bs4
from unidecode import unidecode
from app.crud import get_static_countries, get_all_cities, insert_city_country
from app.db_config import get_db_connection


def get_temperature(country, city):
    url = f"https://www.timeanddate.com/weather/{country}/{city}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = bs4(response.text, "html.parser")
        element = soup.select_one("#qlook > div.h2")
        if element:
            temperature = element.text.strip()
            return temperature
        else:
            return "Temperature element not found"
    else:
        return f"Failed to retrieve data, status code: {response.status_code}"


def update_pairs_city_country(conn) -> list[str]:
    print("update_pairs_city_country")
    countries: list[str] = get_static_countries(conn)
    cities: list[str] = get_all_cities(conn)
    seletor = "body > main > article > section.pdflexi > div > table > *"
    fails = []
    for country in countries:
        try:
            response = requests.get(f"https://www.timeanddate.com/weather/{country}")
            response.raise_for_status()
            soup = bs4(response.text, "html.parser")
            table = soup.select(seletor)
            for row in table:
                city_list = row.select("a")
                for city in city_list:
                    city = unidecode(city.text).strip().lower().replace(" ", "-")
                    if city not in cities:
                        insert_city_country(conn=conn, city=city, country=country)
        except Exception as e:
            msg = f"Skipping country '{country}', ERRO: '{e}'"
            print(msg)
            fails.append(msg)
    return fails
