#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager


dm = DataManager()

fs = FlightSearch(dm.data)
print(fs.cheap_flight)
