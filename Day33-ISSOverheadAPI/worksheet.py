import requests
from datetime import datetime

MY_LAT = 43.646461
MY_LNG = -72.011063

request_parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# request package includes error handling
# returns response object from the request
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
timestamp = data["timestamp"]

print(f"ISS Current Location:\n" +\
      f"Timestamp: {timestamp}\n" +\
      f"Longitude: {longitude}\n" +\
      f"Latitude: {latitude}\n")

sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=request_parameters)
sunset_response.raise_for_status()
data = sunset_response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_hour)