import requests
from pprint import pprint

END_POINT = "https://api.sheety.co/801b4bb028c784ae95f241ed61551800/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = []
        self.search_google_sheet()
        # self.put_iata()
        self.sheet_data = []

    def search_google_sheet(self):
        response = requests.get(url=END_POINT)
        text = response.json()
        pprint(text)
        self.sheet_data = text['prices']

        for index in range(0, len(text['prices'])):
            city = text['prices'][index]['city']
            iata_code = text['prices'][index]['iataCode']
            # if iata_code == '':
            #     self.put_iata(text['prices'][index]['id'])
            lowest_price = text['prices'][index]['lowestPrice']
            id = text['prices'][index]['id']
            self.data.append({'city': city, 'iata_code': iata_code, 'lowest_price': lowest_price, 'id': id})

    def put_iata(self, id, iata):
        changes = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(url=f"{END_POINT}/{id}", json=changes)

        text = response.json()
        pprint(text)
