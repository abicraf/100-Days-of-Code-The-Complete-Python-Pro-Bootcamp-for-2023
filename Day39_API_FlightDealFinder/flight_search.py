import requests, os
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    FLIGHT_KEY = os.environ.get("FLIGHT_KEY")

    TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    search_header = {
        "apikey": FLIGHT_KEY
    }
    search_parameters = {
        "fly_from": "TPE",
        "fly_to": "MEL",
        "date_from": "30/09/2023",  # dd/mm/yyyy
        "date_to": "01/10/2023",
        "return_from": "14/10/2023",
        "return_to": "15/10/2023",
        "curr": "TWD",
        "max_stopovers": 1,
        "price_from": 20000,
        "price_to": 31000,
    }

    response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=search_parameters, headers=search_header)
    print(response.text)
