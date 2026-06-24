# ==========================================
# EMAIL SPAM CLASSIFIER USING NLP
# ==========================================

# Import pandas for data handling
import pandas as pd

# Import nltk for text processing
import nltk

# Download stopwords dataset (only first time)
nltk.download('stopwords')

# Import stop words
from nltk.corpus import stopwords

# Import regular expression library
import re

# Import TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Split dataset into train and test
from sklearn.model_selection import train_test_split

# Naive Bayes classifier
from sklearn.naive_bayes import MultinomialNB

# Accuracy score
from sklearn.metrics import accuracy_score

# Confusion matrix
from sklearn.metrics import confusion_matrix

# Visualization
import matplotlib.pyplot as plt

# ==========================================
# STEP 1 : LOAD DATASET
# ==========================================

print("\nLoading Dataset...\n")

# Read CSV file
df = pd.read_csv("spam.csv")

# Show first 5 rows
print(df.head())

# ==========================================
# STEP 2 : TEXT CLEANING FUNCTION
# ==========================================

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Split sentence into words
    words = text.split()

    # Remove stop words
    words = [
        word for word in words
        if word not in stopwords.words('english')
    ]

    # Join words again
    return " ".join(words)

# ==========================================
# STEP 3 : APPLY CLEANING
# ==========================================

print("\nCleaning Text...\n")

# Create cleaned text column
df["clean_text"] = df["text"].apply(clean_text)

# Show sample cleaned text
print(df[["text", "clean_text"]].head())

# ==========================================
# STEP 4 : CONVERT LABELS
# spam = 1
# ham = 0
# ==========================================

df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# ==========================================
# STEP 5 : TF-IDF VECTORIZATION
# ==========================================

print("\nApplying TF-IDF...\n")

# Create vectorizer object
vectorizer = TfidfVectorizer()

# Convert text into numerical features
X = vectorizer.fit_transform(df["clean_text"])

# Target variable
y = df["label"]

print("Feature Shape:", X.shape)

# ==========================================
# STEP 6 : TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# STEP 7 : TRAIN MODEL
# ==========================================

print("\nTraining Model...\n")

# Create model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

print("Training Complete")

# ==========================================
# STEP 8 : PREDICTION
# ==========================================

# Predict on test data
y_pred = model.predict(X_test)

# ==========================================
# STEP 9 : ACCURACY SCORE
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", round(accuracy * 100, 2), "%")

# ==========================================
# STEP 10 : CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

# ==========================================
# STEP 11 : VISUALIZE CONFUSION MATRIX
# ==========================================

plt.imshow(cm)

plt.title("Confusion Matrix")

plt.colorbar()

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()

# ==========================================
# STEP 12 : USER INPUT TESTING
# ==========================================

print("\n===== TEST YOUR EMAIL =====")

while True:

    message = input("\nEnter Email Text : ")

    # Exit condition
    if message.lower() == "exit":
        break

    # Clean message
    cleaned = clean_text(message)

    # Convert into TF-IDF
    vector = vectorizer.transform([cleaned])

    # Predict
    prediction = model.predict(vector)

    if prediction[0] == 1:
        print("SPAM EMAIL")
    else:
        print("NOT SPAM")