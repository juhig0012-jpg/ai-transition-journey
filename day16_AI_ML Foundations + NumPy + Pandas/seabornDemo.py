#plotting a displot
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

#Plotting a Displot Without the Histogram
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()