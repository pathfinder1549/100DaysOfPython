import requests
import os
from dotenv import load_dotenv
from datetime import datetime

base_folder = os.path.dirname(__file__)
env_path = os.path.join(base_folder, ".env.txt")
load_dotenv(env_path)                       # load .env in root dir, load env vars (all are strings)
USERNAME = os.getenv("pixela_username")     
TOKEN = os.getenv("pixela_token")

# create new user api info
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create a new user with params above
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create graph api info
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# create new graph for user
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# enter new data api info
data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
data_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "4",
}

#response = requests.post(url=data_endpoint, json=data_params, headers=headers)
#print(response.text)

# edit a pixel
edit_endpoint = f"{data_endpoint}/20230728"
edit_params = {
    "quantity": "8",
}

#response = requests.put(url=edit_endpoint, json=edit_params, headers=headers)
#print(response.text)

# delete a pixel
delete_endpoint = edit_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)