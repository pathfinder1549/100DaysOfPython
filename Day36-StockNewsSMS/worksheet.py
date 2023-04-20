import requests
import os
from dotenv import load_dotenv

# set root dir, load .env
base_folder = os.path.dirname(__file__)
env_path = os.path.join(base_folder, ".env.txt")
load_dotenv(env_path)

