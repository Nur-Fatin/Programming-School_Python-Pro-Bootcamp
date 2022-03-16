import requests
from datetime import datetime
import os

# ============ Get Exercise Stats with Natural Language Queries ============ #
GENDER = "female"
WEIGHT_KG = 55
HEIGHT_CM = 163
AGE = 27

NUTRITIONIX_APP_ID = "b1d88381"
NUTRITIONIX_API_KEY = "2bdf3041e424b4fdbfbf485d52e34bea"
SHEET_API_TOKEN = "scjkzlxckln@@#$%&DVFVG^U&67549fj98408t8jfwjxok02"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
database_endpoint = "https://api.sheety.co/462cec205212b3cac21cc6bd2813bd2a/exerciseTrackingApp/workouts"

exercise_text = input("Tell me what exercise you did: ")

exercise_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=exercise_headers)
exercise_data = response.json()["exercises"]

# ============ Saving Exercise Data into Google Sheets ============ #
today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {SHEET_API_TOKEN}"
}

for exercise in exercise_data:
    create_row = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=database_endpoint, json=create_row, headers=bearer_headers)


