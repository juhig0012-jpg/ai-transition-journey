#Create a 2x3 uniform distribution sample:
from numpy import random

x = random.uniform(size=(2, 3))

print(x)

#Visualization of Uniform Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=1000), kind="kde")

plt.show()