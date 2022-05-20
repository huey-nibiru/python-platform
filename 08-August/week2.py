# WEATHER API

import urllib.request
import json
import os
import time

# SET THE APIKEY TO A VARIABLE
api = "8d186df3d3789089c11bdfa3f1bb6a24"

# SET THE BASE URL TO THE WEBSITE
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

# include appid tag for the apikey
api = "&appid=" + api

# GET LOCATION
location = input("Enter a city/town:")

# FULLY FORMED URL TO GET data
url = base_url + location + api 
print(url) 



# BREAK DOWN THE DATA FROM ITS JSON format
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req).read().decode()
data = json.loads(resp)

temp = data["main"]["temp"]
city = data["name"]
tempmin = data["main"]["temp_min"]
tempmax = data["main"]["temp_max"]

print("CITY:", city)
print("TEMP:", temp)
print("MIN TEMP:", tempmin)
print("MAX TEMP:", tempmax)


