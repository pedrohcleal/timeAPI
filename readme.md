![In development](https://img.shields.io/badge/status-In%20development-red)
![FastAPI](https://img.shields.io/badge/FastAPI-007ACC?style=flat&logo=fastapi&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-FFD700?style=flat&logo=python&logoColor=black)
![requests](https://img.shields.io/badge/requests-FF6F61?style=flat&logo=requests&logoColor=white)
![webdriver_manager](https://img.shields.io/badge/webdriver_manager-00B2A9?style=flat&logo=python&logoColor=white)
# Temperature API

This is an API that retrieves the current temperature of cities around the world. The API uses the [Time and Date](https://www.timeanddate.com) website to get weather information.

## Technologies Used

- **FastAPI**: Web framework for creating the API.
- **BeautifulSoup**: For parsing and extracting data from HTML pages.
- **requests**: For making HTTP requests.

## Features

- **/all/countries**: Returns a list of all available countries for queries.
- **/all/cities**: Returns a list of all available cities for queries.
- **/{country}/{city}**: Returns the current temperature of the specified city in the specified country.

## Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/pedrohcleal/timeAPI.git
cd timeAPI
pip install -r requirements.txt
```

## Usage

1. **Update Cities**:
   To update the list of available cities, run the `handler.py` script. This will use Selenium to collect data from Time and Date.

   ```bash
   python handler.py
   ```

2. **Run the FastAPI Server**:
   To start the API server, run the following command:

   ```bash
   cd app
   fastapi dev main.py
   ```

   The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Project Structure

- **handler.py**: Contains functions for collecting and processing city and temperature data.
- **main.py**: Defines the API endpoints using FastAPI.
- **crud.py**: Helper functions for text sanitization and data saving.

## Dependencies

Make sure to keep the `requirements.txt` file updated with all the necessary libraries. The `requirements.txt` file can be generated with:

```bash
pip freeze > requirements.txt
```

## Contribution

If you would like to contribute to the project, feel free to submit pull requests. For issues or questions, open an issue on GitHub.
