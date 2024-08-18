import sqlite3
import os
from typing import List, Optional
from contextlib import contextmanager
from typing import Generator


DATABASE: str = os.path.join(os.path.dirname(__file__), 'timeapi.db')

@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(DATABASE, timeout=30.0)
    try:
        yield conn
    finally:
        conn.close()

def get_all_countries(conn):
    countries = conn.execute('SELECT * FROM countries').fetchall()
    countries = [x[0] for x in countries]
    return countries

def get_all_cities(conn):
    cities = conn.execute('SELECT * FROM cities').fetchall()
    cities = [x[0] for x in cities]
    return cities

# def insert_country(country: str) -> Optional[bool]:
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         country = country.lower().strip().replace(' ', '-')
#         cursor.execute('INSERT INTO countries (country) VALUES (?)', (country,))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.Error as e:
#         print(f'SQL error = {e}')
#         return False

# def insert_city(city: str) -> Optional[bool]:
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         city = city.lower().strip().replace(' ', '-')
#         cursor.execute('INSERT INTO cities (city) VALUES (?)', (city,))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.Error as e:
#         print(f'SQL error = {e}')
#         return False