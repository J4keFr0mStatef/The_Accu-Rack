from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

API_KEY = "c6fac2b39ddd7e66e83a0be39bd11f52"

config = get_default_config()
config["language"] = "en"

owm = OWM('{}'.format(API_KEY))
mgr = owm.weather_manager()

three_h_forecaster = mgr.forecast_at_place("ruston,us", "3h")

observation = mgr.weather_at_place('ruston,us')
w = observation.weather

today = timestamps.r()
print(three_h_forecaster.will_be_rainy_at
