#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# get condition for flight deal
data_manager = DataManager()

# search flight based on the condition
flight_search = FlightSearch(data_manager.data)

# get the information from the result (flight json format)
flight_data = FlightData(flight_search.cheap_flight)

# send SMS notice
notice = NotificationManager(flight_data.message)


