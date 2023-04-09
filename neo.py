# Import needed modules
import requests, json
from datetime import date, timedelta
import pandas as pd


# REST connection information for NASA Near Earth Objects API
url_neo = 'https://api.nasa.gov/neo/rest/v1/feed'
api_key = input("Provide your NASA API key: ")

# Start query from days_past since today
days_past = 1

parameters = {
    'start_date':date.today() - timedelta(days = days_past),
    'end_date': date.today(),
    'api_key': api_key,
    'page': 0
}

# Create an empty list to start near_earth_objects
near_earth_objects = []

# Set up a REST session
# Keeps from setting up a TCP and TLS handshake for every call
session = requests.Session()

response = session.get(url_neo,params=parameters).json()

print(json.dumps(response, indent=2))
