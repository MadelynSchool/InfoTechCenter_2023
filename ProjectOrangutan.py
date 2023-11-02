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