# THIS SCRIPT SERVES TO GET AND DISPLAY WEATHER DATA FROM
# THE OPENWEATHERMAP API INTO A READABLE FORMAT

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
    # getting the main dict block
<<<<<<< Updated upstream
    list = data["list"]
    info = dict(list[0])

    main = info["main"]
=======
    print(data)
    main = data["main"]
>>>>>>> Stashed changes
    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # getting the probability of precipitation
    chance_rain = info['pop']
    # weather report
    report = info['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
    print(f"Chance of Rain: {str(chance_rain * 100) + '%'}")
else:
    # showing the error message
    print("Could not find city.")
