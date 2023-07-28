import requests
import os
from dotenv import load_dotenv

base_folder = os.path.dirname(__file__)
env_path = os.path.join(base_folder, ".env.txt")
load_dotenv(env_path)                   # load .env in root dir, load env vars (all are strings)
APP_IS = os.getenv("app_id")
API_KEY = os.getenv("api_key")      


# nutritionix api
# example at https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
exercise_endpoint = "trackapi.nutritionix.com/v2/natural/exercise"