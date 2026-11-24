import json
from pprint import pprint
from statistics import mean
import requests
from plotly.express import line

from app.alpha import API_KEY


def format_pct(my_number):
    """
    Formats a percentage number like 3.6555554 as percent, rounded to two decimal places.

    Param my_number (float) like 3.6555554

    Returns (str) like '3.66%'
    """
    return f"{my_number:.2f}%"



def fetch_unemployment_data():
    """Fetches unemployment data from the AlphaVantage API.
        Returns data as a list of dictionaries, where each represents the unemployment rate for a given month.
        Formats rates as floats.
    """

    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    data = parsed_response["data"]

    # some months have no data and come back as "." so skip those
    data = [d for d in data if d["value"] != "."]

    for d in data:
        d["value"] = float(d["value"])

    return data