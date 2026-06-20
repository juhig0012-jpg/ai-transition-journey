#A simple pie chart:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

#By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:
#Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:

#The value divided by the sum of all values: x/sum(x)

#Add labels to the pie chart with the labels parameter.
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

#Start Angle
#As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

#The startangle parameter is defined with an angle in degrees, default angle is 0:
#Start the first wedge at 90 degrees:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

#Explode
#ybe you want one of the wedges to stand out? The explode parameter allows you to do that.

#The explode parameter, if specified, and not None, must be an array with one value for each wedge.

#Each value represents how far from the center each wedge is displayed:

#Pull the "Apples" wedge 0.2 from the center of the pie:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

#Add a shadow:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

#Specify a new color for each wedge:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

#To add a list of explanation for each wedge, use the legend() function:
#Add a legend:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

#Legend With Header
#To add a header to the legend, add the title parameter to the legend function.
#Add a legend with a header:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 