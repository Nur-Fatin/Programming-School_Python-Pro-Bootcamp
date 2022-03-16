import datetime as dt
import pandas as pd
import random
import smtplib

current_date = dt.datetime.now()
today = current_date.day
current_month = current_date.month

birthdays_df = pd.read_csv("birthdays.csv")
birthdays_list = birthdays_df.to_dict(orient="records")

MY_EMAIL = "nur_fatin_atiqah@yahoo.com"
PASSWORD = "ypxrnwxeiwssurvd"

for person in birthdays_list:
    if today == person["day"] and current_month == person["month"]:
        file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            message = letter_file.read()
            birthday_wish = message.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Birthday Wish\n\n{birthday_wish}"
            )