import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score


# Step 1: Create Dataset
data = {
    "experience": [1, 2, 3, 4, 5, 6],
    "salary": [30000, 40000, 50000, 60000, 70000, 80000]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)


# Step 2: Split Features and Target

# Input column (Feature)
X = df[["experience"]]

# Output column (Target)
y = df["salary"]


# Step 3: Split Data into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


# Step 4: Create Model

model = LinearRegression()


# Step 5: Train Model

model.fit(X_train, y_train)

print("\nModel Trained Successfully")


# Step 6: Predict New Salary

new_employee = pd.DataFrame({
    "experience": [7]
})

prediction = model.predict(new_employee)

print("\nPredicted Salary for 7 Years Experience:")
print(prediction[0])


# Step 7: Test Model Using Test Data

y_pred = model.predict(X_test)

print("\nActual Salary:")
print(y_test.values)

print("\nPredicted Salary:")
print(y_pred)


# Step 8: Calculate Mean Squared Error

mse = mean_squared_error(
    y_test,
    y_pred
)

print("\nMean Squared Error:")
print(mse)


# Step 9: Calculate R2 Score

score = r2_score(
    y_test,
    y_pred
)

print("\nR2 Score:")
print(score)