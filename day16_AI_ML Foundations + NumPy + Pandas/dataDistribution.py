#Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

#return a 2-D array with 3 rows, each containing 5 values.
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)