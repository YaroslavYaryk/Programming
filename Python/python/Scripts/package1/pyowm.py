import pyowm

owm = pyowm.OWM('2265e7528feb74505afb8cfb36867097')  # api key с сайта openweathermap.org

place = input("В каком городе/стране?: ") # Пользователь вводит город в импут

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w)  