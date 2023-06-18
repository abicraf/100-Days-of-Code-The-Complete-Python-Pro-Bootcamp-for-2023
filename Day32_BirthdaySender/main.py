##################### Extra Hard Starting Project ######################
import pandas, random
import datetime as dt
import os, smtplib

# 1. Update the birthdays.csv

birthday_data = pandas.read_csv("birthdays.csv")

my_email = "xxx@gmail.com"
password = "xxx"

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_random_letter_and_send(name, address):
    print(name)
    random_file = random.choice(os.listdir("letter_templates"))  # change dir name to whatever
    print(random_file)
    with open(f"letter_templates/{random_file}", mode='r') as letter:
        letter_content = letter.read()
        new_letter = letter_content.replace("[NAME]", name)
    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=address,
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.today()
for index, row in birthday_data.iterrows():
    if row.month == today.month:
        if row.day == today.day:
            pick_random_letter_and_send(row["name"], row["email"])
