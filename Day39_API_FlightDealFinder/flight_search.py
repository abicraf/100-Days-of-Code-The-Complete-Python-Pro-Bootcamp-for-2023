import requests, os
from datetime import *
from dateutil.relativedelta import relativedelta

FLIGHT_KEY = os.environ.get("FLIGHT_KEY")
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
#qoQPGtiRCf3cFczK7_zWK6tisgssJyHI
class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        self.cheap_flight = []
        sheet = data
        for index in range(0, len(sheet)):
            location = sheet[index]['iata_code']
            sheet_lowest_price = sheet[index]['lowest_price']

            search_header = {
                "apikey": FLIGHT_KEY
            }

            today = datetime.now()

            # Check for the flights from tomorrow to 6 months later.
            tomorrow = today + timedelta(days=1)
            six_month_later = today + relativedelta(months=+6)

            search_parameters = {
                "fly_from": "TPE",
                "fly_to": location,
                "date_from": tomorrow.strftime("%d/%m/%Y"),  # dd/mm/yyyy
                "date_to": six_month_later.strftime("%d/%m/%Y"),
                # "return_from": "14/10/2023",
                # "return_to": "15/10/2023",
                "curr": "TWD",
                "max_stopovers": 0,
                # "price_from": 25000,
                # "price_to": 30000,
                "limit": 1, # get the lowest price
            }

            response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=search_parameters, headers=search_header)
            response_json = response.json()
            # print(response_json["_results"])
            if response_json["_results"] > 0:
                #print(response_json["data"][0]["price"])
                current_lowest_price = response_json["data"][0]["price"]
                if current_lowest_price < sheet_lowest_price:
                    print(f"{location} current price is {current_lowest_price}, this is cheaper than the excel {sheet_lowest_price} ")
                    self.cheap_flight.append(response_json)