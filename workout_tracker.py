import requests
import datetime
import os

GENDER = os.environ["GENDER"]
WEIGHT_KG = os.environ["WEIGHT_KG"]
HEIGHT_CM = os.environ["HEIGHT_CM"]
AGE = os.environ["AGE"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_ID"]

exercise_endpoint = os.environ["CALCULATOR_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

my_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

USERNAME = os.environ("USERNAME")
PASSWORD = os.environ("PASSWORD")

response = requests.post(exercise_endpoint, json=my_data, headers=headers)
result = response.json()

sheety_api_endpoint = os.environ("SHEETY_API_ENDPOINT")

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_api_endpoint,
                                   json=sheet_inputs,
                                   auth=(USERNAME, PASSWORD))
