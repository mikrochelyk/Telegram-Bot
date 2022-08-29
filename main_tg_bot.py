import requests
import datetime
from config import telegram_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi! Type in your city to know the weather")

@dp.message_handler()
async def get_weather(message: types.Message):
    try: 
        # Запрашиваем данные у openweathermap
        r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
    )

        # Вывод данных в формате json
        data = r.json()
        
        # Обозначаем параметры
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        day_length = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # Вывод всех данных погоды
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Weather in: {city}\nWeather: {cur_weather}°C\n"
            f"Humidity: {humidity}%\nWind: {wind} m/s\n"
            f"Sunrise at: {sunrise_timestamp}\n"
            f"Sunset at: {sunset_timestamp}\n"
            f"Length of the day: {day_length}\n"
            f"Have a *nice day!*"
        )


    # Вывод на случай ошибки в наименовании города
    except:
        await message.reply("Incorrent city name")

if __name__ == '__main__':
    executor.start_polling(dp)