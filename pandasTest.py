import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_json("data.json")

#The values under Duration are the x values and values under Calories become y-values   
# df.plot(kind = 'scatter', x = "Duration", y = "Calories")

# df["Duration"].plot(kind = "hist")
# df = df.cumsum
# plt.show()

# ts = pd.Series(np.random.(loc = 5, scale = 2, size = (1000,4)), index=pd.date_range("1/1/2000", periods=1000))

# ts = ts.cumsum()


# cumsum = cumulative sum, takes the current value and adds it to the previous value 
# df2 = pd.DataFrame(np.random.normal(loc = 1, scale = 3, size = (1000,4)), columns=["A", "B", "C", "D"] )
# print(df2)
# df3 = df2.cumsum()
# print(df3)

# df3.plot()
# plt.show()


# print(df.head(10))
# #use dictionary to automatically assign labels 

# data = {
#     "name": ["Bob", "Joe", "Steph"],
#     "salary": [20000, 300000, 421000],
#     "birthday": ["4/5/89", "6/2/90", "12/23/00"]
# }

#use series for one dimensional
dates = pd.date_range("20260127", periods = 7)
dates  

df = pd.read_table("fruit_data_with_colors.txt")
# specific column
# df["color_score"].fillna(2000,inplace = True)
# print(df)

# heightMean = df["height"].mean()

df2 = df.groupby("fruit_name")
print(df2)

# df3 = df.loc[:, ["height"]]

# df3.plot()
# plt.show()

