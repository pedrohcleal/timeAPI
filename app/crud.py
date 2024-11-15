import sqlite3


def get_static_countries(conn) -> list[str]:
    try:
        countries = conn.execute("SELECT country FROM countries").fetchall()
        countries = [x[0] for x in countries]
        return countries
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []


def get_all_countries(conn) -> list[str]:
    try:
        countries = conn.execute(
            "SELECT DISTINCT country FROM cities_and_countries"
        ).fetchall()
        countries = [x[0] for x in countries]
        return countries
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []


def get_all_cities(conn) -> list[str]:
    try:
        cities = conn.execute("SELECT city FROM cities_and_countries").fetchall()
        cities = [x[0] for x in cities]
        return cities
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []


def insert_city_country(conn: sqlite3.Connection, city: str, country: str) -> bool:
    try:
        query = f"""INSERT INTO cities_and_countries
        VALUES (?, ?)"""
        conn.execute(query, (city, country))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error inserting value, {e}")
        return False


def get_pairs_city_and_countries(conn) -> dict[str, list[str]]:
    pairs = {}
    try:
        cities = conn.execute(
            "SELECT city, country FROM cities_and_countries"
        ).fetchall()
        for city, country in cities:
            if country in pairs.keys():
                pairs[country].append(city)
            else:
                pairs[country] = [city]
            # (pairs)
        return pairs
    except sqlite3.Error as e:
        print(f"SQL error = {e}")
        return []
