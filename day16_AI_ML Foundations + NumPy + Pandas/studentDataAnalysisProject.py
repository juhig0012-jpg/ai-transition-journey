import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("students.csv")

print("=== Student Dataset ===")
print(df)

# Show Statistics
print("\n=== Statistics ===")
print(df.describe())

# Find Topper
topper = df.loc[df["Marks"].idxmax()]
print("\n=== Topper ===")
print(topper)

# Average Marks
avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)

# Filter Students > 90
high_scorers = df[df["Marks"] > 90]
print("\n=== Students Scoring Above 90 ===")
print(high_scorers)

# Add Grade Column
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

df["grade"] = df["Marks"].apply(assign_grade)

print("\n=== Dataset with Grades ===")
print(df)

# Sort by Marks
sorted_df = df.sort_values(by="Marks", ascending=False)

print("\n=== Sorted by Marks ===")
print(sorted_df)

# Plot Graph
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()