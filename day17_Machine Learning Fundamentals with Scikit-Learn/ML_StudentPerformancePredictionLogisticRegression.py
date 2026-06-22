import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report, ConfusionMatrixDisplay)

# --- Same features, binary labels ---
X = np.array([
    [1, 40, 30], [2, 55, 50], [3, 60, 60], [4, 70, 65],
    [5, 75, 70], [6, 80, 80], [7, 85, 85], [8, 90, 90],
    [2, 50, 40], [3, 65, 55], [5, 72, 68], [6, 78, 75],
    [1, 35, 20], [4, 68, 62], [7, 88, 82], [9, 95, 95],
])
y = np.array([0, 0, 1, 1, 1, 1, 1, 1,
              0, 1, 1, 1, 0, 1, 1, 1])  # 0 = Fail, 1 = Pass

# --- Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Train model ---
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # probability of Pass

print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Fail", "Pass"]))

# --- Predict a new student ---
new_student = np.array([[3, 55, 45]])  # borderline case
prob = model.predict_proba(new_student)[0][1]
result = "PASS" if prob >= 0.5 else "FAIL"
print(f"\nNew student → {result} (confidence: {prob*100:.1f}%)")

# --- Confusion matrix ---
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=["Fail", "Pass"])
disp.plot(cmap="Blues")
plt.title("Logistic Regression: Confusion Matrix")
plt.tight_layout()
plt.savefig("logistic_regression_cm.png", dpi=150)
plt.show()