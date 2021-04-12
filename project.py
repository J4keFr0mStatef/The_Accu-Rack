
import requests
import json

########## API INTEGRATION AND DATA GET ############
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name
CITY = "ruston"
# API key
API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = int((int(main['temp']) - 273.15) * 9/5 + 32)
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
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
          
