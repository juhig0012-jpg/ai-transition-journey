#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)
#Visualization of Rayleigh Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()