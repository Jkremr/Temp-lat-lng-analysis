from citipy import citipy
import numpy as np
import pandas as pd
import random
import requests as req
import json

from openWeatherMapApiKeys import apiKey

city = citipy.nearest_city(0, 0)

latDim = {'min': -90, 'max': 90}
lngDim = {'min': -180, 'max': 180}

latVals = np.arange(latDim['min'], latDim['max'], 0.1)
lngVals = np.arange(lngDim['min'], lngDim['max'], 0.1)

colNames = ('cityName', 'countryCode', 'randLat', 'randLng', 'uniqueName')
cities = pd.DataFrame(columns=(colNames))

counter = 0
while counter < 1:
	randLat = random.choice(latVals)
	randLng = random.choice(lngVals)
	city = citipy.nearest_city(randLat, randLng)
	if city.city_name + city.country_code in cities.uniqueName.tolist():
		pass
	else:
		cities.loc[len(cities)] = [city.city_name, city.country_code, randLat, randLng, city.city_name + city.country_code]
	counter += 1


cities['temp'] = ''
#'http://api.openweathermap.org/data/2.5/weather?q=luderitzna,na&units=imperial&APPID=key'
baseUrl = 'http://api.openweathermap.org/data/2.5/weather?q='
units = 'imperial'
for index, row in cities.iterrows():
	url = baseUrl + cities.cityName + ',' + cities.countryCode + '&units=' + units + '&APPID=' + apiKey
	
	weather_response = req.get(url[0])
	weather_json = weather_response.json()
	print(weather_json)
	print(url[0])



