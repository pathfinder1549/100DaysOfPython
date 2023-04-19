import requests


API_KEY = "7e67fc8252fd96b2191ba167b17b6ba1"
API_KEY_ALT = "f42bfd2b4a5b3da3d5ae3a1ebb2680d8"    # OpenWeatherMap.org api key
MY_LAT = 43.646461
MY_LNG = -72.011063
NUM_HOURS = 8

# for api doc -> https://openweathermap.org/api
# tutorial uses hourly data, no longer available for free
# current weather and 5 day/3 hour forecast are available

owm_current_endpoint = "https://api.openweathermap.org/data/2.5/weather"
owm_current_parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
}

owm_forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
owm_forecast_parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": NUM_HOURS,
}

response = requests.get(url=owm_forecast_endpoint, params=owm_forecast_parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

will_rain = False
forecast_list = weather_data["list"]
for forecast in forecast_list:
    weather_id = forecast["weather"][0]["id"]
    weather_main = forecast["weather"][0]["main"]
    print(f"Forecast: {weather_id} - {weather_main}")
    if weather_id < 800:
        will_rain = True

if will_rain:
    print("Rain forecasted in <24h!")
else:
    print("No rain in the forecast.")
