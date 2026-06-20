import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
#Draw a line in a diagram from position (0,0) to position (6,250):
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

