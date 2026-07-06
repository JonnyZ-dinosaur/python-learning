import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv("data.csv")
df2 = df.loc[:,["Price"]]

prices = []

for index, row in df.iterrows():
    prices.append(row["Price"].replace("$",""))

prices = [price.replace(",","") for price in prices]
prices = [int(price) for price in prices]


priceSort = sorted(prices)


ranges = {}
rangeLabels = []

priceArray = []
counter = 0    
maxPrice = 200000  

for price in priceSort:
    if price <= maxPrice:
        priceArray.append(price)
    else:
        ranges[counter] = len(priceArray)
        while maxPrice < price:
            counter += 200000
            maxPrice += 200000
            if maxPrice < price:
                ranges[counter] = 0
        priceArray.clear()
        priceArray.append(price)
ranges[counter] = len(priceArray)

rangeLabels = []

values = list(ranges.values())


for key in ranges.keys():
    label = str(int(key/100000)) + "-" + str(int((key/100000) + 2))
    rangeLabels.append(label)

plt.bar(rangeLabels,values)
plt.xlabel("Price Range($100,000)")
plt.ylabel("Number of Houses")
plt.show()







    