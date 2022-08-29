import requests
import datetime
from pprint import pprint
from config import open_weather_token

# Функция принимает два параметра (город, токен)
def get_weather(city, open_weather_token):
    try: 
        # Запрашиваем данные у openweathermap
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        # Вывод данных в формате json
        data = r.json()
        pprint(data)
        
        # Обозначаем параметры
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        day_length = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # Вывод всех данных погоды
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Weather in: {city}\nWeather: {cur_weather}°C\n"
            f"Humidity: {humidity}%\nWind: {wind} m/s\n"
            f"Sunrise at: {sunrise_timestamp}\n"
            f"Sunset at: {sunset_timestamp}\n"
            f"Length of the day: {day_length}\n"
            f"Have a *nice day!*"
        )


    # Вывод на случай ошибки в наименовании города
    except Exception as ex:
        print(ex)
        print("Incorrent city name")

def main():
    city = input("Enter city: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()