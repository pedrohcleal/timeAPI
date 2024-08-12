from unidecode import unidecode

def sanitize(phrase):
    sanited = unidecode(phrase.lower().replace(' ','-'))
    return sanited

def save_cities(cities):
    with open('cities.py', mode='w') as file:
        file.write('cities = [')
        for city in cities:
            file.write(f'\n\t"{city}", ')
        file.write('\n]')


# def test(cities):
#     with open('cities.py', mode='w') as file:
#         file.write('cities = [')
#         for city in cities:
#             file.write(f'\n\t"{city}", ')
#         file.write('\n]')

# cities = [
#     "New yoªrk", "Los angêles", "chic Aãogo", "houston", "phoenix", "philadelphia", "san antonio", "san diego", "dallas", "san-jose"
# ]
# test(cities)