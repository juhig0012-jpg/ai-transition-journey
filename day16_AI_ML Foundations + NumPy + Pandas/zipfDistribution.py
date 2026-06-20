#Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)
#Sample 1000 points but plotting only ones with value < 10 for more meaningful chart
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()