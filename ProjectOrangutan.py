print("\nWeather Branch\n")



#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Sunny","Snowy","Rainy","Blizzard","Foggy","Windy","Icy","Cloudy","Thunderstorm"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
