class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon valuse are all floats
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    import pandas as pd
    f = pd.read_csv("cities.csv")
    for i in f[['city', 'lat', 'lng']].values.tolist():
      cities.append(City(i[0], i[1], i[2]))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)