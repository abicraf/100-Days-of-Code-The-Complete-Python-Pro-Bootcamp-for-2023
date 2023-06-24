import requests
from datetime import *
from twilio.rest import Client
import os

# environment variable: OWM_API_KEY
api_key = os.environ.get("OWM_API_KEY")

# send SMS via Twilio
account_sid = 'AC62e7000b920136b322b59a628669e1d6'
auth_token = os.environ.get("AUTH_TOKEN")


prameters={
# Taipei's latitude and longitude
    "lat": 25.032969,
    "lon": 121.565414,
    "appid": api_key
}
# # return current weather
# END_POINT_Current = "https://api.openweathermap.org/data/2.5/weather"
# return forecast based on every 3 hours in 5 days.
END_POINT_3hour_forecast = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=END_POINT_3hour_forecast, params=prameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
#
# print(weather_data['list'][0]['weather'][0]['id'])
# weather_id_0 = weather_data['list'][3]['weather'][0]['id']


# Get forecast for the next 12 hours from the url
# 3 hours in one item, so we need to get 4 item for the next 12 hours
will_rain = False
weather_next_12hour = []

current_hour = datetime.now().hour
print(f'Current hour: {current_hour}')

# get the time from the URL and compare it with current time to catch the initial list.
initial_section = weather_data['list'][0]['dt_txt'].split()
initial_section_time = initial_section[1].split(':')
print(f'Initial section hour: {initial_section_time[0]}')
time_gap= current_hour - int(initial_section_time[0])

start_section = 0
if time_gap > 0:
    start_section += int(time_gap / 3)
elif time_gap < 0:
    current_hour += 24
    time_gap = current_hour - int(initial_section_time[0])
    start_section += int(time_gap / 3)

print(f"Start section: {start_section}")

# use "slice" [:4] to get the 4 item
weather_four_section = weather_data['list'][start_section:start_section + 4]
#print(weather_four_section)

for the_weather_section in weather_four_section:
    weather_id = the_weather_section['weather'][0]['id']
    weather_next_12hour.append(weather_id)
    if weather_id < 700:
        will_rain = True
print(weather_next_12hour)

if will_rain:
    print("Next 12 hours will rain. Bring an Umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='xxxx',
        body='Next 12 hours will rain. Bring an Umbrella.',
        to='xxxx'
    )
    print(message.status)


