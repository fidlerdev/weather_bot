import asyncio
from typing import Union
from typing_extensions import Never
import python_weather
import requests
import asyncio

from pprint import pprint

from config import get_config


async def get_weather_by_city(city_name: str) -> int:
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client() as client:
    # fetch a weather forecast from a city
    weather = await client.get(city_name)

    # returns the current day's forecast temperature (int)
    print(weather.temperature, weather.country, weather.coordinates)

    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(daily)

      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly}')

    return weather.temperature

def get_weather_by_location(latitue: float, longitude: float) -> Union[int, Never]:
    api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitue}&lon={longitude}&appid={get_config().weather_token}&units=metric"
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?id&appid={get_config().weather_token}"
    response = requests.get(url=api_url)
    print(response)
    print(response.status_code)
    pprint(response.json)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Ошибка запроса", response=response)

    return response.json()["current"]["temp"]


if __name__ == "__main__":
    asyncio.run(main=get_weather_by_city("Санкт-Петербург"))