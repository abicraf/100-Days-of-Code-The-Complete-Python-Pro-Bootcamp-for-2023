import requests
from flight_search import FlightSearch

END_POINT = "https://api.sheety.co/801b4bb028c784ae95f241ed61551800/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.search_google_sheet()
        self.iata_code = ''
        self.lowest_price = 0

    def search_google_sheet(self):
        response = requests.get(url=END_POINT)
        text = response.json()

        for index in range(0,len(text['prices'])):
            # city = text['prices'][index]['city']
            self.iata_code = text['prices'][index]['iataCode']
            self.lowest_price = text['prices'][index]['lowestPrice']
            # print(f"{city} lowest price: {lowest_price}, IATA code: {iata_code}")
            FlightSearch()

        # self.response = requests.get(url=END_POINT)
        # self.text = self.response.json()
        # print(len(self.text['prices']))
        # for index in range(0,len(self.text['prices'])):
        #     # print(text['prices'][index]['city'])
        #     self.city = self.text['prices'][index]['city']
        #     self.iata_code = self.text['prices'][index]['iataCode']
        #     self.lowest_price = self.text['prices'][index]['lowestPrice']
            # FlightSearch(self.city, self.iata_code, self.lowest_price)
        # return city, iata_code, lowest_price
        # print(f"{city} lowest price: {lowest_price}")
