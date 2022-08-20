import re


# Open the file as read only and declare variable
metro_file = open("metro.txt", 'r')


#Declare variable for the read lines
metroinfo = metro_file.readlines()

#Print the realtimeDepartures
for x in range(9, 37, 7):
    realDepartures = metroinfo[x]

    print(realDepartures)


numbers = [int(word) for word in metroinfo.split() if word.isdigit()]

print(numbers)
