"""
Our Welcome Screen will start our program letting
drivers know that the InfoTch Center 2023 is loading
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep

TimeToSleep = 2

print("\n\nWelcome - InfoTech Center 2023")
time.sleep(TimeToSleep)

#Add code to have ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded" + "\nRetina Scanned, Access Granted!")

print("\n\nChecking gasoline tank\n\n")


# Function that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank", "Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Exxon","Meijer","Costco","Marathon","BP","Circle K","Wesco","No Gas Stations nearby"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(0.75)
        print("\nPlease pull over")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Gas level low, finding nearest gas station...")
        sleep(1.5)
        print("The closet gas station to you is:",listOfGasStations(),"Which is",milesToGasStationsLow,"mile(s) away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a Quarter Tank, looking for gas stations near you...")
        sleep(1.5)
        print("The closet gas station to you is:",listOfGasStations(),"Which is",milesToGasStationsQuarterTank,"mile(s) away.")
    else:
        print("Gas level = Full Tank")

gasLevelAlert()

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