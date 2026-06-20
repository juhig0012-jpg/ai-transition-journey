#Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)
#Visualization of Chi Square Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=1, size=1000), kind="kde")

plt.show()