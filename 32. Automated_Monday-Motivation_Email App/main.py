import smtplib
import random
import datetime as dt

MY_EMAIL = "barangterbaik@gmail.com"
PASSWORD = "I(38tQt4VrONYB+3"
SMTP = "smtp.gmail.com"
RECIPIENT_EMAIL = "nurblissempire@gmail.com"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    """choose a random quote from a list of quotes"""
    with open("quotes.txt") as quote_file:
        quote = random.choice(quote_file.readlines())

    """Send Quote email every Monday"""
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject: {quote}"
        )

