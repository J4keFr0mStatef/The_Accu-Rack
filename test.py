## this file is a reference to how the api get works
## and is not intended for use

import requests

########## API INTEGRATION AND DATA GET ############
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
# City Name
CITY = "ruston"
# API key
API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"
# updating the URL
URL = BASE_URL + "q=" + CITY + "&units=imperial" + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    print(data)
    # getting the main dict block
    main = data[]
    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # getting the probability of precipitation
    chance_rain = data['pop']
    # weather report
    report = data['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
    # showing the error message
    print("Could not find city.")
