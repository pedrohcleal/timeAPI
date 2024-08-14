import sqlite3
import os
from typing import List, Literal

def insert_country(country) -> None | Literal[False]:
    try:
        country = country.lower().strip().replace(' ', '-')
        cursor.execute('INSERT INTO countries (country) VALUES (?)', (country,))
        db.commit()
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False

def insert_city(city) -> None | Literal[False]:
    try:
        city = city.lower().strip().replace(' ', '-')
        cursor.execute('INSERT INTRO cities (city) VALUES (?)', (city,))
        db.commit()
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False
        
def select_city(city) -> List[str] | Literal[False]:
    try:
        cursor.execute('SELECT city FROM cities WHERE city = (?)', (city,))
        item = cursor.fetchmany()
        return item[0][0]
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False

        
def select_country(country) -> List[str] | Literal[False]:
    try:
        cursor.execute('SELECT country FROM countries WHERE country = (?)', (country,))
        item = cursor.fetchmany()
        return item[0][0]
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False

def select_all_cities() -> List[str] | Literal[False]:
    try:
        cursor.execute('SELECT city FROM cities')
        sql_return = cursor.fetchall()
        item_list = [country[0] for country in sql_return]
        print(item_list)
        return item_list
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False
        
def select_all_countries() -> List[List[str]] | Literal[False]:
    try:
        cursor.execute('SELECT country FROM countries')
        sql_return = cursor.fetchall()
        item_list = [country[0] for country in sql_return]
        return item_list
    except sqlite3.Error as e:
        print(f'sql error = {e}')
        return False
        
if __name__ == '__main__':      
    DATABASE: str = os.path.join(os.path.dirname(__file__), 'timeapi.db')

    db: sqlite3.Connection = sqlite3.connect(DATABASE)

    cursor: sqlite3.Cursor = db.cursor()
    
    db.close()