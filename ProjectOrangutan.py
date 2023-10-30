print("******************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank", "Half Tank","Three Quarter Tank","BIBBLE","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)