import requests, json
from typing import List
from bs4 import BeautifulSoup as bs4
from time import sleep
from unidecode import unidecode

continet_list_links = [
    'https://www.timeanddate.com/weather/?continent=namerica',
    'https://www.timeanddate.com/weather/?continent=samerica',
    'https://www.timeanddate.com/weather/?continent=asia'
    'https://www.timeanddate.com/weather/?continent=australasia',
    'https://www.timeanddate.com/weather/?continent=europe'
]

table_css_selector = 'body > div.main-content-div > section.bg--grey.pdflexi-t--small > div > section > div:nth-child(3) > div > table > tbody > tr:nth-child(1)'
names_cities  = 'body > main > article > section.pdflexi > div > table > tbody > tr > td > a'

def get_temperature(country, city):
    url = f'https://www.timeanddate.com/weather/{country}/{city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = bs4(response.text, 'html.parser')
        element = soup.select_one('#qlook > div.h2')
        if element:
            temperature = element.text.strip()
            return temperature
        else:
            return "Temperature element not found"
    else:
        return f"Failed to retrieve data, status code: {response.status_code}"

def update_cities_requests(countries, cities):
    seletor = 'body > main > article > section.pdflexi > div > table > *'

    for country in countries:
        sleep(0.1)
        try:
            response = requests.get(f'https://www.timeanddate.com/weather/{country}')
            if response.status_code == 200:
                soup = bs4(response.text, 'html.parser')
                table = soup.select(seletor) 
                #[cities.append(c.text) for c in row.select('a')] for row in table if c.text not in cities]
                for row in table:
                    city_list = row.select('a')
                    for c in city_list:
                        if c.text not in cities:
                            cities.append(unidecode(c.text))
            else:
                print(f'Failed to get data for country {country}, status code: {response.status_code}')
        except Exception as e:
            print(f'Skipping country {country}, ERRO: {e}')

if __name__ == '__main__':
    json_cities = open('cities.json').read()
    cities: List[str] = json.loads(json_cities)
    
    json_countries = open('countries.json').read()
    countries: List[str] = json.loads(json_countries)
    
    update_cities_requests(countries, cities)
    print('finish')
