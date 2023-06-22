# from tkinter import *
import requests
from datetime import datetime
import smtplib


#
# def get_quote():
#     #Write your code here.
#     response = requests.get("https://api.kanye.rest")
#     # print(response)
#     response.raise_for_status()
#     data = response.json()
#     # print(data)
#     # print(data["quote"])
#     canvas.itemconfig(quote_text, text=f"{data['quote']}")
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()
# https://www.latlong.net/
MY_LATITUDE = 25.032969
MY_LONGITUDE = 121.565414
MEL_LATITUDE = -37.840935
MEL_LONGITUDE = 144.946457

# send email when getting dark.
my_email = "XXX@gmail.com"
password = "XXX"
address = "XXX@hotmail.com"
new_letter = "Look up the SKY!!!!"




# get information from iss
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

# parameters = {
#     "lat": MY_LATITUDE,
#     "lng": MY_LONGITUDE,
#     "formatted": 0
# }

parameters = {
    "lat": MEL_LATITUDE,
    "lng": MEL_LONGITUDE,
    "formatted": 0
}


# get information from sunrise-sunset at my location
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
# print(data["results"]['sunrise'].split("T")[1].split(":")[0])
sunrise = int(data["results"]['sunrise'].split("T")[1].split(":")[0])
sunset = int(data["results"]['sunset'].split("T")[1].split(":")[0])

print("sunrise: " + data["results"]['sunrise'])
print("sunset: " + data["results"]['sunset'])
print(sunrise)
print(sunset)

now_time = datetime.utcnow()
print(now_time)
print(now_time.hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if (iss_latitude - MY_LATITUDE <= 5) or (MY_LATITUDE - iss_latitude <= 5):
    if now_time.hour > sunset:
       print("it's dark")
       with smtplib.SMTP("smtp.gmail.com") as connection:
           connection.starttls()
           connection.login(user=my_email, password=password)
           connection.sendmail(
               from_addr=my_email,
               to_addrs=address,
               msg=f"Subject:ISS is coming!\n\n{new_letter}"
           )
