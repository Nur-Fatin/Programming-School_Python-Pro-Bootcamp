import requests
import os
import random
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_API_KEY = "bd466b8ea03697019d74a926e4cd688e"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACd395ab8f006ee816a1d37ce5d760e140"
auth_token = "353d4bd36f77dd6fecb0f4478f3b4844"

weather_params = {
    "lat": 3.202890,
    "lon": 101.777730,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour in weather_data:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=f"It's going to rain today. Remember your ☔\n{quote}",
        from_='+19705338693',
        to='[Twilio Verified Phone Number]'
    )

    print(message.status)
