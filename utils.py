from unidecode import unidecode
import json

def sanitize(phrase):
    sanited = unidecode(phrase.lower().replace(' ','-'))
    return sanited

def save_cities(cities):
    new_cities = []
    for i in cities:
        new_cities.append(i.strip().replace(' ', '-'))
        
    with open('cities.json', mode='w') as file:
        json_file = json.dumps(new_cities)
        file.write(json_file)
