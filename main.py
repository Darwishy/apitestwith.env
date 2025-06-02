import requests
from datetime import datetime
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

GENDER = "Male"
WEIGHT_KG = 60
HEIGHT_CM = 60
AGE = 37

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
sheet_get = os.getenv("sheet_get")
sheet_post = os.getenv("sheet_post")
exercise_endpoint = os.getenv("exercise_endpoint")
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

#############################


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

bearer_headers = {"Authorization": os.getenv("bearer")}
test_request = requests.post(sheet_post, json=sheet_input, headers=bearer_headers)
print(test_request.text)
