import requests, os
from datetime import *
from dateutil.relativedelta import relativedelta
from data_manager import DataManager

FLIGHT_KEY = os.environ.get("FLIGHT_KEY")
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
#qoQPGtiRCf3cFczK7_zWK6tisgssJyHI
class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        sheet = DataManager()
        location = sheet.iata_code
        price = sheet.lowest_price

        print(location)
        print(price)
        search_header = {
            "apikey": FLIGHT_KEY
        }

        today = datetime.now()

        # Check for the flights from tomorrow to 6 months later.
        tomorrow = today + timedelta(days=1)
        print(tomorrow.day)

        six_month_later = today + relativedelta(months=+6)
        print(six_month_later.month)

        print(six_month_later.strftime("%d/%m/%Y"))

        search_parameters = {
            "fly_from": "TPE",
            "fly_to": "MEL",
            "date_from": tomorrow.strftime("%d/%m/%Y"),  # dd/mm/yyyy
            "date_to": six_month_later.strftime("%d/%m/%Y"),
            # "return_from": "14/10/2023",
            # "return_to": "15/10/2023",
            "curr": "TWD",
            "max_stopovers": 1,
            "price_from": 20000,
            "price_to": 28000,
        }

        # response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=search_parameters, headers=search_header)
        # print(response.text)
