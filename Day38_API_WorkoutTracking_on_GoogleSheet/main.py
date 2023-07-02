import requests
from datetime import *
import os


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
AUTH_HEADER = {
    "Authorization": "Basic bnVsbDpudWxs"
}

SHEET_URL = "https://api.sheety.co/b8a8b9659feb1cd6c5671792f53c7ae9/myWorkouts/workouts"

header_parameters = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise = input("Tell me which exercise you did: ")

body_parameters ={
    "query": exercise,
    "gender": "female",
    "weight_kg": "47",
    "height_cm": "154",
    "age": "37",
}

response = requests.post(url=API_URL, headers=header_parameters, json=body_parameters)
text = response.json()

exercises_name = text['exercises'][0]['name']
calories = float(text['exercises'][0]['nf_calories'])
duration = float(text['exercises'][0]['duration_min'])


# get excel data
response_sheet = requests.get(url=SHEET_URL, headers=AUTH_HEADER)
print(response_sheet.text)

today = datetime.now()
print(today.strftime("%d/%m/%Y"))

add_row = {
  "workout":
    {
      "date": today.strftime("%d/%m/%Y"),
      "time": today.strftime("%X"),
      "exercise": exercises_name.title(),
      "duration": duration,
      "calories": calories,
    }
}
# Add a row to the sheet
response_sheet = requests.post(url=SHEET_URL, json= add_row, headers=AUTH_HEADER)
print(response_sheet.text)
