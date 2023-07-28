import requests
import os
from dotenv import load_dotenv

base_folder = os.path.dirname(__file__)
env_path = os.path.join(base_folder, ".env.txt")
load_dotenv(env_path)                   # load .env in root dir, load env vars (all are strings)

exercise_query = "ran for 25 minutes"

# nutritionix api
# example at https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.getenv("app_id")
API_KEY = os.getenv("api_key")      
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
body = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 59,
    "height_cm": 175,
    "age": 30,
}
response = requests.post(url=exercise_endpoint, headers=header, json=body)
print(response)
# next steps - need to parse json response for calories burned
# need to create user input for exercise query