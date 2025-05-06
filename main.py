import requests

def get_some_weather(city,api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  
        "lang": "ua"
    }
    try:
        response = requests.get(url,params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Погода в місті: {data['name']}")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Відчувається як: {data['main']['feels_like']}°C")
        print(f"Опис: {data['weather'][0]['description']}")
        print(f"Швидкість вітру: {data['wind']['speed']} м/с")
        print(f"Вологість: {data['main']['humidity']}%")
    except requests.exceptions.HTTPError as err:
        print('Помилка HTTP. ', err)
    except requests.exceptions.RequestException as err:
        print('Помилка запиту. ')
    except KeyError:
        print('Не вдалося отримати певні дані. Можливо, місто вказано неправильно. ')

if __name__ == '__main__':
    city = input('Введіть назву міста: ')
    api_key = 'c72f9dd098c4eaeaccc01f5ffc33664e'
    get_some_weather(city,api_key)


    