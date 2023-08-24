import requests
import json
city = input('enter the city: ')
response = requests.get('https://geocoding-api.open-meteo.com/v1/search?name=' + city)

ac = json.loads(response.text)
for i in ac :
    if i == 'results':
        for j in ac[i]:
            if j['country_code'] == 'RU':
                latit = str(j['latitude'])
                longi = str(j['longitude'])
                print(latit,longi)
r = requests.get(' https://api.open-meteo.com/v1/forecast?latitude=' + latit + '&longitude=' + longi + '&hourly=temperature_2m')


am = json.loads(r.text)
for i in am :
    if i == 'hourly':
        for j in am[i]:
            if j == 'temperature_2m':
                temp = am[i][j][0]
                for h in am[i][j]:
                    if h > temp:
                        temp = h
                print('Max temperature in city: ' + str(temp))


            