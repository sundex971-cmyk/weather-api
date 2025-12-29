import requests # type: ignore
from datetime import datetime

# c помощью  API получаем координаты необходимого города
city = input("Введите город: ")
url_for_coord = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
coord = requests.get(url_for_coord).json()
latitude = coord['results'][0]['latitude']
longitude = coord['results'][0]['longitude']

print(type(coord))
# -------------------------------------

# подставляем координаты в API и получаем необходимые параметры
url_for_weather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto&forecast_days=1"
weather = requests.get(url_for_weather).json()

time = weather['current']['time'] 
time = datetime.fromisoformat(time) # создаём объект datetime и форматируем время в более удобном варианте
time_formatted = time.strftime("%d.%m.%Y %H:%M")

temperature = weather['current']['temperature_2m']
humidity = weather['current']['relative_humidity_2m']
wind_speed = weather['current']['wind_speed_10m']

print(f"""
      Город: {city}
      ----------
      
      Текущее время: {time_formatted}
      Температура: {temperature} °C
      Влажность: {humidity} %
      Скорость ветра: {wind_speed} км/ч
      """)


