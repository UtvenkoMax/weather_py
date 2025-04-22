import requests

def get_weather(city,api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  
        "lang": "ua"
    }
    response = requests.get(url,params=params)