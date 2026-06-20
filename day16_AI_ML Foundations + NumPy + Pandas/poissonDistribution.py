#Generate a random 1x10 distribution for occurrence 2:
from numpy import random

x = random.poisson(lam=2, size=10)

print(x)

#Visualization of Poisson Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))

plt.show()