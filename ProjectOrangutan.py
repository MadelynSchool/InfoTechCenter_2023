"""
Our Welcome Screen will start our program letting
drivers know that the InfoTch Center 2023 is loading
"""

#Import Libraries Here
import time

import sys

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