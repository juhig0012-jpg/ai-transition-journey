import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# --- Sample dataset ---
# Features: [study_hours, attendance%, assignments%]
X = np.array([
    [1, 40, 30], [2, 55, 50], [3, 60, 60], [4, 70, 65],
    [5, 75, 70], [6, 80, 80], [7, 85, 85], [8, 90, 90],
    [2, 50, 40], [3, 65, 55], [5, 72, 68], [6, 78, 75],
    [1, 35, 20], [4, 68, 62], [7, 88, 82], [9, 95, 95],
])
y = np.array([30, 45, 52, 61, 68, 74, 80, 87,
              42, 55, 65, 72, 25, 60, 82, 94])  # marks out of 100

# --- Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Train model ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test)
print("Coefficients:", model.coef_)
print("Intercept:   ", round(model.intercept_, 2))
print("MSE:         ", round(mean_squared_error(y_test, y_pred), 2))
print("R² Score:    ", round(r2_score(y_test, y_pred), 2))

# --- Predict a new student ---
new_student = np.array([[5, 75, 70]])   # 5 hrs, 75% attendance, 70% assignments
predicted_marks = model.predict(new_student)
print(f"\nPredicted marks: {predicted_marks[0]:.1f} / 100")

# --- Plot (actual vs predicted) ---
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, color='steelblue', edgecolors='white', s=80)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=1.5, label='Perfect fit')
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Linear Regression: Actual vs Predicted")
plt.legend()
plt.tight_layout()
plt.savefig("linear_regression.png", dpi=150)
plt.show()