
class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data_json):
        self.message = ''
        for index in range(0, len(flight_data_json)):
            departure_iata = flight_data_json[index]["data"][0]["flyFrom"]
            destination_iata = flight_data_json[index]["data"][0]["flyTo"]
            departure_city = flight_data_json[index]["data"][0]["cityFrom"]
            destination_city = flight_data_json[index]["data"][0]["cityTo"]
            flight_price = flight_data_json[index]["data"][0]["price"]
            flight_date_from = flight_data_json[index]["data"][0]["local_departure"]
            flight_date_to = flight_data_json[index]["data"][0]["local_arrival"]
            self.message = f"Low Price Alert! Only TWD${flight_price} to fly from {departure_city}-{departure_iata} " \
                           f"to {destination_city}-{destination_iata}, from {flight_date_from} to {flight_date_to}."
            print(self.message)