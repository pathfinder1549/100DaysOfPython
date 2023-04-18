import requests

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

