#Draw 4 bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#The categories and their values represented by the first and second argument as arrays.
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()

#Draw 4 horizontal bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#Draw 4 red bars:

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

#Bar Width
#Draw 4 very thin bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

#The default width value is 0.8

#Note: For horizontal bars, use height instead of width.
#Draw 4 very thin bars:


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()