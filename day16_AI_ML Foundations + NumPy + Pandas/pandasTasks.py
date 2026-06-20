import pandas as pd
#pandas TASKS 
# Create student dataset
# Filter toppers 
# Find average marks 
# Add grade column
#  Sort by marks

data = {
    "Name": ["Juhi", "Aman", "Priya", "Rahul", "Neha"],
    "Marks": [95, 78, 88, 67, 92]
}

df = pd.DataFrame(data)

print("Student Dataset")
print(df)

toppers = df[df["Marks"] >= 90]
print("\nToppers")
print(toppers)

print("\nAverage Marks:", df["Marks"].mean())

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(grade)

print("\nDataset with Grades")
print(df)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nSorted by Marks")
print(sorted_df)