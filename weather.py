import requests
url ='http://api.weatherapi.com/v1/current.json?key=aca685e9e96343a1b5051012240703&q=London&aqi=no'
response = requests.get(url)
weather_json=response.json()
temp = weather_json.get('current').get('temp_f')
description =weather_json.get('current').get('condition').get('text')
print(temp, description)