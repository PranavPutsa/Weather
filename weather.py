import pyowm

owm = pyowm.OWM('f5b6e1329423db53a8adebac5e1d272a')
obs = owm.weather_at_place("kakinada,IN")
w = obs.get_weather()
weather = {'cloud_coverage': w.get_clouds(), 'wind': w.get_wind(), 'humidity': w.get_humidity(),
           'temp': w.get_temperature(unit='celsius')}
cloud_coverage = ''
wind_speed = weather['wind']['speed']
humidity = weather['humidity']
temp_cur = weather['temp']['temp']
temp_max = weather['temp']['temp_max']
temp_min = weather['temp']['temp_min']
if weather['cloud_coverage'] in range(0, 10):
    cloud_coverage = 'clear sky'
elif weather['cloud_coverage'] in range(11, 50):
    cloud_coverage = 'scattered clouds'
elif weather['cloud_coverage'] in range(51, 90):
    cloud_coverage = 'broken clouds'
elif weather['cloud_coverage'] in range(91, 100):
    cloud_coverage = 'overcast clouds'

print('The weather in Kakinada is ' + str(round(temp_cur)) + ' degrees with ' + cloud_coverage.capitalize() +
      '. It is ' + str(humidity) + '% humid with a wind speed of ' + str(wind_speed) + ' MpH')
