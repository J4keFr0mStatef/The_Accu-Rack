
### WELCOME TO THE ACCU-RACK! ###

### The Accu-Rack ###
Freshman design project for CSC132 at Louisiana Tech University.  This project is a coat hanger that recommends a coat based on local weather data and takes in information from Google Calendars to show the user what events that he/she has going on that day. 

### Authors ###
John Doherty
GitHub: https://github.com/johnpdoherty

Travis Knippers
GitHub: https://github.com/J4keFr0mStatef

Gregory Whitehurst
GitHub: https://github.com/GregWhite2001

### GitHub Repository ###
https://github.com/J4keFr0mStatef/The_Accu-Rack

### Instructions ###
1. place weather wear on the appropriate hook
(1 = umbrella)(2 = raincoat)(3 = light coat)(4 = heavy coat) 
2. Type in a city
3. The LEDs on the Accu-Rack will illuminate
4. Choose the weather apparel under the blinking LED

### Features ###
-Temperature
-Humidity
-Integration of google calendar with planned events for the day
-A button to change between Farenheit and Celsius
-A refresh button to refresh information displayed
-A recommendation of what weather apparel to wear
-A button that allows a change of city

### API Documentation ###
OpenWeatherMap by OpenWeather© 2012-2021
Forecaster Documentation: https://openweathermap.org/forecast5
Reference Code: https://www.tutorialspoint.com/find-current-weather-of-any-city-using-openweathermap-api-in-python

Google Calendar API for Python by Google© 2021
Documentation: https://developers.google.com/calendar/quickstart/python
Reference Code: https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/

### Our Written Functions & Classes ###
1. weather_class
    - This was written to have an easier way to interface with the weather API. It cut down
      on the complexity of the code in regards to OpenWeatherMap. The file, weather_class,
      is used to pull all weather info from the API.

2. KeyboardGUI
    - Contains the keyboard and it's functionality. It is responsible for pulling input from
      the user for the city location. It can differentiate between actual city and a typo.

3. GUI
    - Contains all functionality for the GUI. Contains the buttons for the GUI as well.
      This is the bulk of the code in main.py and took the most work.

### Circuit ###

### Known Bugs ###
- Recommendation of coat does not change until the coat is removed

- Changing cities with coats on the rack will sometimes cause a crash

- The coats are only recommended for Fahrenheit

