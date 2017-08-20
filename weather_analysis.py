from citipy import citipy
import numpy as np
import pandas as pd
import random

city = citipy.nearest_city(0, 0)

latDim = {'min': -90, 'max': 90}
lngDim = {'min': -180, 'max': 180}

latVals = np.arange(latDim['min'], latDim['max'], 0.1)
lngVals = np.arange(lngDim['min'], lngDim['max'], 0.1)

colNames = ('cityName', 'countryCode')
cities = pd.DataFrame(columns=(colNames))
print(cities)




