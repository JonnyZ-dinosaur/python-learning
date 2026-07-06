# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([2, 10])
# ypoints = np.array([9, 300])


# plt.plot(xpoints, ypoints, color = "red")
# plt.savefig("Red Line 2")

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
xpoints = np.array([2, 4, 6, 8])
font1 = {'family':'serif','color':'blue','size':20}

plt.title("line graph", fontdict = font1, loc = 'right')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(ypoints,xpoints, color = "red" , ls = "dotted", lw = 2, marker = "o" )
plt.show()

plt.suptitle("Line")









#grid lines have the same commands as the line itself, change color, size and style
# plt.subplot(1,2,1)
# the rows of graphs, the columns of graphs and what number graph it is

#can use scatter instead of plot to get a scatter plot

#also can use bars, but remember that bars dont have both a x and y value its either or 
# therefore, one should contain values and the other should contain names

#Or you could draw a histogram and you could use numpy to generate random values 
# by calling: variable = np.random.normal(a,b,c)
# a is the number that the values will concentrate around, b is the standard deviation and c is the number of values 

# drawing pie charts:
# only use one set of values(x or y not both), in the array, instead of points its the percentages of the pie
# adding a labels parameter allows for the addition of labels through an array |label = labelArray| 
# start angle parameter allows for you to start at whatever angle you want to, counterclockwise
# explode paramter allows for one section(or more) to stand out and get pulled away from the pie chart
# explode = explodeArray, where in the array, in order, of how much you want to pull the peice away 
# shadows = true turns on shadows(put as a parameter) 
# similar to the rest, adding color in a list
























# y2points = np.array([2, 7, 9, 4])
# x2points = np.array([2, 4, 6, 8])
# font2 = {'family':'serif','color':'red','size':12}

# plt.title("line graph", fontdict = font2, loc = 'left')
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")

# #grid lines have the same commands as the line itself, change color, size and style
# plt.subplot(1,2,2)
# # the rows of graphs, the columns of graphs and what number graph it is

# plt.plot(y2points, x2points,  color = "green" , ls = "dashed", lw = 2)


