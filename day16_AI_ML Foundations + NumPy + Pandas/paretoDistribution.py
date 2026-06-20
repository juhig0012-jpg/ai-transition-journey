#Draw out a sample for pareto distribution with shape of 2 with size 2x3:
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)
#Visualization of Pareto Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()