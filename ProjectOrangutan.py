print("\nWeather Branch\n")



#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Sunny","Snowy","Rainy","Blizzard","Foggy","Windy","Icy","Cloudy","Thunderstorm"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

# VRS() function will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowy":
        print("\nNational Weather Service has updated your Alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, you can drive a maximum of 50 MPH")
    elif weatherAlert =="Blizzard":
        print("\nNational Weather Service has updated your Alarm by 45 mintues because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, you can drive a maximum of 30 MPH")
    elif weatherAlert =="Rainy":
        print("\nNational Weather Service has updated your Alarm by 5 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, your speed will be reduced by a third")
    elif weatherAlert =="Foggy":
        print("\nNational Weather Service has updated your Alarm by 5 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, reducing your speed so you can stop within your range of  vision...")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated your Alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, you can drive a maximum of 45 MPH")
    elif weatherAlert == "Sunny":
        print("Weather is sunny")
    elif weatherAlert == "Thunderstorm":
        print("\nNational Weather Service has updated your Alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System engaged, pulling over soon...")
    else:
        print("Weather is cloudy")
    print("\nDrive safe🚗🚗")




vehicleResponseSystem()