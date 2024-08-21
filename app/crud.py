import sqlite3
import os
from contextlib import contextmanager
from typing import Generator


DATABASE: str = os.path.join(os.path.dirname(__file__), "timeapi.db")


@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(DATABASE, timeout=30.0)
    try:
        yield conn
    except sqlite3.Error as e:
        print(f"DB Error: {e}")
        raise
    finally:
        conn.close()


def get_all_countries(conn) -> list[str]:
    try:
        countries = conn.execute("SELECT * FROM countries").fetchall()
        countries = [x[0] for x in countries]
        return countries
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []


def get_all_cities(conn) -> list[str]:
    try:
        cities = conn.execute("SELECT * FROM cities").fetchall()
        cities = [x[0] for x in cities]
        return cities
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []


def insert_into_table(conn: sqlite3.Connection, table: str, value: str) -> bool:
    try:
        query = f'INSERT INTO {table} ({"country" if table == "countries" else "city"}) VALUES (?)'
        conn.execute(query, (value,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error inserting value into {table}: {e}")
        return False


def insert_country(conn: sqlite3.Connection, country: str) -> bool:
    return insert_into_table(conn, "countries", country)


def insert_city(conn: sqlite3.Connection, city: str) -> bool:
    return insert_into_table(conn, "cities", city)
