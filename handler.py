from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from countries import countries
from utils import save_cities

import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

continet_list_links = [
    'https://www.timeanddate.com/weather/?continent=namerica',
    'https://www.timeanddate.com/weather/?continent=samerica',
    'https://www.timeanddate.com/weather/?continent=asia'
    'https://www.timeanddate.com/weather/?continent=australasia',
    'https://www.timeanddate.com/weather/?continent=europe'
]

table_css_selector = 'body > div.main-content-div > section.bg--grey.pdflexi-t--small > div > section > div:nth-child(3) > div > table > tbody > tr:nth-child(1)'
names_cities  = 'body > main > article > section.pdflexi > div > table > tbody > tr > td > a'

def update_cities_selenium(driver: webdriver.Chrome):
    cities = []  
    for i in countries:
        try:
            driver.get(f'https://www.timeanddate.com/weather/{i}')
            table: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, names_cities)
            print(f'quantidade de cidades {len(table)}')
            for row in table:
                print(row.text)
                cities.append(row.text)
        except Exception:
            print(f'pulando pais {i}, ERRO')
    save_cities(cities)

def get_temperature(country, city):
    url = f'https://www.timeanddate.com/weather/{country}/{city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select_one('#qlook > div.h2')
        if element:
            temperature = element.text.strip()
            return temperature
        else:
            return "Temperature element not found"
    else:
        return f"Failed to retrieve data, status code: {response.status_code}"

def update_cities_bs4(): #to do
    pass


if __name__ == '__main__':
    try:
        #driver.get('https://www.timeanddate.com/weather/usa/new-york')
        update_cities(driver)
        # Encontrar os elementos do formulário de login
        username_field = driver.find_element(By.CSS_SELECTOR, '#qlook > div.h2')
        print(username_field.text)
        
        # 
    finally:
        # Fechar o navegador
        driver.quit()
