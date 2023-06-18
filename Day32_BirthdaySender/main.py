##################### Extra Hard Starting Project ######################
import pandas, random
import datetime as dt
import os, smtplib

# 1. Update the birthdays.csv

birthday_data = pandas.read_csv("birthdays.csv")

my_email = "xxx@gmail.com"
password = "xxx"

# print(birthday_data)
# print(birthday_data.name)
# print(birthday_data.iterrows)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_random_letter_and_send(name):
    print(name)
    random_file = random.choice(os.listdir("letter_templates"))  # change dir name to whatever
    print(random_file)
    with open(f"letter_templates/{random_file}", mode='r') as letter:
        letter_content = letter.read()
        # print(letter_content)
        new_letter = letter_content.replace("[NAME]", name)
        print(new_letter)
        # with open(f"letter_for_{name}.txt", mode="w") as completed_letter:
        #     completed_letter.write(new_letter)
    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="xxx@hotmail.com",
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.today()
for index, row in birthday_data.iterrows():
    # print(index)
    # print(row["name"])
    # print(today.month)
    if row.year == today.year:
        # print(row.year)
        if row.month == today.month:
            if row.day == today.day:
                # print(today)
                # print(row.name)
                pick_random_letter_and_send(row["name"])
