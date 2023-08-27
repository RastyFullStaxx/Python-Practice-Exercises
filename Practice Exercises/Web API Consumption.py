import requests

def get_weather(city):
    api_key = 'your_api_key'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    return temperature, condition

city_name = 'New York'
temperature, weather_condition = get_weather(city_name)
print(f"Current weather in {city_name}: {temperature}°C, {weather_condition}")
