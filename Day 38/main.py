import os
import requests
from datetime import datetime

GENDER = "M"
WEIGHT_KG = 55
HEIGHT_CM = 165
AGE = 21

APP_ID = os.environ.get("NT_APP_ID")
API_KEY = os.environ.get("NT_API_KEY")
Bearer = os.environ.get(" BEARER_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
# print(result)

bearer_headers = {
    "Authorization": Bearer
}

sheet_endpoint = "https://api.sheety.co/a1ce99ba2602220bd65c82a7dd0ac763/workoutsTracking/workouts"

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    exercise_name = exercise['name']
    duration_min = exercise['duration_min']
    calories = exercise['nf_calories']

    sheet_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": duration_min,
            "calories": calories,
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_data, headers=bearer_headers)
    print(sheet_response.text)

