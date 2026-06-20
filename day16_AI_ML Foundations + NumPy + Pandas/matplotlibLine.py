#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#Shorter Syntax
#The line style can be written in a shorter syntax:

#linestyle can be written as ls.

#dotted can be written as :.

#dashed can be written as --.
plt.plot(ypoints, ls = ':')
plt.show()

#Set the line color to red:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# Hexadecimal color values:
plt.plot(ypoints, c = '#4CAF50')
plt.show()

#Plot with a 20.5pt wide line:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

#Multiple Lines
#Draw two lines by specifying a plt.plot() function for each line:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

#Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()