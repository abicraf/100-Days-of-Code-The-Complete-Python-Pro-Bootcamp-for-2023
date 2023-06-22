# from tkinter import *
import requests
from datetime import datetime
import smtplib, time

# API Practice ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
#
# API Practice -----------------------------------------------------------

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


# https://www.latlong.net/
# MEL_LATITUDE = -37.840935
# MEL_LONGITUDE = 144.946457
TAIPEI_LATITUDE = 25.032969
TAIPEI_LONGTITUDE = 121.565414
MY_LATITUDE = TAIPEI_LATITUDE
MY_LONGITUDE = TAIPEI_LONGTITUDE

# send email when getting dark.
my_email = "abicraf@gmail.com"
password = "clerbmduqdiqcagz"
sent_to_address = "coldwr@hotmail.com"
new_letter = "Look up the SKY!!!!"

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

# calculate the time difference and convert the UTC time to Local time.
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    #print(now_timestamp)  # return current time in floating format
    #print(time.localtime()) # return: time.struct_time(tm_year=2023, tm_mon=6, tm_mday=22, tm_hour=17, tm_min=38, tm_sec=29, tm_wday=3, tm_yday=173, tm_isdst=0)
    #print(datetime.fromtimestamp(now_timestamp)) # return current local time
    #print(datetime.utcfromtimestamp(now_timestamp))  # return current UTC time
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    offset = int(str(offset).split(":")[0]) # get the hour difference
    #print(offset)
    #print(utc_datetime + offset)
    local_time = utc_datetime + offset
    if local_time > 24:
        local_time -= 24
    return local_time


def iss_is_closing():
    # get information from iss
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LATITUDE - 5) <= iss_latitude <= (MY_LATITUDE + 5) and (MY_LONGITUDE - 5) <= iss_longitude <= (
            MY_LONGITUDE + 5):
        print("iss is closing!")
        return True
    else:
        print("(iss is far way)")

def is_dark():
    # get information from sunrise-sunset at my location
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #print(data)
    # print(data["results"]['sunrise'].split("T")[1].split(":")[0])
    sunrise = int(data["results"]['sunrise'].split("T")[1].split(":")[0])  # UTC time
    sunset = int(data["results"]['sunset'].split("T")[1].split(":")[0])  # UTC time

    print("UTC sunrise: " + data["results"]['sunrise'])
    print("UTC sunset: " + data["results"]['sunset'])
    # convert the time to Local time
    sunrise = datetime_from_utc_to_local(sunrise)
    sunset = datetime_from_utc_to_local(sunset)
    print(f"Local sunrise hour: {sunrise}")
    print(f"Local sunset hour: {sunset}")

    now_time = datetime.now()
    # print(now_time)
    # print(now_time.hour)

    if now_time.hour >= sunset or now_time.hour <= sunrise:
        print("it's dark")
        return True

# is_dark()

while True:
    time.sleep(60) ## BONUS: run the code every 60 seconds.
    if iss_is_closing() and is_dark():
        # send email
       with smtplib.SMTP("smtp.gmail.com") as connection:
           connection.starttls()
           connection.login(user=my_email, password=password)
           connection.sendmail(
               from_addr=my_email,
               to_addrs=my_email,
               msg=f"Subject:ISS is coming!\n\n{new_letter}"
           )
