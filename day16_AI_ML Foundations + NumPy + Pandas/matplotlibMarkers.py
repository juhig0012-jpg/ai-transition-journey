#Mark each point with a circle:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

#Mark each point with a star:
plt.plot(ypoints, marker = '*')
plt.show()

#Format Strings fmt
#This parameter is also called fmt, and is written with this syntax:

#marker|line|color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
#Note: If you leave out the line value in the fmt parameter, no line will be plotted.
plt.plot(ypoints, 'or')
plt.show()

#Set the size of the markers to 20:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

#Set the  marker EDGE color to red:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#Set the color of both the edge and the face to red:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Hexadecimal color values:
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()