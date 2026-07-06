import csv
import mylib as ml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader) 
    prices = []
    bedrooms = []

    for row in reader:
        # print(row)
        # print(type(row))
        prices.append(row[-1])
        bedrooms.append(int(row[6]))
    prices = [price.replace('$', '') for price in prices]
    prices = [price.replace(',', '') for price in prices]
    prices = [int(p) for p in prices]

    mostExpensive = max(prices)
    cheapest = min(prices)
    print(cheapest)
    print(mostExpensive)

    ranges = {}    
    rangesSorted = {}
    rangeLabels = []

    sixteenOver = 0 

    for price in prices:
        value = int(price/1000000)
        if value > 15:
            sixteenOver += 1 
        elif value in ranges:
            ranges[value] += 1
        else:
            ranges[value] = 1 
    sorted = ml.sort(list(ranges.keys()))

        
    for item in sorted:
        rangesSorted[item] = ranges[item]
        if item < 1:
            rangeLabels.append("0-1")
        else:
            rangeLabels.append(str(item))
    rangeLabels.append("16+")

    rangesSorted["Over sixteen"] = sixteenOver

plt.xlabel("Price(millions)")
plt.ylabel("Number of Houses")
plt.title("Houses in Ranges of Prices")
plt.bar(rangeLabels, rangesSorted.values())
plt.show()









    

def pieChart():
    labels = [str(i) + "-bedroom" for i in range(8)]
    roomCount = {}
    roomCSorted = {}

    for b in bedrooms:
        if b in range(1, 8):
            if b in roomCount:
                roomCount[b] += 1
            else:
                roomCount[b] = 1

    print(roomCount)
    sorted = ml.sort(list(roomCount.keys()))
    pielabels = []
    
    for item in sorted:
        roomCSorted[item] = roomCount[item]
        pielabels.append(str(item) + "-bedroom")
    

    plt.pie(
    roomCSorted.values(),          # Sizes of slices
    labels = pielabels,     # Labels
    autopct="%1.1f%%",      # Show percentages
   )

    plt.title("Number of Bedrooms")
    plt.show()


def findAverage(list):
    allTotal = 0
    average = 0
    for item in list:
        allTotal += item
    average = allTotal/len(list)
    return average


def pieLabels(dictionary):
    labels = []
    for key in dictionary.keys():
        if key == "More than 10":
            labels.append("")
        elif key == 1:
            name = str(key) + " bedroom"
            labels.append(name)
        elif key >= 9:
            labels.append("")
        else:
            name = str(key) + " bedrooms"
            labels.append(name)
    return labels

def barLabels(dictionary):
    labels = []
    for key in dictionary.keys():
        if key == "More than 10":
            labels.append("10+")
        else:
            name = str(key)
            labels.append(name)
    return labels


# def barGraph():
#     plt.xlabel("Number of Bedrooms")
#     plt.ylabel("Number of Houses")
#     plt.title("Histogram of Houses with Number of Bedrooms")
#     amount = np.array(list(rooms.values()))
#     labels = barLabels(rooms)
#     plt.bar(list(labels),amount)
#     plt.show()










