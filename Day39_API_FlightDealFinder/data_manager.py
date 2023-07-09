import requests
#from flight_search import FlightSearch

END_POINT = "https://api.sheety.co/801b4bb028c784ae95f241ed61551800/flightDeals/prices"

class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = []
        # self.data = [{'city': 'Taipei', 'iata_code': 'TPE', 'lowest_price': 0}]
        # self.items = 0
        # self.city = ''
        # self.iata_code = ''
        # self.lowest_price = 0
        self.search_google_sheet()
    def search_google_sheet(self):
        response = requests.get(url=END_POINT)
        text = response.json()
        # self.items = len(text['prices'])
        # print(items)
        # self.city = text['prices'][index]['city']
        # self.iata_code = text['prices'][index]['iataCode']
        # self.lowest_price = text['prices'][index]['lowestPrice']

        for index in range(0,len(text['prices'])):
            city = text['prices'][index]['city']
            iata_code = text['prices'][index]['iataCode']
            lowest_price = text['prices'][index]['lowestPrice']
            self.data.append({'city': city, 'iata_code': iata_code, 'lowest_price': lowest_price})
            # print(f"lowest price: {self.lowest_price}, IATA code: {self.iata_code}")
        #print(self.data)
            # FlightSearch()