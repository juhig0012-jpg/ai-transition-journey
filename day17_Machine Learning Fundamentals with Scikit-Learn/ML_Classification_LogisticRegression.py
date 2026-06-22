import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

#create Dataset
data = {
    "hours":[1,2,3,4,5,6],
    "pass":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)

print(df)

#Features and Target
X = df[["hours"]]

y = df["pass"]

#split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#create model
model = LogisticRegression()

#train model
model.fit(X_train, y_train)

#Predict New Student
new_student = pd.DataFrame({
    "hours":[5]
})

prediction = model.predict(new_student)

print("Prediction:", prediction)

#Get Probability
probability = model.predict_proba(new_student)

print("Probability:", probability)

#Test Model
y_pred = model.predict(X_test)

print(y_pred)

#Calculate Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)
