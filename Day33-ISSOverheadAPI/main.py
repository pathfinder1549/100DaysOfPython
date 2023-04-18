import requests
from datetime import datetime

MY_LAT = 43.646461
MY_LNG = -72.011063
test_hour = 23

# find ISS location
def issLocation():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)

# your position is within +5 or -5 degrees of the ISS position.
def issNearMe(myLoc):
    issLoc = issLocation()
    print(issLoc)
    if issLoc[0] >= myLoc[0] - 5 and issLoc[0] <= myLoc[0] + 5:
        if issLoc[1] >= myLoc[1] - 5 and issLoc[1] <= myLoc[1] + 5:
            return True
        else:
            return False
    else:
        return False

# current time is after sunset or before sunrise
def isNightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour

    #for testing:
    current_hour = test_hour

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    else:
        return False



# main routine
if isNightTime():
    if issNearMe((MY_LAT, MY_LNG)):
        print("ISS is overhead!")
    else:
        print("No ISS :(")
else:
    print("It's daytime :/")

# can put main routine in loop to run constantly with import time
# can use prev project email code to create an email notification when iss overhead



