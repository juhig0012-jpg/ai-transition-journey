import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)