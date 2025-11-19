## Project:Weather Data ETL Pipeline

This project demonstrates a two‑stage ETL pipeline:

- Stage 1: Extracts weather data from [Open-Meteo API](https://open-meteo.com/), transforms it, and loads it into MongoDB.
- Stage 2: Extracts the data from MongoDB, transforms it into relational format, and loads it into MySQL for structured analysis.

## Folder Structure

- .env                      # Environment variables-Not to be pushed to GitHub
- config.py                 # Loads environment variables from .env
- mysql_connection.py       # MySQL connection helper
- mongo_connection.py       # MongoDB connection helper
- fetch_and_store.py        # Fetches API data and stores in MongoDB
- mongodb_to_mysql.py       # Transfers data from MongoDB to MySQL
- read_and_print.py         # Utility to read and print MongoDB data
- requirements.txt          # Dependencies
- .gitignore                # files/folders that shouldnot be pushed to Github
- README.md                 # Project documentation

## SETUP

1. Create and activate virtual environment
   python -m venv env
   .\env\Scripts\activate
2. Install dependencies
   pip install -r requirements.txt
3. Create .env file
   MYSQL_HOST=localhost
   MYSQL_USER=your user name
   MYSQL_PASSWORD=your password
   MYSQL_DATABASE=weather_data
   MONGO_URI=mongodb://localhost:27017/

## Usage

- fetch_and_store.py: Fetch weather data and store in MongoDB
- read_and_print.py: Verify MongoDB data
- mongodb_to_mysql.py: Fetch data from MongoDB and store it in MySQL
