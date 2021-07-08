import requests
import json

class Weather():
  def __init__(self):
    self.api_key = "your API key"
    self.weatherAPIurl = "https://api.openweathermap.org/data/2.5/weather?appid="

  def fahrenheit(self, kelvin):
    return str(int((kelvin - 273.15) * 1.800 + 32.00))

  def celsius(self, kelvin):
    return str(int(kelvin - 273.1500))

  def convertTemp(self, unit, temp):
    if unit == 'kelvin':
      return str(int(temp)) + " degrees Kelvin"

    elif unit == 'fahrenheit':
      return self.fahrenheit(temp) + " degrees Fahrenheit"

    elif unit == 'celsius':
      return self.celsius(temp) + " degrees Celsius"

  def getWeather(self, city):
    response = requests.get(self.weatherAPIurl + self.api_key + "&q=" + city)
    self.weather = json.loads(response.text)

  def feelsLike(self, city, unit):
    self.getWeather(city)
    self.temp = self.weather['main']['feels_like']

    return self.convertTemp(unit, self.temp)

  def averageTemp(self, city, unit):
    self.getWeather(city)
    self.temp = self.weather['main']['temp']

    return self.convertTemp(unit, self.temp)

  def lowTemp(self, city, unit):
    self.getWeather(city)
    self.temp = self.weather['main']['temp_min']

    return self.convertTemp(unit, self.temp)

  def maxTemp(self, city, unit):
    self.getWeather(city)
    self.temp = self.weather['main']['temp_max']

    return self.convertTemp(unit, self.temp)

  def windSpeed(self, city):
    self.getWeather(city)
    self.windSpeed = self.weather['wind']['speed']
    return self.windSpeed

  def description(self, city):
    self.getWeather(city)
    self.info = self.weather['weather'][0]['description']
    return self.info