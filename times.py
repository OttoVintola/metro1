import re
import numpy as np


def convert(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    timers=["{}.{}.{}".format(a, b, c)]
    return timers

# Open the file as read only and declare variable
metro_file = open("metro.txt", 'r')
#Declare variable for the read lines
metroinfo = metro_file.readlines()

listTimes = []
#Print the realtimeDepartures
for x in range(9, 37, 7):
    realDepartures = metroinfo[x]
    # Get numbers from the list and store in list array
    number = [int(s) for s in re.findall(r'\b\d+\b', realDepartures)]
    listTimes.extend(number)
    # Convert to array of integers
    numbers = np.array(listTimes)


# Convert array into array of times
times = []
for i in numbers:
    times.extend(convert(i))

times