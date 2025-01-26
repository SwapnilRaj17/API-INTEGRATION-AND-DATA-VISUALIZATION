import requests
city_name = 'Lonavala'
API_key = '6231eb08963644f96da5dd47bef8c77c'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['weather'][0]['description'])
    print('Current temperature is',data['main']['temp'])
    print('Current temperature feels like', data['main']['feels_like'])
    print('Current humidity is', data['main']['humidity'])
