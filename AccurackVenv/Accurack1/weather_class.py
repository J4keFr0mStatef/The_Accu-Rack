# THIS SCRIPT SERVES TO GET AND DISPLAY WEATHER DATA FROM
# THE OPENWEATHERMAP API INTO A READABLE FORMAT

import requests

# Weather class for API integration and data processing
class Weather:
    # API key
    API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"
    # Base request URL for API
    FORECASTER_URL = "https://api.openweathermap.org/data/2.5/forecast?"

    def __init__(self, city):
        self.city = city
        self.info = {}
        self.refresh = True

    # accessor and mutator for city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        value = str(value)
        # TODO: See if we can check it among a dictionary of cities
        self._city = value

    # accessor and mutator for info
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    # function to ping the server and set all the required values
    # used in all the get() functions to ensure most recent data
    def ping(self):
        # format URL for the server request
        URL = self.FORECASTER_URL + "q=" + self.city + "&units=imperial" + "&appid=" + self.API_KEY
        response = requests.get(URL)
        # check to see if the server responded
        if response.status_code == 200:
            # we have to manipulate the JSON to access the correct part of the dictionary
            # that has the weather data we need
            data = response.json()
            list = data["list"]
            self.info = dict(list[0])
        else:
            raise NameError("There was an invalid response from the OpenWeatherMap server")
    
    # function to find the TEMPERATURE within the JSON file
    def getTemp(self):
        if self.refresh:
            self.ping()
        main = self.info["main"]
        return int(main["temp"])

    # function to find the HUMIDITY within the JSON file
    def getHumidity(self):
        if self.refresh:
            self.ping()
        main = self.info["main"]
        return int(main["humidity"])

    # function to find the PRESSURE within the JSON file
    def getPressure(self):
        if self.refresh:
            self.ping()
        main = self.info["main"]
        return int(main["pressure"])

    # function to find the CURRENT WEATHER within the JSON file
    def getCurrent(self):
        if self.refresh:
            self.ping()
        report = self.info["weather"]
        return report[0]["description"]

    # function to find the CHANCE OF RAIN within the JSON file
    def getRainChance(self):
        if self.refresh:
            self.ping()
        chance = self.info["pop"]
        return chance

    def __str__(self):
        # always refresh data before printing it
        self.ping()
        s = f"Temperature: {self.getTemp()}°F\n"
        s += f"Humidity: {self.getHumidity()}%\n"
        s += f"Weather Report: {self.getCurrent()}\n"
        s += f"Chance of Rain: {self.getRainChance()*100}%\n"
        return s

########################################################################

